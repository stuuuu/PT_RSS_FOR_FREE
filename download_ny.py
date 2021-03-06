import json
from urllib import request
import time


def download(rss_content,rss_name):
    if not rss_content:return {}
    downloaded = []
    with open('config.json','r') as f:
        config = json.load(f)
        torlink = config[rss_name]["torlink"].split()
        path = config[rss_name]["path"]
    opener = request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')]
    request.install_opener(opener)
    for tor_id in rss_content:
        bt_link= torlink[0] +tor_id+torlink[1]
        maxtyies = 6
        for tyies in range(1,maxtyies):
            try:
                request.urlretrieve(bt_link,path+rss_name+tor_id+'.torrent')
                downloaded.append(tor_id)
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+"ID:{}下载成功 TITLE:{} SIZE:{}GB".format(tor_id,rss_content[tor_id]['title'],rss_content[tor_id]['size']))
                break     
            except:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+tor_id+'下载失败，重试第'+str(tyies)+'次中')
                if tyies == 5:
                    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'GG,下一个')          
    return downloaded

if __name__ == "__main__":
    rss_content = {'69327': {'title': 'Down.a.Dark.Hall.2018.BluRay.1080p.x264.DTS-CMCT', 'size': 8.1}, 
                   '52776': {'title': '[足球][2018-04-16][天下足球][CCTV5-HD/国语][MKV][720P]', 'size': 3.34}, 
                   '69325': {'title': 'NBA季后赛.20190415.东部首轮.G1.活塞VS雄鹿.TNT.英语.720P.60FPS.MKV-720pier', 'size': 3.18}, 
                   '3920': {'title': '[2009-03-07][演唱会][纵贯线][纵贯线2009台北<出发>SuperBand.Live.In.Taipei.The.Start.2009.BluRay.ipad.720p.x264.AAC-NYPAD][MP4][720P]', 'size': 2.74}, 
                   '69324': {'title': 'The.Handmaids.Tale.S02.Disc4.Blu-ray.1080p.AVC.DTS-HD.MA.5.1-hyb9373@CMCT', 'size': 43.34}, 
                   '69322': {'title': 'Baptiste.S01.1080p.AMZN.WEB-DL.DDP5.1.H.264-NTb', 'size': 20.67}, 
                   '69321': {'title': 'Distinction.2018.720p.BluRay.x264-WiKi', 'size': 4.41}, 
                   '69319': {'title': 'Perfect.World.2018.720p.BluRay.x264-WiKi', 'size': 4.06}, 
                   '69318': {'title': 'Napping.Kid.2018.720p.BluRay.x264-WiKi','size': 4.9}
                   }
    print(download(rss_content,'nanyang'))
