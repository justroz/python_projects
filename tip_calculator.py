def tip_calculator():
  tip = meal_price * (tip_percent/100)
  print(f"Your tip is {tip}.")

meal_price = float(input("Enter meal cost: "))
tip_percent = float(input("Enter tip percent: "))

tip_calculator()