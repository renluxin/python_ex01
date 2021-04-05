import tkinter as tk
import  re
import urllib
import urllib.request as request
import urllib.error as error
import json

import GetAPI
class Constellation:

    def conGUI(self):
        self.window=tk.Tk()
        self.window.title("星座运势查询系统")
        self. window.geometry("300x400+100+100")
        self.result = ""

        self.l=tk.Label(self.window,text="您的星座：",font="微软雅黑 11",height=2)
        self.l.grid()
        self.l1=tk.Label(self.window,text="查询时间：",font="微软雅黑 11",height=2)
        self.l1.grid()
        self.l2 = tk.Label(self.window, text="综合指数：", font="微软雅黑 11", height=2)
        self.l2.grid()
        self.l3 = tk.Label(self.window, text="幸运色：", font="微软雅黑 11", height=2)
        self.l3.grid()
        self.l4 = tk.Label(self.window, text="幸运数字：", font="微软雅黑 11", height=2)
        self.l4.grid()
        self.l5 = tk.Label(self.window, text="速配星座：", font="微软雅黑 11", height=2)
        self.l5.grid()


        self.var1=tk.StringVar(self.window)
        self.var2 = tk.StringVar(self.window)
        self.var3 = tk.StringVar(self.window)
        self.var4 = tk.StringVar(self.window)
        self.var5 = tk.StringVar(self.window)

        self.e=tk.Entry(self.window,width=30)
        self.e.grid(row=0,column=1)
        self.e1 = tk.Label(self.window, textvariable=self.var1, width=30)
        self.e1.grid(row=1,column=1)
        self.e2 = tk.Label(self.window, textvariable=self.var2, width=30)
        self.e2.grid(row=2, column=1)
        self.e3 = tk.Label(self.window, textvariable=self.var3, width=30)
        self.e3.grid(row=3, column=1)
        self.e4 = tk.Label(self.window, textvariable=self.var4, width=30)
        self.e4.grid(row=4, column=1)
        self.e5 = tk.Label(self.window, textvariable=self.var5, width=30)
        self.e5.grid(row=5, column=1)

        self.b = tk.Button(self.window, text="今日运势", command=self.click, width=10, font="微软雅黑 12")
        self.b.grid(row=6,column=1)

        self.window.mainloop()

    def click(self):
        content=self.e.get()

        Getcon = GetAPI.GetAPI('http://web.juhe.cn:8080/constellation/getAll',"bcb5de22c857694cfada54c549f3891f",content,"today")
        results = Getcon.getInfo()
        if ((results != -1) and (results["error_code"] == 0)):
            self.result = results

            self.var1.set(self.result["datetime"])
            self.e1.update()
            self.var2.set(self.result["all"])
            self.e2.update()
            self.var3.set(self.result["color"])
            self.e3.update()
            self.var4.set(self.result["number"])
            self.e4.update()
            self.var5.set(self.result["QFriend"])
            self.e5.update()
        else:
            self.var1.set("查询失败！！！")
            self.e1.update()
            self.var2.set("查询失败！！！")
            self.e2.update()
            self.var3.set("查询失败！！！")
            self.e3.update()
            self.var4.set("查询失败！！！")
            self.e4.update()
            self.var5.set("查询失败！！！")
            self.e5.update()

        self.window.mainloop()