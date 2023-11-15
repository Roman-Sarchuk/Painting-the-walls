from app import App
from winparam import Img

app = App()
Img.init()
app.rowconfigure(0, weight=1)
for c in range(3): app.columnconfigure(c, weight=1)

if __name__ == '__main__':
    app.start()


app.mainloop()
