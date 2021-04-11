import tkinter as tk

#天气预报类：代码解释参考周公解梦类
import GetAPI
class Weather:

    def weatherGUI(self):
        self.window=tk.Tk()
        self.window.title("实时天气查询系统")
        self. window.geometry("400x400+100+100")
        self.result = {}

        self.l=tk.Label(self.window,text="您的城市：",font="微软雅黑 11",height=2)
        self.l.grid()
        self.l1=tk.Label(self.window,text="天气：",font="微软雅黑 11",height=2)
        self.l1.grid()
        self.l2 = tk.Label(self.window, text="温度：", font="微软雅黑 11", height=2)
        self.l2.grid()
        self.l3 = tk.Label(self.window, text="风向：", font="微软雅黑 11", height=2)
        self.l3.grid()
        self.l4 = tk.Label(self.window, text="风力：", font="微软雅黑 11", height=2)
        self.l4.grid()
        self.l5 = tk.Label(self.window, text="空气质量指数：", font="微软雅黑 11", height=2)
        self.l5.grid()

        self.var1 = tk.StringVar(self.window)
        self.var2 = tk.StringVar(self.window)
        self.var3 = tk.StringVar(self.window)
        self.var4 = tk.StringVar(self.window)
        self.var5 = tk.StringVar(self.window)

        self.e=tk.Entry(self.window,width=36)
        self.e.grid(row=0,column=1)
        self.e1 = tk.Label(self.window, textvariable=self.var1, width=36)
        self.e1.grid(row=1,column=1)
        self.e2 = tk.Label(self.window, textvariable=self.var2, width=36)
        self.e2.grid(row=2, column=1)
        self.e3 = tk.Label(self.window, textvariable=self.var3, width=36)
        self.e3.grid(row=3, column=1)
        self.e4 = tk.Label(self.window, textvariable=self.var4, width=36)
        self.e4.grid(row=4, column=1)
        self.e5 = tk.Label(self.window, textvariable=self.var5, width=36)
        self.e5.grid(row=5, column=1)

        self.b = tk.Button(self.window, text="点击查询", command=self.click, width=10, font="微软雅黑 12")
        self.b.grid(row=6,column=1)

        self.window.mainloop()

    def click(self):
        content=self.e.get()

        GetWeather = GetAPI.GetAPI('http://apis.juhe.cn/simpleWeather/query',"ddcb299c09c77aef07802a38c9457776",content)
        results = GetWeather.getInfo()
        if ((results != -1) and (results["result"] != None)):
            self.result = results["result"]["realtime"]

            self.var1.set(self.result["info"])
            self.e1.update()
            self.var2.set(self.result["temperature"])
            self.e2.update()
            self.var3.set(self.result["direct"])
            self.e3.update()
            self.var4.set(self.result["power"])
            self.e4.update()
            self.var5.set(self.result["aqi"])
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