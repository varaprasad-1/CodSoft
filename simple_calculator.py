import os

def clear_screen():
 os.system('cls')
	
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a,b,a / b
    except ZeroDivisionError:
     while b==0:
      print("\nError: Division by zero")
      b= float(input("Enter another denominator value: "))
     return a,b,a/b

def format_number(n):
    return int(n) if n==int(n) else n
def read_number(prompt):
	
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
  
def main():
    
    while True:
        print("="*40)
        print(" "*9,"Welcome to Calculator"," "*9)
        print("="*40)
        num1 = read_number("\nEnter the first number: ")
        num2 = read_number("Enter the second number: ")

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            num1,num2,result = divide(num1, num2)
            operation = '/'
        else:
            print("❌ Invalid choice! Please try again.\n")
            continue

        print(f"\n✅ Result: {format_number(num1)} {operation} {format_number(num2)} = {format_number(result)}")
        print("-" * 40)

        # Ask user if they want to continue
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip(" ").lower()
        if again not in ('yes', 'y'):
            print("\nThank you for using Calculator! 👋")
            break
            
        clear_screen();
# Run the calculator
if __name__ == "__main__":
    main()
