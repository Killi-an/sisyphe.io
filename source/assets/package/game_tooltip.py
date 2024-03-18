# -*- coding: utf-8 -*-
import tkinter as tk

class ToolTip(object):
    def __init__(self, widget, text='ToolTip'):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.create_tooltip_events()

    def create_tooltip_events(self):
        self.widget.bind('<Enter>', self.show_tip)
        self.widget.bind('<Leave>', self.hide_tip)

    def show_tip(self, event=None):
        "Display text in tooltip window"
        self.x = self.widget.winfo_rootx() + 20
        self.y = self.widget.winfo_rooty() + self.widget.winfo_height() + 20
        self.create_tip_window()
        
    def create_tip_window(self):
        if self.tipwindow or not self.text:
            return
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (self.x, self.y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()