import requests
from lxml.html import etree
from ua_info import ua_list
import random

class MaoyanSpider2(object):
    def __init__(self):
        self.url='https://movie.douban.com/top250?start=0'
        self.headers = {'User-Agent': random.choice(ua_list)}

    def save_html(self):
        html=requests.get(url=self.url,headers=self.headers).text
        parse_html=etree.HTML(html)

        dd_list=parse_html.xpath('//ol[@class="grid_view"]/li')
        print(dd_list)
        item={}
        for dd in dd_list:
            item['name']=dd.xpath('.//span[@class="title"]/text()')[0].strip()
            item['star']=dd.xpath('.//div[@class="bd"]/p/text()')[0].strip()
            print(item)

    def run(self):
        self.save_html()

if __name__ == '__main__':
    spider=MaoyanSpider2()
    spider.run()