
#def function2(a , b,c):
     #   """this program is  working now"""
      #  average = (a+b+c)/3
       # print(average)
      #  return average
 #print(function2.__doc__)

#print(v)
# print("enter the number 1")
#
# num1 = int((input()))
# print("enter the number 2")
# num2=int((input()))
# try:
#  print("the sum of these two numbers is",int(num1)+int(num2))
# except Exception as e:
#         print("this is used for making the code to run whethr above ones are not vallied")



#*******handlinf of file in raeding mode*****
#f=open("tut3.py","r")#store the content of tut3.py
#content=f.read()
#for line in content:# this will give letter to letter type  so to have line to line we need to write "for line in f:"
# for line in f:#read() must be coment out to use this
#    print(line,end="")
#print(content)

# print(f.readlines(),end="")#this will give u result of line by line without for looop
# print(f.readline(),end="")
# print(f.readline(),end="")
# print(f.readline(),end="")

# content=f.read(6777)
# print("1",content)
# content=f.read(6777)
# print("2",content)
# f.close()



#****** handle for writing a file*****
#f=open("tut3.py","w")

#f=open("tut3.py","a")
#f.write("we are dealing with files")#
# a=f.write("we are dealing with new files") this is used to return the value of charaters
#f.write("we are also dealing with code")
#print(a) here character wolud be printed
#f.close()
  #### handle file both in read and write mode
# f=open("tut3.py","r+")
# print(f.read())
#
# f.write(" thank you for visiting there")
# f.close()
# f=open("tut3.py")
# print(f.tell())
# print(f.seek(12))
# print(f.readline())
# print(f.tell())
#
# print(f.readline())
#
# print(f.tell())
# f.close()
#   ****** OPENING OF FILE WITH "WITH OPEN"
#syntax
#with open("tut3.py") as f:
   # a=f.readline()
   # print(a)
# p="this is global function"
# l=20#global we cant change value og global varaible
# def funct1(n):
#
#     global l# now value of global has changed
#     l=34 #local
#     #l=l+4 this method cant be use to change gobal variables it will change loval only  to change the value we need another method that is we will write a key word global for taht
#     l=l+10
#     m=12#local
#     print(l,m)
#     print(n,"this is a function")
# funct1("this is me")
#print(l,m) this wll throw an error because m i locally defined and it is  prninting out of func1
#print(l,p)
# x=89
# def srishti1():
#     x=23
#     def srishti2():# here values are notchanged becaue there is no argument outside the function keyword global takes itration out of nested function
#        global x
#        x=45
#     print("before calling srishti1()",x)
#     srishti2()
#     print("after callpng srpshti2",x)
# srishti1()
# print(x)# this will give another value becuse srishti2 made it global
# # this will not print 89 as global variable will changed by srishti2 function

#*******RECURSIONS AND FACTORIal based on logic --n!=n*(n-1)!

# def iterative_factorial(n):# this is iterative process
#     """
#     :param n: integer
#     :return: n* n-1 * n-2 * n-3 ......1
#     """
#     fac = 1
#     for i in range(n):# this means i is from 0 to n+1
#         fac =fac*(i+1)
#     return fac
# def recursive_factorial(n):# this is iterative process
#     """
#     :param n: integer
#     :return: n* n-1 * n-2 * n-3 ......1
 #   """
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*recursive_factorial(n-1)
#
# number=int(input("enter the number"))
# print("factorial using iterative method",iterative_factorial(number))
# print("factorial using recursive method",recursive_factorial(number))
# print(recursive_factorial.__doc__)

 #PROGRAM FOR FIBNACCI SERIES
# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# number=int(input("enter a number"))

#print(fibonacci(number) )
##***LAMBDA METHOD
# def a_first(a):
#     return a[2]#array
#
# a=[[1,14,34],[2,4,4],[5,354,56],[8,4,6],
#    [4,5,0]]
#
# a.sort(key=a_first)
# print(a)






