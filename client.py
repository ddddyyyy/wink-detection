from tkinter import *
from socketserver import BaseRequestHandler, ThreadingTCPServer

import _thread


class Application(Frame):
    def __init__(self, master=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.transparent = False
        self.top = self.winfo_toplevel()
        self.top.update_idletasks()
        self.top.overrideredirect(True)


def bottom_window(root, w, h):
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = hs - h
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


app = Application()
app.master.title("sample application")
app.master.attributes('-topmost', True)
bottom_window(app.master, 100, 22)

label = Label(app.master, text='我是一个标签')  # text为显示的文本内容
label.pack()


class Handler(BaseRequestHandler):
    def handle(self):
        label.config(text=self.request.recv(1024).decode(), fg='red')
        # print('\r', self.request.recv(1024).decode(), end='')


HOST = '172.20.10.4'
PORT = 6789
ADDR = (HOST, PORT)
server = ThreadingTCPServer(ADDR, Handler)  # 参数为监听地址和已建立连接的处理类


def start_server():
    server.serve_forever()


_thread.start_new_thread(start_server, ())
app.mainloop()
