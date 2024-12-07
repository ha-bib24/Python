num = {1, 2, 3, 4, 5}
num1 = set([4, 5, 6])
num1.add(7)
num1.remove(5)
print(num)
print(8 in num1)
print(9 not in num1)

print(num | num1) # |this is union
print(num & num1)# this is common
print(num - num1) # this is diffrence