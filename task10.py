
str1=input("string 1 ")
str2=input("string 2 ")
char=str1[0]
char1=str2[0]
str1=str1.replace(char,char1)
str2=str2.replace(char1,char)
# str1=str1.replace(str1[0],str2[0])
# str2=str2.replace(str2[0],str1[0])
str3=str1+" " + str2
print(str3)










