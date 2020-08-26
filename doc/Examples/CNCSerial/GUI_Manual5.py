#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.15
# In conjunction with Tcl version 8.6
#    Aug 24, 2018 05:51:16 PM

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

import GUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = CNC_Serial (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_CNC_Serial(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = CNC_Serial (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_CNC_Serial():
    global w
    w.destroy()
    w = None


class CNC_Serial:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("393x351+694+74")
        top.title("CNC Serial")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.options = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.options,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Options")
        self.options.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Serial Port")
        self.help = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.help,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Help")
        self.help.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="About")


        self.Button3 = Button(top)
        self.Button3.place(relx=0.03, rely=0.54, height=74, width=94)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Z0''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.03, rely=0.31, height=74, width=94)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Y0''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.0, rely=0.03, height=21, width=35)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Zeros''')

        self.Label1 = Label(top)
        self.Label1.place(relx=0.66, rely=0.03, height=21, width=28)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Port''')

        self.Listbox1 = Listbox(top)
        self.Listbox1.place(relx=0.76, rely=0.03, relheight=0.06, relwidth=0.21)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=84)

        self.Label1_3 = Label(top)
        self.Label1_3.place(relx=0.66, rely=0.11, height=21, width=28)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#d9d9d9")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''Baud''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.79, rely=0.91, height=21, width=51)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Progress''')
        self.Label3.configure(width=51)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.92, rely=0.91, height=21, width=34)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''0%''')
        self.Label2.configure(width=34)

        self.Button9 = Button(top)
        self.Button9.place(relx=0.64, rely=0.74, height=54, width=134)
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''Stop''')

        self.Button10 = Button(top)
        self.Button10.place(relx=0.66, rely=0.91, height=24, width=44)
        self.Button10.configure(activebackground="#d9d9d9")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''Reset''')

        self.Label4_4 = Label(top)
        self.Label4_4.place(relx=0.64, rely=0.54, height=21, width=55)
        self.Label4_4.configure(activebackground="#f9f9f9")
        self.Label4_4.configure(activeforeground="black")
        self.Label4_4.configure(background="#d9d9d9")
        self.Label4_4.configure(disabledforeground="#a3a3a3")
        self.Label4_4.configure(foreground="#000000")
        self.Label4_4.configure(highlightbackground="#d9d9d9")
        self.Label4_4.configure(highlightcolor="black")
        self.Label4_4.configure(text='''Program''')

        self.Button8 = Button(top)
        self.Button8.place(relx=0.64, rely=0.6, height=44, width=134)
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''Run''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.03, rely=0.09, height=74, width=94)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''X0''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.76, rely=0.11,height=20, relwidth=0.21)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Button6 = Button(top)
        self.Button6.place(relx=0.28, rely=0.54, height=74, width=94)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Z0.5''')

        self.Button4 = Button(top)
        self.Button4.place(relx=0.28, rely=0.09, height=74, width=94)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''XC''')

        self.Button5 = Button(top)
        self.Button5.place(relx=0.28, rely=0.31, height=74, width=94)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''YC''')

        self.Button7 = Button(top)
        self.Button7.place(relx=0.03, rely=0.77, height=74, width=194)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Zero Ferr Mesa''')
        self.Button7.configure(width=194)


##Manually added code:
        import SerialTransfers
        self.Button1.configure(command=SerialTransfers.SendX0)
        self.Button2.configure(command=SerialTransfers.SendY0)
        self.Button3.configure(command=SerialTransfers.SendZ0)        
        self.Button4.configure(command=SerialTransfers.SendXC)
        self.Button5.configure(command=SerialTransfers.SendYC)
        self.Button6.configure(command=SerialTransfers.SendZ0_5)
        self.Button7.configure(command=SerialTransfers.SendZerFerr)
        self.Button8.configure(command=SerialTransfers.SendProgram)

        import serial.tools.list_ports
        comlist = serial.tools.list_ports.comports()
        available = []
        for element in comlist:
            self.Listbox1.insert(END, str(element.device))
        self.Entry1.insert(0, "19200")
        SerialTransfers.OpenPort( 'COM1', 19200)

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="{Segoe UI} 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

    @staticmethod
    def popup2(event, *args, **kwargs):
        Popupmenu2 = Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#f9f9f9")
        Popupmenu2.configure(activeborderwidth="1")
        Popupmenu2.configure(activeforeground="black")
        Popupmenu2.configure(background="#d9d9d9")
        Popupmenu2.configure(borderwidth="1")
        Popupmenu2.configure(disabledforeground="#a3a3a3")
        Popupmenu2.configure(font="{Segoe UI} 9")
        Popupmenu2.configure(foreground="black")
        Popupmenu2.post(event.x_root, event.y_root)

    @staticmethod
    def popup3(event, *args, **kwargs):
        Popupmenu3 = Menu(root, tearoff=0)
        Popupmenu3.configure(activebackground="#f9f9f9")
        Popupmenu3.configure(activeborderwidth="1")
        Popupmenu3.configure(activeforeground="black")
        Popupmenu3.configure(background="#d9d9d9")
        Popupmenu3.configure(borderwidth="1")
        Popupmenu3.configure(disabledforeground="#a3a3a3")
        Popupmenu3.configure(font="{Segoe UI} 9")
        Popupmenu3.configure(foreground="black")
        Popupmenu3.post(event.x_root, event.y_root)

    @staticmethod
    def popup4(event, *args, **kwargs):
        Popupmenu4 = Menu(root, tearoff=0)
        Popupmenu4.configure(activebackground="#f9f9f9")
        Popupmenu4.configure(activeborderwidth="1")
        Popupmenu4.configure(activeforeground="black")
        Popupmenu4.configure(background="#d9d9d9")
        Popupmenu4.configure(borderwidth="1")
        Popupmenu4.configure(disabledforeground="#a3a3a3")
        Popupmenu4.configure(font="{Segoe UI} 9")
        Popupmenu4.configure(foreground="black")
        Popupmenu4.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()


