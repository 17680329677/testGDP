# -*- coding: utf-8 -*-
#目标： 爬取我国1990---2017年的GDP信息，并绘制图像

import matplotlib .pyplot as plt	#导入绘图模块 并重命名为plt
import requests		#导入网页内容抓取包
from bs4 import BeautifulSoup as bs		#导入网页解析模块 并重命名为bs
from pylab import *		#该模块是matplotlib的一个子模块

rcParams['font.sans-serif'] = ['SimHei']	#使matplotlib支持中文

year = []	#横坐标列表
gdp = []	#纵坐标列表
url = "http://value500.com/M2GDP.html"		#抓取数据的网页
content = requests.get(url)		#抓取网页内容
content.encoding = 'utf-8'
content1 = content.text		#获取网页的文本部分
parse = bs(content1,'html.parser')		#进行html解析
data1 = parse.find_all("table")		#获取所有表元素
rows = data1[19].find_all("tr")		#取出包含所有数据的表（网页第20个表）
i = 0	#为了不读取表头元素 设置此变量
for row in rows:
	cols = row.find_all("td")	#把每一行数据存入cols变量
	if(len(cols) > 0 and i == 0):
		i+=1
	else:
		year.append(cols[0].text[:-2])		#取得年份数据（数据最后两个不是数字 需要除去）
		gdp.append(int(cols[2].text))	#取得GDP数据
		
plt.xlim(1989,2018)
plt.ylim(0,700000)
plt.plot(year,gdp,linewidth = 2.0)		#绘制图形 线宽为2
plt.title("1990--2017年的GDP信息")
plt.xlabel("年度")
plt.ylabel("GDP(亿元)")
plt.show()		#显示图像
#print(year)
#print(gdp)