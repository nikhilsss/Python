a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
c=input("Enter which operator('+','-','*','/',) you want: ")
def add(num1,num2):
    print(num1+num2)
def subtract(num1,num2):
    print(num1-num2)
def multiply(num1,num2):
    print(num1*num2)
def divide(num1,num2):
    print(num1/num2)

if c=='+':
    add(a,b)
elif c=='-':
    subtract(a,b)
elif c=='*':
    multiply(a,b)
elif c=='/':
    divide(a,b)
else:
    print("invalid operator")