import customtkinter as ctk


class PortsMainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)

        self.label1 = ctk.CTkLabel(self, text="TESTUJEMY PORTY")
        self.label1.grid(row=0, column=1)

        self.check_box_state = True
        self.check_box = ctk.CTkCheckBox(self, text="Działa?", onvalue=True, offvalue=False,
                                         command=self.check_box_callback)
        self.check_box.select()
        self.check_box.grid(row=2, column=1, pady=(0, 20))

        self.entry_ports_test = ctk.CTkEntry(self, state='disabled', width=200)
        self.entry_ports_test.grid(row=3, column=1, pady=(0, 20))

    def check_box_callback(self):
        self.check_box_state = not self.check_box_state

        if self.check_box_state is True:
            self.entry_ports_test.configure(self, state='disabled', placeholder_text="")
        else:
            self.entry_ports_test.configure(self, state='normal', placeholder_text="wady portów")
