'''def student(id, name):
    print(id, name)

student(101, "habib")'''

def student(*details):
    print(details)

student("rool = 101", "name = habib","cgpa = 3.9")

def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(10, 10)


#XXARGS
def student(**details):
    print(details)

student(id = 101, name = "habib", rool = 224)