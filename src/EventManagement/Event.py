from datetime import datetime
from typing import Callable
from EventManagement.errors import EventDateException
import time

class Event:
  
  def __init__ (self, date: datetime, action: Callable):
    if date < datetime.now():
      raise EventDateException('This is an old date')
    
    self.__target_date: datetime = date
    self.__action: Callable = action
  
  @property
  def TargetDate(self) -> datetime:
    return self.__target_date
    
  @TargetDate.setter
  def TargetDate(self, new_date) -> None:    
    self.__target_date = new_date

  @property
  def Action(self) -> Callable:
    return self.__action
  
  @Action.setter
  def Action(self, new_action: Callable) -> None:
    self.__action = new_action

  def seconds_ahead(self):
    return (self.TargetDate - datetime.now()).seconds
  
  def __gt__(self, other_event):
    if isinstance(other_event, Event):
      return self.seconds_ahead() > other_event.seconds_ahead()
    if isinstance(other_event, datetime):
      return self.gt_datetime(other_event)
    else:
      return NotImplemented

  def gt_datetime(self, date: datetime):
    return self.TargetDate > date 
      
  def __lt__(self, other_event):
    if isinstance(other_event, Event):
      return self.seconds_ahead() < other_event.seconds_ahead()
    else:
      return NotImplemented
    
  def __str__(self):
    return f'({self.TargetDate} -> {self.Action.__name__})'

  def __repr__(self):
    return f'({self.TargetDate} -> {self.Action.__name__})'
  
  def wait(self):
    while self.__target_date > datetime.now():
      time.sleep(1)
    
    self.Action()

    return self
    

  