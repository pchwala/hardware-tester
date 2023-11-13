import customtkinter as ctk


class TouchpadMainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.button_left = ctk.CTkButton(self, text='Lewy', width=180, height=80, state="disabled")
        self.button_left.grid(row=1, column=1, pady=(0, 20))
        self.button_middle = ctk.CTkButton(self, text='Srodkowy', width=180, height=80, state="disabled")
        self.button_middle.grid(row=1, column=2, pady=(0, 20))
        self.button_right = ctk.CTkButton(self, text='Prawy', width=180, height=80, state="disabled")
        self.button_right.grid(row=1, column=3, pady=(0, 20))

        self.button_references = [None, self.button_left, self.button_middle, self.button_right]

        self.check_box_state = True
        self.check_box = ctk.CTkCheckBox(self, text="Działa?", onvalue=True, offvalue=False,
                                         command=self.check_box_callback)
        self.check_box.select()
        self.check_box.grid(row=3, column=2, pady=(0, 20))

        self.entry_touchpad = ctk.CTkEntry(self, state='normal', placeholder_text="Wady touchpada", width=200)
        self.entry_touchpad.grid(row=4, column=2, pady=(0, 20), sticky='ns')

    def check_box_callback(self):
        self.check_box_state = not self.check_box_state

    def mark_button(self, num, key_state):
        match key_state:
            case 'press':
                self.button_references[num].configure(fg_color="yellow")

            case 'release':
                self.button_references[num].configure(fg_color="green")

    def button_event(self, num, key_state):
        try:
            self.mark_button(num, key_state)
        except ValueError:
            pass
