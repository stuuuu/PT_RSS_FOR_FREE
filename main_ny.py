'''
python 3.7
'''
import json,time
from rss_ny import rss
from free_ny import free
from download_ny import download
import sys

if __name__ == "__main__":
    rss_name = sys.argv[1]
    while 1:

        #读取已经下载的种子id   type(tor_dl_id) = list
        with open('download.dat','r') as f:
                tor_dl_id = json.load(f)

        #try:    获取rss内容
        #except: 报错 
        try:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'rss启动')
            rss_content = rss(rss_name).getinfo()
        except:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'rss出了一些小问题')
            rss_content = {}

        #rss中去掉已经下载的种子
        if tor_dl_id and rss_content:
            for tor_id in list(rss_content):
                if tor_id in tor_dl_id: del rss_content[tor_id]

        #try:    查询优惠信息
        #except: 报错
        try:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'free启动')
            rss_content = free(rss_content,rss_name)
        except:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'free出了一些小问题')
            rss_content = {}
        
        #try:    下载种子      
        #except:  报错  
        try:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'download启动')
            downloaded = download(rss_content,rss_name)
        except:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'download出了一些小问题')
            downloaded = []
        if downloaded:
            tor_dl_id+=downloaded
            with open('download.dat','w') as f:
                json.dump(tor_dl_id,f)
        
        #循环间隔 单位秒
        sleep = 30
        for  x in range(sleep,-1,-1):
            djs = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'sleep倒计时'+str(x)+'秒'
            print(djs,end = "")
            print("\b" * (len(djs)*2),end = "",flush=True)
            time.sleep(1)

