class SimpleCalculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

calculator = SimpleCalculator()

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("first number: "))
num2 = float(input("second number: "))

if choice == '1':
    print("Result:", calculator.add(num1, num2))
elif choice == '2':
    print("Result:", calculator.subtract(num1, num2))
elif choice == '3':
    print("Result:", calculator.multiply(num1, num2))
elif choice == '4':
    try:
        print("Result:", calculator.divide(num1, num2))
    except ValueError as e:
        print(e)
else:
    print("Invalid choice")
