'''# SOME PROBLEM IF,ELIF ELSE 

#Problem 01:
num = int(input("Enter THE the Number : "))
if num  > 0 :
    print("This Is  Positive Number . ")
elif num < 0 :
    print("This Is Negative Number . ")
else:
    print("This Is Zero. ")


#problem 02 :
random = float(input("Enter The Number :"))
if random % 2 == 0 :
    print("Even")
else:
    print("Odd")


#Problem 03: test............
year = int (input("Enter bThe Year : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"This is leaf year {year}")
else:
    print(f"This is not leaf year {year}")

#Using if_else.........leaf year
year =  int(input("Enter The year : "))
if year % 4 == 0:
    print("leap year")
elif year % 100 != 0:
    print("not leap year")
elif year % 400 == 0:
    print("leap year")
else:
    print("not leap year")'''


#Only if using check leap year
year = int (input("Enter the year : "))
if year % 4 == 0:
    print("leap year")
if year % 100 == 0:
    print("not leap year")
if year % 400 == 0:
    print("leap year")
else:
    print("not leao year")


