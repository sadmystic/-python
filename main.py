from urllib import request,parse
import time
import random
from ua_info import ua_list

class TiebaSpider(object):
    def __init__(self):
        self.url='http://tieba.baidu.com/f?{}'

    def get_html(self,url):
        req = request.Request(url=url,headers={'User-'
                                               'Agent':random.choice(ua_list)})
        res = request.urlopen(req)
        html=res.read().decode("gbk","ignore")
        return html

    def parse_html(self):
        pass

    def save_html(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)

    def run(self):
        name=input('请输入贴吧名:')
        begin=int(input('输入起始页:'))
        stop=int(input('输入终止页'))
        for page in range(begin,stop+1):
            pn = (page - 1) * 50
            params={
                'kw':name,
                'pn':str(pn)
            }
            params=parse.urlencode(params)
            print(params)
            url=self.url.format(params)
            html=self.get_html(url)
            filename='{}-{}页.html'.format(name,page)
            self.save_html(filename,html)
            print("第%d页抓取成功"%page)
            time.sleep(random.randint(1,2))
            print(url)
if __name__ == '__main__':
    start=time.time()
    spider=TiebaSpider()
    spider.run()
    end=time.time()
    print('执行时间:%.2f'%(end-start))