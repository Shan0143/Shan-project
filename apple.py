a = int(input("Enter first shan no: "))
b = int(input("Enter second shan no: "))

op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operation")
