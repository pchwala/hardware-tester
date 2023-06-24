import customtkinter
import qrcode


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

    def make_qr(self):

        keyboard = self.output.entry_keyboard.get()
        laptop_class = self.output.entry_class.get()
        ports = self.output.entry_ports.get()
        camera = self.output.entry_camera.get()
        sound = self.output.entry_sound.get()
        monitor = self.output.entry_monitor.get()
        notes = self.output.entry_notes.get()

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
                        + "ok\t"\
                        + "ok\t"\
                        + "Cam\t"\
                        + "ok\t" \
                        + keyboard + "\t"\
                        + "\t"\
                        + self.output.license + "\t"\
                        + laptop_class + "\t"\
                        + compiled_notes

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