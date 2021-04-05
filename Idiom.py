import tkinter as tk
import  re
import urllib
import urllib.request as request
import urllib.error as error
import json

import GetAPI
class Idiom:

    def idiomGUI(self):
        self.window=tk.Tk()
        self.window.title("成语大全查询系统")
        self. window.geometry("600x150+100+100")
        self.result = []

        self.l=tk.Label(self.window,text="输入成语：",font="微软雅黑 11",height=2)
        self.l.grid()
        self.l1=tk.Label(self.window,text="成语释义：",font="微软雅黑 11",height=2)
        self.l1.grid()

        self.var=tk.StringVar(self.window)

        self.e=tk.Entry(self.window,width=72)
        self.e.grid(row=0,column=1)
        self.e1 = tk.Label(self.window, textvariable=self.var, width=72)
        self.e1.grid(row=1,column=1)

        self.b = tk.Button(self.window, text="点击查询", command=self.click, width=10, font="微软雅黑 12")
        self.b.grid(row=2,column=1)

        self.window.mainloop()

    def click(self):
        content=self.e.get()

        GetIdiom = GetAPI.GetAPI('http://apis.juhe.cn/idioms/query',"c8f9ae769ba517a33376d722ed85e243",content)
        results = GetIdiom.getInfo()
        if ((results != -1) and (results["result"] != None)):
            self.result = results["result"]["jbsy"]
        else:
            self.result = "查询失败！！！！"

        self.var.set(self.result)
        self.e1.update()
        self.window.mainloop()