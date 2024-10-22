# Task 2: Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        if operation == '+':
            print(f"Result: {add(num1, num2)}")
        elif operation == '-':
            print(f"Result: {subtract(num1, num2)}")
        elif operation == '*':
            print(f"Result: {multiply(num1, num2)}")
        elif operation == '/':
            if num2 != 0:
                print(f"Result: {divide(num1, num2)}")
            else:
                print("Error: Cannot divide by zero!")
        else:
            print("Invalid operation. Please try again.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()



