import customtkinter as ctk


class KeyboardPrimaryFrame(ctk.CTkFrame):
    """
    Primary frame containing all keyboard buttons except NUM-PAD, ARROWS and CONTROL-PAD(PgUP, PgDown and so on)
    Basically a lot of buttons that change colors when pressed and released
    """
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
        self.button_backslash = ctk.CTkButton(self, text="\\  |", width=40, height=30, state="disabled")
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

        self.button_Shift_L = ctk.CTkButton(self, text="Shift", width=40, height=30, state="disabled")
        self.button_Shift_L.grid(row=4, column=1, padx=(10, 2), pady=(5, 5))
        self.button_less = ctk.CTkButton(self, text="< >", width=40, height=30, state="disabled")
        self.button_less.grid(row=4, column=2, padx=(2, 2), pady=(5, 5))
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
                                  self.button_Control_R, self.button_less]

        self.key_names = ['Escape', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
                          'grave', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'minus', 'equal', 'BackSpace',
                          'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'bracketleft', 'bracketright',
                          'backslash', 'Caps_Lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'semicolon',
                          'apostrophe', 'Return', 'Shift_L', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'comma', 'period',
                          'slash', 'Shift_R', 'Control_L', 'Super_L', 'Alt_L', 'space', 'ISO_Level3_Shift', 'Menu',
                          'Control_R', 'less']

        self.alt_key_names = ['Escape', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',
                              'grave', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'minus', 'equal', 'BackSpace',
                              'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'bracketleft', 'bracketright',
                              'backslash', 'Caps_Lock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'semicolon',
                              'apostrophe', 'Return', 'Shift_L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'comma', 'period',
                              'slash', 'Shift_R', 'Control_L', 'Super_L', 'Alt_L', 'space', 'ISO_Level3_Shift', 'Menu',
                              'Control_R', 'greater']


class KeyboardSecondaryFrame(ctk.CTkFrame):
    """
        Secondary frame containing only NUM-PAD, ARROWS and CONTROL-PAD(PgUP, PgDown and so on)
        Basically a lot of buttons that change colors when pressed and released
        This frame is displayed below PrimaryFrame
        """
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(8, weight=1)

        self.button_Print_screen = ctk.CTkButton(self, text="PrtSC", width=60, height=30, state="disabled")
        self.button_Print_screen.grid(row=0, column=1, padx=(2, 2), pady=(5, 5))
        self.button_Scroll_lock = ctk.CTkButton(self, text="ScrLk", width=60, height=30, state="disabled")
        self.button_Scroll_lock.grid(row=0, column=2, padx=(2, 2), pady=(5, 5))
        self.button_Pause = ctk.CTkButton(self, text="Pause", width=60, height=30, state="disabled")
        self.button_Pause.grid(row=0, column=3, padx=(2, 2), pady=(5, 5))

        self.button_Insert = ctk.CTkButton(self, text="Ins", width=60, height=30, state="disabled")
        self.button_Insert.grid(row=1, column=1, padx=(2, 2), pady=(5, 5))
        self.button_Home = ctk.CTkButton(self, text="Home", width=60, height=30, state="disabled")
        self.button_Home.grid(row=1, column=2, padx=(2, 2), pady=(5, 5))
        self.button_Pageup = ctk.CTkButton(self, text="PgUp", width=60, height=30, state="disabled")
        self.button_Pageup.grid(row=1, column=3, padx=(2, 2), pady=(5, 5))
        self.button_Delete = ctk.CTkButton(self, text="Del", width=60, height=30, state="disabled")
        self.button_Delete.grid(row=2, column=1, padx=(2, 2), pady=(5, 5))
        self.button_End = ctk.CTkButton(self, text="End", width=60, height=30, state="disabled")
        self.button_End.grid(row=2, column=2, padx=(2, 2), pady=(5, 5))
        self.button_Pagedown = ctk.CTkButton(self, text="PgDn", width=60, height=30, state="disabled")
        self.button_Pagedown.grid(row=2, column=3, padx=(2, 2), pady=(5, 5))

        self.button_Up = ctk.CTkButton(self, text="↑", width=60, height=30, state="disabled")
        self.button_Up.grid(row=3, column=2, padx=(2, 2), pady=(5, 5))
        self.button_Down = ctk.CTkButton(self, text="↓", width=60, height=30, state="disabled")
        self.button_Down.grid(row=4, column=2, padx=(2, 2), pady=(5, 5))
        self.button_Left = ctk.CTkButton(self, text="←", width=60, height=30, state="disabled")
        self.button_Left.grid(row=4, column=1, padx=(2, 2), pady=(5, 5))
        self.button_Right = ctk.CTkButton(self, text="→", width=60, height=30, state="disabled")
        self.button_Right.grid(row=4, column=3, padx=(2, 2), pady=(5, 5))

        self.button_Numlock = ctk.CTkButton(self, text="NumLk", width=60, height=30, state="disabled")
        self.button_Numlock.grid(row=0, column=4, padx=(80, 2), pady=(5, 5))
        self.button_KP_Divide = ctk.CTkButton(self, text="/", width=60, height=30, state="disabled")
        self.button_KP_Divide.grid(row=0, column=5, padx=(2, 2), pady=(5, 5))
        self.button_KP_Multiply = ctk.CTkButton(self, text="*", width=60, height=30, state="disabled")
        self.button_KP_Multiply.grid(row=0, column=6, padx=(2, 2), pady=(5, 5))
        self.button_KP_Subtract = ctk.CTkButton(self, text="-", width=60, height=30, state="disabled")
        self.button_KP_Subtract.grid(row=0, column=7, padx=(2, 2), pady=(5, 5))

        self.button_KP_Add = ctk.CTkButton(self, text="+", width=60, height=70, state="disabled")
        self.button_KP_Add.grid(row=1, rowspan=2, column=7, padx=(2, 2), pady=(5, 5))
        self.button_KP_Enter = ctk.CTkButton(self, text="Enter", width=60, height=70, state="disabled")
        self.button_KP_Enter.grid(row=3, rowspan=2, column=7, padx=(2, 2), pady=(5, 5))
        self.button_KP_Separator = ctk.CTkButton(self, text=".", width=60, height=30, state="disabled")
        self.button_KP_Separator.grid(row=4, column=6, padx=(2, 2), pady=(5, 5))
        self.button_KP_0 = ctk.CTkButton(self, text="0", width=120, height=30, state="disabled")
        self.button_KP_0.grid(row=4, column=4, columnspan=2, padx=(80, 2), pady=(5, 5))

        self.button_KP_7 = ctk.CTkButton(self, text="7", width=60, height=30, state="disabled")
        self.button_KP_7.grid(row=1, column=4, padx=(80, 2), pady=(5, 5))
        self.button_KP_8 = ctk.CTkButton(self, text="8", width=60, height=30, state="disabled")
        self.button_KP_8.grid(row=1, column=5, padx=(2, 2), pady=(5, 5))
        self.button_KP_9 = ctk.CTkButton(self, text="9", width=60, height=30, state="disabled")
        self.button_KP_9.grid(row=1, column=6, padx=(2, 2), pady=(5, 5))
        self.button_KP_4 = ctk.CTkButton(self, text="4", width=60, height=30, state="disabled")
        self.button_KP_4.grid(row=2, column=4, padx=(80, 2), pady=(5, 5))
        self.button_KP_5 = ctk.CTkButton(self, text="5", width=60, height=30, state="disabled")
        self.button_KP_5.grid(row=2, column=5, padx=(2, 2), pady=(5, 5))
        self.button_KP_6 = ctk.CTkButton(self, text="6", width=60, height=30, state="disabled")
        self.button_KP_6.grid(row=2, column=6, padx=(2, 2), pady=(5, 5))
        self.button_KP_1 = ctk.CTkButton(self, text="1", width=60, height=30, state="disabled")
        self.button_KP_1.grid(row=3, column=4, padx=(80, 2), pady=(5, 5))
        self.button_KP_2 = ctk.CTkButton(self, text="2", width=60, height=30, state="disabled")
        self.button_KP_2.grid(row=3, column=5, padx=(2, 2), pady=(5, 5))
        self.button_KP_3 = ctk.CTkButton(self, text="3", width=60, height=30, state="disabled")
        self.button_KP_3.grid(row=3, column=6, padx=(2, 2), pady=(5, 5))

        self.button_references = [self.button_Print_screen, self.button_Scroll_lock, self.button_Pause,
                                  self.button_Insert, self.button_Home, self.button_Pageup, self.button_Delete,
                                  self.button_End, self.button_Pagedown, self.button_Up, self.button_Down,
                                  self.button_Left, self.button_Right, self.button_Numlock, self.button_KP_Divide,
                                  self.button_KP_Multiply, self.button_KP_Subtract, self.button_KP_Add,
                                  self.button_KP_Enter, self.button_KP_Separator, self.button_KP_0,
                                  self.button_KP_7, self.button_KP_8, self.button_KP_9, self.button_KP_4,
                                  self.button_KP_5, self.button_KP_6, self.button_KP_1, self.button_KP_2,
                                  self.button_KP_3]

        self.key_names = ['Print_Screen', 'Scroll_Lock', 'Pause', 'Insert', 'Home', 'Prior', 'Delete', 'End', 'Next',
                          'Up', 'Down', 'Left', 'Right', 'Num_Lock', 'KP_Divide', 'KP_Multiply', 'KP_Subtract',
                          'KP_Add', 'KP_Enter', 'KP_Separator', 'KP_0', 'KP_7', 'KP_8', 'KP_9', 'KP_4', 'KP_5', 'KP_6',
                          'KP_1', 'KP_2', 'KP_3']

        self.alt_key_names = ['Print_Screen', 'Scroll_Lock', 'Pause', 'Insert', 'Home', 'Prior', 'Delete', 'End',
                              'Next', 'Up', 'Down', 'Left', 'Right', 'Num_Lock', 'KP_Divide', 'KP_Multiply',
                              'KP_Subtract', 'KP_Add', 'KP_Enter', 'KP_Delete', 'KP_Insert', 'KP_Home', 'KP_Up',
                              'KP_Prior', 'KP_Left', 'KP_Begin', 'KP_Right', 'KP_End', 'KP_Down', 'KP_Next']


class KeyboardMainFrame(ctk.CTkFrame):
    """
    Keyboard Main Frame that manages displaying of Primary and Secondary Frames
    """
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)

        self.pf = KeyboardPrimaryFrame(self)
        self.sf = KeyboardSecondaryFrame(self)

        self.pf.configure(fg_color="transparent")
        self.sf.configure(fg_color="transparent")

        self.current_pady = (80, 0)

        self.pf.grid(row=0, column=1, sticky="ew")
        self.sf.grid(row=1, column=1, pady=self.current_pady, sticky="ew")

        self.button_references = self.pf.button_references + self.sf.button_references
        self.key_names = self.pf.key_names + self.sf.key_names
        self.alt_key_names = self.pf.alt_key_names + self.sf.alt_key_names

        self.entry_state = 0

        self.check_box = ctk.CTkCheckBox(self, text="Podświetlenie?", onvalue=True, offvalue=False)
        self.check_box.grid(row=3, column=1, pady=(0, 20))
        self.check_box.select()

        self.entry_layout = ctk.CTkEntry(self, width=200)
        self.entry_layout.grid(row=4, column=1, pady=(0, 20), sticky='ns')
        self.entry_layout.configure(self, state='normal', placeholder_text="Układ klawiatury")
        self.entry_keyboard = ctk.CTkEntry(self, width=200)
        self.entry_keyboard.grid(row=5, column=1, pady=(0, 20), sticky='ns')
        self.entry_keyboard.configure(self, state='normal', placeholder_text="Wady klawiatury")

    def rescale(self, width, height):
        for button in self.pf.button_references + self.sf.button_references:
            current_width = button.cget("width")
            current_height = button.cget("height")
            button.configure(width=current_width * width, height=current_height * height)

        self.current_pady = self.current_pady[0] * width, self.current_pady[1] * width
        self.sf.grid_configure(pady=self.current_pady)

    def mark_key(self, index, key_state):
        match key_state:
            case 'keydown':
                self.button_references[index].configure(fg_color="yellow")

            case 'keyup':
                self.button_references[index].configure(fg_color="green")

    def reset_all(self):
        # Reset color of all buttons back to default
        for x in self.button_references:
            # default color
            x.configure(fg_color="#1F6AA5")

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

    def entry_callback(self):
        self.entry_state += 1

        if self.entry_state == 1:
            self.entry_state = 2
            self.entry_layout.focus()

        else:
            self.entry_state = 0
            self.entry_keyboard.focus()
