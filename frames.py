import customtkinter as ctk


#   LEFT SIDE frame containing all the data gathered during tests
class OutputFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.serial = ""
        self.manufacturer = ""
        self.model = ""
        self.CPU_model = ""
        self.RAM_value = ""
        self.HDD1_value = ""
        self.HDD2_value = ""
        self.GPU_model = ""
        self.battery_health = ""
        self.monitor_size = ""
        self.resolution = ""
        self.license = ""

        self.battery0 = ""
        self.battery1 = ""

        self.label_sn = ctk.CTkLabel(self, text="Serial Number: ")
        self.label_sn.grid(row=0, column=0, padx=10, pady=2, sticky="ns")

        self.label_manufacturer = ctk.CTkLabel(self, text="Producent: ")
        self.label_manufacturer.grid(row=1, column=0, padx=10, pady=2, sticky="ns")

        self.label_model = ctk.CTkLabel(self, text="Model: ")
        self.label_model.grid(row=2, column=0, padx=10, pady=2, sticky="ns")

        self.label_cpu = ctk.CTkLabel(self, text="CPU: ")
        self.label_cpu.grid(row=3, column=0, padx=10, pady=2, sticky="ns")

        self.label_ram = ctk.CTkLabel(self, text="RAM: ")
        self.label_ram.grid(row=4, column=0, padx=10, pady=2, sticky="ns")

        self.label_hdd1 = ctk.CTkLabel(self, text="Dysk: ")
        self.label_hdd1.grid(row=5, column=0, padx=10, pady=2, sticky="ns")

        self.label_hdd2 = ctk.CTkLabel(self, text="Dysk 2: ")
        self.label_hdd2.grid(row=6, column=0, padx=10, pady=2, sticky="ns")

        self.label_gpu = ctk.CTkLabel(self, text="GPU: ")
        self.label_gpu.grid(row=7, column=0, padx=10, pady=2, sticky="ns")

        self.label_battery = ctk.CTkLabel(self, text="Bateria: ")
        self.label_battery.grid(row=8, column=0, padx=10, pady=2, sticky="ns")

        self.label_display = ctk.CTkLabel(self, text="Wyświetlacz: ")
        self.label_display.grid(row=9, column=0, padx=10, pady=2, sticky="ns")

        self.label_resolution = ctk.CTkLabel(self, text="Rozdzielczość: ")
        self.label_resolution.grid(row=10, column=0, padx=10, pady=2, sticky="ns")

        self.label_keyboard = ctk.CTkLabel(self, text="Layout: ")
        self.label_keyboard.grid(row=11, column=0, padx=10, pady=2, sticky="ns")

        self.label_license = ctk.CTkLabel(self, text="Licencja: ")
        self.label_license.grid(row=12, column=0, padx=10, pady=2, sticky="ns")

        self.label_ports = ctk.CTkLabel(self, text="Porty: ")
        self.label_ports.grid(row=13, column=0, padx=10, pady=2, sticky="ns")

        self.label_camera = ctk.CTkLabel(self, text="Kamera: ")
        self.label_camera.grid(row=14, column=0, padx=10, pady=2, sticky="ns")

        self.label_sound = ctk.CTkLabel(self, text="Dźwięk: ")
        self.label_sound.grid(row=15, column=0, padx=10, pady=2, sticky="ns")

        self.label_keyboard_notes = ctk.CTkLabel(self, text="Klawiatura: ")
        self.label_keyboard_notes.grid(row=16, column=0, padx=10, pady=2, sticky="ns")

        self.label_monitor = ctk.CTkLabel(self, text="Matryca: ")
        self.label_monitor.grid(row=17, column=0, padx=10, pady=2, sticky="ns")

        self.label_class = ctk.CTkLabel(self, text="Klasa: ")
        self.label_class.grid(row=18, column=0, padx=10, pady=2, sticky="ns")

        self.label_notes = ctk.CTkLabel(self, text="Uwagi: ")
        self.label_notes.grid(row=19, column=0, padx=10, pady=2, sticky="ns")

        self.entry_sn = ctk.CTkEntry(self, width=400)
        self.entry_sn.grid(row=0, column=1, padx=(0, 10))

        self.entry_manufacturer = ctk.CTkEntry(self, width=400)
        self.entry_manufacturer.grid(row=1, column=1, padx=(0, 10))

        self.entry_model = ctk.CTkEntry(self, width=400)
        self.entry_model.grid(row=2, column=1, padx=(0, 10))

        self.entry_cpu = ctk.CTkEntry(self, width=400)
        self.entry_cpu.grid(row=3, column=1, padx=(0, 10))

        self.entry_ram = ctk.CTkEntry(self, width=400)
        self.entry_ram.grid(row=4, column=1, padx=(0, 10))

        self.entry_hdd1 = ctk.CTkEntry(self, width=400)
        self.entry_hdd1.grid(row=5, column=1, padx=(0, 10))

        self.entry_hdd2 = ctk.CTkEntry(self, width=400)
        self.entry_hdd2.grid(row=6, column=1, padx=(0, 10))

        self.entry_gpu = ctk.CTkEntry(self, width=400)
        self.entry_gpu.grid(row=7, column=1, padx=(0, 10))

        self.entry_battery = ctk.CTkEntry(self, width=400)
        self.entry_battery.grid(row=8, column=1, padx=(0, 10))

        self.entry_display = ctk.CTkEntry(self, width=400)
        self.entry_display.grid(row=9, column=1, padx=(0, 10))

        self.entry_resolution = ctk.CTkEntry(self, width=400)
        self.entry_resolution.grid(row=10, column=1, padx=(0, 10))

        self.entry_keyboard = ctk.CTkEntry(self, width=400)
        self.entry_keyboard.grid(row=11, column=1, padx=(0, 10))

        self.entry_license = ctk.CTkEntry(self, width=400)
        self.entry_license.grid(row=12, column=1, padx=(0, 10))

        self.entry_ports = ctk.CTkEntry(self, width=400)
        self.entry_ports.grid(row=13, column=1, padx=(0, 10))

        self.entry_camera = ctk.CTkEntry(self, width=400)
        self.entry_camera.grid(row=14, column=1, padx=(0, 10))

        self.entry_sound = ctk.CTkEntry(self, width=400)
        # self.entry_sound.insert(0, "ok")
        self.entry_sound.grid(row=15, column=1, padx=(0, 10))

        self.entry_keyboard_notes = ctk.CTkEntry(self, width=400)
        self.entry_keyboard_notes.grid(row=16, column=1, padx=(0, 10))

        self.entry_monitor = ctk.CTkEntry(self, width=400)
        self.entry_monitor.grid(row=17, column=1, padx=(0, 10))

        self.entry_class = ctk.CTkEntry(self, width=400)
        self.entry_class.grid(row=18, column=1, padx=(0, 10))

        self.entry_notes = ctk.CTkEntry(self, width=400)
        self.entry_notes.grid(row=19, column=1, padx=(0, 10))

    def read_hardware_info(self):

        with open("hwinfo.dat", 'r') as file:

            lines = file.read()
            data = []
            for line in lines.split('\n'):
                data.append(line)

            try:
                self.serial = data[0]
                self.manufacturer = data[1]
                self.model = data[2]
                self.CPU_model = data[3]
                self.HDD1_value = data[4]
                self.HDD2_value = data[5]
                self.RAM_value = data[6]
                self.GPU_model = data[7]
                self.battery_health = data[8]
                self.resolution = data[9]
                self.monitor_size = data[10]
                self.license = data[11]

            except IndexError:
                print("Cant read hardware info")

        # erase(truncate) file just in case
        open("hwinfo.dat", 'w').close()

    def fill_hardware_info(self):
        self.entry_sn.insert(0, self.serial)
        self.entry_manufacturer.insert(0, self.manufacturer)
        self.entry_model.insert(0, self.model)
        self.entry_cpu.insert(0, self.CPU_model)
        self.entry_hdd1.insert(0, self.HDD1_value)
        self.entry_hdd2.insert(0, self.HDD2_value)
        self.entry_ram.insert(0, self.RAM_value)
        self.entry_gpu.insert(0, self.GPU_model)
        self.entry_battery.insert(0, self.battery_health)
        self.entry_resolution.insert(0, self.resolution)
        self.entry_display.insert(0, self.monitor_size)
        self.entry_license.insert(0, self.license)

        self.entry_sn.configure(state="disabled")
        self.entry_manufacturer.configure(state="disabled")
        self.entry_model.configure(state="disabled")
        self.entry_cpu.configure(state="disabled")
        self.entry_hdd1.configure(state="disabled")
        self.entry_hdd2.configure(state="disabled")
        self.entry_ram.configure(state="disabled")
        self.entry_gpu.configure(state="disabled")
        self.entry_battery.configure(state="disabled")
        self.entry_resolution.configure(state="disabled")
        self.entry_display.configure(state="disabled")
        self.entry_license.configure(state="disabled")


#   UPPER frame, containing menu buttons
class TestersFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.notebook1 = ctk.CTkButton(self, text='Porty', width=70,
                                       command=lambda: master.button_menu_callback(1))
        self.notebook1.grid(row=0, column=1, padx=(30, 2), sticky="e")

        self.notebook2 = ctk.CTkButton(self, text='Kamera', width=70,
                                       command=lambda: master.button_menu_callback(2))
        self.notebook2.grid(row=0, column=2, padx=2, sticky="e")

        self.notebook3 = ctk.CTkButton(self, text='Mikrofon', width=70,
                                       command=lambda: master.button_menu_callback(3))
        self.notebook3.grid(row=0, column=3, padx=2, sticky="e")

        self.notebook4 = ctk.CTkButton(self, text='Głośniki', width=70,
                                       command=lambda: master.button_menu_callback(4))
        self.notebook4.grid(row=0, column=4, padx=2, sticky="e")

        self.notebook5 = ctk.CTkButton(self, text='Klawiatura', width=70,
                                       command=lambda: master.button_menu_callback(5))
        self.notebook5.grid(row=0, column=5, padx=2, sticky="e")

        self.notebook6 = ctk.CTkButton(self, text='Matryca', width=70,
                                       command=lambda: master.button_menu_callback(6))
        self.notebook6.grid(row=0, column=6, padx=2, sticky="e")

        self.notebook7 = ctk.CTkButton(self, text='Generuj QR', width=70,
                                       command=lambda: master.button_menu_callback(7))
        self.notebook7.grid(row=0, column=7, padx=2, sticky="e")
