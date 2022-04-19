# -*- coding:utf8 -*-
import random

import requests
from threading import Thread
from queue import Queue
import time
from ua_info import ua_list
from lxml.html import etree
import csv
from threading import Lock
import json
class XiaomiSpider(object):
  def __init__(self):
    self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'
    # 存放所有URL地址的队列
    self.q = Queue()
    self.i = 0
    # 存放所有类型id的空列表
    self.id_list = []
    # 打开文件
    self.f = open('XiaomiShangcheng.csv','a',encoding='utf-8')
    self.writer = csv.writer(self.f)
    # 创建锁
    self.lock = Lock()
  def get_cateid(self):
    # 请求
    url = 'http://app.mi.com/'
    headers = { 'User-Agent': random.choice(ua_list)}
    html = requests.get(url=url,headers=headers).text
    # 解析
    parse_html = etree.HTML(html)
    xpath_bds = '//ul[@class="category-list"]/li'
    li_list = parse_html.xpath(xpath_bds)
    for li in li_list:
      typ_name = li.xpath('./a/text()')[0]
      typ_id = li.xpath('./a/@href')[0].split('/')[-1]
      # 计算每个类型的页数
      pages = self.get_pages(typ_id)
      #往列表中添加二元组
      self.id_list.append( (typ_id,pages) )
    # 入队列
    self.url_in()
  # 获取count的值并计算页数
  def get_pages(self,typ_id):
    # 获取count的值，即app总数
    url = self.url.format(0,typ_id)
    html = requests.get(
      url=url,
      headers={'User-Agent':random.choice(ua_list)}
    ).json()
    count = html['count']
    pages = int(count) // 30 + 1
    return pages
  # url入队函数，拼接url，并将url加入队列
  def url_in(self):
    for id in self.id_list:
      # id格式：('4',pages)
      for page in range(1,id[1]+1):
        url = self.url.format(page,id[0])
        # 把URL地址入队列
        self.q.put(url)
  # 线程事件函数: get() -请求-解析-处理数据,三步骤
  def get_data(self):
    while True:
       # 判断队列不为空则执行，否则终止
      if not self.q.empty():
        url = self.q.get()
        headers = {'User-Agent':random.choice(ua_list)}
        html = requests.get(url=url,headers=headers)
        res_html = html.content.decode(encoding='utf-8')
        html=json.loads(res_html)
        self.parse_html(html)
      else:
        break
  # 解析函数
  def parse_html(self,html):
    # 写入到csv文件
    app_list = []
    for app in html['data']:
      # app名称 + 分类 + 详情链接
      name = app['displayName']
      link = 'http://app.mi.com/details?id=' + app['packageName']
      typ_name = app['level1CategoryName']
      # 把每一条数据放到app_list中,并通过writerows()实现多行写入
      app_list.append([name,typ_name,link])
      print(name,typ_name)
      self.i += 1
    # 向CSV文件中写入数据
    self.lock.acquire()
    self.writer.writerows(app_list)
    self.lock.release()
  # 入口函数
  def main(self):
    # URL入队列
    self.get_cateid()
    t_list = []
    # 创建多线程
    for i in range(1):
      t = Thread(target=self.get_data)
      t_list.append(t)
      # 启动线程
      t.start()
    for t in t_list:
        # 回收线程
        t.join()
    self.f.close()
    print('数量:',self.i)
if __name__ == '__main__':
  start = time.time()
  spider = XiaomiSpider()
  spider.main()
  end = time.time()
  print('执行时间:%.1f' % (end-start))