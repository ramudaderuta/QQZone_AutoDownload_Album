from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from tkinter.ttk import *

# 自动隐藏滚动条
def scrollbar_autohide(bar, widget):
    def show():
        bar.lift(widget)

    def hide():
        bar.lower(widget)

    hide()
    widget.bind("<Enter>", lambda e: show())
    bar.bind("<Enter>", lambda e: show())
    widget.bind("<Leave>", lambda e: hide())
    bar.bind("<Leave>", lambda e: hide())

class Simpledialog:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create(title='', prompt='', initialvalue=''):
        root = Tk()
        # 隐藏空白主窗口
        root.withdraw()
        result = simpledialog.askstring(title=title, prompt=prompt, initialvalue=initialvalue)
        root.destroy()
        return result

class SimpleMessagebox:
    def __init__(self) -> None:
        pass

    @staticmethod
    def create(title='', message='', msg_type='error'):
        root = Tk()
        # 隐藏空白主窗口
        root.withdraw()
        result = ''
        if msg_type == 'error':
            result = messagebox.showerror(title=title, message=message)
        elif msg_type == 'warning':
            result = messagebox.showwarning(title=title, message=message)
        root.destroy()
        return result

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.create_widgets()

    def __win(self):
        self.title("QQ空间相册批量下载")

        # 获取屏幕DPI
        dpi = self.winfo_fpixels('1i')

        # 设置窗口大小，根据DPI调整
        width = int(568 * (dpi / 96))  # 96 DPI为标准DPI
        height = int(487 * (dpi / 96))

        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def create_widgets(self):
        # Frame for instructions
        self.frame_note = LabelFrame(self, text="使用说明")
        self.frame_note.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        self.label_note1 = Label(self.frame_note, text="1、由于登录可能有问题，建议先在电脑上登录QQ，以便使用快捷登录。", anchor="w")
        self.label_note1.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.label_note2 = Label(self.frame_note, text="2、填写完信息后，点击“启动”按钮即可；", anchor="w")
        self.label_note2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.label_note3 = Label(self.frame_note, text="3、若对方Q号为空，则为下载自己；若你的Q密为空，则需手动完成登录；", anchor="w")
        self.label_note3.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        # User inputs
        self.label_username = Label(self, text="你的QQ账号", anchor="center")
        self.label_username.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.tk_input_username = Entry(self)
        self.tk_input_username.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.label_password = Label(self, text="你的QQ密码", anchor="center")
        self.label_password.grid(row=1, column=2, padx=10, pady=5, sticky="e")

        self.tk_input_password = Entry(self, show='*')
        self.tk_input_password.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        self.label_other_username = Label(self, text="对方QQ账号", anchor="center")
        self.label_other_username.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.tk_input_other_username = Entry(self)
        self.tk_input_other_username.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.label_threads_num = Label(self, text="下载线程数", anchor="center")
        self.label_threads_num.grid(row=2, column=2, padx=10, pady=5, sticky="e")

        self.tk_input_threads_num = Entry(self)
        self.tk_input_threads_num.insert(0, '4')
        self.tk_input_threads_num.grid(row=2, column=3, padx=10, pady=5, sticky="w")

        self.label_save_path = Label(self, text="保存的路径", anchor="center")
        self.label_save_path.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.tk_input_save_path = Entry(self)
        self.tk_input_save_path.delete('0', END)
        self.tk_input_save_path.insert('0', './QQZone')
        self.tk_input_save_path.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="we")

        self.button_select_path = Button(self, text="选择路径")
        self.button_select_path.grid(row=3, column=3, padx=10, pady=5, sticky="w")

        # Start button
        self.button_start = Button(self, text="启动")
        self.button_start.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        # Debug text box with scrollbar
        self.text_debug = Text(self)
        self.text_debug.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        self.vbar = Scrollbar(self, orient=VERTICAL, command=self.text_debug.yview)
        self.text_debug.configure(yscrollcommand=self.vbar.set)
        self.vbar.grid(row=5, column=4, sticky='ns')

        scrollbar_autohide(self.vbar, self.text_debug)

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def update_debug(self, strings):
        self.text_debug.delete('1.0', END)
        self.text_debug.insert('1.0', strings)
        self.text_debug.update()
        self.text_debug.see(END)

    def append_debug(self, strings, end='\n'):
        self.text_debug.insert(END, str(strings) + end)
        self.text_debug.update()
        self.text_debug.see(END)

    def start(self, evt):
        pass

    def select_path(self, evt):
        path = filedialog.askdirectory(title='请选择一个目录')
        if path:
            self.tk_input_save_path.delete('0', END)
            self.tk_input_save_path.insert('0', path)

    def __event_bind(self):
        self.button_start.bind('<Button-1>', self.start)
        self.button_select_path.bind('<Button-1>', self.select_path)

    def disable_button_start(self):
        self.button_start.config(state=DISABLED, text="运行中...")
        self.button_start.update()
        self.button_start.unbind("<Button-1>")

    def enable_button_start(self):
        self.button_start.config(state=NORMAL, text="启动")
        self.button_start.update()
        self.button_start.bind('<Button-1>', self.start)

if __name__ == "__main__":
    win = Win()
    win.mainloop()
