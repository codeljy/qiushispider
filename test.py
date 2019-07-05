# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         ljy
# Description:  
# Author:       lenovo
# Date:         2019/7/5
#-------------------------------------------------------------------------------


# import requests
# page = requests.get('https://www.qiushibaike.com/hot/page/1',
#                     headers={
#                         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
#                     },proxies={'https':'https://60.191.57.72:23162'})
# print(page.text.encode('ISO-8859-1').decode('utf-8'))

import random
import math

for i in range(10):
    print(math.floor(random.random()*3+1))

