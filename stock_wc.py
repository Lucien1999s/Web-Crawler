# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 00:52:38 2022

@author: 林則廷
"""

from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd
import datetime

url = 'D:/python.project/web crawler/stock.xlsx'    #欲存放爬取資訊的xlsx檔位置

yf.pdr_override()                          #股票資訊爬取
while True:

    print('\n--股市資料爬取--')                         #獲取資料和選項
    choose = input('\n1.美股 2.台股(輸入1 or 2):')
    choose1 = input('\n1.批量股票爬取 2.單一股票爬取:')
    start_year = int(input('\n開始年份:'))
    start_month = int(input('\n開始月份:'))
    start_day = int(input('\n開始日期:'))
    end_year = int(input('\n結束年份:'))
    end_month = int(input('\n結束月份:'))
    end_day = int(input('\n結束日期:'))
    choose2 = input('\n1.取代現有資料(批量建議取代) 2.保留並新增表格 (輸入1 or 2):')
    
    start = datetime.datetime(start_year, start_month, start_day)
    end = datetime.datetime(end_year, end_month, end_day)
    
    if(choose1 == '1'):                          #批量股票處理
        stockid = []
        while True:
            code = input('\n公司代碼:')
            if(choose == '1'):
                company = code
            else:
                company = code+'.tw'
            stockid.append(company)
            over = input('\n結束輸入over:')
            if(over == 'over'):
                break
        if(choose2 == '1'):
            writer = pd.ExcelWriter(url)
        else:
            writer = pd.ExcelWriter(url,mode='a')
        
        for i in range(0,len(stockid)):
            df = pdr.get_data_yahoo(stockid[i], start,end)
            df.to_excel(writer,stockid[i])
    else:
        code = input('\n公司代碼:')              #單一股票處理
        if(choose == '1'):
            company = code
        else:
            company = code+'.tw' 
        df = pdr.get_data_yahoo(company,start,end)
        if(choose2 == '1'):
            writer = pd.ExcelWriter(url)
        else:
            writer = pd.ExcelWriter(url,mode='a')
        sheet = input('\n創建表格(表格命名):')
        df.to_excel(writer,sheet)
        
    writer.save()                                 #存檔
    out = input('\n欲結束爬取，輸入out:')
    if(out == 'out'):
        break