s=input("Введите текст")

s=s.split()
x=len(s[0])
for i in s:
    if x>len(i):
        x=len(i)
print(x)