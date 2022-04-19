import requests
import time
import random
import re
import json
from ua_info import ua_list

class DoubanSpider(object):
    def __init__(self):
        self.url='https://movie.douban.com/j/chart/top_list?'
        self.i=0

    def get_headers(self):
        headers={'User-Agent':random.choice(ua_list)}
        return headers

    def get_page(self,params):
        html=requests.get(url=self.url,params=params,headers=self.get_headers()).text
        html=json.loads(html)
        self.parse_page(html)

    def parse_page(self,html):
        item={}
        for one in html:
            item['name']=one['title'].strip()
            item['score']=float(one['score'].strip())
            print(item)
            self.i+=1

    def total_number(self,type_number):

        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type_number)
        headers=self.get_headers()
        html=requests.get(url=url,headers=headers).json()
        print('123456')
        total=int(html['total'])

        return total


    def get_all_type_films(self):
        url='https://movie.douban.com/chart'
        headers=self.get_headers()
        html=requests.get(url=url,headers=headers).text
        re_bds=r'<a href=.*?type_name=(.*?)&type=(.*?)&.*?</a>'
        pattern=re.compile(re_bds,re.S)
        r_list=pattern.findall(html)
        type_dict={}
        menu=''
        for r in r_list:
            type_dict[r[0].strip()]=r[1].strip()
            menu+=r[0].strip()+'|'
        return type_dict,menu

    def main(self):
        type_dict,menu=self.get_all_type_films()
        menu=menu+'\n你想了解什么类型电影:'
        name=input(menu)
        type_number=type_dict[name]
        total=self.total_number(type_number)
        for start in range(0,(total+1),20):
            params = {
                'type' : type_number,
                'interval_id' : '100:90',
                'action' : '',
                'start' : str(start),
                'limit' : '20'
            }
            self.get_page(params)
            time.sleep(random.randint(1,3))
            print('电影总数:%d'%self.i)

if __name__=='__main__':
    spider=DoubanSpider()
    spider.main()
