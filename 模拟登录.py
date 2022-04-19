import requests
from lxml.html import etree

class login(object):
    def __init__(self):
        self.url='https://www.zhihu.com/people/mystic-94'
        self.headers={
            'Cookie':'_zap=cf10d60b-091d-475e-948e-03e7fcdbb7db; d_c0="AAAQPGhl_hOPTv04h21SDiQg5F8sS0g2auc=|1636269749"; _9755xjdesxxd_=32; YD00517437729195:WM_TID=6DAVrkG7IZZFERFQEVY+se7SND3urLBa; _xsrf=djoHHgqnTKgsVugqizgBEcbhWbhSDqqN; __snaker__id=80bPUVqZDhHMUcDC; q_c1=67633cc848b64adc9793be568a904ff4|1642351137000|1642351137000; __utma=51854390.623714349.1642351136.1642351136.1642351136.1; __utmz=51854390.1642351136.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100--|2=registration_date=20170718=1^3=entry_date=20170718=1; gdxidpyhxdE=AIHZVmMKKHhWbjzfPbbBsxPHlxQ9/t5yBHpnOcRbaDkVbMd4fgMm3Q6ft3\ev\ZxxE+Azdd/0NhMImiN3WjpDatf0hT9XHCIX24a4igxC7ra+xrdWN3vkiLPIEsWHPB0oTTIDQzAOMVenNmm7c\/+bYmUS/K0BRnK00NDj/W\+gyh70B:1647240857281; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eea4f73986b9f7ace86eed8e8eb6c54a868e8abaaa3dfb9ee1b8cb798896fad7b22af0fea7c3b92aa397fa90d24aa389fed1ca49bc88a0d8ef62f186a895f534a6bbb9d6f64b8aa8ba94cc608defb8ccd65ff1ab8185cf3bf8ec88a2ec45b5ef8ea7b55de994baa8d74ebce8878fb44aaa91c0d6d4629bbd85d5e73fbb9185b1c97babf19bb3b346b4b9aa8adc65839f8ed9cc7c8cba8fa9e15d978981a2ea69b695abb1f07b85a6ab8ed037e2a3; YD00517437729195:WM_NI=aI6oSBaW20KCxXP7lj3Zhtv8few5wAJxvsITO1x+WU3uOdL144HAiOw1BF6W+LvGTFx8In1BjOp5QjYcK4d5yOKPJqi/UR0NpgfiYoAAB8IpHfAHbWUWOAkcvKePmqGzemM=; captcha_session_v2="2|1:0|10:1647239984|18:captcha_session_v2|88:NitWbkUwbDBkTGRnWnlRazJWYU1iTUViMGswV1dOaFZ5ZkVQTFBlOENSazd5MVpKbGVvRzlPLytseDhwbCtoZA==|2b7e71c53b8e41137dbadb30886d4b49f9d157d44a06fd5c5934508ef34044da"; captcha_ticket_v2="2|1:0|10:1647239996|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfMUZEUHdsTnFmX0dXdlBDVVB1UHU0VTRBd2Z5R0tYY3JrNXFQNzFsSVhhTVI4Z0Q2OEZ5THdId0x1cHJaQnlobnRxai5hc2FtQ2NEeXcuMkxlLlhtZldTRUNra1dGMDB6UHF5TDVMN1BsakloZmhfWnpoQmhpNG83Qks3SFoxQ1VDbm9tYmtZQUdGZGNvTWdfaE5jS0Zqek9jam5pNEJVQ3h5cUtZN011SFFvNGdFZTdPTlVicHZsV2d0OUExOERRSmpHNjRsWGNsOTU1dVFycjV4aVJQTTdEZS1jLXBDWXR4c0FtdVhONDlzUlhRLUxrTVp4cEd3dVYyc1dJd0FNV2ZreXpheGhCLjRyVEZ3Z0J0cHdES2NjNEFscy04Mk4uMXBBQVRpeUhKTHJmNEFhVHdIRnk5bDYycDc3OXVBRURZQW0uT3FmQTYxVjB5UUtSSFpYYWxjQ28uV2QySTd4MXJZZ05hQVNjQjhOWkYxdlZLMUQxRzlBV1ZFRmxKQm5yT09CV192WEc0Z2FVUDBRcHJLYnRvNm1xeXpFQUo0RS1mQ3hiUDIwaGJjNkdEYVVQa2Z5aC5LMTg3VElBZHFCSHhESjdvZXNKVXNRT1hhWW1jVC1zZnZNQnBlZ0M0NXVIb0Myd1cwMFF4MmpGTHM4d2pkc2wxT1ctd2VJMyJ9|c9242fb356e3130a212edcff5cd492cb815e9a661aa93727ef51d6c0dc2dfc01"; z_c0="2|1:0|10:1647239997|4:z_c0|92:Mi4xV3FONEJRQUFBQUFBQUJBOGFHWC1FeVlBQUFCZ0FsVk5QREVjWXdESVR0aUhHZVJzTWdpT3BEU0EtdkhYM09qbUR3|ae7f956aff89de43348fd8d24b2cdfdfa5dfdecd9b9afa053a7e189959b424ac"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1646961695,1647065669,1647239956,1647264810; tst=h; NOT_UNREGISTER_WAITING=1; SESSIONID=5KMVZ2FUrUl0xmBFA75HmpuM7WVvuOTYPKWgM4qLk1u; JOID=UlAVAE--XGtwkGZpEr1wdTD-AJsBgx8lIc5cJ0TIAQ9D7w8jXJMTQBGcZmIWdmuCRLquhS1mZZ06AbF8jIVlNVo=; osd=V1EcBE67XWJ0kWNoG7lxcDH3BJoEghYhIMtdLkDJBA5K6w4mXZoXQRSdb2YXc2qLQLurhCRiZJg7CLV9iYRsMVs=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1647264926; KLBRSID=af132c66e9ed2b57686ff5c489976b91|1647264960|1647264810'
            ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }
    def get_html(self):
        html=requests.get(url=self.url,headers=self.headers).text
        self.parse_html(html)

    def parse_html(self,html):
        parse_html=etree.HTML(html)
        r_name=parse_html.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[1]/text()')
        print(r_name)
        r_school=parse_html.xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[2]/text()')
        print(r_school)


if __name__=='__main__':
    spider=login()
    spider.get_html()