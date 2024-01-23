from datetime import datetime, timedelta, time
from YahooFinance.YahooFinance import DefinedTicker, DefinedHistoryNames as DH
from EventManagement.EventPoolSync import EventPoolSync
from YahooScrapper.YahooScrapper import YahooScrapper

tickers = ['^GSPC', '^DJI', '^IXIC', 'MXN=X']

ticker_objects: dict[str, DefinedTicker] = {}
scrapper = YahooScrapper()

@EventPoolSync.mid_week_event(time(hour=15, minute=32))
def print_yahoo_data_sync():
  print('Getting yahoo data sync')
  print(scrapper.get_today_data_from_tickers(tickers))


    
EventPoolSync.run()