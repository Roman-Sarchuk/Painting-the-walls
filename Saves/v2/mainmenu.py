from menu import *


class MainMenu(Menu):
    _btn_imgs = (Img.get_img("button_info"), Img.get_img("button_info"), Img.get_img("button_info"),
                 Img.get_img("button_area"), Img.get_img("button_primer"), Img.get_img("button_paint"))
    _btn_pos = ((0, 0), (1, 0), (2, 0),
                (0, 1), (1, 1), (2, 1))
    _btn_cmds = (None, None, None,
                 None, None, None)

    def __init__(self, master, title_img: ImageTk.PhotoImage):
        super(MainMenu, self).__init__(master, title_img)
        # Init button frame
        self.__btn_frm = Frame(self)
        self.__btn_frm.configure(bg=BACKGROUND)
        # Add button calc
        self._btn_calc = Button(self, image=Img.get_img("button_calc"), bg=BACKGROUND, border=0)

    def __add_button_gr(self):
        length = len(self._btn_imgs)
        if len(self._btn_cmds) == length == len(self._btn_pos):
            for i in range(length):
                self.__dict__[f'btn{i + 1}'] = Button(self.__btn_frm, image=self._btn_imgs[i], bg=BACKGROUND, border=0)
                self.__dict__[f'btn{i + 1}'].grid(row=self._btn_pos[i][0], column=self._btn_pos[i][1])

    def create(self, pos: tuple):
        super(MainMenu, self).create(pos)
        self.__btn_frm.pack()
        self.__add_button_gr()
        self._btn_calc.pack()
