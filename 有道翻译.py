import random
import time
from hashlib import md5
from ua_info import ua_list
import requests

class YoudaoSpider(object):
    def __init__(self):
        self.url='https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        self.headers={"User_Agent":random.choice(ua_list)}

    def get_lts_salt_sign(self,word):
        lts=str(int(time.time()*1000))
        salt=lts+str(random.randint(0,9))
        string ="fanyideskweb"+word+salt+"Ygy_4c=r#e#4EX^NUGUc5"
        s=md5()
        s.update(string.encode())
        sign=s.hexdigest()
        print(lts,salt,sign)
        return lts,salt,sign

    def attack_vd(self,word):
        lts,salt,sign=self.get_lts_salt_sign(word)
        data={
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": lts,
            "bv": "c2777327e4e29b7c4728f13e47bde9a5",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
        res=requests.post(
            url=self.url,
            data=data,
            headers=self.headers,
        )
        html=res.json()
        print(html)
        result=html["translateResult"][0][0]["tgt"]
        print('翻译结果:',result)

    def run(self):
        try:
            word=input('请输入要翻译的单词:')
            self.attack_vd(word)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    spider=YoudaoSpider()
    spider.run()
