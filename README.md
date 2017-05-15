# Spiderman

## 运行环境介绍 ##

系统：KaLi 2016

软件：Python3.5 , 基于 PyQuery 和 Requests 2个模块

## 目的 ##
主要是为了学习这2个模块才写了这个蜘蛛脚本.
> 好吧其实我是为了看妹子才写的

## 脚本亮点 ##

1. 最亮眼的就是这个自动代理功能，煎蛋的反爬机制我没能力越过，只能采取自动更换代理的方式爬取。
2. 暂时没有想到。

## 功能介绍 ##

主体功能都在DownHtml.py这个文件里

> GetProxy函数

抓取[http://www.xicidaili.com/nn](http://www.xicidaili.com/nn "西刺代理")

记录到一个list里

> CheckProxy函数

检查代理的可用性，设置超时时间为10秒。

> GetHtml函数

主要功能保存网页,在meizi.py里面我是先保存HTML再去解析里面的妹子图片的URL，然后再下载的一个过程。

> GetPageNum

获取妹子图片的页数，我发现妹子图从1500页以前的都不显示了，所以只能抓取1500到目前最新的页码的妹子图片。

> GetImageUrl函数

获取妹子图片的URL从已经下载到本地的HTML中

> GetImage函数

下载妹子图到本地

## 美图鉴赏 ##

![](https://github.com/hgz6536/hgz6536.github.io/blob/master/images/4bf31e43jw1ey9lcsyn4cj20dw099dh8.jpg)

![](https://github.com/hgz6536/hgz6536.github.io/blob/master/images/66b3de17gw1f03odjhxynj20nm0zkgnp.jpg)

![](https://github.com/hgz6536/hgz6536.github.io/blob/master/images/ec49d501gw1ewvrivx6wxj20m80x2djr.jpg)


