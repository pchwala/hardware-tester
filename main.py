from GUI import *
from frames import *

from ListRemovable import *
from RecordSound import *
from PlaySound import *
from CameraCapture import *

from queue import Queue

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


# 1. Zle czyta karte graficzna jesli są dwie
# 2. Duze zuzycie procesora na idle
#       - dodanie time delaya typu 0.1s w odpowiedni sposob znaczaco poprawia wydajnosc - do implementacji
# 3. Mikrofon nie dziala pod root'em. W celu naprawy wymagana gruntowna przebudowa struktury:
#       - zmiana uruchamiania main z roota na usera( stream input modułu 'pyaudio' nie dziala pod rootem
#         ( problem albo z urzedzaniami wirtualnymi, albo ze sterownikami albo z samym modulem,
#           w sumie chuj wie)
#       - wydzielenie podprogramu czytujacego hardware info
#       - dodanie tego podporgramu do /etc/sudoers.d
#       - integracja powyzszego podprogramu z glownym programem
# 4. kamera jakos dziwnie znieksztalca ale tylko na niektorych modelach
#       - pewnie jakies operacje na frame z opencv tak robia
# 5. dodac skalowanie okienka kamery i qrcode


# Main App class
# 1 - Controls an execution of all threads and data flow between them
# 2 - Controls the execution of GUI class methods and transition between testers
# 3 - DATA FLOW between threads:
#     - App ---> GUI        - Start GUI execution
#     - GUI ---> App        - What to ask from Threads
#     - App ---> Threads    - Ask Threads
#     - App <--- Threads    - Get answer
#     - App ---> GUI        - Pass that answer


class App:
    def __init__(self):
        super().__init__()

        # Threads list
        self.threads = []

        self.sleeper = True

        # All Queues for controlling data flow between threads
        # Input Queues for passing data for a thread
        # Output Queues for getting data from a thread
        self.q_GUI_input = Queue()
        self.q_GUI_output = Queue()

        self.q_ports_input = Queue()
        self.q_ports_output = Queue()

        self.q_camera_input = Queue()
        self.q_camera_output = Queue()

        # these threads have only input queue
        # they don't return any data
        self.q_play = Queue()
        self.q_playback = Queue()

        # Very simple pointers for each thread handle in the 'threads[]' list
        self.t_GUI = 0
        self.t_play = 1
        self.t_playback = 2
        self.t_ports = 3
        self.t_camera = 4

        # Create and start a thread and pass 'stop' into an input queue
        # So that every thread is initiated and loaded into memory
        self.threads.append(GUI(self.q_GUI_input, self.q_GUI_output, args='stop'))
        self.threads[self.t_GUI].start()
        self.threads[self.t_GUI].input_queue.put('stop')

        self.threads.append(PlaySound(self.q_play, args='stop'))
        self.threads[self.t_play].start()
        self.threads[self.t_play].queue.put('stop')

        self.threads.append(RecordSound(self.q_playback, args='stop'))
        self.threads[self.t_playback].start()
        self.threads[self.t_playback].queue.put('stop')

        self.threads.append(ListRemovable(self.q_ports_input, self.q_ports_output, args='stop'))
        self.threads[self.t_ports].start()
        self.threads[self.t_ports].input_queue.put('stop')

        self.threads.append(CameraCapture(self.q_camera_input, self.q_camera_output, args='stop'))
        self.threads[self.t_camera].start()
        self.threads[self.t_camera].input_queue.put('stop')

        # Callback for GUI thread, calls method inside GUI thad handle window closing and cleans after that
        self.threads[self.t_GUI].protocol("WM_DELETE_WINDOW", self.threads[self.t_GUI].on_closing)

# # # MAIN LOOP   MAIN LOOP   MAIN LOOP   MAIN LOOP   MAIN LOOP   MAIN LOOP
        while True:
            # Basically the same as calling tk.mainloop(), but it allows to put additional lines in the loop
            self.threads[self.t_GUI].update_idletasks()
            self.threads[self.t_GUI].update()
            if self.sleeper is True:
                time.sleep(0.1)

            # Constantly get output from GUI thread and handle it accordingly
            try:
                current = self.q_GUI_output.get_nowait()
                match current:
                    case 'stop_all':
                        self.sleeper = True
                        self.q_ports_input.put('stop')
                        self.q_play.put('stop')
                        self.q_playback.put('stop')
                        self.q_camera_input.put('stop')

                    case 'terminate_all':
                        self.q_ports_input.put('terminate')
                        self.q_play.put('terminate')
                        self.q_playback.put('terminate')
                        self.q_camera_input.put('terminate')
                        return

                    case 'start_ports':
                        self.q_ports_input.put('start')

                    case 'start_play':
                        self.q_play.put('start')

                    case 'start_playback':
                        self.q_playback.put('start')

                    case 'start_camera':
                        self.sleeper = False
                        self.q_camera_input.put('start')

            except queue.Empty:
                pass

            # pass info from ListRemovable instance to GUI instance
            try:
                current = self.q_ports_output.get_nowait()
                print("ports INTERVAL")
                self.q_GUI_input.put(current)
                self.threads[self.t_GUI].process_queue('ports')

            except queue.Empty:
                pass

            # pass info from CameraCapture instance to GUI instance
            try:
                current = self.q_camera_output.get_nowait()
                print("camera INTERVAL")
                print(current)
                self.q_GUI_input.put(current)
                self.threads[self.t_GUI].process_queue('camera')

            except queue.Empty:
                pass
# # # MAIN LOOP END   MAIN LOOP END   MAIN LOOP END   MAIN LOOP END   MAIN LOOP END


result = subprocess.run("./python-sudo.sh hwinfo.py", shell=True)

App = App()
