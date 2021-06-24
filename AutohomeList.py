import requests
from lxml import html

#先获取汽车大类的链接保存下来
class GetList(object):
    def __init__(self):
        self.headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        }
        self.base_url = "https://car.autohome.com.cn"
        self.url = "https://car.autohome.com.cn/diandongche/index.html"
        
    #获取主页的侧边汽车大类链接
    def get_urls(self):
        response=requests.get(self.url,headers=self.headers).text
        etree=html.etree
        res=etree.HTML(response)
        carlist_href = res.xpath("//div[@id='cartree']/ul/li/h3/a/@href") #xpath获取车列表
        carlist_href=[self.base_url+ch_url for ch_url in carlist_href]
        return carlist_href

    #获取大类中的各个车型链接并保存到txt文件中
    def get_attribute(self):
        carlist=self.get_urls()
        etree=html.etree
        file=open(r"./CarHref.txt","w")
        i=0
        while i<len(carlist):
            url=carlist[i]
            response = requests.get(url, headers=self.headers).text
            res=etree.HTML(response)
            chlist_href=res.xpath("//*[contains(@id,'series_')]/@href")
            for ele in chlist_href:
                print(ele)
                #print(type(output))
                file.write(self.base_url+str(ele))
                file.write("\n")
            i=i+1
        file.close()
