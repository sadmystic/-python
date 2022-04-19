#coding:utf8
import requests
import random
from lxml.html import etree
import time
from ua_info import ua_list

class LinajiaSpider(object):
    def __init__(self):
        self.url ='https://bj.lianjia.com/ershoufang/pg{}'
        self.blog=1

    def get_header(self):
        headers={'User-Agent':random.choice(ua_list)}
        return headers

    def get_html(self,url):
        if self.blog<=3:
            try:
                res=requests.get(url=url,headers=self.get_header(),timeout=3)
                html=res.text
                return html
            except Exception as e:
                print(e)
                self.blog+=1
                self.get_html(url)

    def parse_html(self,url):
        html=self.get_html(url)
        if html:
            p=etree.HTML(html)
            h_list=p.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
            for h in h_list:
                item={}
                name_list=h.xpath('.//a[@data-el="region"]/text()')
                item['name']=name_list[0] if name_list else None
                info_list=h.xpath('.//div[@class="houseInfo"]/text()')
                if info_list:
                    L=info_list[0].split('|')
                    if len(L)>=5:
                        item['model'] = L[0].strip()
                        item['area'] = L[1].strip()
                        item['direction'] = L[2].strip()
                        item['perfect'] = L[3].strip()
                        item['floor'] = L[4].strip()
                address_list = h.xpath('.//div[@class="positionInfo"]/a/text()')
                item['address'] = address_list[0].strip() if address_list else None
                total_list = h.xpath('.//div[@class="totalPrice"]/span/text()')
                item['total_list'] = total_list[0].strip() if total_list else None
                price_list = h.xpath('.//div[@class="unitPrice"]/span/text()')
                item['price_list'] = price_list[0].strip() if price_list else None
                print(item)

    def run(self):
        try:
            for i in range(1,101):
                url=self.url.format(i)
                self.parse_html(url)
                time.sleep(random.randint(1,3))
                #每次抓取一页要初始化一次self.blog
                self.blog=1
        except Exception as e:
            print('发生错误',e)

if __name__ == '__main__':
    spider=LinajiaSpider()
    spider.run()