print("Wassup bro")


class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, x, y):
        """Perform addition"""
        return x + y

    def subtract(self, x, y):
        """Perform subtraction"""
        return x - y

    def multiply(self, x, y):
        """Perform multiplication"""
        return x * y

    def divide(self, x, y):
        """Perform division with error handling"""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

    def power(self, x, y):
        """Calculate power"""
        return x ** y

    def square_root(self, x):
        """Calculate square root"""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return x ** 0.5

    def store_memory(self, value):
        """Store value in memory"""
        self.memory = value
        return self.memory

    def recall_memory(self):
        """Recall value from memory"""
        return self.memory

    def clear_memory(self):
        """Clear memory"""
        self.memory = 0
        return self.memory


def main():
    calc = Calculator()

    while True:
        print("\n--- Python Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Memory Store")
        print("8. Memory Recall")
        print("9. Memory Clear")
        print("0. Exit")

        choice = input("Enter your choice (0-9): ")

        try:
            if choice == '0':
                print("Exiting calculator. Goodbye!")
                break

            if choice in ['1', '2', '3', '4', '5']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))

                if choice == '1':
                    result = calc.add(x, y)
                    print(f"{x} + {y} = {result}")
                elif choice == '2':
                    result = calc.subtract(x, y)
                    print(f"{x} - {y} = {result}")
                elif choice == '3':
                    result = calc.multiply(x, y)
                    print(f"{x} * {y} = {result}")
                elif choice == '4':
                    result = calc.divide(x, y)
                    print(f"{x} / {y} = {result}")
                elif choice == '5':
                    result = calc.power(x, y)
                    print(f"{x} ^ {y} = {result}")

            elif choice == '6':
                x = float(input("Enter number: "))
                result = calc.square_root(x)
                print(f"√{x} = {result}")

            elif choice == '7':
                value = float(input("Enter value to store in memory: "))
                calc.store_memory(value)
                print(f"Stored {value} in memory")

            elif choice == '8':
                memory_value = calc.recall_memory()
                print(f"Memory value: {memory_value}")

            elif choice == '9':
                calc.clear_memory()
                print("Memory cleared")

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()