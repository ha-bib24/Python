num = [1,2,3,4,5]
r = list(map(lambda x : x*x, num))
print(r)

ex = [1,2,3,4,5]
result = [a*a*a for a in ex]
print(result)


q =[1,2,3,4,5,6,7,8,9]
rsq  = [x for x in q if x%2 !=0]
rs = list(filter(lambda x: x%2 !=0, q))
print(rsq)
