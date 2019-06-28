numbers = [1, 2, 3, 4, 5]
duplicate = []


def duplicate_array():
  counter = 2
  while counter > 0:
    for i in numbers:
      duplicate.append(i)
    counter -= 1
    
  print(duplicate)

duplicate_array()