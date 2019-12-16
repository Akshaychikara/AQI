# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:06:30 2019

@author: Akshay
"""
import os
import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def aqi_dailyAvg_cal(file):
    """ 
    This function calculate average per day AQI value (PM2.5) 
    from hourly AQI and return datewise average as a dict.
    """
    
    print("calculating daily average for year: ",file)
    average = {}
    for day_data in pd.read_csv(file, chunksize=24):
        data=[]
        
        # fetch date and make it dictonary keys 
        date = day_data['Date'].unique()[0]
       # datetime.strptime(date, '%d/%m/%Y')
        
        # fetch data in each row
        for i in day_data['PM2.5']:
            if type(i) is int or type(i) is float:
                data.append(i)
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="---" and i!="InVld":
                    data.append(float(i))
                    
        # Calculate average
        day_avg = np.mean(data)
        
       # append day_avg for each dates to average dict
        average[date] = day_avg

    print('Done....AQI calculated for days:', len(average))
    return average
    
if __name__ == "__main__":
    
    AQI_data = "Data/AQI/"
    if os.path.exists(AQI_data):
        files = os.listdir(AQI_data)
    
    df_temp = pd.DataFrame()
    df = pd.DataFrame()
    for file in files:
        #df[file] = pd.Series(aqi_dailyAvg_cal(AQI_data + file))
        # convert dict to data frame and append 
        df_temp = pd.DataFrame.from_dict(aqi_dailyAvg_cal(AQI_data + file), orient='index')
        df = df.append(df_temp)
        
        
        
    # plot
 #   fig = plt.figure(figsize=(15,8))
 #   for f in files:
 #       plt.plot(range(0,365), df[f], label=f)
 #   plt.legend()
 #   plt.show()
        
  