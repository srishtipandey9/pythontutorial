# n=7
# num2= 20
# #this is my guessing game
# intnum =int(input("enter numbers betwwen 1to50"))
# while n<=7:
#     if intnum>num2 or intnum<num2:
#         print("your number is not matched and try again ")
#         Guess=+1
#
#
#
#         if intnum==num2:
#             print("you have entered correct number and you wins the game ")
#             print("game over")
#         break
#    excerise 4
# pattern print
# input = integer n
# boolean =true /false
# true n=4
# n=no. of rows
# *
# **
# ***
# ****
# false n=4
# ****
# ***
# **
# *
# num1 =int(input("enter the number")) apun
#
# if num1==1:
#     print("true")
#     print("*\n"
#           "**\n"
#           "***\n"
#           "****\n")
# elif num1==0:
#     print("false")
#     print("****\n"
#          "***\n"
#           "**\n"
#           "*\n")
# else:
#     print("you entered wrong number")
### second approach  u tube
# print("how many rows u want")
# n=int(input("enter an integer"))
# print("enter 1 0r 0")
# boolean_var=int(input("1 for true and 0 for false" ))
# if boolean_var == 1:
#         for i in range( 0, n + 1 ):
#
#            print("*"*int(i))

# if boolean_var==0:
#         for i in range( n,0,-1):
#
#             print("*"*int(i))
#         print("*i,i+1",)
# elif n==1:
#         print("false")
#         print("*i+1,i")

#HEALTH MANAGEMENT ECERCISE 5
# 3 clients = rohna, harry,hammad
#make 6 files for food and excercise
#write a function as when excuted it ask client name as input
#one for function to retrieve food for any client

# import datetime
# def getdate():
#   return datetime.datetime.now()
#
#
# def managment(k):
#   print("1 for raina ,2 for harry and 3 for hammad")
#   n=int(input("enter name of client " ))
#   managment(n)
#
#   if n==1:
#     f=open("raina.text.py","r")
#     print(f.read())
#     f.close()
#   elif n==2:
#     f=open("harry.py","r")
#     print(f.read())
#     f.close()
#   else:
#     f=open("hamad.py","r")
#   print(f.read)
#f.close()


# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
  import datetime
  return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


# bhai ye rha program
import datetime

def gettime():
  return datetime.datetime.now()


def take(k):
  if k == 1:
    c = int( input( "enter 1 for excersise and 2 for food" ) )
    if (c == 1):
      value = input( "type here\n" )
      with open( "harry-ex.txt", "a" ) as op:
        op.write( str( [str( gettime() )] ) + ": " + value + "\n" )
      print( "successfully written" )
    elif (c == 2):
      value = input( "type here\n" )
      with open( "harry-food.txt", "a" ) as op:
        op.write( str( [str( gettime() )] ) + ": " + value + "\n" )
      print( "successfully written" )
  elif (k == 2):
    c = int( input( "enter 1 for excersise and 2 for food" ) )
    if (c == 1):
      value = input( "type here\n" )
      with open( "rohan-ex.txt", "a" ) as op:
        op.write( str( [str( gettime() )] ) + ": " + value + "\n" )
      print( "successfully written" )
    elif (c == 2):
      value = input( "type here\n" )
      with open( "rohan-food.txt", "a" ) as op:
        op.write( str( [str( gettime() )] ) + ": " + value + "\n" )
      print( "successfully written" )
  elif (k == 3):
    c = int( input( "enter 1 for excersise and 2 for food" ) )
    if (c == 1):
      value = input( "type here\n" )
      with open( "hammad-ex.txt", "a" ) as op:
        op.write( str( [str( gettime() )] ) + ": " + value + "\n" )
      print( "successfully written" )
    elif (c == 2):
      value = input( "type here\n" )
      with open( "hammad-food.txt", "a" ) as op:
        op.write( str( [str( gettime() )] ) + ": " + value + "\n" )
      print( "successfully written" )
  else:
    print( "plz enter valid input (1(harry),2(rohan),3(hammad)" )


def retrieve(k):
  if k == 1:
    c = int( input( "enter 1 for excersise and 2 for food" ) )
    if (c == 1):
      with open( "harry-ex.txt" ) as op:
        for i in op:
          print( i, end="" )
    elif (c == 2):
      with open( "harry-food.txt" ) as op:
        for i in op:
          print( i, end="" )
  elif (k == 2):
    c = int( input( "enter 1 for excersise and 2 for food" ) )
    if (c == 1):
      with open( "rohan-ex.txt" ) as op:
        for i in op:
          print( i, end="" )
    elif (c == 2):
      with open( "rohan-food.txt" ) as op:
        for i in op:
          print( i, end="" )
  elif (k == 3):
    c = int( input( "enter 1 for excersise and 2 for food" ) )
    if (c == 1):
      with open( "hammad-ex.txt" ) as op:
        for i in op:
          print( i, end="" )
    elif (c == 2):
      with open( "hammad-food.txt" ) as op:
        for i in op:
          print( i, end="" )
  else:
    print( "plz enter valid input (harry,rohan,hammad)" )


print( "health management system: " )
a = int( input( "Press 1 for log the value and 2 for retrieve " ) )

if a == 1:
  b = int( input( "Press 1 for harry 2 for rohan 3 for hammad " ) )
  take( b )
else:
  b = int( input( "Press 1 for harry 2 for rohan 3 for hammad " ) )
  retrieve( b )




















