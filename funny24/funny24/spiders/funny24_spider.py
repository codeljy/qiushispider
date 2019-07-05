# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         ljy
# Description:  
# Author:       lenovo
# Date:         2019/7/3
#-------------------------------------------------------------------------------

import scrapy
import requests
import bs4
import datetime as dt
import os
import time
import random
import math

class funny24(scrapy.Spider):

    name = 'funny24'
    BASE_URL = 'https://www.qiushibaike.com'

    def start_requests(self):
        url = self.BASE_URL + '/hot/page/'
        page_size = self.getPageSize(url)
        for i in range(page_size):
            yield scrapy.Request(url=url + str(i+1), callback=self.parse)

    def getPageSize(self,url):
        page = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'})
        soup = bs4.BeautifulSoup(page.text, 'html5lib')
        return int(soup.select('.page-numbers')[-1].text)

    def parse(self, response):
        # self.saveHtml(response)
        time.sleep(1) # 睡眠一秒
        article_url = response.css("div[id^='qiushi_tag'] a[class='contentHerf']::attr(href)").extract()
        for article in article_url: # 详情数据爬取
            yield scrapy.Request(self.BASE_URL+article, callback=self.detail_parse)

    # 保存每一页html文件
    def saveHtml(self, response):
        date = str(dt.datetime.now().strftime('%Y%m%d'))  # 获取日期
        if not os.path.exists('./html/' + date + '/page'):  # 建立文件目录
            os.makedirs('./html/' + date + '/page')
        page = response.url.split("/")[-2]
        filename = './html/' + date + '/page/funny24-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件：%s' % filename)

    def detail_parse(self, response):
        time.sleep(math.floor(random.random()*3+1)) # 随机睡眠1-3秒
        self.saveDetailHtml(response) # 存储详情html文件
        self.analysisHtml(response) # 解析html，保存数据到mysql

    # 保存每一篇文章的详情html文件
    def saveDetailHtml(self, response):
        date = str(dt.datetime.now().strftime('%Y%m%d'))  # 获取日期
        if not os.path.exists('./html/' + date + '/detail'):  # 建立文件目录
            os.makedirs('./html/' + date + '/detail')
        article_id = response.url.split("/")[-1]
        filename = './html/' + date + '/detail/funny24-%s.html' % article_id
        with open(filename, 'wb') as f:
            f.write(response.body)
            f.close()
        self.log('保存文件：%s' % filename)

    def analysisHtml(self, response):
        user_name = response.css("div[id='articleSideLeft'] a[href^='/users/'] img::attr(alt)").extract_first()
        user_id = str(response.css("a[class='side-left-userinfo']::attr(href)").extract_first()).split('/')[-2]
        user_url = self.BASE_URL + response.css("a[class='side-left-userinfo']::attr(href)").extract_first()
        article_id = response.url.split("/")[-1]
        article_url = response.url
        article_content = response.css("div[class^='article block'] .content::text").extract_first()
        article_picture_url = response.css("div[class^='article block'] .thumb img::attr(src)").extract_first()
        article_time = str(response.css(".stats-time::text").extract_first()).replace('\\','').replace('n','')
        article_good = response.css(".number::text").extract_first()

        date = str(dt.datetime.now().strftime('%Y%m%d'))  # 获取日期
        if not os.path.exists('./html/' + date):  # 建立文件目录
            os.makedirs('./html/' + date)
        filename = './html/' + date + '/funny24-message.html'
        with open(filename, 'a+') as f:
            f.write(user_name + " " + str('' if article_time is None else article_time) + "发布糗事：\n")
            f.write('user_name：' + str('' if user_name is None else user_name) + '\n')
            f.write('user_id：' + str('' if user_id is None else user_id) + '\n')
            f.write('user_url：' + str('' if user_url is None else user_url) + '\n')
            f.write('article_id：' + str('' if article_id is None else article_id) + '\n')
            f.write('article_url：' + str('' if article_url is None else article_url) + '\n')
            f.write('article_content：' + str('' if article_content is None else article_content) + '\n')
            f.write('article_picture_url：' + str('' if article_picture_url is None else article_picture_url) + '\n')
            f.write('article_time：' + str('' if article_time is None else article_time) + '\n')
            f.write('article_good：' + str('' if article_good is None else article_good) + '\n')
            f.close()
        self.log('保存文件：%s' % filename)

a = 'fuck'

print(str('' if a is None else a))

