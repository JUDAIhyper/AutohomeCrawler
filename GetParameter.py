import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

#下载车型配置表
class Car_Config(object):
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://car.autohome.com.cn"
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        }

    def getExcel(self,url):
        response = requests.get(url, headers=self.headers).text
        soup=BeautifulSoup(response,'lxml')
        #从配置链接获取详情页面跳转
        data=soup.select("body > div.content > div.row > div.column.grid-16.contentright.fn-visible > div:nth-child(7) > div > div.car-cont > div > div > div > div.list-cont-main > div.main-lever > div.main-lever-right > div.main-lever-link > a:nth-child(4)")
        for item in data:
            target_url=item.get('href')
        #拿到目标链接用以解析
        target_url=str(target_url)
        return target_url
    
    #获取下载链接
    def getDownloadUrl(self,target_url):
        full_url=self.base_url+target_url
        response = requests.get(full_url, headers=self.headers).text
        soup=BeautifulSoup(response,'lxml')
        #下载链接是网页重定向，因此解析详情页的标题作为文件名
        title_tag=soup.select("body > div.mainWrap.sub_nav > div.subnav > div.subnav-title > div.subnav-title-name > a")
        for s in title_tag:
            title=s.string
        dl_tag=soup.select("th > div > a ")
        if title and dl_tag:
            for item in dl_tag:
                dl_url=item.get('href')
                return [title,dl_url]
        return [None,None]
    
    #通过下载链接下载表格文件
    def downloadExcel(self,url,path,filename):
        r=urlopen(url)
        filetype=os.path.basename(url).split('.')[2]
        file=path+filename+"."+str(filetype)
        with open(file,"wb") as code:
            code.write(r.read())
