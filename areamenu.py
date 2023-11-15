from menu import *
from winparam import BTN_PARAM
from tkinter import ttk


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


class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        # widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        # canvas
        self.canvas = Canvas(self, background='red', scrollregion=(0, 0, self.winfo_width(), self.list_height))
        self.canvas.pack(expand=True, fill='both')

        # display frame
        self.frame = ttk.Frame(self)

        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill='both', pady=4, padx=10)

        # scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

        # events
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
        self.bind('<Configure>', self.update_size)

    def update_size(self, event):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.canvas.bind_all('<MouseWheel>',
                                 lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
            self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        else:
            height = self.winfo_height()
            self.canvas.unbind_all('<MouseWheel>')
            self.scrollbar.place_forget()

        self.canvas.create_window(
            (0, 0),
            window=self.frame,
            anchor='nw',
            width=self.winfo_width(),
            height=height)

    def create_item(self, index, item):
        frame = ttk.Frame(self.frame)

        # grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

        # widgets
        ttk.Label(frame, text=f'#{index}').grid(row=0, column=0)
        ttk.Label(frame, text=f'{item[0]}').grid(row=0, column=1)
        ttk.Button(frame, text=f'{item[1]}').grid(row=0, column=2, columnspan=3, sticky='nsew')

        return frame


class AreaMenu(Menu):
    _STS_PAD = {'ipadx': 10, 'ipady': 0}
    _BTN_PAD = {'pady': (4, 0)}

    def __init__(self, master, title_img):
        super(AreaMenu, self).__init__(master, title_img)
        # |=== init frames ===|
        # -- setting frame --
        self._stng_frm = Frame(self, bg=BACKGROUND)
        # status frame (setting frame)
        self._sts_frm = Frame(self._stng_frm, bg=BACKGROUND)
        # painting area frame (setting frame)
        self._ptar_frm = Frame(self._stng_frm, bg=BACKGROUND)
        # -- data frame --
        self._data_frm = Frame(self, bg=BACKGROUND)

        # |=== init RadioButton ===|  (status frame (setting frame))
        self._rbt = [Button(self._sts_frm, image=Img.get('point_on'), **BTN_PARAM,
                            command=lambda n=0: self.__change_point_ico(n)),
                     Button(self._sts_frm, image=Img.get('point_off'), **BTN_PARAM,
                            command=lambda n=1: self.__change_point_ico(n))]
        self._rbt[0].grid(row=0, column=0)
        self._rbt[1].grid(row=1, column=0)
        self.__active_rbt = 0
        # |=== create list of widgets ===|
        self._data_add = [DataField()]
        self._data_sbstr = [DataField()]

    def __change_point_ico(self, rbt_num):
        print(self.__active_rbt, '>>', rbt_num)
        if rbt_num != self.__active_rbt:
            self._rbt[rbt_num]['image'] = Img.get('point_on')
            self._rbt[self.__active_rbt]['image'] = Img.get('point_off')
            self.__active_rbt = rbt_num

    def __fill_stng_frm(self):
        """This function create several frames to fill settings frame(first frame in AreaMenu)"""
        # |=== init status frame ===|
        self._sts_frm.grid(row=0, column=0, **self._STS_PAD)
        for r in range(2): self._sts_frm.rowconfigure(r, weight=1)
        for c in range(2): self._sts_frm.columnconfigure(c, weight=1)
        # add point buttons
        self._rbt[0].grid(row=0, column=0)
        self._rbt[1].grid(row=1, column=0)
        # add labels
        lb_status = [Label(self._sts_frm, image=Img.get('area_status1'), bg=BACKGROUND),
                     Label(self._sts_frm, image=Img.get('area_status2'), bg=BACKGROUND)]
        lb_status[0].grid(row=0, column=1)
        lb_status[1].grid(row=1, column=1)

        # |=== init painting area frame ===|
        pnt_frm = Frame(self._stng_frm, bg=BACKGROUND)
        pnt_frm.grid(row=0, column=1)

        # -- area entry frame --
        area_frm = Frame(pnt_frm, bg=BACKGROUND)
        area_frm.grid(row=0, column=0, columnspan=2)
        # area border
        lb_brd = Label(area_frm, image=Img.get('frm_paintingarea'), bg=BACKGROUND)
        lb_brd.grid(row=0, column=0, rowspan=2)
        # area label
        lb_area = Label(area_frm, image=Img.get('txt_paintingarea'), bg=BACKGROUND)
        lb_area.grid(row=0, column=0)
        # area entry
        entry_bg = Label(area_frm, image=Img.get('entry_paintingarea'), bg=BACKGROUND)
        entry_bg.grid(row=1, column=0)
        en_area = Entry(area_frm, width=10, border=0)
        en_area.insert(0, '123')
        en_area.grid(row=1, column=0)

        # -- operation buttons --
        # calculate button
        btn_calc = Button(pnt_frm, image=Img.get('button_areacalc'), **BTN_PARAM)
        btn_calc.grid(row=1, column=0, **self._BTN_PAD)
        # save button
        btn_save = Button(pnt_frm, image=Img.get('button_areasave'), **BTN_PARAM)
        btn_save.grid(row=1, column=1, **self._BTN_PAD)

    def __fill_data_frm(self):
        # |=== create outline ===|
        lb = Label(self._data_frm, image=Img.get('frm_data'), bg=BACKGROUND)
        lb.grid(row=0, column=0, columnspan=3)
        line = Label(self._data_frm, image=Img.get('line_data'), bg=BACKGROUND)
        line.grid(row=0, column=1)

        # |=== add frames with data field lists ===|
        frm_add = Frame(self._data_frm, bg=BACKGROUND)
        frm_add.grid(row=0, column=0)
        frm_sbstr = Frame(self._data_frm, bg=BACKGROUND)
        frm_sbstr.grid(row=0, column=2)

        # |=== add data field titles ===|
        title_add = Label(frm_add, image=Img.get('txt_entryadd'), bg=BACKGROUND)
        title_add.pack()
        title_sbstr = Label(frm_sbstr, image=Img.get('txt_entrysbstr'), bg=BACKGROUND)
        title_sbstr.pack()

        # |=== add scrolling ===|
        '''frmlist_param = {'width': 10, 'bg': BACKGROUND}
        frmlist_add = Frame()
        frmlist_sbstr = Frame()
        frmlist_add.pack(side=LEFT, fill=BOTH, expand=1)
        frmlist_sbstr.pack(side=LEFT, fill=BOTH, expand=1)
        scbr_add = Scrollbar(frm_add, orient="vertical", command=frmlist_add.yview)
        scbr_sbstr = Scrollbar(frm_sbstr, orient="vertical", command=frmlist_sbstr.yview)
        scbr_add.pack(side=RIGHT, fill=Y)
        scbr_sbstr.pack(side=RIGHT, fill=Y)'''
        text_list1 = [('label', 'button'), ('thing', 'click'), ('third', 'something'), ('label1', 'button'),
                     ('label2', 'button'), ('label3', 'button'), ('label4', 'button')]
        list_frame1 = ListFrame(frm_add, text_list1, 10)
        text_list2 = [('label', 'button'), ('thing', 'click'), ('third', 'something'), ('label1', 'button'),
                     ('label2', 'button'), ('label3', 'button'), ('label4', 'button')]
        list_frame2 = ListFrame(frm_sbstr, text_list2, 10)

    def create(self):
        super(AreaMenu, self).create()
        # create setting frame
        self._stng_frm.pack()
        self.__fill_stng_frm()
        # create data frame
        self._data_frm.pack()
        self.__fill_data_frm()
