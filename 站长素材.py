from unicodedata import name
import urllib.request
from lxml import etree

# https://sc.chinaz.com/tupian/
# https://sc.chinaz.com/tupian/index_2.html
url = 'https://sc.chinaz.com/tupian/'


def qqdxdz(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def hqym(request):
    request = urllib.request.urlopen(request)
    content = request.read().decode('utf-8')
    return content


def dowwnload(content):
    tree = etree.HTML(content)
    name_list=tree.xpath('//div[@id="container"]//a/img/@alt')
    src_list = tree.xpath('//div[@id="container"]//a/img/@src')
    for i in range(len(name_list)):
        name=name_list[i]
        src='https:'+src_list[i]
        urllib.request.urlretrieve(src, './download/'+name+'.jpg')
        print(name)



if __name__ == '__main__':
    pass
    first = int(input('请输入第一页：'))
    end = int(input('请输入最后一页：'))
    for first in range(first, end):
        if first == 1:
            url = 'https://sc.chinaz.com/tupian/'
        else:
            url = 'https://sc.chinaz.com/tupian/index_' + str(first) + '.html'
        # 调用函数 请求对象的定??
        request = qqdxdz(url)
        # 获取网页源码
        content= hqym(request)
        # 下载图片
        dowwnload(content)
