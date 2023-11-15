from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

BACKGROUND = '#D9D9D9'
CENTER_LINE = "#C0BCBC"
MENU_POS = {'mainmenu': (0, 0), 'parammenu': (0, 2)}

root = Tk()
root.title("Painting the walls")
root.iconbitmap("imgs/Logo.ico")
root.geometry("525x370")
root.configure(bg=BACKGROUND)
# root.resizable(False, False)
for c in range(3): root.columnconfigure(c, weight=1)
root.rowconfigure(0, weight=1)


class Img:
    _imgs = {
        'title_mainmenu': ImageTk.PhotoImage(Image.open("imgs/Title-MainMenu.png")),
        'title_parameters': ImageTk.PhotoImage(Image.open("imgs/Title-Parameters.png")),
        'button_calc': ImageTk.PhotoImage(Image.open("imgs/Button-Calc.png")),
        'button_info': ImageTk.PhotoImage(Image.open("imgs/Button-Info.png")),
        'button_area': ImageTk.PhotoImage(Image.open("imgs/Button-Area.png")),
        'button_primer': ImageTk.PhotoImage(Image.open("imgs/Button-Primer.png")),
        'button_paint': ImageTk.PhotoImage(Image.open("imgs/Button-Paint.png")),
        'tableField_doodles': ImageTk.PhotoImage(Image.open("imgs/TableField-Doodles.png")),
        'tableField_primer': ImageTk.PhotoImage(Image.open("imgs/TableField-Primer.png")),
        'tableField_paint': ImageTk.PhotoImage(Image.open("imgs/TableField-Paint.png")),
        'tableField_number': ImageTk.PhotoImage(Image.open("imgs/TableField-Number.png")),
        'tableField_price': ImageTk.PhotoImage(Image.open("imgs/TableField-Price.png")),
        'tableField_amount': ImageTk.PhotoImage(Image.open("imgs/TableField-Amount.png")),
        'doodles': ImageTk.PhotoImage(Image.open("imgs/Doodles.png"))
    }

    @classmethod
    def get_img(cls, name):
        if type(name) is str:
            return cls._imgs[name]
        raise ValueError("'name' must be of type str")
