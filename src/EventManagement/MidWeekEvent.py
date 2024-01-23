from .Event import Event
from datetime import datetime, time, timedelta
from .DaysEvent import Days
from typing import Callable
from time import sleep

midWeekDays: list[Days] = [Days.MONDAY, Days.TUESDAY, Days.WEDNESDAY, Days.THURSDAY, Days.FRIDAY]

class MidWeekEvent(Event):
        
    def get_next_iso_day(comparation_time: time) -> Days:
        isoweek_day = datetime.now().date().isoweekday()
        
        
        if isoweek_day >= 5:
            return Days.MONDAY
        else:
            if datetime.now().time() >= comparation_time:
                return midWeekDays[isoweek_day]
            else:
                return midWeekDays[isoweek_day - 1]
            
    def generate_next_datetime(time_to_execute: time) -> datetime:
        next_iso_day: Days = MidWeekEvent.get_next_iso_day(time_to_execute)
        now = datetime.now()
        
        try:
            next_datetime = datetime.fromisocalendar(year=now.year, week=now.isocalendar().week, day=next_iso_day.value)
        except ValueError:
            next_datetime = datetime.fromisocalendar(year=now.year+1, week=1, day=next_iso_day.value)
        
        next_datetime = next_datetime + timedelta(hours=time_to_execute.hour, minutes= time_to_execute.minute, seconds=time_to_execute.second)

        return next_datetime
            
    
    def __init__(self, time_to_execute: time, action: Callable):
        self.__time_to_execute: time = time_to_execute
        self.__target_date = MidWeekEvent.generate_next_datetime(time_to_execute)
        print(self.__target_date)
        print(action)
        
        self.__action = action

    def wait(self):
        while self.__target_date > datetime.now():
            sleep(1)
        self.__action()
        self.__target_date = MidWeekEvent.generate_next_datetime(self.__time_to_execute)

        print(self.__target_date)

        return self

if __name__ == '__main__':
    def something():
        pass
    event = MidWeekEvent(time(hour=15), something)       
    