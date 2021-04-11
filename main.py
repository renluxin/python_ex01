# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
import  re
import urllib
import urllib.request as request
import urllib.error as error
import json
import Dreaming
import Weather
import Idiom
import Constellation
import Weather_Reptile

'''
dream = Dreaming.Dreaming()
dream.dreamGUI()
'''
dream = None
def dream():#调用周公解梦模块
    dream = Dreaming.Dreaming()
    dream.dreamGUI()

def weather():#调用天气预报模块
    weather = Weather.Weather()
    weather.weatherGUI()

def idiom():#调用成语大全模块
    joke = Idiom.Idiom()
    joke.idiomGUI()

def constellation():#调用星座运势模块
    constellation = Constellation.Constellation()
    constellation.conGUI()

def weather_reptile():
    weather_reptile = Weather_Reptile.Weather_Reptile("http://www.weather.com.cn/weather/101220101.shtml")
    weather_reptile.draw()

if __name__ == "__main__":
    #定义窗口
    mainWindow=tk.Tk()
    mainWindow.title("第一次python作业")
    mainWindow.geometry("330x120+100+100")
    #定义按钮
    b1=tk.Button(mainWindow,text="周公解梦",command=dream,width=10,font="微软雅黑 12")
    b1.grid(row = 2,column = 2)
    b2=tk.Button(mainWindow,text="天气预报",command=weather,width=10,font="微软雅黑 12")
    b2.grid(row = 2,column = 4)
    b3=tk.Button(mainWindow,text="成语大全",command=idiom,width=10,font="微软雅黑 12")
    b3.grid(row = 3,column = 2)
    b4=tk.Button(mainWindow,text="星座运势",command=constellation,width=10,font="微软雅黑 12")
    b4.grid(row = 3,column = 4)
    b4 = tk.Button(mainWindow, text="气温走势(爬虫获取)", command=weather_reptile, width=15, font="微软雅黑 12")
    b4.grid(row=4, column=3)

    b5=tk.Button(mainWindow,text="退出",command=mainWindow.quit,width=10,font="微软雅黑 12")
    b5.grid(row=5,column=3)
    #展示
    mainWindow.mainloop()
