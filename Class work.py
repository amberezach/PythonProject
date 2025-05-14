class BasicCalculator:
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

    def addition(self):
        return self.firstNumber + self.secondNumber

    def subtraction(self):
        return self.firstNumber - self.secondNumber

    def multiplication(self):
        return self.firstNumber * self.secondNumber

    def division(self):
        if self.secondNumber != 0:
            return self.firstNumber / self.secondNumber
        else:
            return "Division by zero is not allowed."


# Demonstration
calc = BasicCalculator(10, 5)
print("Addition:", calc.addition())
print("Subtraction:", calc.subtraction())
print("Multiplication:", calc.multiplication())
print("Division:", calc.division())


# Function to greet the user
def GreetUser(username):
    print("Hello, " + username + "! Welcome to the Python course.")


# Function call with your name
GreetUser("John")


# Function to calculate the average of three numbers
def CalculateAverage(num1, num2, num3):
    return (num1 + num2 + num3) / 3


# Calling the function with different sets of numbers
average1 = CalculateAverage(10, 20, 30)
print("The average of 10, 20, and 30 is", average1)

# Count Lines in a File
with open('file1.txt', 'r') as file:         # Opens the file in read mode
    count = sum(1 for line in file)          # Iterates through each line, counting as it goes
    print(f'Total number of lines: {count}') # Prints the total count

ItemsInCart = 0


def add_to_cart(items_to_add):
    global ItemsInCart
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")

    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    ItemsInCart += items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsInCart}")


# Example of using the function
try:
    add_to_cart(2)  # Add 2 items
    add_to_cart(-1)  # This should raise an exception
except Exception as e:
    print(e)



# Handle Tuple modification exception with Try Catch
person = ("Rahul", 25, 5.9)
# Print the second element of the tuple
print(f"Age: {person[1]}")

# Attempt to change the name in the tuple (this will raise an error)
try:
    person[0] = "John"  # This will not work
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")