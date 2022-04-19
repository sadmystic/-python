from urllib import request
import re
import time
import random
import csv
import pymysql
from ua_info import ua_list

class DoubanSpider(object):
    def __init__(self):
        # 初始化属性对象
        self.url='https://movie.douban.com/top250?start={}'
        # 数据库连接对象
        self.db = pymysql.connect(
            host='localhost', user='root', password='123456', database='maoyandb', charset='utf8')
        # 创建游标对象
        self.cursor = self.db.cursor()

    def get_html(self,url):
        headers={'User-Agent':random.choice(ua_list)}
        req=request.Request(url=url,headers=headers)
        res=request.urlopen(req)
        html = res.read().decode()
        # 直接解析
        self.parse_html(html)

    def parse_html(self,html):
        re_bds='<div class="info">.*?"title">(.*?)</span>.*?导演:(.*?)&nbsp.*?<br>(.*?)&nbsp;'
        pattern = re.compile(re_bds,re.S)
        r_list=pattern.findall(html)
        self.save_html(r_list)

    def save_html(self,r_list):
        L = []
        sql ='insert into filmtab values(%s,%s,%s)'
        # with open('douban.csv','a',newline='',encoding='utf-8') as f:
        #    writer = csv.writer(f)
        for r in r_list:
                t = (
                        r[0].strip(),
                        r[1].strip(),
                        r[2].strip()
                )
                L.append(t)
        #        writer.writerow(L)
                print(L)
        try:
            self.cursor.executemany(sql,L)
            self.db.commit()
        except:
            self.db.rollback()

    def run(self):
        for start in range(0,250,25):
            url = self.url.format(start)
            self.get_html(url)
            time.sleep(random.uniform(1,3))

        # 断开游标与数据库连接
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
        start=time.time()
        spider = DoubanSpider()
        spider.run()
        end=time.time()
        print("执行时间:%.2f"%(end-start))