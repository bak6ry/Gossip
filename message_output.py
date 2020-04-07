# _*_ coding: utf-8 _*_
import warnings
#import spider_main.py
from typing import List
import pymysql
import csv
# warnings.filterwarnings("ignore")


def create(dbuser,dbpassword):
    conn = pymysql.connect(host='localhost', user='%s'%(dbuser), password='%s'%(dbpassword), db='mysql', charset='utf8mb4')
    cur = conn.cursor()
    cur.execute('SET CHARACTER SET utf8;')
    cur.execute('CREATE DATABASE IF NOT EXISTS `data` DEFAULT CHARSET utf8 COLLATE utf8_general_ci;')
    cur.execute('use data')
    cur.execute("CREATE TABLE IF NOT EXISTS `contents`(urls varchar(200),keywords varchar(100),content varchar(1000), id INT AUTO_INCREMENT,PRIMARY KEY(id))ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")
    print"data数据库已经创建了\ncontents数据表已经创建"
    conn.commit()
def insert(dbuser, dbpassword, url, key, data):

    str = ''.join(data)
    conn = pymysql.connect(host='localhost', user='%s'%(dbuser), password='%s'%(dbpassword), db='data', charset='utf8mb4')
    cur = conn.cursor()
    cur.execute('use data')
    # sql = ("INSERT INTO contents(urls,content)" "VALUES(%s,%s,%s)")
    # sqldata = (urls, key_message)
    # cur.execute(sql, sqldata)
    cur.execute("INSERT INTO contents(urls,keywords,content) VALUES('%s','%s','%s');"%(url, key, str))
    conn.commit()
    cur.close()
    conn.close()


dbuser = 'root'
dbpassword = 'root1'
url = 'www.baidu.com'
keywords = ['我', '的']
key_message = ['大王', '阿达', '完全']
create(dbuser, dbpassword)
key = '+'.join(keywords)
for data in key_message:
    insert(dbuser, dbpassword, url, key, data)






