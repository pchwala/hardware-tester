import subprocess
import re
import tkinter as tk
import customtkinter as ctk
from PIL import Image

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

        self.label_keyboard = ctk.CTkLabel(self, text="Klawiatura: ")
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
        self.entry_camera.insert(0, "Cam")
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
        all_info = self.exec_and_output('sudo dmidecode | grep -A 9 "System Information"')
        for line in all_info.split("\n"):
            if "Manufacturer" in line:
                self.manufacturer = re.sub(".*Manufacturer.*: ", "", line, 1)

            elif "Product Name" in line:
                self.model += re.sub(".*Product Name.*: ", "", line, 1)

            elif "Version" in line:
                self.model += " (" + re.sub(".*Version.*: ", "", line, 1) + ")"

            elif "Serial Number" in line:
                self.serial = re.sub(".*Serial Number.*: ", "", line, 1)

        disk_devices = []
        all_info = self.exec_and_output("sudo smartctl --scan")
        for line in all_info.split("\n"):
            temp = re.split(r'\s', line, 1)
            if '/dev' in temp[0]:
                disk_devices.append(temp[0])

        if len(disk_devices) > 0:
            self.HDD1_value = self.get_disk_info(disk_devices[0])
        if len(disk_devices) > 1:
            self.HDD2_value = self.get_disk_info(disk_devices[1])

        all_info = self.exec_and_output("sudo lshw -short")
        for line in all_info.split("\n"):
            if "System Memory" in line:
                self.RAM_value = re.search("\d*G", line).group(0) + "B"
                self.RAM_value = re.sub(r'GB', " GB", self.RAM_value, 1)

            if "processor" in line:
                temp = re.sub(".*processor\s*", "", line, 1)
                try:
                  self.CPU_model = re.search("i\d.*", temp).group(0)

                except AttributeError:
                    self.CPU_model = temp

            if "display" in line:
                temp = re.sub(".*display\s*", "", line, 1)
                # FORMATTING ERRORS CHECK FOR AMD GPUs
                temp = re.sub(".*\[", "", temp, 1)
                temp = re.sub("\]", "", temp, 1)
                self.GPU_model = temp

        all_info = self.exec_and_output("xdpyinfo | grep dimensions")
        self.resolution = re.search("\d+x\d+", all_info).group(0)
        if "1920x1080" in self.resolution:
            self.monitor_size = "FHD"
        elif "1366x768" in self.resolution:
            self.monitor_size = "HD"
        elif "2560x1440" in self.resolution:
            self.monitor_size = "QHD"

        command = "sudo hexdump -s 56 -e '" + '"MSDM key: " /29 "%s\n"' + "' /sys/firmware/acpi/tables/MSDM"
        try:
            all_info = self.exec_and_output(command)
            self.license = all_info
        except:
            self.license = "brak licencji"

        all_info = self.exec_and_output('acpi -bi')
        for line in all_info.split("\n"):
            if "Battery 0" in line:
                if "capacity" in line:
                    self.battery0 = re.search(r'\d*%', line).group(0)

            if "Battery 1" in line:
                if "capacity" in line:
                    try:
                        self.battery1 = re.search(r'\d*%', line).group(0)
                    except Exception:
                        self.battery1 = "XD"

        if (self.battery0 != "") and (self.battery1 != ""):
            self.battery_health = self.battery0 + "/" + self.battery1

        elif (self.battery0 != "") or (self.battery1 != ""):
            self.battery_health = self.battery0 + self.battery1

        else:
            self.battery_health = "brak"

    def exec_and_output(self, command):
        return subprocess.check_output(command, shell=True).decode().strip()

    def get_disk_info(self, device):
        command = "sudo smartctl -i " + device
        all_info = subprocess.check_output(command, shell=True).decode().strip()
        disk = ""
        model = ""

        if "nvm" in device:
            for line in all_info.split("\n"):
                if "Total" in line:
                    temp = re.sub(".*\[", "", line, 1)
                    disk += re.search("\d+ \w+", temp).group(0)
                    disk += " | NVMe"

                if "Model" in line:
                    model += re.sub("Model Number:\s*", "", line, 1)

            if model != "":
                disk += " | "
                disk += model

        else:
            for line in all_info.split("\n"):
                if "Capacity" in line:
                    temp = re.sub(".*\[", "", line, 1)
                    disk += re.search("\d* \w*", temp).group(0)
                    disk += " | "

                if "Rotation Rate" in line:
                    match = re.search("\d", line)
                    if match:
                        disk += "HDD"
                    else:
                        disk += "SSD"

                if "Form Factor" in line:
                    disk += " | "
                    disk += re.sub(".*Form Factor:\s*", "", line, 1)

                if "Device Model" in line:
                    model += re.sub(".*Device Model:\s*", "", line, 1)

            if model != "":
                disk += " | "
                disk += model

        print(disk)
        return disk


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
        self.entry_resolution.configure(state="disabled")
        self.entry_display.configure(state="disabled")
        self.entry_license.configure(state="disabled")


#   UPPER frame, containing menu buttons
class TestersFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.notebook1 = ctk.CTkButton(self, text='Porty', width=70,
                                                 command=lambda: self.master.button_menu_callback(1))
        self.notebook1.grid(row=0, column=1, padx=(30, 2), sticky="e")

        self.notebook2 = ctk.CTkButton(self, text='Kamera', width=70,
                                                 command=lambda: self.master.button_menu_callback(2))
        self.notebook2.grid(row=0, column=2, padx=2, sticky="e")

        self.notebook3 = ctk.CTkButton(self, text='Mikrofon', width=70,
                                                 command=lambda: self.master.button_menu_callback(3))
        self.notebook3.grid(row=0, column=3, padx=2, sticky="e")

        self.notebook4 = ctk.CTkButton(self, text='Głośniki', width=70,
                                                 command=lambda: self.master.button_menu_callback(4))
        self.notebook4.grid(row=0, column=4, padx=2, sticky="e")

        self.notebook5 = ctk.CTkButton(self, text='Klawiatura', width=70,
                                                 command=lambda: self.master.button_menu_callback(5))
        self.notebook5.grid(row=0, column=5, padx=2, sticky="e")

        self.notebook6 = ctk.CTkButton(self, text='Matryca', width=70,
                                                 command=lambda: self.master.button_menu_callback(6))
        self.notebook6.grid(row=0, column=6, padx=2, sticky="e")

        self.notebook7 = ctk.CTkButton(self, text='Generuj QR', width=70,
                                                 command=lambda: self.master.button_menu_callback(7))
        self.notebook7.grid(row=0, column=7, padx=2, sticky="e")


#   CENTRAL frame containing various testing subprograms
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


class CameraMainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)

        self.label1 = ctk.CTkLabel(self, text="TESTUJEMY KAMERĘ")
        self.label1.grid(row=0, column=1, pady=20)

        self.check_box_state = True
        self.check_box = ctk.CTkCheckBox(self, text="Działa?", onvalue=True, offvalue=False,
                                                   command=self.check_box_callback)
        self.check_box.select()
        self.check_box.grid(row=2, column=1, pady=(0, 20))

        self.entry_camera_test = ctk.CTkEntry(self, state='disabled', width=200)
        self.entry_camera_test.grid(row=3, column=1, pady=(0, 20))

    def check_box_callback(self):
        self.check_box_state = not self.check_box_state

        if self.check_box_state is True:
            self.entry_camera_test.configure(self, state='disabled', placeholder_text="")
        else:
            self.entry_camera_test.configure(self, state='normal', placeholder_text="wady kamery")

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
        self.grid_rowconfigure(3, weight=0)

        self.label1 = ctk.CTkLabel(self, image=self.play_image, text='')
        self.label1.grid(row=0, column=1)

        self.check_box_state = True
        self.check_box = ctk.CTkCheckBox(self, text="Działa?", onvalue=True, offvalue=False,
                                                   command=self.check_box_callback)
        self.check_box.select()
        self.check_box.grid(row=2, column=1, pady=(0, 20))

        self.entry_both = ctk.CTkEntry(self, state='disabled', width=200)
        self.entry_both.grid(row=3, column=1, pady=(0, 20), sticky='ns')

    def check_box_callback(self):
        self.check_box_state = not self.check_box_state

        if self.check_box_state is True:
            self.entry_both.configure(self, state='disabled', placeholder_text="")
        else:
            self.entry_both.configure(self, state='normal', placeholder_text="wady głośników")

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

        self.check_box_state = True
        self.check_box = ctk.CTkCheckBox(self, text="Działa?", onvalue=True, offvalue=False,
                                                   command=self.check_box_callback)
        self.check_box.select()
        self.check_box.grid(row=2, column=1, pady=(0, 20))

    def check_box_callback(self):
        self.check_box_state = not self.check_box_state



class KeyboardMainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(17, weight=1)

        self.button_ESC = ctk.CTkButton(self, text="ESC", width=40, height=30, state="disabled")
        self.button_ESC.grid(row=0, column=1, padx=(10, 2), pady=(30, 5))
        self.button_F1 = ctk.CTkButton(self, text="F1", width=40, height=30, state="disabled")
        self.button_F1.grid(row=0, column=3, padx=(2, 2), pady=(30, 5))
        self.button_F2 = ctk.CTkButton(self, text="F2", width=40, height=30, state="disabled")
        self.button_F2.grid(row=0, column=4, padx=(2, 2), pady=(30, 5))
        self.button_F3 = ctk.CTkButton(self, text="F3", width=40, height=30, state="disabled")
        self.button_F3.grid(row=0, column=5, padx=(2, 2), pady=(30, 5))
        self.button_F4 = ctk.CTkButton(self, text="F4", width=40, height=30, state="disabled")
        self.button_F4.grid(row=0, column=6, padx=(2, 2), pady=(30, 5))
        self.button_F5 = ctk.CTkButton(self, text="F5", width=40, height=30, state="disabled")
        self.button_F5.grid(row=0, column=7, padx=(2, 2), pady=(30, 5))
        self.button_F6 = ctk.CTkButton(self, text="F6", width=40, height=30, state="disabled")
        self.button_F6.grid(row=0, column=8, padx=(2, 2), pady=(30, 5))
        self.button_F7 = ctk.CTkButton(self, text="F7", width=40, height=30, state="disabled")
        self.button_F7.grid(row=0, column=9, padx=(2, 2), pady=(30, 5))
        self.button_F8 = ctk.CTkButton(self, text="F8", width=40, height=30, state="disabled")
        self.button_F8.grid(row=0, column=10, padx=(2, 2), pady=(30, 5))
        self.button_F9 = ctk.CTkButton(self, text="F9", width=40, height=30, state="disabled")
        self.button_F9.grid(row=0, column=11, padx=(2, 2), pady=(30, 5))
        self.button_F10 = ctk.CTkButton(self, text="F10", width=40, height=30, state="disabled")
        self.button_F10.grid(row=0, column=12, padx=(2, 2), pady=(30, 5))
        self.button_F11 = ctk.CTkButton(self, text="F11", width=40, height=30, state="disabled")
        self.button_F11.grid(row=0, column=13, padx=(2, 2), pady=(30, 5))
        self.button_F12 = ctk.CTkButton(self, text="F12", width=40, height=30, state="disabled")
        self.button_F12.grid(row=0, column=14, padx=(2, 2), pady=(30, 5))

        self.button_grave = ctk.CTkButton(self, text="~", width=40, height=30, state="disabled")
        self.button_grave.grid(row=1, column=1, padx=(10, 2), pady=(5, 5))
        self.button_1 = ctk.CTkButton(self, text="1", width=40, height=30, state="disabled")
        self.button_1.grid(row=1, column=2, padx=(2, 2), pady=(5, 5))
        self.button_2 = ctk.CTkButton(self, text="2", width=40, height=30, state="disabled")
        self.button_2.grid(row=1, column=3, padx=(2, 2), pady=(5, 5))
        self.button_3 = ctk.CTkButton(self, text="3", width=40, height=30, state="disabled")
        self.button_3.grid(row=1, column=4, padx=(2, 2), pady=(5, 5))
        self.button_4 = ctk.CTkButton(self, text="4", width=40, height=30, state="disabled")
        self.button_4.grid(row=1, column=5, padx=(2, 2), pady=(5, 5))
        self.button_5 = ctk.CTkButton(self, text="5", width=40, height=30, state="disabled")
        self.button_5.grid(row=1, column=6, padx=(2, 2), pady=(5, 5))
        self.button_6 = ctk.CTkButton(self, text="6", width=40, height=30, state="disabled")
        self.button_6.grid(row=1, column=7, padx=(2, 2), pady=(5, 5))
        self.button_7 = ctk.CTkButton(self, text="7", width=40, height=30, state="disabled")
        self.button_7.grid(row=1, column=8, padx=(2, 2), pady=(5, 5))
        self.button_8 = ctk.CTkButton(self, text="8", width=40, height=30, state="disabled")
        self.button_8.grid(row=1, column=9, padx=(2, 2), pady=(5, 5))
        self.button_9 = ctk.CTkButton(self, text="9", width=40, height=30, state="disabled")
        self.button_9.grid(row=1, column=10, padx=(2, 2), pady=(5, 5))
        self.button_10 = ctk.CTkButton(self, text="10", width=40, height=30, state="disabled")
        self.button_10.grid(row=1, column=11, padx=(2, 2), pady=(5, 5))
        self.button_minus = ctk.CTkButton(self, text="-", width=40, height=30, state="disabled")
        self.button_minus.grid(row=1, column=12, padx=(2, 2), pady=(5, 5))
        self.button_equal = ctk.CTkButton(self, text="=", width=40, height=30, state="disabled")
        self.button_equal.grid(row=1, column=13, padx=(2, 2), pady=(5, 5))
        self.button_backspace = ctk.CTkButton(self, text="Backspace", width=80, height=30, state="disabled")
        self.button_backspace.grid(row=1, column=14, columnspan=2, padx=(2, 2), pady=(5, 5))

        self.button_Tab = ctk.CTkButton(self, text="Tab", width=80, height=30, state="disabled")
        self.button_Tab.grid(row=2, column=1, columnspan=2, padx=(10, 2), pady=(5, 5))
        self.button_q = ctk.CTkButton(self, text="Q", width=40, height=30, state="disabled")
        self.button_q.grid(row=2, column=3, padx=(2, 2), pady=(5, 5))
        self.button_w = ctk.CTkButton(self, text="W", width=40, height=30, state="disabled")
        self.button_w.grid(row=2, column=4, padx=(2, 2), pady=(5, 5))
        self.button_e = ctk.CTkButton(self, text="E", width=40, height=30, state="disabled")
        self.button_e.grid(row=2, column=5, padx=(2, 2), pady=(5, 5))
        self.button_r = ctk.CTkButton(self, text="R", width=40, height=30, state="disabled")
        self.button_r.grid(row=2, column=6, padx=(2, 2), pady=(5, 5))
        self.button_t = ctk.CTkButton(self, text="T", width=40, height=30, state="disabled")
        self.button_t.grid(row=2, column=7, padx=(2, 2), pady=(5, 5))
        self.button_y = ctk.CTkButton(self, text="Y", width=40, height=30, state="disabled")
        self.button_y.grid(row=2, column=8, padx=(2, 2), pady=(5, 5))
        self.button_u = ctk.CTkButton(self, text="U", width=40, height=30, state="disabled")
        self.button_u.grid(row=2, column=9, padx=(2, 2), pady=(5, 5))
        self.button_i = ctk.CTkButton(self, text="I", width=40, height=30, state="disabled")
        self.button_i.grid(row=2, column=10, padx=(2, 2), pady=(5, 5))
        self.button_o = ctk.CTkButton(self, text="O", width=40, height=30, state="disabled")
        self.button_o.grid(row=2, column=11, padx=(2, 2), pady=(5, 5))
        self.button_p = ctk.CTkButton(self, text="P", width=40, height=30, state="disabled")
        self.button_p.grid(row=2, column=12, padx=(2, 2), pady=(5, 5))
        self.button_bracketL = ctk.CTkButton(self, text="[", width=40, height=30, state="disabled")
        self.button_bracketL.grid(row=2, column=13, padx=(2, 2), pady=(5, 5))
        self.button_bracketR = ctk.CTkButton(self, text="]", width=40, height=30, state="disabled")
        self.button_bracketR.grid(row=2, column=14, padx=(2, 2), pady=(5, 5))
        self.button_backslash = ctk.CTkButton(self, text="\ |", width=40, height=30, state="disabled")
        self.button_backslash.grid(row=2, column=15, padx=(2, 2), pady=(5, 5))

        self.button_Caps = ctk.CTkButton(self, text="Caps", width=80, height=30, state="disabled")
        self.button_Caps.grid(row=3, column=1, columnspan=2, padx=(10, 2), pady=(5, 5))
        self.button_a = ctk.CTkButton(self, text="A", width=40, height=30, state="disabled")
        self.button_a.grid(row=3, column=3, padx=(2, 2), pady=(5, 5))
        self.button_s = ctk.CTkButton(self, text="S", width=40, height=30, state="disabled")
        self.button_s.grid(row=3, column=4, padx=(2, 2), pady=(5, 5))
        self.button_d = ctk.CTkButton(self, text="D", width=40, height=30, state="disabled")
        self.button_d.grid(row=3, column=5, padx=(2, 2), pady=(5, 5))
        self.button_f = ctk.CTkButton(self, text="F", width=40, height=30, state="disabled")
        self.button_f.grid(row=3, column=6, padx=(2, 2), pady=(5, 5))
        self.button_g = ctk.CTkButton(self, text="G", width=40, height=30, state="disabled")
        self.button_g.grid(row=3, column=7, padx=(2, 2), pady=(5, 5))
        self.button_h = ctk.CTkButton(self, text="H", width=40, height=30, state="disabled")
        self.button_h.grid(row=3, column=8, padx=(2, 2), pady=(5, 5))
        self.button_j = ctk.CTkButton(self, text="J", width=40, height=30, state="disabled")
        self.button_j.grid(row=3, column=9, padx=(2, 2), pady=(5, 5))
        self.button_k = ctk.CTkButton(self, text="K", width=40, height=30, state="disabled")
        self.button_k.grid(row=3, column=10, padx=(2, 2), pady=(5, 5))
        self.button_l = ctk.CTkButton(self, text="L", width=40, height=30, state="disabled")
        self.button_l.grid(row=3, column=11, padx=(2, 2), pady=(5, 5))
        self.button_semicolon = ctk.CTkButton(self, text="; :", width=40, height=30, state="disabled")
        self.button_semicolon.grid(row=3, column=12, padx=(2, 2), pady=(5, 5))
        self.button_apostrophe = ctk.CTkButton(self, text="\' \"", width=40, height=30, state="disabled")
        self.button_apostrophe.grid(row=3, column=13, padx=(2, 2), pady=(5, 5))
        self.button_Return = ctk.CTkButton(self, text="Enter", width=80, height=30, state="disabled")
        self.button_Return.grid(row=3, column=14, columnspan=2, padx=(2, 2), pady=(5, 5))

        self.button_Shift_L = ctk.CTkButton(self, text="Shift", width=80, height=30, state="disabled")
        self.button_Shift_L.grid(row=4, column=1, columnspan=2, padx=(10, 2), pady=(5, 5))
        self.button_z = ctk.CTkButton(self, text="Z", width=40, height=30, state="disabled")
        self.button_z.grid(row=4, column=3, padx=(2, 2), pady=(5, 5))
        self.button_x = ctk.CTkButton(self, text="X", width=40, height=30, state="disabled")
        self.button_x.grid(row=4, column=4, padx=(2, 2), pady=(5, 5))
        self.button_c = ctk.CTkButton(self, text="C", width=40, height=30, state="disabled")
        self.button_c.grid(row=4, column=5, padx=(2, 2), pady=(5, 5))
        self.button_v = ctk.CTkButton(self, text="V", width=40, height=30, state="disabled")
        self.button_v.grid(row=4, column=6, padx=(2, 2), pady=(5, 5))
        self.button_b = ctk.CTkButton(self, text="B", width=40, height=30, state="disabled")
        self.button_b.grid(row=4, column=7, padx=(2, 2), pady=(5, 5))
        self.button_n = ctk.CTkButton(self, text="N", width=40, height=30, state="disabled")
        self.button_n.grid(row=4, column=8, padx=(2, 2), pady=(5, 5))
        self.button_m = ctk.CTkButton(self, text="M", width=40, height=30, state="disabled")
        self.button_m.grid(row=4, column=9, padx=(2, 2), pady=(5, 5))
        self.button_comma = ctk.CTkButton(self, text=", <", width=40, height=30, state="disabled")
        self.button_comma.grid(row=4, column=10, padx=(2, 2), pady=(5, 5))
        self.button_period = ctk.CTkButton(self, text=". >", width=40, height=30, state="disabled")
        self.button_period.grid(row=4, column=11, padx=(2, 2), pady=(5, 5))
        self.button_slash = ctk.CTkButton(self, text="/ ?", width=40, height=30, state="disabled")
        self.button_slash.grid(row=4, column=12, padx=(2, 2), pady=(5, 5))
        self.button_Shift_R = ctk.CTkButton(self, text="Shift", width=120, height=30, state="disabled")
        self.button_Shift_R.grid(row=4, column=13, columnspan=3, padx=(2, 2), pady=(5, 5))

        self.button_Control_L = ctk.CTkButton(self, text="Ctrl", width=40, height=30, state="disabled")
        self.button_Control_L.grid(row=5, column=2, padx=(2, 2), pady=(5, 5))
        self.button_Super_L = ctk.CTkButton(self, text="Win", width=40, height=30, state="disabled")
        self.button_Super_L.grid(row=5, column=3, padx=(2, 2), pady=(5, 5))
        self.button_Alt_L = ctk.CTkButton(self, text="Alt", width=40, height=30, state="disabled")
        self.button_Alt_L.grid(row=5, column=4, padx=(2, 2), pady=(5, 5))
        self.button_space = ctk.CTkButton(self, text="Space", width=280, height=30, state="disabled")
        self.button_space.grid(row=5, column=5, columnspan=7, padx=(2, 2), pady=(5, 5))
        self.button_Alt_R = ctk.CTkButton(self, text="Alt", width=40, height=30, state="disabled")
        self.button_Alt_R.grid(row=5, column=12, padx=(2, 2), pady=(5, 5))
        self.button_Menu = ctk.CTkButton(self, text="Sel", width=40, height=30, state="disabled")
        self.button_Menu.grid(row=5, column=13, padx=(2, 2), pady=(5, 5))
        self.button_Control_R = ctk.CTkButton(self, text="Ctrl", width=40, height=30, state="disabled")
        self.button_Control_R.grid(row=5, column=14, padx=(2, 2), pady=(5, 5))


        self.button_references = [self.button_ESC, self.button_F1, self.button_F2, self.button_F3, self.button_F4,
                                  self.button_F5, self.button_F6, self.button_F7, self.button_F8, self.button_F9,
                                  self.button_F10, self.button_F11, self.button_F12,
                                  self.button_grave, self.button_1, self.button_2, self.button_3, self.button_4,
                                  self.button_5, self.button_6, self.button_7, self.button_8, self.button_9,
                                  self.button_10, self.button_minus, self.button_equal, self.button_backspace,
                                  self.button_Tab, self.button_q, self.button_w, self.button_e, self.button_r,
                                  self.button_t, self.button_y, self.button_u, self.button_i, self.button_o,
                                  self.button_p, self.button_bracketL, self.button_bracketR, self.button_backslash,
                                  self.button_Caps, self.button_a, self.button_s, self.button_d, self.button_f,
                                  self.button_g, self.button_h, self.button_j, self.button_k, self.button_l,
                                  self.button_semicolon, self.button_apostrophe, self.button_Return,
                                  self.button_Shift_L, self.button_z, self.button_x, self.button_c, self.button_v,
                                  self.button_b, self.button_n, self.button_m, self.button_comma, self.button_period,
                                  self.button_slash, self.button_Shift_R, self.button_Control_L, self.button_Super_L,
                                  self.button_Alt_L, self.button_space, self.button_Alt_R, self.button_Menu,
                                  self.button_Control_R]

        self.key_names = ['Escape', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
                          'grave', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'minus', 'equal', 'BackSpace',
                          'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'bracketleft', 'bracketright',
                          'backslash', 'Caps_Lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'semicolon',
                          'apostrophe', 'Return', 'Shift_L', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'comma', 'period',
                          'slash', 'Shift_R', 'Control_L', 'Super_L', 'Alt_L', 'space', 'ISO_Level3_Shift', 'Menu',
                          'Control_R']

        self.alt_key_names = ['Escape', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
                              'grave', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'minus', 'equal', 'BackSpace',
                              'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'bracketleft', 'bracketright',
                              'backslash', 'Caps_Lock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'semicolon',
                              'apostrophe', 'Return', 'Shift_L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'comma', 'period',
                              'slash', 'Shift_R', 'Control_L', 'Super_L', 'Alt_L', 'space', 'ISO_Level3_Shift', 'Menu',
                              'Control_R']

    def mark_key(self, index, key_state):
        match key_state:
            case 'keydown':
                self.button_references[index].configure(fg_color="yellow")

            case 'keyup':
                self.button_references[index].configure(fg_color="green")

    def key_event(self, key, key_state):
        try:
            index = self.key_names.index(key)
            self.mark_key(index, key_state)
        except ValueError:
            pass

        try:
            index = self.alt_key_names.index(key)
            self.mark_key(index, key_state)
        except ValueError:
            pass