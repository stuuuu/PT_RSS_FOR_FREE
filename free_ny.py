
'''
python 3.7
根据种子ID和页面链接判断优惠，目前只搞了判断free

输入输出rss_content格式：   #就是rss(config.rss_name).getinfo()输出的东西
{
    ID1：{},
    ID2：{},
    ID3：{},
    ...
}
输出结果会把不符合优惠条件的key删掉

使用方法:

需提前配置config.json
{
    rss_name:{            #随便什么str，起个名字就好，记得加双引号
    "cookies":cookies     # 网站的cookie  chorme 为例  F12→Network→F5→点最上面链接→Request Header里的cookie 字串全部
    "pagelink":pagelink   #种子的详情页面链接前缀，一般都是"https://xxx.com/details.php?id="，其实可以从自动从rss链接里提取但是懒得改了ε=(´ο｀*)))
    }
}

import free from free_ny
rss_content = free(rss_content,rss_name)

'''
import re
import json
from urllib import request
import time

def free(rss_content,rss_name):
    if not rss_content:return {}
    with open('config.json','r') as f:
        config = json.load(f)
        pagelink = config[rss_name]["pagelink"]
        cookies = config[rss_name]["cookies"]
    for tor_id in list(rss_content):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+tor_id+'查询优惠')
        id_link= pagelink+tor_id
        headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                  'cookie':cookies}
        maxtyies = 6
        for tyies in range(1,maxtyies):
            try:
                id_request=request.Request(url=id_link,headers=headers)
                html=request.urlopen(id_request).read().decode('utf-8','ignore')
                title=re.findall('<h1 align="center" id="top">(.+?)</h1>',html)[0]
                try:
                    youhui = re.findall('<b>(.+?)</b>',title)[0]
                except:
                    youhui = ''
                if 'free' not in youhui:
                    del rss_content[tor_id]
                break
            except:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+tor_id+'查询free失败，重试第'+str(tyies)+'次中')
                if tyies == 5:
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'GG,下一个')
                    del rss_content[tor_id]
                continue
    return rss_content

if __name__ == "__main__":
    rss_content = {'52776': {'title': 'Down.a.Dark.Hall.2018.BluRay.1080p.x264.DTS-CMCT', 'size': 8.1},
                   }
    print(free(rss_content,'nanyang'))
    
