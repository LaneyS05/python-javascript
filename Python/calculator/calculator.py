while True:
    print("select operation to perform:")
    print("+. ADD")
    print("-. SUBTRACT")
    print("*. MULTIPLY")
    print("/. DIVIDE")

    operation = input()

    if operation == "+":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print(" the sum is " + str(int(num1) + int(num2)))

    elif operation == "-":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print(" the difference is " + str(int(num1) - int(num2)))

    elif operation == "*":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print(" the product is " + str(int(num1) * int(num2)))

    elif operation == "/":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print(" the quotient is " + str(int(num1) / int(num2)))

    else:
        print("Invalid Entry")


    again = input("Would you like to go again? y=yes n=no: ")


    if again.lower() == "n":
        print("Thanks for stopping by")
        break
    elif again.lower() != "y":
        print("Invalid input. Please enter 'y' or 'n'.")
