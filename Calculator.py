def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def calculator():
    print("Select an operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Quit")
    
    while True:
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Exiting the calculator.")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue
            
            if choice == '1':
                print(f"The result of addition: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of subtraction: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of multiplication: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of division: {divide(num1, num2)}")
        else:
            print("Invalid choice. Please select a valid option.")
        
        print() 
        
calculator()
