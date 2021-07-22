import tkinter as tk

win = tk.Tk()          #创建窗口
win.title("Hello")
label1 = tk.Label(win, text="用户名: ")
label2 = tk.Label(win, text="密码: ")
etUsername = tk.Entry(win)       # 编辑框
etPassword = tk.Entry(win)
label1.grid(row=0, column=0, padx=5, pady=5)   # Label放在0行0列，上下左右留白5像素
label2.grid(row=1, column=0, padx=5, pady=5)
etUsername.grid(row=0, column=1, padx=5, pady=5)
etPassword.grid(row=1, column=1, padx=5, pady=5)
btLogin = tk.Button(win, text="登录")
btLogin.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
win.geometry("800x500+200+100")
win.mainloop()      # 显示窗口
