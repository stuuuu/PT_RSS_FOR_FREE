'''
python 3.7
修改line12 rss_name = 
'''
import json,time
from rss_ny import rss
from free_ny import free
from download_ny import download

if __name__ == "__main__":
    while 1:       
        rss_name = 'nanyang'
        try:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'rss启动')
            rss_content = rss(rss_name).getinfo()
        except:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'rss出了一些小问题')
            rss_content = {}
        try:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'free启动')
            rss_content = free(rss_content,rss_name)
        except:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'free出了一些小问题')
            rss_content = {}
        try:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'download启动')
            downloaded = download(rss_content,rss_name)
        except:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'download出了一些小问题')
            downloaded = {}
        if downloaded:
            with open('download.json','r') as f:
                download_ = json.load(f)
            download_.update(downloaded)
            with open('download.json','w') as f:
                json.dump(download_,f)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'  '+'sleep')
        time.sleep(600)

