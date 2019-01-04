#coding=utf-8

import requests
from bs4 import BeautifulSoup
import os
import urllib
import datetime
# 第一个参数自然是网络地址，第二个参数就是网络传输的头数据。
# 为什么要头数据呢？
# 如果我们直接申请请求，有些网站有反爬虫的设置，就会断开连接。
# 而头则是为了让服务器误判请求是浏览器。

url = 'https://www.zbjuran.com/dongtai/'

# 爬取图片的网站都是静态的
#下载图片，默认保存到当前py文件夹下单images文件夹下
def save_img(img_url,file_name,file_path='images'):
    try:
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_path))
        if not os.path.exists(file_path):
            # os.system(r'touch {}'.format(file_path)),创建文件的方法
            os.makedirs(file_path)#创建文件夹
        #获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        if len(file_suffix) == 0:
            print('不是图片地址：')
            print(img_url)
            return
        #拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
        # print(filename)
       #下载图片，并保存到文件夹中
        urllib.urlretrieve(img_url,filename=filename)
    except IOError as e:
        print '文件操作失败',e
    except Exception as e:
        print '错误 ：',e
#根据链接，获取图片链接
def getImegUrls(url):
    header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
    html = requests.get(url,headers = header)
    html.encoding = html.apparent_encoding#解决中文乱码
    # 那么我们进行下一步，如何批量爬取一个网站的图片呢？
    # 关键是就是如何获取一个网站的图片列表。
    mess = BeautifulSoup(html.text,"html.parser")
    # 返回文本的数据。
    # 查找所有img属性的图片
    print(html.text)
    print('---------------------------')
    protocol, s1 = urllib.splittype(url)


    # ('http', '//www.freedom.com:8001/img/people')
    print(protocol, s1)
    host, s2 = urllib.splithost(s1)
    # ('www.freedom.com:8001', '/img/people')
    hostUrl = protocol + '://'+host
    print(hostUrl)  # http://www.freedom.com:8001
    #图片的大标签，百度图片的是li+data-imgurl
    labels = ['img','li']    
    # 然后一个循环下载同上
    list = [];
    for label in labels:
        pic_url = mess.find_all(label)
        for i in range(len(pic_url)):
            print('--------原嘛:' + str(i))
            print(pic_url[i])
            #图片URL的可能标签
            type =['src','data-src','data-imgurl']
            imageUrl = ''
            for item in type:
                if pic_url[i].has_attr(item) and pic_url[i][item]:
                    imageUrl = pic_url[i][item]
                    if len(imageUrl)>0:
                        break
            print('image = '+imageUrl)
            if imageUrl.startswith('//'):
                #有的图片没有加http
                imageUrl = 'http:' + imageUrl   
            #src="/uploads/allimg/181031/2-1Q031162H40-L.jpg"
            if imageUrl.startswith('/')
            if imageUrl.startswith('http'):
                #CSDN的图片后缀用=进行替换了,百度用;
                wordDic = {'=':'.', ';':'&'}
                for key in wordDic.keys():                
                    if key in imageUrl:
                        imageUrl = imageUrl.replace(key, wordDic[key])
                print('是图片链接')
                list.append(imageUrl)
            else:
                print('非图片链接')
    print('有效图片：%s 个' %len(list) )
    return list
if __name__ == '__main__':
    print('-----开始------')
    list = getImegUrls(url)
    print('-----下载图片-----')
    for index,item in enumerate(list):
        print('下载进度：%f' %(index*100/len(list)))
        nowTime=datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')#现在
        folder = 'images/'+datetime.datetime.now().strftime('%Y-%m-%d-%H')
        save_img(item,nowTime,folder)
    print('-----完成------')
