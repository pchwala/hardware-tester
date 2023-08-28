import customtkinter as ctk


class CameraMainFrame(ctk.CTkFrame):
    """

    """
    def __init__(self, master):
        super().__init__(master)

        # Configure grid like this:
        #    0 1 2
        # 0 |_|_|_|
        # 1 |_|_|_|
        # 2 |_|_|_|
        #    .....
        # where 1-1 square has the highest weight

        self.camera_number = 0

        self.grid_columnconfigure(1, weight=3)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)

        self.label1 = ctk.CTkLabel(self, text="WAITING FOR CAMERA")
        self.label1.grid(row=0, column=1, pady=20)

        self.button1 = ctk.CTkButton(self, text="Zmień kamerę", command=self.button_change_camera)
        self.button1.grid(row=2, column=1, pady=20)

        self.check_box_state = True
        self.check_box = ctk.CTkCheckBox(self, text="Działa?", onvalue=True, offvalue=False,
                                         command=self.check_box_callback)
        self.check_box.select()
        self.check_box.grid(row=3, column=1, pady=(0, 20))

        self.entry_camera_test = ctk.CTkEntry(self, state='normal', placeholder_text="Wady kamery", width=200)
        self.entry_camera_test.grid(row=4, column=1, pady=(0, 20), sticky="ns")

    def check_box_callback(self):
        self.check_box_state = not self.check_box_state

    def button_change_camera(self):
        if self.camera_number == 0:
            self.camera_number = 2
            self.master.camera_number_update(2)

        else:
            self.camera_number = 0
            self.master.camera_number_update(0)
