import random
lst=[random.randint(-100,100) for i in range(10)]
print(lst)
lst1=[i for i in lst if i %2==0]
lst1.sort()
print(lst1)