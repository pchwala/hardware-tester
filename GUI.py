from frames import *
from PortsTester import *
from CameraTester import *
from SoundTesters import *
from KeyboardTester import KeyboardMainFrame
from DisplayTester import MonitorMainFrame
from QRGenerator import *

import threading
import tkinter
from tkinter import *
import queue


class GUI(customtkinter.CTk, threading.Thread):
    """
    GUI class, using customtkinter.
    1 - GUI based on tkinter frames and grid
    2 - Manages displaying all main elements of the GUI
    3 - Handle user input and output
    4 - All data that is displayed for the user must flows through this class at some point

    'input_queue' and 'output_queue' for communicating with App class through commands
    """
    def __init__(self, input_queue, output_queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        super().__init__()

        self.input_queue = input_queue
        self.output_queue = output_queue
        self.daemon = True
        self.receive_data = args

        # Entry inputs from the user
        self.ports_test = ""
        self.camera_test = ""
        self.sound_test = ""
        self.keyboard_test = ""
        self.display_test = ""
        self.frame_test = ""

        # Result of automatic wifi-check
        self.wlan_status = False

        # Previous strings stored in corresponding tester_frame or output_frame
        # Enables interchangeable editing data in those entries on the fly
        self.testers_previous = ["", "", "", "", "", "", ""]
        self.output_previous = ["", "", "", "", "", "", ""]

        # Simple "pointers" for each entry frame
        self.e_ports = 0
        self.e_camera = 1
        self.e_sound = 2
        self.e_display = 3
        self.e_frame = 4
        self.e_keyboard = 5
        self.e_layout = 6

        self.title("Vedion Notebook Tester ver. beta-3.0")
        self.geometry('1280x1000+1500+0')

        # Configure middle row as the one taking all available space
        # This is the row where main_frame is
        self.rowconfigure(1, weight=1)

        # Bind all global shortcuts for the App
        self.bind("<KeyPress>", self.key_press_callback)
        self.bind("<KeyRelease>", self.key_release_callback)

        self.bind("<Shift-less>", self.button_prev_callback)
        self.bind("<Shift-greater>", self.button_next_callback)
        self.bind("<Shift-m>", self.button_reset_callback)
        self.bind("<Shift-M>", self.button_reset_callback)
        self.bind("<Control-r>", self.button_reset_callback)
        self.bind("<Control-R>", self.button_reset_callback)
        self.bind("<Shift-s>", self.shortcut_start_stop)
        self.bind("<Shift-S>", self.shortcut_start_stop)
        self.bind("<Control-c>", self.shortcut_start_stop)
        self.bind("<Control-C>", self.shortcut_start_stop)
        self.bind("<Shift-Return>", self.shortcut_return)

        # Overwrite default behaviour of TAB button
        self.bind("<Tab>", self.tab_callback)
        self.bind("<ISO_Left_Tab>", self.left_tab_callback)

        self.unbind_all("<<NextWindow>>")
        self.unbind_all("<<PrevWindow>>")

        # Configure grid layout / LEFT SIDE frame
        self.output_frame = OutputFrame(self)
        self.output_frame.grid(row=0, column=0, rowspan=19, columnspan=2, padx=(10, 0), pady=10, sticky="ens")

        # UPPER frame
        self.testers_frame = TestersFrame(self)
        self.testers_frame.grid(row=0, column=2, columnspan=6, padx=10, pady=(10, 0), sticky="ew")
        self.testers_frame.configure(self, fg_color="transparent")

        # Create all the testers frames, show only first - ports tester frame
        self.ports_main_frame = PortsMainFrame(self)
        self.ports_main_frame.grid(row=1, column=2, columnspan=6, padx=40, pady=40, sticky="ewns")

        self.camera_main_frame = CameraMainFrame(self)
        self.sound_main_frame = SoundMainFrame(self)
        self.microphone_main_frame = MicrophoneMainFrame(self)
        self.keyboard_main_frame = KeyboardMainFrame(self)
        self.monitor_main_frame = MonitorMainFrame(self)
        self.qr_main_frame = QRMainFrame(self, self.output_frame, self.monitor_main_frame)

        # Array with references to all the testers frames
        # For making it easier to hide and show consecutive frames with NEXT and PREV buttons
        # First element is None so testers numbering starts with 1!
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

        self.tab_state = -1
        self.output_entry = [self.output_frame.entry_keyboard, self.output_frame.entry_ports,
                             self.output_frame.entry_camera, self.output_frame.entry_sound,
                             self.output_frame.entry_keyboard_notes, self.output_frame.entry_monitor,
                             self.output_frame.entry_class, self.output_frame.entry_notes]

    def button_next_callback(self, event=None):
        self.tab_number += 1
        self.display_main_frame(self.tab_number-1)

    def button_prev_callback(self, event=None):
        self.tab_number -= 1
        self.display_main_frame(self.tab_number+1)

    def button_reset_callback(self, event=None):
        """
        Reset by calling the same frame again with itself as previous frame

        :param event:
        :return: None
        """
        print("\n")

        # Reset all keyboard buttons to default color
        #  but only when keyboard tester is displayed
        if self.tab_number == 5:
            self.keyboard_main_frame.reset_all()

        self.display_main_frame(self.tab_number)

    def button_menu_callback(self, frame_number):
        """
        Display specific frame

        :param frame_number:
        :return: None
        """
        temp = self.tab_number
        self.tab_number = frame_number
        self.display_main_frame(temp)

    def reset_start_stop(self):
        """
        For testing purposes. Currently unused

        :return: None
        """
        reference3 = self.microphone_main_frame.button_stop
        reference4 = self.sound_main_frame.button_stop
        self.button_start_stop(reference3, "Start", "playback")
        self.button_start_stop(reference4, "Start", "play")

    def shortcut_start_stop(self, event=None):
        """
        Starts or stops testing microphone or speakers
        Also changes text on according buttons

        :param event:
        :return: None
        """
        match self.tab_number:
            case 3:
                reference = self.microphone_main_frame.button_stop
                self.button_start_stop(reference, reference.cget("text"), "playback")

            case 4:
                reference = self.sound_main_frame.button_stop
                self.button_start_stop(reference, reference.cget("text"), "play")

    def button_start_stop(self, reference, state, tester):
        if state == "Stop":
            reference.configure(text="Start")
            output_command = "stop_" + tester
            self.output_queue.put(output_command)

        elif state == "Start":
            reference.configure(text="Stop")
            output_command = "start_" + tester
            self.output_queue.put(output_command)

    def key_press_callback(self, event):
        print("pressed", event.keysym)
        if self.tab_number == 5:
            self.keyboard_main_frame.key_event(event.keysym, 'keydown')

        if event.keysym == 'Escape':
            # remove focus from widget by focusing main Window
            self.focus()

    def key_release_callback(self, event):
        if self.tab_number == 5:
            print("released " + event.keysym)
            self.keyboard_main_frame.key_event(event.keysym, 'keyup')

    def tab_callback(self, event=None):
        self.tab_state += 1
        self.output_entry[self.tab_state].focus()
        if self.tab_state > 6:
            self.tab_state = -1

    def left_tab_callback(self, event=None):
        self.tab_state -= 1
        self.output_entry[self.tab_state].focus()
        if self.tab_state < 0:
            self.tab_state = 7

    def shortcut_return(self, event=None):
        current_frame = self.frame_references[self.tab_number]

        match self.tab_number:
            case 1:
                if current_frame.check_box_state is True:
                    current_frame.check_box.deselect()
                    current_frame.check_box_callback()
                    current_frame.entry_ports_test.focus()

                else:
                    current_frame.check_box.select()
                    current_frame.check_box_callback()

            case 2:
                if current_frame.check_box_state is True:
                    current_frame.check_box.deselect()
                    current_frame.check_box_callback()
                    current_frame.entry_camera_test.focus()

                else:
                    current_frame.check_box.select()
                    current_frame.check_box_callback()

            case 3:
                if current_frame.check_box_state is True:
                    current_frame.check_box.deselect()
                    current_frame.check_box_callback()

                else:
                    current_frame.check_box.select()
                    current_frame.check_box_callback()

            case 4:
                if current_frame.check_box_state is True:
                    current_frame.check_box.deselect()
                    current_frame.check_box_callback()
                    current_frame.entry_both.focus()

                else:
                    current_frame.check_box.select()
                    current_frame.check_box_callback()

            case 5:
                current_frame.entry_callback()

            case 6:
                current_frame.entry_callback()

    def process_queue(self, data_type):
        """
        Process all commands and data from input queue

        :param data_type:
        :return: None
        """
        if data_type == 'ports':
            try:
                current = self.input_queue.get_nowait()

                if type(current) == str:
                    # display output from executing 'lsblk'
                    self.ports_main_frame.label1.configure(self, text=current, justify='left')
                    self.ports_main_frame.label1.cget("font").configure(size=20)

                else:
                    print("type exception")

            except queue.Empty:
                pass

        if data_type == 'camera':
            try:
                current = self.input_queue.get_nowait()

                # Display frame from Camera
                if type(current) != str:
                    self.camera_main_frame.label1.configure(self, image=current, text="")

                else:
                    print("type exception")

            except queue.Empty:
                pass
            except TclError:
                pass

    def wlan_status_update(self, status):
        self.wlan_status = status

    def display_main_frame(self, previous):
        """
        Main method that handles all testers mainframes and transitions between them

        :param previous: number of the frame that was on display when this function was called
        :return:
        """
        print("\nTab number: " + str(self.tab_number))

        self.fill_all_entries()

        # Stop all testers
        self.output_queue.put('stop_all')

        # Unbind TAB
        # I think its kind of wrong, but it works
        # Better way to do it will be so it is only executed once after keyboardTester
        self.bind("<Tab>", self.tab_callback)
        self.bind("<ISO_Left_Tab>", self.left_tab_callback)

        # And start the next one
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
                self.unbind("<Tab>")
                self.unbind("<ISO_Left_Tab>")

            case 6:
                self.monitor_main_frame.show_fullscreen()

            case 7:
                # It needs to be executed a second time in this section by the flaw in design
                # of checkboxes and entries in DisplayTester
                self.fill_all_entries()
                camera = self.camera_main_frame.check_box_state
                sound = self.sound_main_frame.check_box_state
                keyboard = self.keyboard_main_frame.check_box.get()

                self.qr_main_frame.make_qr(camera, sound, keyboard, self.wlan_status)

            case 8:
                # Can't exceed tab number 7
                self.tab_number = 7

        # hide previous frame and configure and show current frame
        self.frame_references[previous].grid_forget()
        self.frame_references[self.tab_number].grid(row=1, column=2, columnspan=5, padx=40, pady=40, sticky="ewns")

    def fill_all_entries(self):

        self.fill_entry(self.ports_main_frame.entry_ports_test, self.output_frame.entry_ports, self.e_ports)
        self.fill_entry(self.camera_main_frame.entry_camera_test, self.output_frame.entry_camera, self.e_camera)
        self.fill_entry(self.sound_main_frame.entry_both, self.output_frame.entry_sound, self.e_sound)
        self.fill_entry(self.monitor_main_frame.entry_display, self.output_frame.entry_monitor, self.e_display)
        self.fill_entry(self.monitor_main_frame.entry_frame, self.output_frame.entry_notes, self.e_frame)
        self.fill_entry(self.keyboard_main_frame.entry_keyboard, self.output_frame.entry_keyboard_notes, self.e_keyboard)
        self.fill_entry(self.keyboard_main_frame.entry_layout, self.output_frame.entry_keyboard, self.e_layout)

        class_str = self.monitor_main_frame.class_segmented.get() + " " + self.monitor_main_frame.polska_segmented.get()
        self.output_frame.entry_class.delete(0, tkinter.END)
        self.output_frame.entry_class.insert(0, class_str)

    def fill_entry(self, tester_entry, output_entry, entry_number):
        tester_data = tester_entry.get()
        output_data = output_entry.get()

        if tester_data != self.testers_previous[entry_number]:
            output_entry.delete(0, tkinter.END)
            output_entry.insert(0, tester_data)

        elif output_data != self.output_previous[entry_number]:
            tester_entry.delete(0, tkinter.END)
            tester_entry.insert(0, output_data)

        else:
            output_entry.delete(0, tkinter.END)
            output_entry.insert(0, output_data)
            tester_entry.delete(0, tkinter.END)
            tester_entry.insert(0, tester_data)

        self.testers_previous[entry_number] = tester_data
        self.output_previous[entry_number] = output_data

    def on_closing(self):
        self.output_queue.put('terminate_all')
        GUI.destroy(self)
