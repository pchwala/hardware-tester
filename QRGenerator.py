import customtkinter
import qrcode
import re
import numpy as np
from PIL import Image


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

        self.size_x = 512
        self.size_y = 512
        self.size = (self.size_x, self.size_y)
        
        # Game of Life attributes
        self.game_grid = None
        self.game_running = False
        self.update_job = None

    def rescale(self, width, height):
        self.size_x = int(self.size_x * width * 1.25)
        self.size_y = int(self.size_y * height * 1.25)
        self.size = (self.size_x, self.size_y)

    def make_qr(self, camera_checkbox, sound_checkbox, wlan_status, touchpad):

        keyboard_notes = self.output.entry_keyboard_notes.get()
        keyboard_layout = self.output.entry_keyboard.get()
        ports = self.output.entry_ports.get()
        camera = self.output.entry_camera.get()
        sound = self.output.entry_sound.get()
        monitor = self.output.entry_monitor.get()
        notes = self.output.entry_notes.get()
        model = self.output.entry_model.get()
        magazyn = self.output.entry_magazyn.get()
        nrzwrotu = self.output.entry_nrzwrotu.get()
        nrid = self.output.entry_id.get()

        # Get button states instead of segmented button values
        backlight_state = self.monitor.backlight_state
        touchscreen_state = self.monitor.touchscreen_state
        laptop_class = self.monitor.class_segmented.get()
        if laptop_class == ' ': laptop_class = 'A-'
        polska_segmented = self.monitor.polska_segmented.get()

        klapa_gorna = "X" if self.monitor.checkbox_klapa_gorna.get() == 1 else ""
        klapa_dolna = "X" if self.monitor.checkbox_klapa_dolna.get() == 1 else ""
        matryca = "X" if self.monitor.checkbox_matryca.get() == 1 else ""
        ramka = "X" if self.monitor.checkbox_ramka.get() == 1 else ""
        palmrest = "X" if self.monitor.checkbox_palmrest.get() == 1 else ""
        touchpad_odnowienie = "X" if self.monitor.checkbox_touchpad.get() == 1 else ""
        LAN_switch = "ok"
        if wlan_status is True:
            WLAN_switch = "ok"
        else:
            WLAN_switch = "brak"

        ant_switch = ""
        m2_switch = ""
        sata25_switch = ""
        wwan_switch = ""
        oryg_switch = ""
        polska_switch = ""

        if re.search(r'2\.5', self.output.HDD1_value) is not None:
            sata25_switch = "tak"

        if re.search(r'NVMe', self.output.HDD1_value) is not None:
            m2_switch = "tak"

        if re.search(r'SSD', self.output.HDD1_value) is not None:
            if sata25_switch == "":
                m2_switch = "tak"

        if touchscreen_state:
            touchscreen = " Dotyk"
        else:
            touchscreen = ""

        if backlight_state:
            pods_switch = "pods"
        else:
            pods_switch = ""

        if camera_checkbox is False:
            camera_switch = "uszk"
        else:
            camera_switch = "Cam"

        if sound_checkbox is False:
            sound_switch = "uszk"
        else:
            sound_switch = "ok"

        if polska_segmented == "2":
            polska_switch = "2"
        else:
            if laptop_class == "A":
                polska_switch = "ZAG"

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

        if touchpad != "":
            if self.compiled_notes != "":
                self.compiled_notes += " | "
            self.compiled_notes += touchpad

        self.input_data = "\t\t"\
                        + self.output.serial + "\t"\
                        + self.output.manufacturer + "\t"\
                        + model + "\t"\
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
                        + self.compiled_notes + "\t"\
                        + nrzwrotu + "\t\t"\
                        + magazyn + "\t"\
                        + nrid + "\t\t\t\t\t"\
                        + ant_switch + "\t\t\t\t\t\t"\
                        + klapa_gorna + "\t"\
                        + palmrest + "\t"\
                        + klapa_dolna + "\t"\
                        + ramka + "\t"\
                        + touchpad_odnowienie + "\t\t"\
                        + matryca

        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)

        qr.add_data(self.input_data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save('qrcode.png')
        
        # Convert QR code to numpy array for Game of Life
        pil_img = img.get_image()
        pil_img = pil_img.resize((200, 200))  # Resize for better performance
        img_array = np.array(pil_img.convert('L'))
        # Create binary grid: 1 for black (alive), 0 for white (dead)
        self.game_grid = (img_array < 128).astype(int)
        
        output_image = customtkinter.CTkImage(None, dark_image=pil_img, size=self.size)
        self.label1 = customtkinter.CTkLabel(self, image=output_image, text='')
        self.label1.grid(row=1, column=1)
        
        # Start Game of Life simulation
        self.game_running = True
        self.update_game_of_life()
    
    def count_neighbors(self, grid, row, col):
        """Count alive neighbors for a cell"""
        rows, cols = grid.shape
        count = 0
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                    
                # Wrap around edges (toroidal topology)
                neighbor_row = (row + i) % rows
                neighbor_col = (col + j) % cols
                count += grid[neighbor_row, neighbor_col]
        
        return count
    
    def next_generation(self):
        """Compute next generation according to Conway's Game of Life rules"""
        if self.game_grid is None:
            return
        
        rows, cols = self.game_grid.shape
        new_grid = np.zeros_like(self.game_grid)
        
        for i in range(rows):
            for j in range(cols):
                neighbors = self.count_neighbors(self.game_grid, i, j)
                
                # Conway's Game of Life rules:
                if self.game_grid[i, j] == 1:  # Cell is alive
                    if neighbors in [2, 3]:
                        new_grid[i, j] = 1  # Survives
                else:  # Cell is dead
                    if neighbors == 3:
                        new_grid[i, j] = 1  # Becomes alive
        
        self.game_grid = new_grid
    
    def update_game_of_life(self):
        """Update Game of Life display (refresh every 1 second)"""
        if not self.game_running or self.game_grid is None:
            return
        
        # Compute next generation
        self.next_generation()
        
        # Convert grid to image
        img_array = (self.game_grid * 255).astype(np.uint8)
        img_array = 255 - img_array  # Invert: 0=white, 255=black
        pil_img = Image.fromarray(img_array, mode='L')
        
        # Update display
        output_image = customtkinter.CTkImage(None, dark_image=pil_img, size=self.size)
        self.label1.configure(image=output_image)
        self.label1.image = output_image  # Keep a reference
        
        # Schedule next update (1000ms = 1 second)
        self.update_job = self.after(1000, self.update_game_of_life)
    
    def stop_game_of_life(self):
        """Stop the Game of Life simulation"""
        self.game_running = False
        if self.update_job is not None:
            self.after_cancel(self.update_job)
            self.update_job = None
