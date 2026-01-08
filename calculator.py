print("Simple Calculator")

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

operation = input("Enter operation (+, -, *, /): ")

# Perform calculationpython 
if operation == "+":
    result = num1 + num2
    print("Result:", result)

elif operation == "-":
    result = num1 - num2
    print("Result:", result)

elif operation == "*":
    result = num1 * num2
    print("Result:", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid operation")
