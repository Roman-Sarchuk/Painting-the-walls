from app import *
import mainmenu


if __name__ == '__main__':
    # Creating "MainMenu"
    main_menu = mainmenu.MainMenu(root, Img.get_img("title_mainmenu"))
    main_menu.create(MENU_POS['mainmenu'])

    # Creating "CenterLine"
    btn_line = Button(root, state="disable", bg=CENTER_LINE, border=0)
    btn_line.grid(row=0, column=1, sticky="NS")

    # Creating "ParamMenu"
    #param_menu = Menu(root, Img.get_img("title_parameters"))
    #param_menu.create((0, 2))
    #doodles = Label(param_menu, image=Img.get_img("doodles"), bg=BACKGROUND)
    #doodles.pack()

root.mainloop()
