import customtkinter


class MonitorMainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

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
        self.check_box2 = customtkinter.CTkCheckBox(self, text="Touchpad wytarty", onvalue=True, offvalue=False)
        self.check_box2.grid(row=8, column=1, pady=(0, 20))
        self.check_box3 = customtkinter.CTkCheckBox(self, text="Palmrest wytarty", onvalue=True, offvalue=False)
        self.check_box3.grid(row=8, column=2, pady=(0, 20))

        self.polska_segmented = customtkinter.CTkSegmentedButton(
            self, values=['Zagranica', 'Polska'])
        self.polska_segmented.set('Zagranica')
        self.polska_segmented.grid(row=9, column=1, pady=(20, 20))

        self.entry_state = 0

        self.entry_display = customtkinter.CTkEntry(self, state='normal', placeholder_text="Wady matrycy", width=300)
        self.entry_display.grid(row=10, column=1, pady=(100, 20), sticky='ns')

        self.entry_frame = customtkinter.CTkEntry(self, state='normal', placeholder_text="Pozostałe wady", width=300)
        self.entry_frame.grid(row=11, column=1, pady=(0, 20), sticky='ns')

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
    def __init__(self, parent):
        super().__init__(parent)

        self.title('Toplevel Window')
        self.attributes('-fullscreen', True)

        self.bind("<Key>", self.key_callback)
        self.bind("<Button>", self.button_callback)

        self.colors = ['black', 'white', 'red', 'green', 'blue']
        self.current_color = 1

    def change_color(self, color):
        self.configure(fg_color=color)

    def key_callback(self, event):
        print("FULLSCREEN key pressed: ", event.keysym)

        if event.keysym in ['space', 'Up', 'Right', 'w', 'W', 'd', 'D']:
            self.increment_color()
            self.change_color(self.colors[self.current_color])

        elif event.keysym in ['Down', 'Left', 's', 'S', 'a', 'A']:
            self.decrement_color()
            self.change_color(self.colors[self.current_color])

        elif event.keysym in ['Return', 'greater', 'less']:
            self.destroy()

    def button_callback(self, event):
        print("FULLSCREEN button pressed: ", event.num)

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
