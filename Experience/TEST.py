from tkinter import *
from tkinter import ttk
from winparam import *


class DataField(Frame):
    # data for calc area
    _BACKGROUND = '#C4C4C4'

    def __init__(self, master=None):
        super(DataField, self).__init__(master)
        self.configure(bg=BACKGROUND)
        # create background for data field
        bg = Label(self, image=Img.get('bg_datafield'), bg=BACKGROUND)
        bg.grid(row=0, column=1)
        # create data frame that will be contain bt_plus or two lb and two entry
        self.__frm = Frame(self, bg=self._BACKGROUND)
        self.__frm.grid(row=0, column=1)
        # create close button
        self._bt_close = Button(self, text='x', font=('Comic Sans MS', 5), fg='#000000', command=self.delete,
                                border=0, bg=BACKGROUND, activebackground=BACKGROUND, cursor='hand2')
        # create button_plus to change itself on two lb and two entry
        self._bt_plus = Button(self.__frm, image=Img.get('button_plus'), command=self.new,
                               border=0, bg=self._BACKGROUND, activebackground=BACKGROUND, cursor='hand2')
        self._bt_plus.grid(row=0, column=0)

    def new(self):
        """Function change filed with button_plus to field with two entry and two label"""
        self._bt_plus.destroy()
        self._bt_close.grid(row=0, column=0, sticky='nw')
        # init data field widgets
        lb_w = Label(self.__frm, image=Img.get('txt_width'), bg=self._BACKGROUND, width=29)
        lb_l = Label(self.__frm, image=Img.get('txt_length'), bg=self._BACKGROUND, width=29)
        bg_entry_w = Label(self.__frm, image=Img.get('entry_datafield'), bg=self._BACKGROUND)
        bg_entry_l = Label(self.__frm, image=Img.get('entry_datafield'), bg=self._BACKGROUND)
        self.entry_w = Entry(self.__frm, width=10, border=0, font=("Arial", 7))
        self.entry_l = Entry(self.__frm, width=10, border=0, font=("Arial", 7))
        # grid data field widgets
        lb_w.grid(row=0, column=0)
        lb_l.grid(row=1, column=0)
        bg_entry_w.grid(row=0, column=1)
        bg_entry_l.grid(row=1, column=1)
        self.entry_w.grid(row=0, column=1)
        self.entry_l.grid(row=1, column=1)

    def delete(self):
        self.destroy()

    def get(self):
        try:
            return self.entry_w.get(), self.entry_l.get()
        except TclError:
            return None


BG_ROOT = '#ba03fc'     # purple
BG_LSTFRM = '#03e3fc'   # blue
BG_CANVAS = '#fc4503'   # red
BG_MINIFRM = '#fcdf03'  # yellow


# setup
root = Tk()
root.geometry('500x400')
root.title('Scrolling')
root.configure(bg=BG_ROOT)
Img.init()

editor = Text(state=NORMAL)
editor.pack(expand=1, fill=BOTH)


def click():
    editor.insert("2.0", "\n")
    editor.window_create("2.0", window=DataField(editor))


btn = ttk.Button(editor, text="Click", command=click)
editor.window_create("1.0", window=btn)

# run
root.mainloop()