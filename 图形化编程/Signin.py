import tkinter as tk


def cbPassword_click():
    if showPassword.get():
        etPassword["show"] = ""  # 显示密码
    else:
        etPassword["show"] = "*"


def btLogin_click():
    if username.get() == "minster" and password.get() == "123456":
        lbHint["text"] = "登录成功"
        lbHint["fg"] = "black"  # 文字变为黑色，“fg”表示前景色，“bg”表示背景色
    else:
        username.set("")  # 清空输入框
        password.set("")
        lbHint["fg"] = "red"
        lbHint["text"] = "用户名或密码错误，请重新输入！"


win = tk.Tk()
win.title("登录")
lbUsername = tk.Label(win, text="用户名: ")
lbPassword = tk.Label(win, text="密码: ")
username, password = tk.StringVar(), tk.StringVar()  # 字符串变量，用于关联用户名输入和密码输入框
etUsername = tk.Entry(win, textvariable=username)  # 用户名输入框，与username关联
etPassword = tk.Entry(win, textvariable=password, show='*')
lbHint = tk.Label(win, text="请登录")
lbHint.grid(row=0, column=0, columnspan=2)
lbUsername.grid(row=1, column=0, padx=5, pady=5)
lbPassword.grid(row=2, column=0, padx=5, pady=5)
etUsername.grid(row=1, column=1, padx=5, pady=5)
etPassword.grid(row=2, column=1, padx=5, pady=5)
showPassword = tk.BooleanVar()  # 用于关联“显示密码”当选框
showPassword.set(True)  # 一开始为选中状态
cbPassword = tk.Checkbutton(win, text="显示密码", variable=showPassword, command=cbPassword_click())
# cbPassword关联showPassword,其事件响应函数是cbPassword_click
cbPassword.grid(row=3, column=0, padx=5, pady=5)
btLogin = tk.Button(win, text="登录", command=btLogin_click)
btQuit = tk.Button(win, text="退出", command=win.quit())
btLogin.grid(row=4, column=0, pady=5)
btQuit.grid(row=4, column=1, pady=5)
win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)
win.rowconfigure(0, weight=1)
win.rowconfigure(1, weight=1)
win.rowconfigure(2, weight=1)
win.rowconfigure(3, weight=1)
win.rowconfigure(4, weight=1)
win.geometry("500x200")
win.mainloop()
