from re import match


def calculator (a,b,operator):
    match operator:
       case '+' :
            return a+b
       case '-':
            return a-b
       case '*':
            return a*b
       case '/':
            if b != 0:
                return a/b
            else:
                return "Division by zero is not allowed"
       case _:
            return "Invalid operation"
       
    
a = int(input("enter first number:"))
b = int(input("enter second number:"))