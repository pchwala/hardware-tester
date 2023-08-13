import customtkinter


class MonitorMainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Configure grid like this:
        #    0 1 2
        # 0 |_|_|_|
        # 1 |_|_|_|
        # 2 |_|_|_|
        #    .....
        # where all columns have equal weights and row 1 have highest row-weight

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.label1 = customtkinter.CTkLabel(self, text="Częste wady:")
        self.label1.cget("font").configure(size=20)
        self.label1.grid(row=2, column=1, pady=(0, 20))

        self.check_box1 = customtkinter.CTkCheckBox(self, text="Klapa porysowana", onvalue=True, offvalue=False)
        self.check_box1.grid(row=8, column=0, pady=(0, 20))
        self.check_box2 = customtkinter.CTkCheckBox(self, text="Klapa wytarta", onvalue=True, offvalue=False)
        self.check_box2.grid(row=8, column=1, pady=(0, 20))
        self.check_box3 = customtkinter.CTkCheckBox(self, text="Lakier odchodzi", onvalue=True, offvalue=False)
        self.check_box3.grid(row=8, column=2, pady=(0, 20))

        self.check_box4 = customtkinter.CTkCheckBox(self, text="Klawiatura wytarta", onvalue=True, offvalue=False)
        self.check_box4.grid(row=9, column=0, pady=(0, 20))
        self.check_box5 = customtkinter.CTkCheckBox(self, text="Touchpad wytarty", onvalue=True, offvalue=False)
        self.check_box5.grid(row=9, column=1, pady=(0, 20))
        self.check_box6 = customtkinter.CTkCheckBox(self, text="Palmrest wytarty", onvalue=True, offvalue=False)
        self.check_box6.grid(row=9, column=2, pady=(0, 20))

        self.check_box7 = customtkinter.CTkCheckBox(self, text="Wyraźny Hotspot", onvalue=True, offvalue=False)
        self.check_box7.grid(row=10, column=0, pady=(0, 20))
        self.check_box8 = customtkinter.CTkCheckBox(self, text="Wyraźna Rysa", onvalue=True, offvalue=False)
        self.check_box8.grid(row=10, column=1, pady=(0, 20))
        self.check_box9 = customtkinter.CTkCheckBox(self, text="Badpixele", onvalue=True, offvalue=False)
        self.check_box9.grid(row=10, column=2, pady=(0, 20))

        self.touchscreen_segmented = customtkinter.CTkSegmentedButton(
            self, values=['Dotyk', 'Brak dotyku'])
        self.touchscreen_segmented.set('Brak dotyku')
        self.touchscreen_segmented.grid(row=11, column=1, pady=(0, 60))

        self.class_segmented = customtkinter.CTkSegmentedButton(
            self, values=['A', 'A-', 'B', 'C'])
        self.class_segmented.set('A')
        self.class_segmented.grid(row=12, column=1, pady=(0, 20))

        self.polska_segmented = customtkinter.CTkSegmentedButton(
            self, values=['Zagranica', 'Polska'])
        self.polska_segmented.set('Zagranica')
        self.polska_segmented.grid(row=13, column=1, pady=(0, 20))

        self.entry_state = 0

        self.entry_display = customtkinter.CTkEntry(self, state='normal', placeholder_text="Wady matrycy", width=300)
        self.entry_display.grid(row=14, column=1, pady=(100, 20), sticky='ns')

        self.entry_frame = customtkinter.CTkEntry(self, state='normal', placeholder_text="Pozostałe wady", width=300)
        self.entry_frame.grid(row=15, column=1, pady=(0, 20), sticky='ns')

        self.fullscreen = None

    def show_fullscreen(self):
        self.fullscreen = Fullscreen(self)

    def destroy_fullscreen(self):
        self.fullscreen.destroy()

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
    def __init__(self, parent):
        super().__init__(parent)

        self.title('Toplevel Window')
        self.attributes('-fullscreen', True)

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

        elif event.keysym in ['Return', 'Escape', 'greater', 'less']:
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
