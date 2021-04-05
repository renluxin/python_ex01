import tkinter as tk
import  re
import urllib
import urllib.request as request
import urllib.error as error
import json

import GetAPI

window=tk.Tk()
window.title("周公解梦查询系统")
window.geometry("400x150+100+100")

l=tk.Label(window,text="您的梦境：",font="微软雅黑 11",height=2)
l.grid()
l1=tk.Label(window,text="梦境解析：",font="微软雅黑 11",height=2)
l1.grid()

var=tk.StringVar()

e=tk.Entry(window,width=32)
e.grid(row=0,column=1)
e1=tk.Entry(window,textvariable=var,width=32)
e1.grid(row=1,column=1)

def click():
    content=e.get()
    GetDream = GetAPI.GetAPI('http://v.juhe.cn/dream/query',"2ba1f0a85f0cbe98201aa07ecbd6b8b5",content)
    result = GetDream.getInfo()
    var.set(result["result"][1]["des"])
b=tk.Button(window,text="点击查询",command=click,width=10,font="微软雅黑 12")
b.grid()
b1=tk.Button(window,text="退出",command=window.quit,width=10,font="微软雅黑 12")
b1.grid(row=2,column=1)

if __name__ == "__main__":
    window.mainloop()
