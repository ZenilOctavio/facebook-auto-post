from Event import Event
from enum import Enum
from datetime import datetime, timedelta
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
    
    def __init__(self, repetition_days: list[Days] = []):
        repetition_days = [*set(repetition_days)] #Remove repeated elements
        
        self.__repetition_days = self.__sort_days(repetition_days) #Sort days introduced
        print(self.__get_next_position())
        
        print(self.__repetition_days)

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
    
    def __get_next_position(self):
        current_day: datetime = datetime.now().isoweekday()
        next_day: Days = self.__repetition_days[0]
            
        i: int = 1

        while i < len(self.__repetition_days) and current_day >= self.__repetition_days[i].value:
            
            next_day = self.__repetition_days[i]                
            i += 1
        
        if next_day.value == current_day:
            next_day = self.__repetition_days[i]
            
        
        # print(f'Iterations: {i}')
        return next_day
        

if __name__ == "__main__":
    event = DaysEvent([Days.MONDAY, Days.FRIDAY, Days.SATURDAY, Days.SUNDAY, Days.THURSDAY])