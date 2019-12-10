# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:23:49 2019

@author: Akshay
"""

import os
import time
import sys
import requests



def retrieve_html():
    cities = {'New Delhi':'421810','Bangalore':'432950'}

    for city, code in cities.items():
        for year in range(2013,2019):
            for month in range(1,13):
                # Create dynamic url with month, year and city code
                # url format is : https://en.tutiempo.net/climate/04-2013/ws-432950.html
                # replace month, year and city code with variables, Note month format is 0i
                # for i<10
                
                if (month < 10):
                    url = 'https://en.tutiempo.net/climate/0{}-{}/ws-{}.html'.format(month, year, code)
                else:
                    url = 'https://en.tutiempo.net/climate/{}-{}/ws-{}.html'.format(month, year, code)
                
                # read data from url
                html = requests.get(url)
                html = html.text.encode(encoding='utf-8')
                
                # create directory structure if not already exist
                folders = 'Data/html/{}/{}'.format(city, year)
                if not os.path.exists(folders):
                    os.makedirs(folders, mode=777)
                
                # write html raw data to directory
                with open(folders + '/{}.html'.format(month), 'wb') as output:
                    output.write(html)
                    
                sys.stdout.flush()
                
                
if __name__ =='__main__':
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print("Time taken : ", stop_time-start_time)
    
    