from .exceptions import NotValidTicker
from playwright.sync_api import sync_playwright, Page
from bs4 import BeautifulSoup

table_order = ['date', 'open', 'high', 'low', 'close', 'adj close', 'volume']

class YahooScrapper:
    
    def __init__ (self):
        pass
    
    def __get_history_url_for_ticker(self, ticker: str) -> str:
        if not ticker:
            raise NotValidTicker('A ticker is required')
        
        return f'https://finance.yahoo.com/quote/{ticker}/history?p={ticker}'
    
    def __get_history_table(self, page: Page) -> str:
        return page.locator('table').inner_html()
    
    def __get_last_day_history_table(self, history_table_string: str) -> dict[str, str]:
        soup = BeautifulSoup(history_table_string, 'lxml')
        last_row = soup.tbody.tr
        
        data: dict[str, str] = {}
        
        for index, td_element in enumerate(last_row.childGenerator()):
            # print(td_element)
            if not td_element.span:
                continue
            data[table_order[index]] = td_element.span.text
            
        return data
    
    def get_today_data(self, ticker: str) -> dict:
        url: str = self.__get_history_url_for_ticker(ticker)
        data: dict
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            
            table_code = self.__get_history_table(page)
            # print(table_code)
            data = self.__get_last_day_history_table(table_code)
        
        return data
    
    
    def get_today_data_from_tickers(self, tickers: list[str]) -> str:
        urls = [self.__get_history_url_for_ticker(ticker) for ticker in tickers]
        list_data: list[dict] = []
        
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page()
            
            for url in urls:
                page.goto(url)
                table_code = self.__get_history_table(page)
                name = self.__get_ticker_full_name(page)
                data = self.__get_last_day_history_table(table_code)   
                data['name'] = name
                data = self.__parse_history_data_row(data)
                list_data.append(data)
        
        return list_data
    

    def __get_ticker_full_name(self, page: Page) -> str:
        page_title = page.title()
        index = page_title.find(')')
        
        return page_title[0:index+1]
    
    
    def __parse_history_data_row(self, data: dict) -> dict:
        new_data = {}
        for field, ovalue in data.items():
            if field == 'date' or field == 'name':
                new_data[field] = ovalue
                continue
            new_value = ovalue.replace(' ','')
            new_value = new_value.replace(',','')
            new_data[field] = float(new_value)
        
        return new_data
            
if __name__ == '__main__':
    scrapper = YahooScrapper()
    scrapper.get_today_data('^GSPC')
            
            
            
          
        
        
        
        