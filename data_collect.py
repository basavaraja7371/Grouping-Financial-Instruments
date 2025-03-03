import yfinance as yf
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr

url='https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sp500_table = pd.read_html(url)
sp500_df = sp500_table[0]
sp500_tickers = sp500_df['Symbol'].tolist()
sp500_tickers = [ticker.replace('.', '-') for ticker in sp500_tickers]

additional_tickers = ['GLD', 'SLV', 'USO', 'TLT', 'HYG',
                      'BTC-USD', 'ETH-USD', 'BNB-USD', 'XRP-USD', 'ADA-USD',
                      'EURUSD=X', 'JPY=X', 'GBPUSD=X', 'GC=F', 'SI=F', 'CL=F',
                      'SPY', 'QQQ', 'IWM', 'VOO'
                     ]

all_tickers = sp500_tickers + additional_tickers
print(f'Total tickers: {len(all_tickers)}')

data = yf.download(
    tickers=all_tickers,
    start='2018-01-01',
    end='2023-01-01',
    group_by='ticker',
    progress=False,
    auto_adjust=True
)

data.to_csv('finance_raw.csv')
