from PIL import Image, ImageTk

# window colors
BACKGROUND = '#D9D9D9'
CENTER_LINE = "#C0BCBC"
# app parameters
WIN_SIZE = '530x360'
MENU_PAD = {'padx': 7, 'pady': (12, 0)}
BTN_PARAM = {'border': 0, 'bg': BACKGROUND, 'activebackground': BACKGROUND, 'cursor': 'hand2'}
LOGO = 'imgs/Other/Logo.ico'
# Images in folders are recorded by Train-Case, and image keys in list are recorded by snake_case
IMGS = {'title_parameters': Image.open('imgs/Other/Title-Parameters.png'),
        'doodles': Image.open('imgs/Other/Doodles.png'),
        'title_mainmenu': Image.open('imgs/MainMenu/Title-MainMenu.png'),
        'button_calc': Image.open('imgs/MainMenu/Button-Calc.png'),
        'button_info': Image.open('imgs/MainMenu/Button-Info.png'),
        'button_area': Image.open('imgs/MainMenu/Button-Area.png'),
        'button_primer': Image.open('imgs/MainMenu/Button-Primer.png'),
        'button_paint': Image.open('imgs/MainMenu/Button-Paint.png'),
        'tablefield_doodles': Image.open('imgs/MainMenu/TableField-Doodles.png'),
        'tablefield_primer': Image.open('imgs/MainMenu/TableField-Primer.png'),
        'tablefield_paint': Image.open('imgs/MainMenu/TableField-Paint.png'),
        'tablefield_number': Image.open('imgs/MainMenu/TableField-Number.png'),
        'tablefield_price': Image.open('imgs/MainMenu/TableField-Price.png'),
        'tablefield_amount': Image.open('imgs/MainMenu/TableField-Amount.png'),
        'tablefield_void': Image.open('imgs/MainMenu/TableField-Void.png'),
        'tablefield_longvoid': Image.open('imgs/MainMenu/TableField-LongVoid.png'),
        'title_area': Image.open('imgs/AreaMenu/Title-Area.png'),
        'point_off': Image.open('imgs/AreaMenu/Point-Off.png'),
        'point_on': Image.open('imgs/AreaMenu/Point-On.png'),
        'area_status1': Image.open('imgs/AreaMenu/Area-Status1.png'),
        'area_status2': Image.open('imgs/AreaMenu/Area-Status2.png'),
        'button_areacalc': Image.open('imgs/AreaMenu/Button-AreaCalc.png'),
        'button_areasave': Image.open('imgs/AreaMenu/Button-AreaSave.png'),
        'frm_paintingarea': Image.open('imgs/AreaMenu/Frm-PaintingArea.png'),
        'txt_paintingarea': Image.open('imgs/AreaMenu/Txt-PaintingArea.png'),
        'entry_paintingarea': Image.open('imgs/AreaMenu/Entry-PaintingArea.png'),
        'frm_data': Image.open('imgs/AreaMenu/Frm-Data.png'),
        'line_data': Image.open('imgs/AreaMenu/Line-Data.png'),
        'txt_entryadd': Image.open('imgs/AreaMenu/Txt-EntryAdd.png'),
        'txt_entrysbstr': Image.open('imgs/AreaMenu/Txt-EntrySbstr.png'),
        'bg_datafield': Image.open('imgs/AreaMenu/Bg-DataField.png'),
        'txt_length': Image.open('imgs/AreaMenu/Txt-Length.png'),
        'txt_width': Image.open('imgs/AreaMenu/Txt-Width.png'),
        'entry_datafield': Image.open('imgs/AreaMenu/Entry-DataField.png'),
        'ico_close': Image.open('imgs/AreaMenu/Ico-Close.png'),
        'button_plus': Image.open('imgs/AreaMenu/Button-Plus.png'),
        }


class Img:
    """This class exists to contain opened images."""
    __imgs = {}

    @classmethod
    def __fill_imglist(cls):
        cls.__imgs = IMGS.copy()
        try:
            for i in cls.__imgs:
                cls.__imgs[i] = ImageTk.PhotoImage(cls.__imgs[i])
        except:
            raise RuntimeError("!! You must init 'Img' object after initializing 'Tk' object !!")

    @classmethod
    def init(cls):
        cls.__fill_imglist()

    @classmethod
    def get(cls, img_name):
        if type(img_name) is not str:
            raise ValueError("!! 'img_name' must be of type 'str' !!")
        if len(cls.__imgs) == 0:
            raise RuntimeError("!! Firstly you must init 'Img' object after initializing 'Tk' object !!")
        return cls.__imgs[img_name]
