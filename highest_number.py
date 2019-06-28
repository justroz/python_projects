numbers = [1, 3, 5, 6, 2, 35, 8, 202]

def high_number():
  highest_number = 0
  for i in numbers:
    if i > highest_number:
      highest_number = i
  print (highest_number)


high_number()