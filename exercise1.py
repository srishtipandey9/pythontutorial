#d1={"convense":"234","inquesting":"675","joy":"563","verdict":"342"}

#word=input("enter the word\n")
#print(d1[word])
#faulty calculator_design a caulator which take operator and two numbers as input it shuold give correct answersi except following -
#34+45=76,56*3=123,54/6=8

intnum1=int(input("enter the first number"))

intnum2=int(input("enter the second number "))
op=input("select operator{+ - / * %}:")

if op=='+':
    print("the result is:",int(intnum1)+int(intnum2))

    if op=='-':
        print("the result is:", int(intnum1) - int(intnum2))

if op=='/':
    print("the result is:",int(intnum1)/int(intnum2))

elif intnum1==34 and intnum2==45:
    print("the result is 76")
elif intnum1==54 and intnum2==6:

        print( "tje result is:8")





