from typing import Callable
from datetime import datetime, timedelta
from EventManagement.Event import Event
from EventManagement.RepetitionEvent import RepetitionEvent
from EventManagement.reverse import enumerate_reverse_list
from EventManagement.errors import EventDateException

class EventPoolSync:
  events: list[Event | None] = []
  
  """
    This method inserts a event in the pool and returns the index where it got placed.
  """
  def insert_event(new_event: Event) -> int: 
    list_size: int = len(EventPoolSync.events)

    if list_size == 0:
      EventPoolSync.events.append(new_event)
      return 0
    
    EventPoolSync.events.append(None)    
    # print(f'Start of inserting {EventPoolSync.events}')
    for index, current_event in enumerate_reverse_list(EventPoolSync.events, 1):
      # print(f'Move: (Current: {current_event}) vs (Inserting: {new_event})')    
      if current_event > new_event:
        EventPoolSync.events[index + 1] = current_event 
              
      else:
        EventPoolSync.events[index + 1] = new_event
        return
        
    
    EventPoolSync.events[0] = new_event
    pass
    
  def run() -> None:
    while len(EventPoolSync.events):
      current_event = EventPoolSync.events.pop(0)
      
      new_event = current_event.wait()
      
      if issubclass(new_event.__class__, Event):
        EventPoolSync.insert_event(new_event)
  
  
    
  def event_at(date: datetime):
    def wrapper(function: Callable):
      try:
        new_event = Event(date, function)
        EventPoolSync.insert_event(new_event)
      except EventDateException:
        print(f'The event date is not valid {new_event}')

    return wrapper

  def repeat_event(next_date: datetime, time_interval: timedelta):  
      def repeat_event_creation(function: Callable):

        def wrapper():
          function()
          return next_date + time_interval

        EventPoolSync.insert_event(RepetitionEvent(time_interval, next_date, wrapper))
        
      return repeat_event_creation
    
    
  
if __name__ == '__main__':
  def fun1():
    print('fun1')

  t1 = timedelta(seconds=3)
  
  event1 = Event(datetime.now() + t1, fun1)
  EventPoolSync.insert_event(event1)