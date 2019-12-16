# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 20:02:21 2019

@author: Akshay
"""

import os
import pandas as pd
from Step2_AQI_Avgdata import aqi_dailyAvg_cal
from Step3_scrap_html_to_df import scrap_html_table


def collect_tables():
    """
    This function collect tables produced by scrap_html_table() from 2013 to 2018
    and join it with AQI average data produced from aqi_dailyAvg_cal()
    """
    climate_df =pd.DataFrame()
    
    # collect table from each month for years 2013 to 2018
    for year in range(2013,2019):
        for month in range(1,13):
            df_table = scrap_html_table(year, month)
            print("shape of table = ",df_table.shape)
            climate_df = climate_df.append(df_table, ignore_index = True)
            
        new_df = climate_df.set_index(climate_df.Date)   
            
    
    
    # Calculate daily average AQI
    AQI_data = "Data/AQI/"
    if os.path.exists(AQI_data):
        files = os.listdir(AQI_data)
    
    df_temp = pd.DataFrame()
    aqi_df = pd.DataFrame()
    for file in files:
        # convert dict to data frame and append 
        df_temp = pd.DataFrame.from_dict(aqi_dailyAvg_cal(AQI_data + file), orient='index')
        aqi_df = aqi_df.append(df_temp)
   
    
    # merge AQI data into climate data collected above
    dataset = new_df.merge(aqi_df, left_index=True, right_index=True)
    
    return dataset
    
if __name__ == '__main__':
    
    df = pd.DataFrame()
    df = collect_tables()
    print("Shape of collected data is : ", df.shape)
    
    # write data to csv file
    if not os.path.exists("Data/DataSet/"):
        os.mkdir("Data/DataSet/")
    df.to_csv("Data/DataSet/AQI_dataset.csv")



