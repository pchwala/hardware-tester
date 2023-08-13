import customtkinter as ctk
from PIL import Image


class SoundMainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.play_image = ctk.CTkImage(None, dark_image=Image.open("play.png"), size=(256, 256))

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.label1 = ctk.CTkLabel(self, image=self.play_image, text='')
        self.label1.grid(row=0, column=1)

        self.button_stop = ctk.CTkButton(self, text='Stop', width=70)
        self.button_stop.configure(command=lambda: master.button_start_stop(self.button_stop,
                                                                            self.button_stop.cget("text"),
                                                                            "play"))
        self.button_stop.grid(row=2, column=1, pady=(0, 20))

        self.check_box_state = True
        self.check_box = ctk.CTkCheckBox(self, text="Działa?", onvalue=True, offvalue=False,
                                         command=self.check_box_callback)
        self.check_box.select()
        self.check_box.grid(row=3, column=1, pady=(0, 20))

        self.entry_both = ctk.CTkEntry(self, state='normal', placeholder_text="Wady głośników", width=200)
        self.entry_both.grid(row=4, column=1, pady=(0, 20), sticky='ns')

    def check_box_callback(self):
        self.check_box_state = not self.check_box_state


class MicrophoneMainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.mic_image = ctk.CTkImage(None, dark_image=Image.open("mic.png"), size=(256, 256))

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.label1 = ctk.CTkLabel(self, image=self.mic_image, text='')
        self.label1.grid(row=0, column=1)

        self.button_stop = ctk.CTkButton(self, text='Stop', width=70)
        self.button_stop.configure(command=lambda: master.button_start_stop(self.button_stop,
                                                                            self.button_stop.cget("text"),
                                                                            "playback"))
        self.button_stop.grid(row=2, column=1, pady=(0, 20))

        self.check_box_state = True
        self.check_box = ctk.CTkCheckBox(self, text="Działa?", onvalue=True, offvalue=False,
                                         command=self.check_box_callback)
        self.check_box.select()
        self.check_box.grid(row=3, column=1, pady=(0, 20))

    def check_box_callback(self):
        self.check_box_state = not self.check_box_state
