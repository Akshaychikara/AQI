# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 00:33:29 2019

@author: Akshay
"""
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from AQI_Avgdata import aqi_dailyAvg_cal
from datetime import date


def scrap_html_table(year, month):
    """ This function fetch and return the table from a html page """
    
     # read data from stored html file to data frame
    html_file = "Data/html/Sarafganj/{}/{}.html".format(year, month)
    df_table = pd.read_html(html_file,header=0, attrs={'class':'medias mensuales numspan'})[0]
    
    # Drop other empty columns alongwith last two rows (This data 
    # is not require)
    df_table.drop(axis = 1, columns = ['SLP','VG','RA','SN','TS','FG'], inplace=True)
    df_table.drop(df_table.tail(2).index, axis = 0, inplace=True)
    
    # create a date column
    df_table['Month'] = 1
    df_table['Year'] = 2013
    
    df_table['Date'] = pd.to_datetime(df_table[['Year','Month','Day']]).dt.date
    
    # Drop day, year and month columns
    df_table.drop(axis = 1, columns = ['Day','Month','Year'], inplace=True)
   
    return df_table
      
