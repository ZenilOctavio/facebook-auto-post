from yfinance import Ticker
from enum import Enum

class DefinedHistoryNames(Enum):
  Open = 0
  High = 1
  Low = 2
  Close = 3 
  Volume = 4 
  Dividends = 5 
  Splits = 6


class DefinedTicker:
  
  def __init__(self, ticker_name):
    self.raw = Ticker(ticker_name)
    self.shortName: str = self.raw.info['shortName']
    self.sector: str = self.raw.info['sector']
    self.currency: str = self.raw.info['financialCurrency']

  def today_data(self, columns: list[DefinedHistoryNames] = [DefinedHistoryNames.Open, DefinedHistoryNames.High, DefinedHistoryNames.Low, DefinedHistoryNames.Close, DefinedHistoryNames.Volume, DefinedHistoryNames.Dividends, DefinedHistoryNames.Splits]) -> dict[str, float]:
    todays_data = self.raw.history(period='1d')
    dictionary = {}
    
    for column in columns:
      dictionary[column.name] = todays_data.iloc[0,column.value]
    
    return dictionary

  
if __name__ == '__main__':
  microsoft = DefinedTicker('MSFT')
  print(microsoft.today_data())  
  print(microsoft.currency)

    