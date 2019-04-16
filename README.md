# PT_RSS_FOR_FREE

可以从RSS里获取种子ID，判断是否FREE后下载<br>
PYTHON 3.7 <br>

###使用方法

####1 配置config

{<br>
　rss_name:{　　　　　　　　#随便什么str，起个名字就好,记得加双引号<br>
　　"link":str,　　　　　　&nbsp;#rss链接，订阅时勾选标题和大小即可<br>
　　"sizerule":list,　　　　#体积大小的格式，一般都是["KB","MB","GB","TB"]，但也有例外比如U2就是KiB，所以加上了 <br>
　　"sizefilter":list,　　　#体积大小范围，单位是GB，不在范围内的rss会被直接筛掉<br>
　　"pagelink":str,　　　　&nbsp;#种子的详情页面链接前缀，一般都是"https://xxx.com/details.php?id="， 其实可以从自动从rss链接里提取但是懒得改了ε=(´ο｀*))) <br>
　　"cookies":str,　　　　　#网站的cookie  chorme 为例  F12→Network→F5→点最上面链接→Request Header里的cookie 字串全部 <br>
　　"torlink":str,　　　　　#种子的下载链接，一般都是"https://xxx.com/download.php?id= &passkey=xxx"，种子ID处留个空格，这一条主要是为了下V6种子 <br>
　　"path": str　　　　　　&nbsp;#种子保存目录 不填就是当前目录  记得用反斜线 例如"e:/" <br>
　}<br>
}<br>

####2 运行

py main_ny.py rss_name




