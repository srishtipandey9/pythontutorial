var1="hello world"
var2 = 34
var3 = 36.2
var4 = "45"
var5= "67"

#print(var1+var2)this will throw error becuse the var 1 is string and var 2 is an integer
#print(var2+var3)
#print(var1+var4+var5)#this will just print the string as it is it will not provide the result
"""
we have to use type cast to change the data type 
str()
flaot()
int()
"""
print(int(var5)+int(var4))
print(str(var3)+str(var2))
print(type(var5))
"""
#to use or print the string  more than one time multiply that wth desired number to get that"""
print("enter first number")
inpnum1=input()
print("enter second number")
inpnum2=input()
print("the result is:",int(inpnum1)+int(inpnum2))

