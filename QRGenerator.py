import customtkinter
import qrcode
import re


class QRMainFrame(customtkinter.CTkFrame):
    def __init__(self, master, output, monitor):
        super().__init__(master)

        self.output = output
        self.monitor = monitor

        self.input_data = "VOID"

        self.compiled_notes = ""

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.label1 = customtkinter.CTkLabel(self, text='')

    def make_qr(self, camera_checkbox, sound_checkbox, keyboard_checkbox, wlan_status):

        keyboard_notes = self.output.entry_keyboard_notes.get()
        keyboard_layout = self.output.entry_keyboard.get()
        ports = self.output.entry_ports.get()
        camera = self.output.entry_camera.get()
        sound = self.output.entry_sound.get()
        monitor = self.output.entry_monitor.get()
        notes = self.output.entry_notes.get()

        touchscreen_segmented = self.monitor.touchscreen_segmented.get()
        laptop_class = self.monitor.class_segmented.get()
        polska_segmented = self.monitor.polska_segmented.get()

        LAN_switch = "ok"
        if wlan_status == True:
            WLAN_switch = "wifi-ok"
        else:
            WLAN_switch = "wifi-brak"

        ant_switch = ""
        m2_switch = ""
        sata25_switch = ""
        wwan_switch = ""
        oryg_switch = "tak"

        if re.search(r'2\.5', self.output.HDD1_value) is not None:
            sata25_switch = "tak"

        if re.search(r'NVMe', self.output.HDD1_value) is not None:
            m2_switch = "tak"

        if re.search(r'SSD', self.output.HDD1_value) is not None:
            if sata25_switch == "":
                m2_switch = "tak"

        if touchscreen_segmented == "Brak dotyku":
            touchscreen = ""
        else:
            touchscreen = " Dotyk"

        if camera_checkbox is False:
            camera_switch = "uszk C"
        else:
            camera_switch = "Cam"

        if sound_checkbox is False:
            sound_switch = "uszk S"
        else:
            sound_switch = "ok"

        if keyboard_checkbox is True:
            pods_switch = "pods"
        else:
            pods_switch = "brak"

        if polska_segmented == "Polska":
            polska_switch = "2"
        else:
            polska_switch = ""

        self.compiled_notes = ""

        if ports != '':
            self.compiled_notes += ports + ", "

        if camera != '':
            self.compiled_notes += camera + ", "

        if sound != '':
            self.compiled_notes += sound + ", "

        if keyboard_notes != '':
            self.compiled_notes += keyboard_notes + ", "

        if monitor != '':
            self.compiled_notes += monitor + ", "

        self.compiled_notes += notes

        if self.monitor.check_box1.get() == 1:
            self.compiled_notes += " | klapa porysowana"

        if self.monitor.check_box2.get() == 1:
            self.compiled_notes += " | klapa wytarta"

        if self.monitor.check_box3.get() == 1:
            self.compiled_notes += " | lakier odchodzi"

        if self.monitor.check_box4.get() == 1:
            self.compiled_notes += " | klawiatura wytarta"

        if self.monitor.check_box5.get() == 1:
            self.compiled_notes += " | touchpad wytarty"

        if self.monitor.check_box6.get() == 1:
            self.compiled_notes += " | palmrest wytarty"

        if self.monitor.check_box7.get() == 1:
            self.compiled_notes += " | wyrazny hotspot"

        if self.monitor.check_box8.get() == 1:
            self.compiled_notes += " | wyrazna rysa"

        if self.monitor.check_box9.get() == 1:
            self.compiled_notes += " | badpixele"

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
                        + self.output.monitor_size + touchscreen + "\t"\
                        + self.output.resolution + "\t"\
                        + LAN_switch + "\t"\
                        + WLAN_switch + "\t"\
                        + camera_switch + "\t"\
                        + sound_switch + "\t" \
                        + keyboard_layout + "\t"\
                        + polska_switch + "\t"\
                        + self.output.license + "\t"\
                        + laptop_class + "\t"\
                        + self.compiled_notes + "\t\t\t\t\t\t\t\t\t"\
                        + ant_switch + "\t"\
                        + pods_switch + "\t"\
                        + m2_switch + "\t"\
                        + sata25_switch + "\t"\
                        + wwan_switch + "\t"\
                        + oryg_switch + "\t"\

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
