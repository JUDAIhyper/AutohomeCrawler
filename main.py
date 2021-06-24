from AutohomeList import GetList
from GetParameter import Car_Config
import time


if __name__=="__main__":
    gl = GetList()
    gl.get_attribute()

    time.sleep(3)

    file = open("./CarHref.txt")
    cf = Car_Config()
    lines = file.readlines()
    #根据文本中的连接获取下载地址
    count = 0
    for line in lines:
        url = line
        target_url = cf.getExcel(url)
        #解析详情页并下载官方表格
        dl_attr = cf.getDownloadUrl(target_url)
        file_name = str(dl_attr[0])
        dl_url = dl_attr[1]
        if dl_url:
            #在根目录下建立一个download文件夹再运行
            cf.downloadExcel(dl_url, "./download/", file_name)
            count += 1
            print("第%d个文件下载完成", count)
    print("finish!")
    file.close()
