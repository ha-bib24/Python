'''n = input("enter a text of number : ")
list = n.split()
sum = 0

for num in list :
    sum = sum + int (num)
print(sum) '''

nw = 0
nl = 0
nd = 0

text = input("entyer a text of number : ")
for x in text:
    x = x.lower()
    if x  >= 'a' and x <= 'z':
        nl = nl + 1  

    elif x >= '0' and x <= '9':
        nd = nd +1

    elif x == ' ':
        nw = nw +1

print("numbers of letters :", nl )
print("number of digits :", nd)
print("numbers of words :", nw)