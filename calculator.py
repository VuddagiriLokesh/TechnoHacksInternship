def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero.")

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1-4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("the sum of two numbers :")
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print("the diff between two numbers :")
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print("the multiplying of two numbers :")
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4': 
            print("the division of two numbers :")
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(str(e))
        break
    else:
        print("Invalid input. Please try again.")
