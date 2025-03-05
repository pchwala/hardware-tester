import customtkinter
import tkinter


class MonitorMainFrame(customtkinter.CTkFrame):
    def __init__(self, master, output):
        super().__init__(master)

        # Configure grid like this:
        #    0 1 2 3 4
        # 0 |_|_|_|_|_|
        # 1 |_|_|_|_|_|
        # 2 |_|_|_|_|_|
        #    .....

        self.output = output

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.label1 = customtkinter.CTkLabel(self, text="Statusy:")
        self.label1.cget("font").configure(size=20)
        self.label1.grid(row=2, column=2, pady=(0, 20))

        self.label_wwan1 = customtkinter.CTkLabel(self, text="WWAN:")
        self.label_wwan1.cget("font").configure(size=14)
        self.label_wwan1.grid(row=9, column=1, pady=(0, 20), sticky="e")
        self.label_wwan2 = customtkinter.CTkLabel(self, text="Nie wykryto", text_color="red")
        self.label_wwan2.cget("font").configure(size=14)
        self.label_wwan2.grid(row=9, column=2, pady=(0, 20))

        self.label_backlight1 = customtkinter.CTkLabel(self, text="Podswietlenie:")
        self.label_backlight1.cget("font").configure(size=14)
        self.label_backlight1.grid(row=10, column=1, pady=(0, 20), sticky="e")
        self.label_backlight2 = customtkinter.CTkLabel(self, text="Nie wykryto", text_color="red")
        self.label_backlight2.cget("font").configure(size=14)
        self.label_backlight2.grid(row=10, column=2, pady=(0, 20))

        self.label_touchscreen1 = customtkinter.CTkLabel(self, text="Dotyk:")
        self.label_touchscreen1.cget("font").configure(size=14)
        self.label_touchscreen1.grid(row=11, column=1, pady=(0, 60), sticky="e")
        self.label_touchscreen2 = customtkinter.CTkLabel(self, text="Nie wykryto", text_color="red")
        self.label_touchscreen2.cget("font").configure(size=14)
        self.label_touchscreen2.grid(row=11, column=2, pady=(0, 60))

        self.wwan_segmented = customtkinter.CTkSegmentedButton(
            self, values=['WWAN', 'Brak WWAN'])
        self.wwan_segmented.set('Brak WWAN')
        self.wwan_segmented.grid(row=9, column=3, pady=(0, 20), sticky="w")

        self.backlight_segmented = customtkinter.CTkSegmentedButton(
            self, values=['Podswietlenie', 'Brak podswietlenia'])
        self.backlight_segmented.set('Brak podswietlenia')
        self.backlight_segmented.grid(row=10, column=3, pady=(0, 20), sticky="w")

        self.touchscreen_segmented = customtkinter.CTkSegmentedButton(
            self, values=['Dotyk', 'Brak dotyku'])
        self.touchscreen_segmented.set('Brak dotyku')
        self.touchscreen_segmented.grid(row=11, column=3, pady=(0, 60), sticky="w")

        self.class_segmented = customtkinter.CTkSegmentedButton(
            self, values=[' ', 'A', 'A-', 'B', 'C'])
        self.class_segmented.set(' ')
        self.class_segmented.grid(row=12, column=2, pady=(0, 20))

        self.polska_segmented = customtkinter.CTkSegmentedButton(
            self, values=['Zagranica', '2'])
        self.polska_segmented.set('Zagranica')
        self.polska_segmented.grid(row=13, column=2, pady=(0, 20))

        self.entry_state = 0

        self.entry_display = customtkinter.CTkEntry(self, state='normal', placeholder_text="Wady matrycy", width=300)
        self.entry_display.grid(row=14, column=2, pady=(100, 20), sticky='ns')

        self.entry_frame = customtkinter.CTkEntry(self, state='normal', placeholder_text="Pozostałe wady", width=300)
        self.entry_frame.grid(row=15, column=2, pady=(0, 20), sticky='ns')

        self.fullscreen = None


    def set_segmented(self):
        # Checking if backlight, touchscreen and wwan were detected
        # And if so, configuring corresponding labels and switches
        if self.output.kbd_backlight is True:
            self.label_backlight2.configure(text="Wykryto")
            self.label_backlight2.configure(text_color="green")
            self.backlight_segmented.set('Podswietlenie')

        if self.output.touchscreen is True:
            self.label_touchscreen2.configure(text="Wykryto")
            self.label_touchscreen2.configure(text_color="green")
            self.touchscreen_segmented.set('Dotyk')

        if self.output.WWAN is True:
            self.label_wwan2.configure(text="Wykryto")
            self.label_wwan2.configure(text_color="green")
            self.wwan_segmented.set('WWAN')


    def show_fullscreen(self):
        self.fullscreen = Fullscreen(self)

    def destroy_fullscreen(self):
        self.fullscreen.destroy()

    def prev_callback(self):
        self.master.button_prev_callback()

    def next_callback(self):
        self.master.button_next_callback()

    def entry_callback(self):
        self.entry_state += 1

        if self.entry_state == 1:
            self.entry_state = 2
            self.entry_display.focus()

        else:
            self.entry_state = 0
            self.entry_frame.focus()


class Fullscreen(customtkinter.CTkToplevel):
    """
    Creates new CTk Toplevel fullscreen Window
    that can change colors to Black, White, Red, Green and Blue with button and key presses
    """
    def __init__(self, master):
        super().__init__(master)

        self.title('Toplevel Window')
        self.attributes('-fullscreen', True)

        # Specially for Martin
        # self.label = customtkinter.CTkLabel(self, text="Pamiętaj o przyciskach touchpada xD")
        # self.label.cget("font").configure(size=10)
        # self.label.pack(expand=True)

        self.bind("<Key>", self.key_callback)
        self.bind("<Button>", self.button_callback)

        self.colors = ['#fff', '#000', '#f00', '#0f0', '#00f']
        self.current_color = 0

        self.change_color(self.colors[self.current_color])


    def change_color(self, color):
        self.configure(fg_color=color)

    def key_callback(self, event):
        print("FULLSCREEN key pressed: ", event.keysym)

        # Define keys that change screen color
        if event.keysym in ['space', 'Up', 'Right', 'w', 'W', 'd', 'D']:
            self.increment_color()
            self.change_color(self.colors[self.current_color])

        elif event.keysym in ['Down', 'Left', 's', 'S', 'a', 'A']:
            self.decrement_color()
            self.change_color(self.colors[self.current_color])

        elif event.keysym in ['Return', 'Escape', 'greater']:
            self.master.next_callback()
            self.destroy()

        elif event.keysym in ['less']:
            self.master.prev_callback()
            self.destroy()


    def button_callback(self, event):
        print("FULLSCREEN button pressed: ", event.num)

        # Increment color for Left and Middle mouse buttons
        # Decrement for Right mouse button
        if event.num == 1:
            self.increment_color()
            self.change_color(self.colors[self.current_color])

        elif event.num == 2:
            self.increment_color()
            self.change_color(self.colors[self.current_color])

        elif event.num == 3:
            self.decrement_color()
            self.change_color(self.colors[self.current_color])

    def increment_color(self):
        self.current_color += 1

        if self.current_color > 4:
            self.current_color = 0

    def decrement_color(self):
        self.current_color -= 1

        if self.current_color < 0:
            self.current_color = 4
