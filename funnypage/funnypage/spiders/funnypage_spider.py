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

class funnypage(scrapy.Spider):

    name = 'funnypage'

    def start_requests(self):
        url = 'https://www.qiushibaike.com/imgrank/page/'
        page_size = self.getPageSize(url)
        for i in range(page_size):
            yield scrapy.Request(url=url + str(i+1), callback=self.parse)

    def getPageSize(self,url):
        page = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'})
        soup = bs4.BeautifulSoup(page.text, 'html5lib')
        return int(soup.select('.page-numbers')[-1].text)

    def parse(self, response):
        date = str(dt.datetime.now().strftime('%Y%m%d'))
        if not os.path.exists('./html/' + date):
            os.makedirs('./html/' + date)
        page = response.url.split("/")[-2]
        filename = './html/' + date + '/funnypage-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件：%s' % filename)

