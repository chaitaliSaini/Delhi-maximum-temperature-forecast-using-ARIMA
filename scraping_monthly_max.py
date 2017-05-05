# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:46:49 2017

@author: chait
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:14:43 2017

@author: chait
"""
import csv
import bs4 as bs
import urllib.request
import re
with open("temp_delhi_dataset.csv","w") as scoreFile:
    scoreFileWriter = csv.writer(scoreFile)
    for year in range(2010,2018):
        for month in range(1,13):
            if month<10:
                month_str="0"+str(month)
            else:
                month_str=str(month)
            
            year_str=str(year)
            string_web="https://www.timeanddate.com/weather/india/delhi/historic?month="+str(month)+"&year="+str(year)
            sauce = urllib.request.urlopen(string_web).read()
            soup=bs.BeautifulSoup(sauce,'lxml')
            
            
            arr=soup.get_text()
            
            ans=[m.start() for m in re.finditer(',"templow"', arr)]
            temp=[]
            for index in ans:
                if arr[index-2]=='0' or arr[index-2]=='1' or arr[index-2]=='2' or arr[index-2]=='3'or arr[index-2]=='4' or arr[index-2]=='5' or arr[index-2]=='6'or arr[index-2]=='7'or arr[index-2]=='8'or arr[index-2]=='9':
                    temp_curr=arr[index-2]+arr[index-1]
                    temp_curr=int(temp_curr)
                else:
                    temp_curr=arr[index-1]
                    temp_curr=int(temp_curr)
                temp.append(temp_curr)
            print(temp)
            max_temp=max(temp)
            print(max_temp)
           


            date=month_str+"-"+year_str
            scoreFileWriter.writerow([date,max_temp])
scoreFile.close()
                    
                
