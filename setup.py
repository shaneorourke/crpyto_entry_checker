import sqlite3 as sql
conn = sql.connect('crypto_trading.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS position (Currency text, position boolean, quantity int)')
conn.commit()

c.execute('INSERT OR REPLACE INTO position VALUES ("BTCUSDT",0,0.001),("SOLUSDT",0,0.001),("ETHUSDT",0,0.001),("XRPUSDT",0,0.001),("APEUSDT",0,0.001),("LUNAUSDT",0,0.001)')
conn.commit()