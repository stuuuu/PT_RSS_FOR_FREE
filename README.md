# PT_RSS_FOR_FREE
![](https://img.shields.io/badge/python-3.7-red.svg)

可以从RSS里获取种子ID，判断是否FREE后下载；可以通过种子php页面收藏所有免费种子。<br>

## 使用方法

### 1 配置

| 参数 | 类型 |说明|
|:---|:---|:---|
|config.keys|str|配置名|
|link|str|rss链接 |
|sizerule|list|站点文件体积规则|
|sizefilter|list|[min,max]文件体积筛选|
|pagelink|str|种子详情页面前缀|
|cookies|str|网站cookies|
|torlink|str|种子下载地址前缀|
|path|str|种子下载地址 |
|torpage|str|种子目录页面 |
|booklink|str|种子收藏链接前缀 |

### 2 使用

RSS下载种子
```powershell
py main_ny.py config.keys
```

收藏种子
```powershell
py mark_free_ny.py config.keys
```
