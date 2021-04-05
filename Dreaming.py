import tkinter as tk
import  re
import urllib
import urllib.request as request
import urllib.error as error
import json

import GetAPI
class Dreaming:

    def dreamGUI(self):#界面
        #窗口的定义
        self.window=tk.Tk()
        self.window.title("周公解梦查询系统")
        self. window.geometry("600x150+100+100")

        #提示语：
        self.l=tk.Label(self.window,text="您的梦境：",font="微软雅黑 11",height=2)
        self.l.grid()
        self.l1=tk.Label(self.window,text="梦境解析：",font="微软雅黑 11",height=2)
        self.l1.grid()

        #存储变量：
        self.var=tk.StringVar(self.window)
        self.result = ""

        #输入与输出
        self.e=tk.Entry(self.window,width=72)
        self.e.grid(row=0,column=1)
        self.e1 = tk.Label(self.window, textvariable=self.var, width=72)
        self.e1.grid(row=1,column=1)

        #按钮
        self.b = tk.Button(self.window, text="点击查询", command=self.click, width=10, font="微软雅黑 12")
        self.b.grid(row=2,column=1)

        self.window.mainloop()

    def click(self):#点击后触发，调接口
        content=self.e.get()    #获取用户输入

        #调用GetAPI类实现调用接口
        GetDream = GetAPI.GetAPI('http://v.juhe.cn/dream/query',"2ba1f0a85f0cbe98201aa07ecbd6b8b5",content)
        results = GetDream.getInfo()

        #成功获取数据后存储所需部分，否则显示失败
        if ((results != -1) and (results["result"] != None)):
            self.result = results["result"][0]["des"]
        else:
            self.result = "查询失败！！！"

        #输出展示
        self.var.set(self.result)
        self.e1.update()

        self.window.mainloop()