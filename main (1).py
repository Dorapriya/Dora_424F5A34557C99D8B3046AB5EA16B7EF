year=int(input("Enter the year to be checked:"))
if (year % 4 == 0 and year % 100 != 9 or year % 400 == 0):
  print("The year is a leap year!")
else:
  print("The  year isn't a leap year!")