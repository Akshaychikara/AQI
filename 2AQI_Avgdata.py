# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:06:30 2019

@author: Akshay
"""
import os
import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt

def aqi_dailyAvg_cal(file):
    print("calculating daily average for year: ",file)
    average = []
    for day_data in pd.read_csv(file, chunksize=24):
        data=[]
        
        for i in day_data['PM2.5']:
            if type(i) is int or type(i) is float:
                data.append(i)
            elif type(i) is str:
                if i!="NoData" and i!="PwrFail" and i!="---" and i!="InVld":
                    data.append(float(i))
        
        day_avg = np.mean(data)
        
        average.append(day_avg)
    print('Done.............', len(average))
    return average
    
if __name__ == "__main__":
    
    AQI_data = "Data/AQI/"
    if os.path.exists(AQI_data):
        files = os.listdir(AQI_data)
    
    df = pd.DataFrame()
    for file in files:
        df[file] = pd.Series(aqi_dailyAvg_cal(AQI_data + file))
        
    # plot
    fig = plt.figure(figsize=(15,8))
    for f in files:
        plt.plot(range(0,365), df[f], label=f)
    plt.legend()
    plt.show()
        
  