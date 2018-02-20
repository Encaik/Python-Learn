#CrawUnivRankingB.py
import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "解析页面出现错误"

def fillUnivList(ulist,html):
	try:
		soup = BeautifulSoup(html,"html.parser")
		for tr in soup.find('tbody').children:
			if isinstance(tr,bs4.element.Tag):
				tds = tr('td')
				ulist.append([tds[2].string,tds[1].string,tds[3].string])
	except:
		return "获取信息出现错误"

def printUnivList(ulist,num):
	try:
		tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
		print("排名",end="\t")
		print(tplt.format("省份","学校名称","总分",chr(12288)))
		for i in range(num):
			u = ulist[i]
			print(i+1,end="\t")
			print(tplt.format(u[0],u[1],u[2],chr(12288)))
	except:
		return "打印数据出现错误"

def main():
	uinfo = []
	url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
	html = getHTMLText(url)
	fillUnivList(uinfo, html)
	printUnivList(uinfo, 40)

main()
