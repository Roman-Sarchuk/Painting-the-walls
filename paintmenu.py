from menu import *


class PaintMenu(Menu):
    def __init__(self, master, title_img=None):
        super(PaintMenu, self).__init__(master, title_img)

    def create(self):
        super(PaintMenu, self).create()
