from locale import currency
from binance import Client
import pandas as pd
import binance_keys as bk
import sqlite3 as sql

conn = sql.connect('crypto_trading.db')
c = conn.cursor()

client = Client(api_key=bk.API_KEY,api_secret=bk.SECRET_KEY)

currencies = pd.read_sql('SELECT Currency FROM position',conn)

stop_loss_percentage = 0.03


replace = ['(',')',',','./data/','csv','.','[',']']
replace_number = ['(',')',',','[',']']

def clean_up_sql_out(text,isnumber):
    if isnumber == 1:
        for s in replace_number:
            text = str(text).replace(s,'')      
    else:
        for s in replace:
            text = str(text).replace(s,'')
    return text

def round_float(value):
    value = round(float(value),4)
    return value

def gethourlydata(symbol):
    frame = pd.DataFrame(client.get_historical_klines(symbol,'1h','50 hours ago UTC'))
    frame = frame.iloc[:,:5]
    frame.columns = ['Time','Open','High','Low','Close']
    frame[['Open','High','Low','Close']] = frame[['Open','High','Low','Close']].astype(float)
    frame.Time = pd.to_datetime(frame.Time, unit='ms')
    return frame

def applytechnicals(df):
    df['FastSMA'] = df.Close.rolling(7).mean()
    df['SlowSMA'] = df.Close.rolling(25).mean()
    df['SuperSlow'] = df.Close.rolling(50).mean()


def trader(curr):
    df = gethourlydata(curr)
    applytechnicals(df)
    lastrow = df.iloc[-1]
    Close = round(lastrow.Close,4)
    FastSMA = round(lastrow.FastSMA,4)
    FastSMA = round(lastrow.FastSMA,4)
    SlowSMA = round(lastrow.SlowSMA,4)
    SuperSlowSMA = round(lastrow.SuperSlow,4)
    print(f'Currency:{curr}')
    print(f'Close:{Close}')
    #print(f'FastSMA:{FastSMA}')
    #print(f'SlowSMA:{SlowSMA}')
    #print(f'SuperSlow:{SuperSlowSMA}')
    if lastrow.FastSMA > lastrow.SuperSlow:
        if lastrow.FastSMA > lastrow.SlowSMA:
            if lastrow.Close < lastrow.SlowSMA:
                print('long')
                take_profit = Close + (Close * 0.01)
                stop_loss = Close - (Close * 0.001)
                print(f'TP:{take_profit}')
                print(f'SL:{stop_loss}')
            else:
                distance = round(lastrow.SlowSMA - lastrow.Close,4)
                print(f'Distance from LONG:{distance}')
    if lastrow.FastSMA < lastrow.SuperSlow:
        if lastrow.FastSMA < lastrow.SlowSMA:
            if lastrow.Close > lastrow.SlowSMA:
                print('short')
                take_profit = round(Close + (Close * 0.01),4)
                stop_loss = round(Close - (Close * 0.001),4)
                print(f'TP:{take_profit}')
                print(f'SL:{stop_loss}')
            else:
                distance = round(lastrow.SlowSMA - lastrow.Close,4)
                print(f'Distance from SHORT:{distance}')


for curr in currencies.Currency:
    trader(curr)
    print()