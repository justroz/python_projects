number = int(input("Enter number: "))

for i in range(2,(number-1)):
  if number % i == 0:
    print("This number is not prime.")
    break
  #else:
   #print("This number is prime.")
    #break