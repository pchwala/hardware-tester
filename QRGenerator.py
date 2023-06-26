import customtkinter
import qrcode
import re

class QRMainFrame(customtkinter.CTkFrame):
    def __init__(self, master, output):
        super().__init__(master)

        self.output = output

        self.input_data = "VOID"

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.label1 = customtkinter.CTkLabel(self, text='')

        self.ant_switch = ""
        self.pods_switch = "brak"
        self.m2_switch = ""
        self.sata25_switch = ""
        self.wwan_switch = ""
        self.oryg_switch = "tak"

        self.polska_switch = ""

    def make_qr(self, camera_checkbox, sound_checkbox, keyboard_checkbox, polska_checkbox):

        keyboard = self.output.entry_keyboard.get()
        laptop_class = self.output.entry_class.get()
        ports = self.output.entry_ports.get()
        camera = self.output.entry_camera.get()
        sound = self.output.entry_sound.get()
        monitor = self.output.entry_monitor.get()
        notes = self.output.entry_notes.get()

        LAN_switch = "ok"
        WLAN_switch = ""
        camera_switch = "Cam"
        sound_switch = "ok"

        if re.search(r'2\.5', self.output.HDD1_value) is not None:
            self.sata25_switch = "tak"

        # TUTAJ CHYBA JESZCZE DODAC M.2!!!!!
        if re.search(r'NVMe', self.output.HDD1_value) is not None:
            self.m2_switch = "tak"

        if camera_checkbox is False:
            camera_switch = "uszk"

        if sound_checkbox is False:
            sound_switch = "uszk"

        if keyboard_checkbox is True:
            self.pods_switch = "tak"

        if polska_checkbox == "Polska":
            self.polska_switch = "2"

        compiled_notes = ""

        if ports != '':
            compiled_notes += ports + ", "

        if camera != '':
            compiled_notes += camera + ", "

        if sound != '':
            compiled_notes += sound + ", "

        if monitor != '':
            compiled_notes += monitor + ", "

        compiled_notes += notes

        self.input_data = "\t\t"\
                        + self.output.serial + "\t"\
                        + self.output.manufacturer + "\t"\
                        + self.output.model + "\t"\
                        + self.output.CPU_model + "\t"\
                        + self.output.RAM_value + "\t"\
                        + self.output.HDD1_value + "\t"\
                        + self.output.HDD2_value + "\t"\
                        + self.output.GPU_model + "\t"\
                        + self.output.battery_health + "\t"\
                        + self.output.monitor_size + "\t"\
                        + self.output.resolution + "\t"\
                        + LAN_switch + "\t"\
                        + WLAN_switch + "\t"\
                        + camera_switch + "\t"\
                        + sound_switch + "\t" \
                        + keyboard + "\t"\
                        + self.pods_switch + "\t"\
                        + self.output.license + "\t"\
                        + laptop_class + "\t"\
                        + compiled_notes + "\t\t\t\t\t\t\t\t\t"\
                        + self.ant_switch + "\t"\
                        + self.pods_switch + "\t"\
                        + self.m2_switch + "\t"\
                        + self.sata25_switch + "\t"\
                        + self.wwan_switch + "\t"\
                        + self.oryg_switch + "\t"\

        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)

        qr.add_data(self.input_data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save('qrcode.png')
        output_image = customtkinter.CTkImage(None, dark_image=img.get_image(), size=(512, 512))
        self.label1 = customtkinter.CTkLabel(self, image=output_image, text='')
        self.label1.grid(row=1, column=1)