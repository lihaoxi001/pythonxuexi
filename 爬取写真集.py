# -*- coding: utf-8 -*-

from ast import Str
from time import time
import urllib.request
from lxml import etree

# https://everia.club/page/3/

url = 'https://everia.club/page/'


def qqdxdz(url):
    headers = {
        'user-agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/102.0.5005.63Safari/537.36Edg/102.0.1245.39'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def hqym(request):
    request = urllib.request.urlopen(request,timeout=15)
    content = request.read().decode('utf-8')
    return content


def hqtp(request):
    request = urllib.request.urlopen(request,timeout=25)
    content = request.read()
    return content


def dowwnloadtp(url, name, i, i2):
    # 调用函数 请求对象

    request = qqdxdz(url)
    # 获取网页源码

    try:
        content = hqtp(request)

        # content= hqtp(request)

        print(str(name)+ str(i2) + str(i))
        f = open('./download/' + str(name) + str(i2) + str(i) + '.jpg', 'wb')
        f.write(content)
        f.close()
    except Exception as err:
        print(err.__class__.__name__)  # 错误类型

        print(err)  # 错误明细

        print('下载失败')
    # content= hqtp(request)


    # # content= hqtp(request)

    # print(str(name)+str(i))

    # f=open('./download/'+str(name)+str(i)+str(i2)+'.jpg','wb')

    # f.write(content)

    # f.close()



def dowwnload(content, name, i2):
    tree = etree.HTML(content)
    src_list = tree.xpath(
        '//figure[@class="wp-container-2 wp-block-gallery-1 wp-block-gallery has-nested-images columns-1"]//img/@src')
    for i in range(len(src_list)):
        # name=name+str(i)

        src = src_list[i]
        print(src)
        # urllib.request.urlretrieve(src, './download/'+name+src)

        dowwnloadtp(src, name, i, i2)
        # print(str(name)+i)



def lb(content, name):
    tree = etree.HTML(content)
    # name_list=tree.xpath('//div[@class="posts-wrapper"]//h2/a')

    url_list = tree.xpath('//div[@class="posts-wrapper"]//h2/a/@href')
    print(str(len(url_list)) + '页')
    for i in range(len(url_list)):
        i2 = i
        try:
            # name=name_list[i]

            url = url_list[i]
            print('抓取' + url)
            # 调用函数 请求对象

            request = qqdxdz(url)
            # 获取网页源码

            content = hqym(request)
            # 下载图片

            dowwnload(content, name, i2)
        except Exception as err:
            print(err.__class__.__name__)  # 错误类型

            print(err)  # 错误明细

            print('抓取失败')
        # url=url_list[i]

        # print('抓取'+url)

        # # 调用函数 请求对象

        # request = qqdxdz(url)

        # # 获取网页源码

        # content= hqym(request)

        # #下载图片

        # dowwnload(content,name,i2)



if __name__ == '__main__':
    first = int(input('请输入第一页：'))
    i = 1
    end = int(input('请输入最后一页：'))
    for i in range(first, end):
        if first == 1:
            url = 'https://everia.club/'
        else:
            url = 'https://everia.club/page/' + str(first) + '/'
        try:
            # 调用函数 请求对象

            request = qqdxdz(url)
            # 获取网页源码


            content = hqym(request)

            # 解析列表

            lb(content, i)
        except Exception as err:
            print(err.__class__.__name__)  # 错误类型

            print(err)  # 错误明细

            print('本页列表抓取失败')
            
            
            
