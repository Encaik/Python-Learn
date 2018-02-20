# *-* coding:utf-8 *-*

from __future__ import print_function
import requests
import bs4
from bs4 import BeautifulSoup
import re


global name
global book


def getHtml(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "解析页面出现错误"


def getTitle(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        tag1 = soup.h1
        tag2 = soup.find('div', {'id': 'list'})
        global name
        name = tag1.text
        print('开始下载'+name)
        htm = str(tag2.get_text)
        global book
        href = re.findall(r'%s\d{8}\.html' % book, htm)
        for end in href:
            textUrl = 'http://www.xbiqiwu.com'+end
            html = getHtml(textUrl)
            getText(html)
    except:
        return "获取信息出现错误"


def getText(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        tag1 = soup.find('div', {'id': 'content'})
        tag2 = soup.h1
        text1 = BeautifulSoup(str(tag1), 'lxml')
        txtstr1 = text1.div.text.replace('\xa0', '')
        txtstr2 = tag2.text
        print("正在下载"+txtstr2)
        txtFile('\n'+txtstr2+'\n\n'+txtstr1+'\n ')
    except:
        return "获取正文出现错误"


def txtFile(txtstr):
    global name
    file = open(name+'.txt', 'a')
    file.write(txtstr)
    file.close()


def main():
    global book
    url = 'http://www.xbiqiwu.com'
    num = input("请输入书号")
    key = num[:-3]
    value = num[-3:]
    book = '/b/'+key+'/'+key+value+'/'
    html = getHtml(url+book)
    getTitle(html)

main()
print("下载完成")
