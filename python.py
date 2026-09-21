def calculator (a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if b!= 0:
            return a/b
        else:
            return "Division by zero is not allowed"
    else:
        return "Invalid operation"

a = int(input("enter first number:"))
b = int(input("enter second number:"))