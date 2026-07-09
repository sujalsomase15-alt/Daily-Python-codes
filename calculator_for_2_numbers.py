def calculator():
    #Display welcome message
    print("\n" + "=+"*50)
    print("      SIMPLE CALCULATOR")
    print("="*50)

    #Get two numbers from the user
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    #Display operation options
    print("\n" + "="*50)
    print("Choose an Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("-"*50)

    #Get user's choice of operation
    choice = input("Enter your choice (1/2/3/4): ")

    #Perform calculation based on choice
    if choice == '1':
        result = num1 + num2
        operator = '+'
        operation = "Addition"

    elif choice == '2':
        result = num1 - num2
        operator = '-'
        operation = "Subtraction"

    elif choice == '3':
        result = num1 * num2
        operator = '*'
        operation = "Multiplication"

    elif choice == '4':
        #check for division by zero
        if num2 == 0:
            print("ERROR: cannot divide by zero.")
            print("!"*50)
            return
        result = num1 / num2
        operator = '/'
        operation = "Division"
    else:
        print("\n" + "!"*50)
        print("ERROR: Invalid choice! Please select 1, 2, 3, or 4.")
        print("!"*50)
        return

    #Display the result in readable format
    print("\n" + "="*50)
    print(f"    {operation} RESULT")
    print("="*50)
    print(f"    {num1} {operator} {num2} = {result}")
    print("="*50)

    #Display detalied breakdown
    print("\nDetailed Calculation:")
    print(f"    First Number: {num1}")
    print(f"    Second Number: {num2}")
    print(f"    Operation: {operation} ({operator})")
    print(f"    Result: {result}")
    print("="*50)


#run the calculator 
calculator()
