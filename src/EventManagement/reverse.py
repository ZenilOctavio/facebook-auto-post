from typing import TypeVar

T = TypeVar('T')

def reverse_list(values: list[T]):
  size = len(values)

  if size == 0:
    return
  
  index = size - 1
  del(size)
  
  while index >= 0:
    yield values[index]

def enumerate_reverse_list(values: list[T], skip_tail: int):
  size = len(values)

  if size == 0:
    return
  
  if skip_tail >= size:
    raise Exception(f'No valid value for skiptail ({skip_tail}) with a list lenght of {size}')
  
  index = size - skip_tail - 1
  
  del(skip_tail)
  del(size)
  
  while index >= 0:
    yield (index , values[index])
    index -= 1
  

if __name__ == '__main__':
  values = [1,1,1,1,1,1,2,3]
  for index, value in enumerate_reverse_list(values,3):
    print(index,value)