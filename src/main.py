from datetime import datetime, timedelta
from YahooFinance.YahooFinance import DefinedTicker, DefinedHistoryNames as DH
from EventManagement.EventPoolSync import EventPoolSync
from YahooScrapper.YahooScrapper import YahooScrapper

tickers = ['^GSPC', '^DJI', '^IXIC', 'MXN=X']

ticker_objects: dict[str, DefinedTicker] = {}
scrapper = YahooScrapper()

# for ticker in tickers:
#   try: 
#     ticker_objects[ticker] = DefinedTicker(ticker)
#   except :
#     print(f'Ticker not found: {ticker}')

@EventPoolSync.repeat_event(datetime.now() + timedelta(seconds=5), timedelta(minutes=1))
def print_yahoo_data_sync():
  print(scrapper.get_today_data_from_tickers(tickers))



    
EventPoolSync.run()