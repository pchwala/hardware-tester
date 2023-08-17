import customtkinter


class CreditsWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("520x300")
        self.title("")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.label1 = customtkinter.CTkLabel(self, text="Skróty klawiszowe:")
        self.label1.cget("font").configure(size=20)
        self.label1.grid(row=0, column=1, pady=(20, 20))

        self.label2 = customtkinter.CTkLabel(self, text="SHIFT + >")
        self.label2.grid(row=1, column=0, padx=(20, 0), sticky="w")
        self.label22 = customtkinter.CTkLabel(self, text="Następny tester")
        self.label22.grid(row=1, column=2, padx=(0, 20), sticky="w")

        self.label3 = customtkinter.CTkLabel(self, text="SHIFT + <")
        self.label3.grid(row=2, column=0, padx=(20, 0), sticky="w")
        self.label32 = customtkinter.CTkLabel(self, text="Poprzedni tester")
        self.label32.grid(row=2, column=2, padx=(0, 20), sticky="w")

        self.label4 = customtkinter.CTkLabel(self, text="SHIFT + ENTER")
        self.label4.grid(row=3, column=0, padx=(20, 0), sticky="w")
        self.label42 = customtkinter.CTkLabel(self, text="Wybór pola z opisem wady")
        self.label42.grid(row=3, column=2, padx=(0, 20), sticky="w")

        self.label5 = customtkinter.CTkLabel(self, text="CTRL + C")
        self.label5.grid(row=4, column=0, padx=(20, 0), sticky="w")
        self.label52 = customtkinter.CTkLabel(self, text="Zatrzymaj/uruchom ponownie tester")
        self.label52.grid(row=4, column=2, padx=(0, 20), sticky="w")

        self.label6 = customtkinter.CTkLabel(self, text="CTRL + R")
        self.label6.grid(row=5, column=0, padx=(20, 0), sticky="w")
        self.label62 = customtkinter.CTkLabel(self, text="Reset")
        self.label62.grid(row=5, column=2, padx=(0, 20), sticky="w")

        self.label7 = customtkinter.CTkLabel(self, text="Design and programming:\nPrzemysław Chwała, 08.2023")
        self.label7.configure(justify="left", text_color="RoyalBlue1")
        self.label7.cget("font").configure(size=20)
        self.label7.grid(row=6, column=0, columnspan=3, pady=(20, 20), padx=(20, 0), sticky="w")
