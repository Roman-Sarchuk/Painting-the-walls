from tkinter import *
from tkinter import ttk
from winparam import *
from menu import Menu
from mainmenu import MainMenu
from areamenu import AreaMenu
from primermenu import PrimerMenu
from paintmenu import PaintMenu


class App(Tk):
    # menu objects
    _mainmenu: Menu = None    # it will be an object of class "MainMenu"
    _parammenu: Menu = None   # it will be an object of class "Menu"
    _areamenu: Menu = None    # it will be an object of class "AreaMenu"
    _primermenu: Menu = None  # it will be an object of class "PrimerMenu"
    _paintmenu: Menu = None   # it will be an object of class "PaintMenu"
    # app cache
    __current_menu: Menu = None

    def __init__(self):
        super(App, self).__init__()
        # window options
        self.title('Painting the walls')
        self.iconbitmap(LOGO)
        self.geometry(WIN_SIZE)
        self.configure(bg=BACKGROUND)

    def __change_menu(self, new_menu: Menu):
        """Change current menu to new menu"""
        self.__current_menu.hide()
        new_menu.show()
        self.__current_menu = new_menu

    def _info_area(self):
        pass

    def _info_primer(self):
        pass

    def _info_paint(self):
        pass

    def _btn_area(self):
        self.__change_menu(self._areamenu)

    def _btn_primer(self):
        self.__change_menu(self._primermenu)

    def _btn_paint(self):
        self.__change_menu(self._paintmenu)

    def start(self):
        # Creating "MainMenu"
        cmds = (self._info_area, self._info_primer, self._info_paint,
                self._btn_area, self._btn_primer, self._btn_paint)
        self._mainmenu = MainMenu(self, Img.get('title_mainmenu'), cmds)
        self._mainmenu.create()
        # Creating "CenterLine"
        btn_line = Button(self, state="disable", bg=CENTER_LINE, border=0)
        btn_line.grid(row=0, column=1, sticky="NS")
        # Creating "ParamMenu"
        self._parammenu = Menu(self)
        self._parammenu.create()
        self.__current_menu = self._parammenu
        # Init "AreaMenu"
        self._areamenu = AreaMenu(self, Img.get('title_area'))
        self._areamenu.create()
        self._areamenu.hide()
        # Init "PrimerMenu"
        self._primermenu = PrimerMenu(self)
        self._primermenu.create()
        self._primermenu.hide()
        # Init "PainMenu"
        self._paintmenu = PaintMenu(self)
        self._paintmenu.create()
        self._paintmenu.hide()
