# from base64 import encode
#
# import scrapy
# import logging

from tutorial.items import DemoItem, SingerItem

# from scrapy.contrib.spiders import CrawlSpider,Rule
# from scrapy.contrib.linkextractors import LinkExtractor
# from scrapy.contrib.spiders import SitemapSpider
#
# class MySpider(scrapy.Spider):
#     name = 'demo'
#     allowed_domains = ['163.com']
#     start_urls = ["http://music.163.com/#/user/home?id=52366445"]
#
#     def parse(self, response):
#         with open('Books', 'wb') as f:
#             f.write(response.body)
#
#
#
# # class DemoSpider(SitemapSpider):
# #     name = "demo"
#
#     # def __init__(self, category = None, *args, **kwargs):
#     #     super(DemoSpider,self).__init__(*args, **kwargs)
#     #     self.start_urls = ["http://dmoztools.net/Computers/Programming/Languages/Python/%s" % category]
#     # allowed_domains = ["dmoztools.net"]
#     # start_urls = [
#     #     "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
#     #     "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
#     # ]
#     # sitemap_urls = ["https://www.jd.com/sitemap.xml"]
#     #
#     # sitemap_rules = [
#     #     ('book', 'parse_book'),
#     #     ('shouji', 'parse_shouji'),
#     # ]
#
#     # other_urls = ['https://www.baidu.com']
#
#     # def parse(self, response):
#     #     # filename = response.url.split("/")[-2]
#     #     # with open(filename, 'wb') as f:
#     #     #     f.write(response.body)
#     #     for sel in response.xpath('//ul/li'):
#     #         item = DemoItem()
#     #         item['title'] = sel.xpath('a/text()').extract()
#     #         item['link'] = sel.xpath('a/@href').extract()
#     #         item['desc'] = sel.xpath('text()').extract()
#     #         yield item
#
#     # def start_requests(self):
#     #     req = list(super(DemoSpider,self).start_requests())
#     #     # req += [scrapy.Request(x, self.parse_other) for x in self.other_urls]
#     #     return req
#
#     # def parse_book(self, response):
#     #     for sel in response.xpath('//dl/dt'):
#     #         item = DemoItem()
#     #         item['title'] = sel.xpath('a/text()').extract()
#     #         item['link'] = sel.xpath('a/@href').extract()
#     #         item['desc'] = sel.xpath('text()').extract()
#     #         yield item
#     # def parse_shouji(self, response):
#     #     for sel in response.xpath('//dl/dt'):
#     #         item = DemoItem()
#     #         item['title'] = sel.xpath('a/text()').extract()
#     #         item['link'] = sel.xpath('a/@href').extract()
#     #         item['desc'] = sel.xpath('text()').extract()
#     #         yield item
#
#     # def parse_other(self, response):
#     #     pass
#
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
import json


class AlbumCover():
    # name = 'demo'
    def __init__(self):
        # self.init_url = "http://music.163.com/#/artist/album?id=101988&limit=10&offset=0" #请求网址
        self.init_url = "http://music.163.com/#/search/m/?id=101988&limit=10&offset=10&s=sia"
        self.folder_path = "D:/tutorial_img"  # 想要存放的文件目录

    # def save_img(self, url, file_name):  ##保存图片
    #     print('开始请求图片地址，过程会有点长...')
    #     img = self.request(url)
    #     print('开始保存图片')
    #     f = open(file_name, 'ab')
    #     f.write(img.content)
    #     print(file_name, '图片保存成功！')
    #     f.close()

    def request(self, url):  # 封装的requests 请求
        r = requests.get(url)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
            return True
        else:
            print(path, '文件夹已经存在了，不再创建')
            return False

    # def get_files(self, path):  # 获取文件夹中的文件名称列表
    #     pic_names = os.listdir(path)
    #     return pic_names

    def spider(self):
        print("Start!")
        phantomjs_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe'
        driver = webdriver.PhantomJS(phantomjs_path)
        driver.get(self.init_url)
        driver.switch_to.frame("g_iframe")
        html = driver.page_source

        # self.mkdir(self.folder_path)  # 创建文件夹
        # print('开始切换文件夹')
        # os.chdir(self.folder_path)  # 切换路径至上面创建的文件夹
        #
        # file_names = self.get_files(self.folder_path)  # 获取文件夹中的所有文件名，类型是list

        # all_li = BeautifulSoup(html, 'lxml').find(id='m-song-module').find_all('li')
        # # print(type(all_li))
        #
        # for li in all_li:
        #     album_img = li.find('img')['src']
        #     album_name = li.find('p', class_='dec')['title']
        #     album_date = li.find('span', class_='s-fc3').get_text()
        #     end_pos = album_img.index('?')
        #     album_img_url = album_img[:end_pos]
        #
        #     photo_name = album_date + ' - ' + album_name.replace('/', '').replace(':', ',') + '.jpg'
        #     print(album_img_url, photo_name)
        #
        #     if photo_name in file_names:
        #         print('图片已经存在，不再重新下载')
        #     else:
        #         self.save_img(album_img_url, photo_name)

        all_li = BeautifulSoup(html, 'lxml').find_all(attrs={'class': 'item f-cb h-flag '})
        count = 0
        for li in all_li:
            print("item begin")
            item = SingerItem()
            song_mv = li.find(attrs={'class': 'td w0'}).find_all('a')
            item['song_name_link'] = song_mv[0]['href']
            item['song_name'] = song_mv[0].find('b')['title']
            if len(song_mv) == 2:
                item['song_mv_link'] = song_mv[1]['href']
            else:
                item['song_mv_link'] = ""
            song_artist_li = li.find(attrs={'class': 'td w1'}).find_all('a')
            for i in range(len(song_artist_li)):
                if i == 0:
                    item['song_artist_name_link'] = song_artist_li[i]['href']
                    item['song_artist_name'] = song_artist_li[i].string
                else:
                    item['song_artist_name_link'] = item['song_artist_name_link'] + "\\" + song_artist_li[i]['href']
                    item['song_artist_name'] = item['song_artist_name'] + "\\" + song_artist_li[i].string

            song_album = li.find(attrs={'class': 'td w2'}).find('a')
            item['song_album_name_link'] = song_album['href']
            item['song_album_name'] = song_album['title']
            print(item)
            print("item end")
            with open('C:\\Users\\capit\\Desktop\\StudentGradeMS\\website\\login\\static\\dist\\resource\\sia.json', 'a+') as f:
                line = json.dumps(dict(item)) + "\n"
                f.write(line)
            count += 1
        print(count)

album_cover = AlbumCover()
album_cover.spider()
