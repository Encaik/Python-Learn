import threading
import queue
import re
import urllib.request
import time
import urllib.error


urlqueue = queue.Queue()
# 模拟成浏览器
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                         "Applewebkit/537.36 "
                         "(KHTML, like Gecko) "
                         "Chrome/38.0.2125.12"
                         "2 Safari/537.36 "
                         "SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
# 将opener安装为全局
urllib.request.install_opener(opener)
listurl = []


# 使用代理服务器的函数
def use_proxy(proxy_addr, url):
    try:
        proxy = urllib.request.ProxyHandler({'http':proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('utf-8')
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)
