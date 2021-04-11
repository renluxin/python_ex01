#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib.request as request
import urllib.error as error
import json

#GetAPI类：调接口的类
# 将传入的参数处理为能够调用接口的标准参数格式，并申请调用接口，返回相应信息或异常。
class GetAPI:
    def __init__(self,url,key,*otherPara):#初始化，将传入参数赋给类的对象
        self.url = url      #API地址
        self.key = key      #API密钥
        self.getPara(*otherPara)    #不同API需要的其他不同参数

    def getPara(self,*otherPara):#被初始化调用，用来处理不同API需要的不同参数
        self.otherPara = []     #存储传入的参数
        for item in otherPara:
            self.otherPara.append(item)

        self.params_dict = {}   #存储标准的可用于调用接口的参数的格式
        #由于不同接口需要的参数不同，下面的几个if语句用来处理不同接口的参数

        #周公解梦参数
        if(self.url == "http://v.juhe.cn/dream/query"):
            self.params_dict["key"] = self.key
            self.params_dict["q"] = self.otherPara[0]
        #天气预报参数
        if (self.url == "http://apis.juhe.cn/simpleWeather/query"):
            self.params_dict["key"] = self.key
            self.params_dict["city"] = self.otherPara[0]
        #成语大全参数
        if (self.url == "http://apis.juhe.cn/idioms/query"):
            self.params_dict["key"] = self.key
            self.params_dict["wd"] = self.otherPara[0]
        # 星座运势参数
        if (self.url == "http://web.juhe.cn:8080/constellation/getAll"):
            self.params_dict["key"] = self.key
            self.params_dict["consName"] = self.otherPara[0]
            self.params_dict["type"] = self.otherPara[1]

    def getInfo(self):#传入参数调用接口的具体核心过程
        api_url = self.url      #API接口地址
        params = urllib.parse.urlencode(self.params_dict)       #参数列表
        try:#请求访问并检查异常
            req = request.Request(api_url, params.encode())
            response = request.urlopen(req)
            content = response.read()
            if content:
                try:
                    result = json.loads(content)
                    return result
                except Exception as e:
                    return -1       #解析异常
            else:
                # 可能网络异常等问题，无法获取返回内容，请求异常
                return -1
        except error.HTTPError as err:
            return -1
        except error.URLError as err:
        # 其他异常
            return -1