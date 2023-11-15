from app import *


class Menu(Frame):
    def __init__(self, master, title_img: ImageTk.PhotoImage):
        super(Menu, self).__init__(master)
        self._title_img = title_img
        self.configure(bg=BACKGROUND)

    def _set_title(self):
        lbl = Label(self, image=self._title_img, bg=BACKGROUND)
        lbl.pack()

    def create(self, pos: tuple):
        # Create menu frame
        self.grid(row=pos[0], column=pos[1])
        # Create frame title
        self._set_title()

    def add_button(self, btn_pos: tuple, btn_img: tuple):
        frm = Frame(self)
        frm.configure(bg=BACKGROUND)
        frm.pack()
        length = len(btn_img)
        if length == len(btn_pos):
            for i in range(length):
                self.__dict__[f'btn{i+1}'] = Button(frm, image=btn_img[i], bg=BACKGROUND, border=0)
                self.__dict__[f'btn{i + 1}'].grid(row=btn_pos[i][0], column=btn_pos[i][1])
