# import random
#
# random_number=random.randint(0,5)## it will print integers randomly from 0 to 5
# print(random_number)
# random2 =random.random()*100
# print(random2)
# lst=["star plus","ddtv","aaj tak"]
# content=random.choice(lst)
# print(content)
# import time
#
# seconds =time.time()
# print("no of seconds since epoch",seconds)
# seconds2=45453636.65655
# local_time=time.ctime(seconds2)
# print(local_time,"is local time")
# import time
# print("this sholud be printed immediately")
# time.sleep(5)
#print("coding is good to do","this sholud be printed after 5 seconds")



# *******F'STRING AND STRING FORMATTING
# me="srishti"
# import math
# a1=2
# #a="this is my name %s %s"%(me,a1)
#a=f"this is my name {me}{a1}{math.cos(45)}"#this reduces time and gives good readability

#print(a)

###*ARGS AND **KWARGS
# def new(teacher,*argsme,**kwargsme):## in this order normal, args and kwargs should be written
#     print(taecher)
#     #print( args[0] )
#     for item in argsme:
#         print(item)
#         print("now i will tell the quantity of elements\n")
#         for key,value in kwargsme.items():
#             #print(key,value)
#             print(f" the quantity of {key} is a {value}")##f sting s used
#             #print(type(kwargs))
        #print(type(*args))# this is always in form of tuple
# n=("school","teachers","board","pen","bench ","computer")
# list={"shampoo":5,"oil":3,"comb":1,"soap":4,"towel":1,"sanitizer":3}
# taecher="i am taecher and this should written first in bolth function and prnit() and the elements found in school are: "
# #new(normal,n)
# new(taecher,*n,**list)

#list=["pen","notebook","pencil","charts paper","eraser"]
# i=1
# for item in list:
#     if i%2==0:
#         print(f"bring {item}")
#     i+=1
#
## USING ENUMERATE FUNCTTION
#for index,item in  enumerate(list):
#    if index%2!=0:
#        print(f"bring {item}")

#HOW TO IMPORT FILE OR ANY MODULE
# import sys
# print(sys.path)

# from sklearn.ensemble import RandomForestClassifier
#
# print(RandomForestClassifier())
# import  file
# print(file.a)
#
# file.printjoke("this was funny joke")




















