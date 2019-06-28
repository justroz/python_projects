numbers = [0, 1, 2, 4, 5, 6, 8, 9]

def missing_element():
  check = numbers[0]
  for i in numbers:
    if i == check:
      check += 1
  
  print(check)

missing_element ()