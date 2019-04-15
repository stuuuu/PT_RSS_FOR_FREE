'''
python 3.7
rss类
从rss链接提取种子ID、大小、名字
链接失败5次后会返回空气

使用方法：

需提前配置config.json
{
    rss_name:{         #随便什么str，起个名字就好,记得加双引号
    "link":rss_link,    #rss链接，订阅时勾选标题和大小即可
    "sizerule":sizerule,   #体积大小的格式，一般都是["KB","MB","GB","TB"]，但也有例外比如U2就是KiB，所以加上了
    "sizefilter":[-1,99999] #体积大小范围，单位是GB，不在范围内的rss会被直接筛掉
    }
}

from rss_ny import rss  
res  = rss(config.rss_name).getinfo()    #config里可以保存多个rss配置，这里填要用的rss_name

res 格式
{ID：{
    'title':title_str,
    'size'size_float:
}}
'''

from xml.etree import ElementTree
from urllib import request
from io import BytesIO
import json
import time
class rss():
    def __init__(self,rss_name):
        with open('config.json','r') as f:
            config = json.load(f)
            self.rss_link = config[rss_name]["link"]
            self.sizerule = config[rss_name]["sizerule"]
            self.sizefilter = config[rss_name]["sizefilter"]
    def getinfo(self):
        maxtry = 6
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        for tyies in range(1,maxtry):
            try:
                rss_html = request.Request(url = self.rss_link,headers = headers)
                f = BytesIO(request.urlopen(rss_html).read())
                break
            except:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'rss网络连接失败，重试第'+str(tyies)+'次中')
                if tyies == 5:
                    print('GG')
                    return {}
                continue
        tree = ElementTree.parse(f)
        f.close() 
        row = 0
        res = {}
        for emement in tree.getiterator():
            if emement.tag == 'item':
                row+=1
            if row>0:
                if emement.tag == 'title':
                    tor_title = emement.text[::-1]
                    ind = tor_title.index('[')
                    title = tor_title[ind+1:][::-1]
                    size = tor_title[1:ind][::-1].split()
                    size = float(size[0])*10**(self.sizerule.index(size[1])-2)
                    tor_title = {'title':title,
                                'size':size}
                if emement.tag == 'link':
                    if self.sizefilter[0]<=tor_title['size']<=self.sizefilter[1]:
                        tor_id   = emement.text.split('=')[1]
                        res[tor_id] = tor_title
        return res
if __name__ == "__main__":
    print(rss('nanyang').getinfo())
