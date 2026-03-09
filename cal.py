def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
while True:
    choice=int(input("enter the choice 1 to 4"))
    num1=int(input("enter the value 1"))
    num2=int(input("enter the value 2"))
    if choice==1:
        print(add(num1,num2))
    elif choice==2:
        print(mul(num1,num2))
    elif choice==3:
        print(sub(num1,num2))
    elif choice==4:
        print(div(num1,num2))
    else:
        print("exit")
        
               
