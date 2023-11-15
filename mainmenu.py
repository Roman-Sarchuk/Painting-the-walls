from menu import *
from winparam import BTN_PARAM


class MainMenu(Menu):
    _BTGR_PAD = {'padx': 0, 'pady': 4, 'ipadx': 8, 'ipady': 15}
    _BTCALC_PAD = {'padx': 0, 'pady': (5, 0)}
    _TBL_PAD = {'padx': 0, 'pady': (10, 0)}

    def __init__(self, master, title_img, btn_cmds: tuple):
        super(MainMenu, self).__init__(master, title_img, 0)
        # init button frame
        self.__btn_frm = Frame(self)
        self.__btn_frm.configure(bg=BACKGROUND)
        self._btn_cmds = btn_cmds
        # init table frame
        self.__tbl_frm = Frame(self)
        self.__tbl_frm.configure(bg=BACKGROUND)
        # -- init result fields (table) --
        lb_param = {'master': self.__tbl_frm, 'image': Img.get('tablefield_void'),
                    'compound': 'center', 'bg': BACKGROUND}
        # Adding 4 short and 1 long (as 2 short) void fields
        self._res_tbl = [Label(**lb_param) for _ in range(4)]           # add short void fields to list
        self._res_tbl.append(Label(self.__tbl_frm, image=Img.get('tablefield_longvoid'),
                                   compound='center', bg=BACKGROUND))   # add long void field to list

    def __add_button_gr(self):
        # parameters of widgets
        btn_imgs = (Img.get("button_info"), Img.get("button_info"), Img.get("button_info"),
                    Img.get("button_area"), Img.get("button_primer"), Img.get("button_paint"))
        btn_pos = ((0, 0), (1, 0), (2, 0),
                   (0, 1), (1, 1), (2, 1))
        length = len(btn_imgs)
        # verify number of parameter button tuples
        if length != len(btn_pos):
            raise ValueError("!! Number items of 'btn_imgs' and 'btn_pos' are different !!")
        elif len(self._btn_cmds) > length:
            raise ValueError("!! Number items of 'btn_cmds' are more than 'btn_imgs' !!")
        elif len(self._btn_cmds) < length:
            raise ValueError("!! Number items of 'btn_cmds' are less than 'btn_imgs' !!")
        # button centering
        for r in range(3): self.__btn_frm.rowconfigure(r, weight=1)
        for c in range(2): self.__btn_frm.columnconfigure(c, weight=1)
        # add buttons
        for i in range(length):
            bt = Button(self.__btn_frm, image=btn_imgs[i], command=self._btn_cmds[i], **BTN_PARAM)
            bt.grid(row=btn_pos[i][0], column=btn_pos[i][1])

    def __add_table(self):
        # parameters of widgets
        tbl_img = (Img.get('tablefield_doodles'), Img.get('tablefield_primer'), Img.get('tablefield_paint'),
                   Img.get('tablefield_number'), Img.get('tablefield_price'), Img.get('tablefield_amount'))
        img_pos = ((0, 0), (0, 1), (0, 2),
                   (1, 0), (2, 0), (3, 0))
        resfld_pos = ((1, 1), (1, 2), (2, 1),
                      (2, 2), (3, 1))
        # add info fields
        length = len(tbl_img)
        if length == len(img_pos):
            for i in range(length):
                lb = Label(self.__tbl_frm, image=tbl_img[i], bg=BACKGROUND)
                lb.grid(row=img_pos[i][0], column=img_pos[i][1])
        # add result fields
        # This is four short void fields and one long void field(it's two short void field)
        length = len(resfld_pos)
        if length == len(self._res_tbl):
            for i in range(len(resfld_pos[:-1])):
                self._res_tbl[i].grid(row=resfld_pos[i][0], column=resfld_pos[i][1])
            self._res_tbl[-1].grid(row=resfld_pos[-1][0], column=resfld_pos[-1][1], columnspan=2)

    def create(self):
        super(MainMenu, self).create()
        # add group of buttons: ('Info'3x, 'Area', 'Primer', 'Paint')
        self.__btn_frm.pack(anchor='w', **self._BTGR_PAD)
        self.__add_button_gr()
        # add button calc
        btn_calc = Button(self, image=Img.get("button_calc"), **BTN_PARAM)
        btn_calc.pack(**self._BTCALC_PAD)
        # add table group
        self.__tbl_frm.pack(**self._TBL_PAD)
        self.__add_table()
