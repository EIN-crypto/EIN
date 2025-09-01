def calculator():
    print("🧮 Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("⚠️ Invalid choice. Please try again.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("⚠️ Please enter valid numbers!")
        return

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("⚠️ Division by zero is not allowed!")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")

# Run the calculator
calculator()
