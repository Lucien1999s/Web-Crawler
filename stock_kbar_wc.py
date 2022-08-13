# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 23:35:25 2022

@author: 林則廷
"""

import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as fplt
import datetime

print('--股票k線圖繪製--')
while True:
    start_year = int(input('\n開始年份:'))    #獲取時間
    start_month = int(input('\n開始月份:'))
    start_day = int(input('\n開始日期:'))
    end_year = int(input('\n結束年份:'))
    end_month = int(input('\n結束月份:'))
    end_day = int(input('\n結束日期:'))

    start = datetime.datetime(start_year,start_month,start_day)
    end = datetime.datetime(end_year,end_month,end_day)

    choose = input('\n1.美股 2.台股(輸入1 or 2):')    
    code = input('\n公司代碼:')
    choose1 = input('\n1.直接存檔 2.現場繪製(輸入1 or 2):')
    if(choose == '1'):
        company = code
    else:
        company = code+'.tw'
    ohlc = yf.download(company,start,end)             #爬取資料
    ohlc = ohlc.loc[:, ["Open", "High", "Low", "Close", "Volume"]]


    mc = fplt.make_marketcolors(      #設定圖標顏色
         up='tab:red',down='tab:green',
         wick={'up':'red','down':'green'},
         volume='tab:blue',
        )
    s  = fplt.make_mpf_style(marketcolors=mc)
    
    if(choose1 == '1'):
        file = input('\n輸入檔案名:')
        file = file + '.png'
        fplt.plot(                          #繪製K線圖
            ohlc,
            type = 'candle',
            style = s,
            title = code,
            ylabel = 'Price ($)', 
            volume = True,
            savefig = file,
        )
    else:
        fplt.plot(                          #繪製K線圖
            ohlc,
            type = 'candle',
            style = s,
            title = code,
            ylabel = 'Price ($)', 
            volume = True,
            
        )
    plt.show()                          #畫K線圖並顯示
    out = input('\n欲結束程式請輸入out:')
    if(out == 'out'):
        break