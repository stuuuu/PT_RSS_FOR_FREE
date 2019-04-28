import json
from urllib import request
import re
import time
import sys

def get_info(PageLink,cookies,sizerule):
    headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                  'cookie':cookies}
    maxtry = 4
    for tyies in range(1,maxtry):
        try:
            _request=request.Request(url=PageLink,headers=headers)
            html=request.urlopen(_request,timeout=30).read().decode('utf-8','ignore')
        except:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'网络连接失败，重试第'+str(tyies)+'次中')
            if tyies == 3:
                print('GG')
                return {}
            continue
    torrentinfo=re.finditer('<table class="torrentname" width="100%">(.+?)<td class="rowfollow nowrap" valign="middle"',html,re.S)
    maxfind = 2
    nowfind = 0
    res = {}
    for p in torrentinfo:
        info_all = p.group()
        tor_id = re.search('details.php(.+?)&amp',info_all).group()[15:-4]
        if not 1:
            break
        tor_title = re.search('a title="(.+?)"',info_all).group()[9:-1]
        tor_youhui = re.search('class="pro_(.+?)"',info_all)
        tor_youhui=tor_youhui.group()[11:-1] if tor_youhui else 'None'
        tor_star = re.search('javascript: bookmark(.+?)bookmark',info_all).group()
        tor_star  = True if 'delbookmark' not in tor_star else False
        tor_size =  re.search('<td class="rowfollow nowrap">(.+?)<td class="rowfollow">(.+?)</td>(.+?)</td>',info_all).group()
        tor_seed =  0 if 'red' in tor_size else int(re.findall('seeders">(.+?)</a>',tor_size)[0])
        tor_time =  ' '.join(re.findall('<td class="rowfollow nowrap">(.+?)<br />(.+?)</td>',tor_size)[0])
        tor_size =  re.findall('class="rowfollow">(.+?)<br />(.+?)</td>',tor_size)[0]
        tor_size = float(tor_size[0])*10**(sizerule.index(tor_size[1])-2)
        res[tor_id] = [tor_star,tor_youhui,tor_size,tor_title,tor_time,tor_seed]
        nowfind+=1
        if nowfind == maxfind :break
    return res




if __name__ == "__main__":
    rss_name = sys.argv[1]
    with open('config.json','r') as f:
        config = json.load(f)
        cookies = config[rss_name]["cookies"]
        sizerule = config[rss_name]["sizerule"]
        sizefilter = config[rss_name]["sizefilter"]
        PageLink = config[rss_name]["torpage"]
        getstar = config[rss_name]["booklink"]
    tor_info = get_info(PageLink,cookies,sizerule)
    headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                  'cookie':cookies}
    for tor_id in list(tor_info):
        if  not tor_info[tor_id][0] and  sizefilter[0]<tor_info[tor_id][2]<sizefilter[1] and tor_info[tor_id][1] =='free' and tor_info[tor_id][5]:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+tor_info[tor_id][3])
            maxtry = 4
            for tyies in range(1,maxtry):
                try:
                    get = request.Request(url=getstar+tor_id,headers=headers)            
                    page = request.urlopen(get).read()
                except:
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'网络连接失败，重试第'+str(tyies)+'次中')
                    if tyies == 3:
                        print('GG')
                    continue    

