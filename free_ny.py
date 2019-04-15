
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
    nofree = []
    for tor_id in rss_content:
        with open('download.json','r') as f:
            download_ = json.load(f)
            havedown = download_.keys()
        if tor_id in havedown:
            nofree.append(tor_id)
            break
        id_link= pagelink+tor_id
        headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                  'cookie':cookies}
        maxtyies = 6
        for tyies in range(1,maxtyies):
            try:
                id_request=request.Request(url=id_link,headers=headers)
                html=request.urlopen(id_request).read().decode('utf-8','ignore')
                title=re.findall('<h1 align="center" id="top">(.+?)</h1>',html)[0]
                youhui = re.findall('<b>(.+?)</b>',title)[0]
                if 'free' not in youhui:
                    nofree.append(tor_id)
                break
            except:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+tor_id+'查询free失败，重试第'+str(tyies)+'次中')
                if tyies == 5: 
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'GG,下一个')
                    nofree.append(tor_id)
                continue
    for tor_id in nofree:
        rss_content.pop(tor_id)
    return rss_content

if __name__ == "__main__":
    rss_content = {'69327': {'title': 'Down.a.Dark.Hall.2018.BluRay.1080p.x264.DTS-CMCT', 'size': 8.1}, 
                   '52776': {'title': '[足球][2018-04-16][天下足球][CCTV5-HD/国语][MKV][720P]', 'size': 3.34}, 
                   '999999999': {'title': 'Bel.Ami.2012.BluRay.720p.x264.AC3-CMCT', 'size': 3.01}, 
                   '69325': {'title': 'NBA季后赛.20190415.东部首轮.G1.活塞VS雄鹿.TNT.英语.720P.60FPS.MKV-720pier', 'size': 3.18}, 
                   '3920': {'title': '[2009-03-07][演唱会][纵贯线][纵贯线2009台北<出发>SuperBand.Live.In.Taipei.The.Start.2009.BluRay.ipad.720p.x264.AAC-NYPAD][MP4][720P]', 'size': 2.74},
                   '69324': {'title': 'The.Handmaids.Tale.S02.Disc4.Blu-ray.1080p.AVC.DTS-HD.MA.5.1-hyb9373@CMCT', 'size': 43.34}, 
                   '69322': {'title': 'Baptiste.S01.1080p.AMZN.WEB-DL.DDP5.1.H.264-NTb', 'size': 20.67}, 
                   '69321': {'title': 'Distinction.2018.720p.BluRay.x264-WiKi', 'size': 4.41}, 
                   '69319': {'title': 'Perfect.World.2018.720p.BluRay.x264-WiKi', 'size': 4.06}, 
                   '69318': {'title': 'Napping.Kid.2018.720p.BluRay.x264-WiKi', 'size': 4.9}
                   }
    print(free(rss_content,'nanyang'))
    
