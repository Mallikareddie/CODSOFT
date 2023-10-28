# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def sub(x, y):
    return x - y

# Function to perform multiplication
def mul(x, y):
    return x * y

# Function to perform division
def div(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

userinput = input("enter the operation:")

if userinput in ("addition", "subtraction", "multiplication", "division"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if userinput == "addition":
            print("Result:", add(num1, num2))
        elif userinput == "subtraction":
            print("Result:", sub(num1, num2))
        elif userinput == "multiplication":
            print("Result:", mul(num1, num2))
        elif userinput == "division":
            print("Result:", div(num1, num2))
else:
        print("Invalid input.")


    