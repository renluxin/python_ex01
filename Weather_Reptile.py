#-*- codeing = utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib.request
import matplotlib.pyplot as plt
from pylab import *

class Weather_Reptile:
    def __init__(self,url):
        self.url = url

    def askURL(self):
        head = {  # 浏览器头部信息
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 81.0.4044.113Safari / 537.36"
        }

        request = urllib.request.Request(self.url, headers=head)  # 浏览器头部信息+网页地址信息
        self.html = ""  # 定义一个字符串html来存储即将获取的网页源代码
        try:
            response = urllib.request.urlopen(request)  # 在服务器中获取信息
            self.html = response.read().decode("utf-8")  # 提取获得的网页源代码，utf-8用来正常显示中文
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)

    def getData(self):


        findDate = re.compile(r'<h1>(.*?)</h1>')
        findHtemperature = re.compile(r'<span>(.*?)</span>')
        findLtemperature = re.compile(r'<i>(.*?)℃</i>')
        findWeather = re.compile(r'<p class="wea" title="(.*?)">')

        soup = BeautifulSoup(self.html, "html.parser")  # 解析html，以树形结构存入soup
        for item in soup.find_all("ul", class_="t clearfix"):  # 查找符合要求的字符串形成列表
            self.data = [[], [], [], [], [], [], []]  # 分别用来保存一天的天气情况
            item = str(item)  # 将列表item转换为字符串

            Dates = re.findall(findDate, item)
            Htemperatures = re.findall(findHtemperature, item)
            Ltemperatures = re.findall(findLtemperature, item)
            Htemperatures.insert(0, Ltemperatures[0])
            Weathers = re.findall(findWeather, item)

            i = 0
            for Date in Dates:
                self.data[i].append(Dates[i])
                self.data[i].append(int(Htemperatures[i]))
                self.data[i].append(int(Ltemperatures[i]))
                self.data[i].append(Weathers[i])
                i = i + 1
        return self.data

    def draw(self):
        self.askURL()
        self.getData()
        mpl.rcParams['font.sans-serif'] = ['SimHei']

        names = [self.data[i][0] for i in range(1,6)]
        x = range(len(names))
        yMax = [self.data[i][1] for i in range(1,6)]
        yMin = [self.data[i][2] for i in range(1,6)]
        plt.plot(x, yMax, marker='o', mec='r', mfc='w', label=u'最高温')
        plt.plot(x, yMin, marker='*', ms=10, label=u'最低温')
        plt.ylim(min(yMin)*0.75, max(yMax)*1.25)
        plt.legend()  # 让图例生效
        plt.xticks(x, names, rotation=45)
        plt.margins(0)
        plt.subplots_adjust(bottom=0.25)
        plt.xlabel(u"日期")  # X轴标签
        plt.ylabel("温度（℃）")  # Y轴标签
        plt.title("合肥市气温走势")  # 标题

        plt.show()