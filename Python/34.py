'''print((lambda a, b : a + b)(2, 3))
a = ((lambda a, b : a -b) (5, 9))
print(a)

sub = ((lambda c, d : c - d)(10, 5))
print(sub)

#map  function......
def sqr(a):
    return a*a
num = [1,2,3,4,5]
result = list(map(sqr,num))
print(result)


from math import*
print(sqrt(25,))


i = 1
while i <=10:
    sqr = i*i
    i += 1
    print(sqr)


for i in range(1,11):
    sqr = i *i
    i +=1
    print(sqr)

def sqr(x):
    return x*x
a = [1,2,3,4,5,6,7,8,9,10]
p = list(map(sqr,a))
print(p)

def qube(s):
    return s*s*s
q = [1, 2, 3, 4, 5]
qq = list(map(qube,q))
print(qq)




#filter function........
num = [1,2,3,4,5]
a = list (filter(lambda x : x%2 ==0,num))
print(a)'''


num1 = [1,2,3,4,5,6,7,8,9]
a = list (filter(lambda x : x%2!=0,num1))
print(a)