from EventManagement.Event import Event
from datetime import datetime, timedelta
from typing import Callable

class RepetitionEvent(Event):
  
  def __init__(self, time_interval: timedelta, next_date: datetime, action: Callable):
    super().__init__(next_date, action)
    self.time_interval: timedelta = time_interval
  
  def wait(self):
    super().wait()

    self.TargetDate += self.time_interval
    
    return self

  
  
  
  