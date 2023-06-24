from frames import *
from DisplayTester import *
from QRGenerator import *

import threading
import tkinter
from tkinter import *
import queue


# GUI class, using customtkinter
# 1 - GUI based on tkinter frames and grid
# 2 - Handle user input and output
# 3 - All data flows through this class at some point
class GUI(customtkinter.CTk, threading.Thread):
    def __init__(self, input_queue, output_queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        super().__init__()

        self.input_queue = input_queue
        self.output_queue = output_queue
        self.daemon = True
        self.receive_data = args

        self.ports_test = ""
        self.camera_test = ""
        self.sound_test = ""
        self.keyboard_test = ""
        self.display_test = ""
        self.frame_test = ""

        self.title("Vedion Notebook Tester ver. beta-3.0")
        self.geometry('1280x1000+1500+0')

        # Configure middle row as the one taking all available space
        # This is the row where main_frame is
        self.rowconfigure(1, weight=1)

        self.bind("<KeyPress>", self.key_callback)
        self.bind("<KeyRelease>", self.key_release_callback)

        self.bind("<Shift-less>", self.button_prev_callback)
        self.bind("<Shift-greater>", self.button_next_callback)

        # configure grid layout / LEFT SIDE frame
        self.output_frame = OutputFrame(self)
        self.output_frame.grid(row=0, column=0, rowspan=19, columnspan=2, padx=(10, 0), pady=10, sticky="ens")

        # UPPER frame
        self.testers_frame = TestersFrame(self)
        self.testers_frame.grid(row=0, column=2, columnspan=6, padx=10, pady=(10, 0), sticky="ew")
        self.testers_frame.configure(self, fg_color="transparent")

        # create all the testers frames, show only first - ports tester frame
        self.ports_main_frame = PortsMainFrame(self)
        self.ports_main_frame.grid(row=1, column=2, columnspan=6, padx=40, pady=40, sticky="ewns")

        self.camera_main_frame = CameraMainFrame(self)
        self.sound_main_frame = SoundMainFrame(self)
        self.microphone_main_frame = MicrophoneMainFrame(self)
        self.keyboard_main_frame = KeyboardMainFrame(self)
        self.monitor_main_frame = MonitorMainFrame(self)
        self.qr_main_frame = QRMainFrame(self, self.output_frame)

        # array with references to all the testers frames
        # for making it easier to hide and show consecutive frames with NEXT and PREV buttons
        # first element is None so testers numbering starts with 1!
        self.frame_references = [None, self.ports_main_frame, self.camera_main_frame, self.microphone_main_frame,
                                 self.sound_main_frame, self. keyboard_main_frame, self.monitor_main_frame,
                                 self.qr_main_frame]

        # BOTTOM SIDE frame
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(5, weight=1)

        self.button_next = customtkinter.CTkButton(self, text="Dalej", command=self.button_next_callback)
        self.button_next.grid(row=19, column=6, padx=(10, 30), pady=10, sticky="e")

        self.button_prev = customtkinter.CTkButton(self, text="Cofnij", command=self.button_prev_callback)
        self.button_prev.grid(row=19, column=5, padx=10, pady=10, sticky="e")

        self.button_reset = customtkinter.CTkButton(self, text="Resetuj", command=self.button_reset_callback)
        self.button_reset.grid(row=19, column=2, padx=10, pady=10, sticky="w")

        # Read all hardware info and then put it in the output frame for display
        self.output_frame.read_hardware_info()
        self.output_frame.fill_hardware_info()

        # which tester to show at any given time
        # show ports tester at the start
        self.tab_number = 1
        self.display_main_frame(self.tab_number)

    # Self-explanatory`
    def button_next_callback(self, event):
        self.tab_number += 1
        self.display_main_frame(self.tab_number-1)

    def button_prev_callback(self, event):
        self.tab_number -= 1
        self.display_main_frame(self.tab_number+1)

    # Reset by calling the same frame again with itself as previous frame
    def button_reset_callback(self):
        print("\n")
        self.display_main_frame(self.tab_number)

    # Display specific frame
    def button_menu_callback(self, frame_number):
        temp = self.tab_number
        self.tab_number = frame_number
        self.display_main_frame(temp)

    def key_callback(self, event):
        print("pressed", event.keysym)
        if self.tab_number in [1, 2, 3, 4, 6, 7]:
            if event.keysym in ['m', 'M']:
                self.button_reset_callback()

        elif self.tab_number == 5:
            if event.keysym == 'M':
                self.button_reset_callback()

            else:
                self.keyboard_main_frame.key_event(event.keysym, 'keydown')

        if self.tab_number in [1, 2, 3, 4, 5, 6, 7]:
            if event.keysym == 'Escape':
                # remove focus from widget
                self.focus()

        if event.keysym == 'Return':
            match self.tab_number:
                case 1:
                    if self.frame_references[self.tab_number].check_box_state is True:
                        self.frame_references[self.tab_number].check_box.deselect()
                        self.frame_references[self.tab_number].check_box_callback()
                        self.frame_references[self.tab_number].entry_ports_test.focus()

                    else:
                        self.frame_references[self.tab_number].check_box.select()
                        self.frame_references[self.tab_number].check_box_callback()

                case 2:
                    if self.frame_references[self.tab_number].check_box_state is True:
                        self.frame_references[self.tab_number].check_box.deselect()
                        self.frame_references[self.tab_number].check_box_callback()
                        self.frame_references[self.tab_number].entry_camera_test.focus()

                    else:
                        self.frame_references[self.tab_number].check_box.select()
                        self.frame_references[self.tab_number].check_box_callback()

                case 3:
                    if self.frame_references[self.tab_number].check_box_state is True:
                        self.frame_references[self.tab_number].check_box.deselect()
                        self.frame_references[self.tab_number].check_box_callback()

                    else:
                        self.frame_references[self.tab_number].check_box.sele()
                        self.frame_references[self.tab_number].check_box_callback()

                case 4:
                    if self.frame_references[self.tab_number].check_box_state is True:
                        self.frame_references[self.tab_number].check_box.deselect()
                        self.frame_references[self.tab_number].check_box_callback()
                        self.frame_references[self.tab_number].entry_both.focus()

                    else:
                        self.frame_references[self.tab_number].check_box.select()
                        self.frame_references[self.tab_number].check_box_callback()

    def key_release_callback(self, event):
        if self.tab_number == 5:
            self.keyboard_main_frame.key_event(event.keysym, 'keyup')

    # Process all commands and data from input queue
    # For now it only processes data incomming from checking ports
    def process_queue(self, data_type):
        if data_type == 'ports':
            try:
                current = self.input_queue.get_nowait()

                if type(current) == str:
                    # display output from executing 'lsblk'
                    self.ports_main_frame.label1.configure(self, text=current, justify='left')

                else:
                    print("type exception")

            except queue.Empty:
                pass

        if data_type == 'camera':
            try:
                current = self.input_queue.get_nowait()

                if type(current) != str:
                    self.camera_main_frame.label1.configure(self, image=current, text="")

                else:
                    print("type exception")

            except queue.Empty:
                pass
            except TclError:
                pass

    # Main method that handles all testers mainframes and transitions between them
    def display_main_frame(self, previous):
        print("\nTab number: " + str(self.tab_number))

        # stop all testers
        self.output_queue.put('stop_all')

        # and start the next one
        match self.tab_number:
            case 0:
                # can't go tab number below 1
                self.tab_number = 1
                return

            case 1:
                self.output_queue.put('start_ports')

            case 2:
                self.output_queue.put('start_camera')

            case 3:
                self.output_queue.put('start_playback')

            case 4:
                self.output_queue.put('start_play')

            case 5:
                pass

            case 6:
                self.monitor_main_frame.show_fullscreen()

            case 7:
                self.qr_main_frame.make_qr()

            case 8:
                # can't exceed tab number 7
                self.tab_number = 7

        self.fill_entries()

        # hide previous frame and configure and show current frame
        self.frame_references[previous].grid_forget()
        self.frame_references[self.tab_number].grid(row=1, column=2, columnspan=5, padx=40, pady=40, sticky="ewns")

    def fill_entries(self):

        self.ports_test = self.ports_main_frame.entry_ports_test.get()
        self.camera_test = self.camera_main_frame.entry_camera_test.get()
        self.sound_test = self.sound_main_frame.entry_both.get()
        self.display_test = self.monitor_main_frame.entry_display.get()
        self.frame_test = self.monitor_main_frame.entry_frame.get()

        self.output_frame.entry_ports.delete(0, tkinter.END)
        self.output_frame.entry_ports.insert(0, self.ports_test)
        self.output_frame.entry_camera.delete(0, tkinter.END)
        self.output_frame.entry_camera.insert(0, self.camera_test)
        self.output_frame.entry_sound.delete(0, tkinter.END)
        self.output_frame.entry_sound.insert(0, self.sound_test)
        self.output_frame.entry_monitor.delete(0, tkinter.END)
        self.output_frame.entry_monitor.insert(0, self.display_test)
        self.output_frame.entry_notes.delete(0, tkinter.END)
        self.output_frame.entry_notes.insert(0, self.frame_test)


    def on_closing(self):
        self.output_queue.put('terminate_all')
        GUI.destroy(self)
