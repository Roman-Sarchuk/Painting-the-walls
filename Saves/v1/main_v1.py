from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Painting the walls")
root.iconbitmap("imgs/Logo.ico")
root.geometry("525x370")
# root.resizable(False, False)


class Part(Frame):
    def _title(self, title_img: str):
        photo = ImageTk.PhotoImage(Image.open(title_img))
        lbl = Label(self, image=img)
        lbl.pack()


    def create(self, position: list, photo: str):
        self.grid(row=position[0], column=position[1])
        self._title(photo)


if __name__ == '__main__':
    img = ImageTk.PhotoImage(Image.open("imgs/Title-MainMenu.png"))
    for c in range(3): root.columnconfigure(c, weight=1)
    root.rowconfigure(0, weight=1)

    """frm1 = Frame(root)
    frm1.grid(row=0, column=0)
    frm2 = Frame(root)
    frm2.grid(row=0, column=2)

    # Create a Label Widget to display the text or Image
    label1 = Label(frm1, image=imgs)
    label1.pack()
    button1 = Button(frm1, image=imgs)
    button1.pack()

    # Create line
    btn_line = Button(root, state="disable", bg="#C0BCBC")
    btn_line.grid(row=0, column=1, sticky="NS")

    # Create a Label Widget to display the text or Image
    label2 = Label(frm2, image=imgs)
    label2.pack()
    button2 = Button(frm2, image=imgs)
    button2.pack()"""

    part_main = Part(root, width=234, height=333)
    part_main.create([0, 0], "imgs/Title-MainMenu.png")

    btn_line = Button(root, state="disable", bg="#C0BCBC")
    btn_line.grid(row=0, column=1, sticky="NS")

    part_parameter = Part(root, width=234, height=333)
    part_parameter.create([0, 2], "imgs/Title-Parameters.png")

root.mainloop()
