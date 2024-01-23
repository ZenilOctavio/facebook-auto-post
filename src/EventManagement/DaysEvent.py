from .Event import Event
from enum import Enum
from datetime import datetime, timedelta, time
from itertools import cycle
from time import sleep

class Days(Enum):
    MONDAY=1
    TUESDAY=2
    WEDNESDAY=3
    THURSDAY=4
    FRIDAY=5
    SATURDAY=6
    SUNDAY=7
    

class DaysEvent(Event):
    
    def __init__(self, repetition_days: list[Days] = [], time: time = time(0,0,0)):
        repetition_days = [*set(repetition_days)] #Remove repeated elements
        
        self.__repetition_days = self.__sort_days(repetition_days) #Sort days introduced
        self.__time_to_execute = time

        next_day = self.__get_next_day_in_list()
        next_datetime = self.__get_next_datetime(next_day)
        print(next_datetime)

    def __sort_days(self, days_list: list[Days]):
        n: int = len(days_list)
        if  n <= 1:
            return days_list

        for i in range(1,n):
            day: Days = days_list[i]
            # print(day)
            j = i - 1

            while j >= 0 and day.value <= days_list[j].value:
                days_list[j+1] = days_list[j]
                j -= 1
            
            days_list[j+1] = day 
        
        return days_list
    

    def __get_current_day(self) -> Days:
        today_isoday: int = datetime.now().isoweekday()
        
        return list(Days)[today_isoday-1]
    
    def __get_next_day_in_list(self):
        print(self.__repetition_days)
        current_day: Days = Days.FRIDAY
        next_day: Days = self.__repetition_days[0]
            
        i: int = 0

        while True:
            if i >= len(self.__repetition_days):
                return self.__repetition_days[0]

            if current_day.value < self.__repetition_days[i].value:
                break
            
            next_day = self.__repetition_days[i]
            i += 1       

        if current_day.value == next_day.value:
            next_day = self.__repetition_days[i]
        
        return next_day
    
    def __get_next_datetime(self, next_day: Days) -> datetime:
        current_iso_calendar = datetime.isocalendar(datetime.now())
        current_day: Days = self.__get_current_day()
        current_week: int = current_iso_calendar[1]
        current_year = current_iso_calendar[0]
        target_week: int = current_week

        next_datetime: datetime
        
        if current_day.value > next_day.value:
            target_week += 1
        
        
        try:
            next_datetime = datetime.fromisocalendar(current_year, current_week, next_day.value)

        except ValueError:
            next_datetime = datetime.fromisocalendar(current_year+1, 1, next_day.value)
        
        next_datetime = next_datetime + timedelta(hours=self.__time_to_execute.hour, 
                                                   minutes=self.__time_to_execute.minute, 
                                                   seconds=self.__time_to_execute.second)        

        return next_datetime
    
    def wait():
        super().wait()
        
        

if __name__ == "__main__":
    event = DaysEvent([Days.MONDAY, Days.TUESDAY, Days.WEDNESDAY, Days.THURSDAY, Days.FRIDAY], time(hour=12))