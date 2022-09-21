import string
import random
lst=[chr(n) for n in range(97,123)]
a=[i for i in range (1,27)]
dct=dict(zip(lst,a))
print(dct)
x=input("Введите букву ")
if x in dct:
    print("True")
else:
    print("False")









