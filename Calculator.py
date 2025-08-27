def calculator():
    print("Simple Calculator (type 'exit' or 'q' anytime to quit)\n")

    while True:
        print("Operations:")
        print(" 1) Add")
        print(" 2) Subtract")
        print(" 3) Multiply")
        print(" 4) Divide")
        print(" 5) Exit")

        choice = input("Choose (1/2/3/4/5): ").strip().lower()

        if choice in ('5', 'exit', 'quit', 'q'):
            print("Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice — please pick 1, 2, 3, 4 or 5.\n")
            continue

        # read numbers with validation
        def read_number(prompt):
            while True:
                s = input(prompt).strip()
                if s.lower() in ('exit', 'quit', 'q'):
                    return None
                try:
                    return float(s)
                except ValueError:
                    print("That's not a valid number. Try again or type 'q' to quit.")

        num1 = read_number("Enter first number: ")
        if num1 is None:
            print("Exiting...")
            break
        num2 = read_number("Enter second number: ")
        if num2 is None:
            print("Exiting...")
            break

        # perform operation
        try:
            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                result = num1 / num2  # may raise ZeroDivisionError
            print(f"Result: {result}\n")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.\n")
        except Exception as e:
            print("Unexpected error:", e, "\n")


if __name__ == "__main__":
    try:
        calculator()
    except KeyboardInterrupt:
        print("\nInterrupted. Bye!")
