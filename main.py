option = int(input("What would you like to do\n1.Check if a number is negative or positive\n2.Check if a number is prime\n3.Check if a number is even or odd\n4.Check if a number is a perfect square\n5.Check if a number is a integer or a float\nType the number of the option you want to do: "))
if option == 1:
  num = int(input("Enter a number: "))
  if num > 0:
    print("The number is positive")
  elif num < 0:
    print("The number is negative")
  else:
    print("The number is 0")
if  option == 2:
  num = int(input("Enter a number: "))
  check = (num ** 2+17)%12
  if check == 6:
    print("it is prime")
  else:
    print("it is not prime")
if option == 3:
  num = int(input("Enter a number: "))
  if num % 2 == 0:
    print("The number is even")
  else:
    print("The number is odd")
if option == 4:
  num = int(input("Enter a number: "))
  if num ** 0.5 == int(num ** 0.5):
    print("The number is a perfect square")
  else:
    print("The number is not a perfect square")
if option == 5:
  num = input("Enter a number: ")
  if num == int(num):
    print("The number is a integer")
  else:
    print("The number is a float")
  