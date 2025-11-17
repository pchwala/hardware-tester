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
        
        # Button states
        self.backlight_state = False
        self.touchscreen_state = False
        
        # Replace segmented buttons with toggle buttons
        self.backlight_button = customtkinter.CTkButton(
            self, text='Brak podswietlenia', 
            command=self.toggle_backlight,
            height=60)
        self.backlight_button.grid(row=3, column=1, pady=(0, 20), sticky="w")

        self.touchscreen_button = customtkinter.CTkButton(
            self, text='Brak dotyku',
            command=self.toggle_touchscreen,
            height=60)
        self.touchscreen_button.grid(row=3, column=3, pady=(0, 20), sticky="e")

        # Checkboxes for hardware components
        self.checkbox_klapa_gorna = customtkinter.CTkCheckBox(self, text="Klapa górna")
        self.checkbox_klapa_gorna.grid(row=4, column=1, pady=(60, 30), sticky="e")

        self.checkbox_klapa_dolna = customtkinter.CTkCheckBox(self, text="Klapa dolna")
        self.checkbox_klapa_dolna.grid(row=5, column=1, pady=(0, 30), sticky="e")

        self.checkbox_matryca = customtkinter.CTkCheckBox(self, text="Matryca")
        self.checkbox_matryca.grid(row=4, column=2, pady=(60, 30), sticky="e")

        self.checkbox_ramka = customtkinter.CTkCheckBox(self, text="Ramka")
        self.checkbox_ramka.grid(row=5, column=2, pady=(0, 30), sticky="e")

        self.checkbox_palmrest = customtkinter.CTkCheckBox(self, text="Palmrest", )
        self.checkbox_palmrest.grid(row=4, column=3, pady=(60, 30), sticky="e")

        self.class_segmented = customtkinter.CTkSegmentedButton(
            self, values=[' ', 'A', 'A-', 'B', 'C'],
            border_width=6)
        self.class_segmented.set(' ')
        self.class_segmented.grid(row=6, column=2, pady=(40, 20))

        self.polska_segmented = customtkinter.CTkSegmentedButton(
            self, values=['Zagranica', '2'],
            border_width=6)
        self.polska_segmented.set('Zagranica')
        self.polska_segmented.grid(row=7, column=2, pady=(0, 20))

        self.magazyn_segmented = customtkinter.CTkSegmentedButton(
            self, values=['M2', 'M5', 'M15', 'M47', 'M18'],
            border_width=6)
        self.magazyn_segmented.set('M2')
        self.magazyn_segmented.grid(row=8, column=2, pady=(0, 20))

        self.entry_state = 0

        self.entry_display = customtkinter.CTkEntry(self, state='normal', placeholder_text="Wady matrycy")
        self.entry_display.grid(row=9, column=2, pady=(100, 20), sticky='ns')

        self.entry_frame = customtkinter.CTkEntry(self, state='normal', placeholder_text="Pozostałe wady")
        self.entry_frame.grid(row=10, column=2, pady=(0, 20), sticky='ns')

        self.fullscreen = None

    def toggle_backlight(self):
        """Toggle backlight button state"""
        self.backlight_state = not self.backlight_state
        if self.backlight_state:
            self.backlight_button.configure(text='Podswietlenie', fg_color='green')
        else:
            self.backlight_button.configure(text='Brak podswietlenia', fg_color=['#3B8ED0', '#1F6AA5'])
    
    def toggle_touchscreen(self):
        """Toggle touchscreen button state"""
        self.touchscreen_state = not self.touchscreen_state
        if self.touchscreen_state:
            self.touchscreen_button.configure(text='Dotyk', fg_color='green')
        else:
            self.touchscreen_button.configure(text='Brak dotyku', fg_color=['#3B8ED0', '#1F6AA5'])

    def set_segmented(self):
        # Checking if backlight and touchscreen were detected
        # And if so, configuring corresponding buttons
        if self.output.kbd_backlight is True:
            self.backlight_state = True
            self.backlight_button.configure(text='Podswietlenie', fg_color='green')

        if self.output.touchscreen is True:
            self.touchscreen_state = True
            self.touchscreen_button.configure(text='Dotyk', fg_color='green')


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

        # Create canvas for drawing touch lines
        self.canvas = tkinter.Canvas(self, highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        # Specially for Martin
        # self.label = customtkinter.CTkLabel(self, text="Pamiętaj o przyciskach touchpada xD")
        # self.label.cget("font").configure(size=10)
        # self.label.pack(expand=True)

        self.bind("<Key>", self.key_callback)
        self.bind("<Button>", self.button_callback)
        
        # Bind touch/mouse motion events for drawing
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.canvas.bind("<ButtonPress-1>", self.start_draw)

        self.colors = ['#fff', '#000', '#f00', '#0f0', '#00f']
        self.current_color = 0
        
        # Track drawing state
        self.last_x = None
        self.last_y = None
        self.line_items = []  # Store (canvas_id, timestamp) tuples

        self.change_color(self.colors[self.current_color])
        
        # Start fade-out timer
        self.fade_lines()


    def change_color(self, color):
        self.canvas.configure(bg=color)

    def start_draw(self, event):
        """Initialize drawing position"""
        self.last_x = event.x
        self.last_y = event.y

    def draw_line(self, event):
        """Draw line from last position to current position"""
        if self.last_x is not None and self.last_y is not None:
            # Determine line color based on background
            # Use inverted color for visibility
            if self.current_color == 0:  # white background
                line_color = '#000'
            elif self.current_color == 1:  # black background
                line_color = '#fff'
            else:  # colored backgrounds
                line_color = '#fff'
            
            # Draw line
            line_id = self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                fill=line_color, width=3, capstyle=tkinter.ROUND, smooth=True
            )
            
            # Store line with current time
            import time
            self.line_items.append((line_id, time.time()))
        
        self.last_x = event.x
        self.last_y = event.y

    def fade_lines(self):
        """Remove lines older than 1 second"""
        import time
        current_time = time.time()
        
        # Remove old lines
        self.line_items = [(line_id, timestamp) 
                          for line_id, timestamp in self.line_items
                          if current_time - timestamp <= 1.0]
        
        # Delete lines from canvas that are no longer tracked
        all_canvas_items = set(self.canvas.find_all())
        tracked_items = {line_id for line_id, _ in self.line_items}
        
        for item in all_canvas_items:
            if item not in tracked_items:
                try:
                    self.canvas.delete(item)
                except:
                    pass
        
        # Schedule next check
        self.after(100, self.fade_lines)


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
