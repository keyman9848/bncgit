#coding:utf-8

from bs4 import BeautifulSoup
import urllib.request
import pprint
import re

soup.prettify("gbk")

# BeautifulSoup 对象初始化
# url = 'http://reeoo.com'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request, timeout=20)

content = response.read()
soup = BeautifulSoup(content, 'html.parser') # 没有第二个参数，会选择合适解析器进行处理，不过会给出警告信息
# pp = pprint.PrettyPrinter(depth=6)
# pp.pprint(soup)

print(soup)




# Tag对象
tag0 = soup.title
tag1 = soup.title.text.replace("\n","").replace(" ","")
tag2 = soup.select('title')[0].text.replace("\n","").replace(" ","")
tag3 = soup.article.div.ul
tag4 = soup.article

# 子节点
# print(tag3.contents)
# for child in tag3.children:
#     print(child)


# 通过Tag对象的name属性
# print(tag4.parent.name)

# 通过 find_all() 方法
# print(soup.find_all('footer',id='footer')) # 加上标签的参数
# print(soup.find_all('div', class_='thumb')) # 缩略图用 class 为 thumb 标记
# print(soup.find_all(target=True)) #target 属性的标签
# print(soup.find_all(src=re.compile("reeoo.com"), class_='lazy')[0])
# print(soup.find_all(attrs={'data-original': re.compile("reeoo.qiniudn.com")})) # attrs 参数:字符串、正则表达式、列表、True/False。
# print(soup.find_all('div', class_='thumb', limit=3)) # limit 参数
# print(soup.find_all(string=re.compile("Reeoo"))) #string 参数

# CSS选择器

# print(soup.select('article ul li')) # 搜索 article 标签下的 ul 标签中的 li 标签

# 搜索 class 为 thumb 的标签
# print(soup.select('.thumb'))
# print(soup.select('[class~=thumb]'))
#

# 搜索 id 为 sponsor 的标签
# print(soup.select('#sponsor'))
# # print(soup.select('li[id]'))
# print(soup.select('li[id="sponsor"]'))

# 获取图片地址
# print(soup.find_all(attrs={'data-original': re.compile("reeoo.qiniudn.com")})[0])

# print(soup.find_all('img',class_='lazy'))


