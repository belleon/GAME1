import numpy as np
a=[]
for i in range(1,20):
    if i != 10:
        for f in str(i):
            a.append(f)

a=np.array(a)
a=a.reshape(3, 9)
print(a)

def sim_hor(x,y):
    num = a[x][y]
    num1=a[x+1][y]
    if num == num1:
        a[x][y]=a[x+1][y]=" "
        return (a)
    return False







x=int(input())
y=int(input())
# print(a[1][1])
print(sim_hor(x,y))
