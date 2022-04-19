from urllib import parse
query_string = {
    'wd' : '爬虫'
}
result = parse.urlencode(query_string)
url = 'http://www.baidu.com/s?{}'.format(result)
print(url)