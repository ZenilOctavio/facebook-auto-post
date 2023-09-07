from datetime import datetime, timedelta
from YahooFinance.YahooFinance import DefinedTicker, DefinedHistoryNames as DH
from EventManagement.EventPoolSync import EventPoolSync

tickers = ['HOMEX.MX', 'TV', 'TSLA', 'AAPL', 'KO']

ticker_objects: dict[str, DefinedTicker] = {}

for ticker in tickers:
  try: 
    ticker_objects[ticker] = DefinedTicker(ticker)
  except :
    print(f'Ticker not found: {ticker}')

@EventPoolSync.repeat_event(datetime.now() + timedelta(seconds=5), timedelta(minutes=1))
def print_yahoo_data_sync():
  for ticker_object in ticker_objects.values():
    print(f'{ticker_object.shortName} -> {ticker_object.today_data(columns= [DH.Open, DH.Close])}')
    
EventPoolSync.run()