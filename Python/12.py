'''#if else statement
age = 20
if age < 18:
    print("You are minor. ")
elif age >= 18 and age < 65 :
    print("You are an adult. ")
else:
    print("You are a senior. ")


#Grading system
score = int(input(85))
if score >= 90:
    print("Grade : A")
elif score >= 70:
    print("geade : B")
elif score >= 60:
    print("geade : C")
elif score >= 50:
    print("grade : D")
elif score >= 40:
    print("Grade : E")
else:
    print("Grade : F")'''


# Check the numbere odd,even , and zero
number = int(input("Enetr the number : "))
if number > 0:
    print("This is positive number ")
elif number < 0:
    print("This is negetive number ")
else:
    print("this is zero")
