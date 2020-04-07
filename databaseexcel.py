
from pyExcelerator import *#导入用到的包
import pymysql
import time
import os

def intoexcel(dbuser, dbpassword):
    w = Workbook()  # 创建一个Excel文件
    ws = w.add_sheet('datas')  # 创建一个工作表
    #采用坐标的形式定义表的第一行
    ws.write(0, 0, 'id')
    ws.write(0, 1, 'url')
    ws.write(0, 2, 'keyword')
    ws.write(0, 3, 'content:')

#连接数据库
    conn = pymysql.connect(host='127.0.0.1', user='%s'%(dbuser), passwd='%s'%(dbpassword), db='mysql', charset='utf8mb4')
    cursor = conn.cursor()#获取游标

#try:
    cursor.execute("use data;")
    cursor.execute("select id from contents;")#执行sql语句
    conn.commit()
    outputid = cursor.fetchall()#获取执行结果

    print "导入id成功"#测试
    i=1#坐标定义
    j=0
    for outid in outputid:
        ws.write(i,j,outid[0])#write函数的参数分别是行、列、要写入的数据
        i=i+1#实现循环


    cursor.execute("use data;")
    cursor.execute("select urls from contents;")#执行sql语句
    outputid = cursor.fetchall()#获取执行结果
    conn.commit()
    print "导入urls成功"#测试
    i=1#坐标定义
    j=1
    for outid in outputid:
        ws.write(i,j,outid[0])#write函数的参数分别是行、列、要写入的数据
        i=i+1#实现循环


    cursor.execute("use data;")
    cursor.execute("select keywords from contents;")#执行sql语句
    outputid = cursor.fetchall()#获取执行结果
    conn.commit()
    print "导入key成功"#测试
    i=1#坐标定义
    j=2
    for outid in outputid:
        ws.write(i, j, outid[0])#write函数的参数分别是行、列、要写入的数据
        i=i+1#实现循环

    cursor.execute("use data;")
    cursor.execute("select content from contents;")#执行sql语句
    outputid = cursor.fetchall()#获取执行结果
    conn.commit()
    print "导入content成功"#测试
    i=1#坐标定义
    j=3
    for outid in outputid:
        ws.write(i,j,outid[0])#write函数的参数分别是行、列、要写入的数据
        i=i+1#实现循环

    #except:
     #   print "error"
    conn.close()
    b = os.getcwd()
    c = '%s\output'%(b)
    if not os.path.exists(c):
        os.mkdir('%s'%(c))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    fname = "%s"%(c) + now + "sreport.xls"

    w.save('%s'%(fname))#将文件保存到指定目录下
# def path():
#

intoexcel('root','root1')
