"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""


def request_sanitized_number(prompt: str) -> float:
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please input a number.")





def simple_calculator(num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    # Sanitizing the operations

    

    while True:
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
        try:

            result = None

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
            else:
                raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
        
            if result is not None:
                print(f"The result of {operation}ing {num1} and {num2} is: {result}")
                return result

        except ZeroDivisionError:
            print("Cannot divide by zero. Please divide using a different number.")

        except ValueError:
            print("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")


        

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = request_sanitized_number("Enter the first number: ")
    num2 = request_sanitized_number("Enter the second number: ")
    

    # Perform the calculation and display the result
    result = simple_calculator(num1, num2)
    


if __name__ == "__main__":
    main()
