#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jun 04, 2018 06:36:21 PM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import gui_support


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = Tk()
    gui_support.set_Tk_var()
    top = New_Toplevel(root)
    gui_support.init(root, top)
    root.mainloop()


w = None


def create_New_Toplevel(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    gui_support.set_Tk_var()
    top = New_Toplevel(w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def create_callback(self, event=None):
        import organizeSchoolWork
        organizeSchoolWork.new_doc(gui_support.combobox.get(), self.TEntry1.get())

    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""
        _bgcolor = "#d9d9d9"  # X11 color: 'gray85'
        _fgcolor = "#000000"  # X11 color: 'black'
        _compcolor = "#d9d9d9"  # X11 color: 'gray85'
        _ana1color = "#d9d9d9"  # X11 color: 'gray85'
        _ana2color = "#d9d9d9"  # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use("winnative")
        self.style.configure(".", background=_bgcolor)
        self.style.configure(".", foreground=_fgcolor)
        self.style.configure(".", font="TkDefaultFont")
        self.style.map(
            ".", background=[("selected", _compcolor), ("active", _ana2color)]
        )

        top.geometry("600x308+361+213")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.rootFrame = ttk.Frame(top)
        self.rootFrame.place(relx=-0.1, rely=-0.1, relheight=2.45, relwidth=1.23)

        self.rootFrame.configure(borderwidth="2")
        self.rootFrame.configure(width=735)

        self.TLabel1 = ttk.Label(self.rootFrame)
        self.TLabel1.place(relx=0.26, rely=0.15, height=20, width=58)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(text="""Subject:""")

        self.TCombobox1 = ttk.Combobox(self.rootFrame)
        self.TCombobox1.place(relx=0.34, rely=0.15, relheight=0.04, relwidth=0.28)
        self.TCombobox1.configure(textvariable=gui_support.combobox)
        self.TCombobox1.configure(takefocus="")

        self.TLabel2 = ttk.Label(self.rootFrame)
        self.TLabel2.place(relx=0.18, rely=0.19, height=20, width=119)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief=FLAT)
        self.TLabel2.configure(text="""Document Name:""")

        self.TEntry1 = ttk.Entry(self.rootFrame)
        self.TEntry1.place(relx=0.34, rely=0.19, relheight=0.03, relwidth=0.27)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")
        self.TEntry1.bind('<Return>', self.create_callback)

        self.TButton1 = ttk.Button(self.rootFrame, command=self.create_callback)
        self.TButton1.place(relx=0.39, rely=0.24, height=24, width=87)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text="""Create""")


if __name__ == "__main__":
    vp_start_gui()
