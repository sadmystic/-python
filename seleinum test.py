#coding:utf8
from selenium import webdriver
import time
import pymongo

class JdSpider(object):
    def __init__(self):
        self.url='http://www.jd.com/'
        self.options=webdriver.ChromeOptions() # 无头模式
        self.options.add_argument('--headless')
        self.browser=webdriver.Chrome(options=self.options) # 创建无界面参数的浏览器对象
        self.i=0  #计数，一共有多少件商品
        #输入地址+输入商品+点击按钮，切记这里元素节点是京东首页的输入栏、搜索按钮
    def get_html(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('python书籍')
        self.browser.find_element_by_xpath("//*[@class='form']/button").click()
        #把进度条件拉倒最底部+提取商品信息
    def get_data(self):
        # 执行js语句，拉动进度条件
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        # 给页面元素加载时预留时间
        time.sleep(2)
        #用 xpath 提取每页中所有商品，最终形成一个大列表
        li_list=self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            #构建空字典
            item={}
            item['name']=li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text.strip()
            item['price']=li.find_element_by_xpath('.//div[@class="p-price"]').text.strip()
            item['count']=li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text.strip()
            item['shop']=li.find_element_by_xpath('.//div[@class="p-shopnum"]').text.strip()
            print(item)
            self.i+=1
    def run(self):
        #搜索出想要抓取商品的页面
        self.get_html()
        #循环执行点击“下一页”操作
        while True:
            #获取每一页要抓取的数据
            self.get_data()
            #判断是否是最一页
            if self.browser.page_source.find('pn-next disabled')==-1:
                self.browser.find_element_by_class_name('pn-next').click()
                #预留元素加载时间
                time.sleep(1)
            else:
                print('数量',self.i)
                break
if __name__ == '__main__':
    spider=JdSpider()
    spider.run()