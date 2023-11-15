from tkinter import *
from winparam import BACKGROUND
from winparam import Img
from winparam import MENU_PAD


class Menu(Frame):
    _PARMDODL_PAD = {'padx': 0, 'pady': (11, 0)}

    def __init__(self, master, title_img=None, column=2):
        super(Menu, self).__init__(master)
        self._title_img = title_img
        self.configure(bg=BACKGROUND)
        self._column = column

    def _add_title(self, title_img):
        lbl = Label(self, image=title_img, bg=BACKGROUND)
        lbl.pack()

    def _create_parammenu(self):
        self._add_title(Img.get('title_parameters'))
        doodles = Label(self, image=Img.get('doodles'), bg=BACKGROUND)
        doodles.pack(**self._PARMDODL_PAD)

    def create(self):
        # Create menu frame
        self.show()
        # Create frame title
        if self._title_img is not None:
            self._add_title(self._title_img)
        else:
            self._create_parammenu()

    def hide(self):
        self.grid_forget()

    def show(self):
        self.grid(row=0, column=self._column, sticky='n', **MENU_PAD)
