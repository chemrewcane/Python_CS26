print(f"{'='*5}FUNCTION-BASED CALCULATOR{'='*5}")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b=1):
    if b == 0:
        return None
    return a / b

def calculate_average(*scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

while True:
    print("\nChoose an operation: \
    \n1. Addition \
    \n2. Subtraction \
    \n3. Multiplication \
    \n4. Division \
    \n5. Calculate Average \
    \n6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = add(a=num1, b=num2)
        print(f"Result: {result:.2f}")

    elif choice == "2":

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = subtract(num1, num2)
        print(f"Result: {result:.2f}")

    elif choice == "3":

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = multiply(num1, num2)
        print(f"Result: {result:.2f}")

    elif choice == "4":

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = divide(num1, num2)

        if result is None:
            print("Cannot divide by zero.")
        else:
            print(f"Result: {result:.2f}")

    elif choice == "5":

        scores = input("Enter scores (separate it by using space): ")
        scores = [float(score) for score in scores.split()]

        result = calculate_average(*scores)
        print(f"Average: {result:.2f}")

    elif choice == "6":
        print("Come back if you need any help :)")
        break

    else:
        print("Invalid choice. Please try again.")