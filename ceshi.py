# _*_ coding: utf-8 _*_
import urllib2
from bs4 import BeautifulSoup
import requests

def getHTML(url):
    # 给头文件伪装成浏览器访问
    req = requests.get(url)
    req.encoding = 'utf-8'

    print req.text
    return req.text

def creatSoup(url):
    req = requests.get(url)
    req.encoding = 'utf-8'
    html_text = req.text
    soup_0 = BeautifulSoup(html_text, 'html.parser')
    return soup_0


url = "https://weibo.com/"
req = requests.get(url)
req.encoding = 'utf-8'
html_text = req.text
soup = BeautifulSoup(html_text, 'html.parser')
a_soup = soup.findAll("a")

for content in a_soup:
    print content.get_text()

