def calculator():
    print("=" * 40)
    print("       Simple Python Calculator")
    print("=" * 40)

    # Get first number
    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            break
        except ValueError:
            print("  Invalid input. Please enter a valid number.")

    # Get second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("  Invalid input. Please enter a valid number.")

    # Display operation menu
    print("\nSelect an operation:")
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Modulus        (%)")
    print("  6. Exponentiation (**)")

    # Get operation choice
    operations = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "%", "6": "**"}
    while True:
        choice = input("\nEnter your choice (1-6): ").strip()
        if choice in operations:
            operator = operations[choice]
            break
        else:
            print("  Invalid choice. Please enter a number between 1 and 6.")

    # Perform calculation
    print("\n" + "-" * 40)
    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("  Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        elif operator == "%":
            if num2 == 0:
                print("  Error: Modulus by zero is not allowed.")
                return
            result = num1 % num2
        elif operator == "**":
            result = num1 ** num2

        # Format result: show int if whole number, else float
        formatted_result = int(result) if result == int(result) else round(result, 6)
        num1_fmt = int(num1) if num1 == int(num1) else num1
        num2_fmt = int(num2) if num2 == int(num2) else num2

        print(f"  Result: {num1_fmt} {operator} {num2_fmt} = {formatted_result}")

    except OverflowError:
        print("  Error: Result is too large to compute.")

    print("-" * 40)

# Run calculator in a loop
if __name__ == "__main__":
    while True:
        calculator()
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThank you for using the calculator. Goodbye!")
            break
        print()