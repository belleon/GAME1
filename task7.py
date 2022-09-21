import numpy as np
import random
k=int(input("Номер кол-ва рядов"))
n=int(input( "кол-ва столбцов"))
a=np.random.randint(1, 100, (k,n))
print(a)
print (np.flip(a, axis=1))


