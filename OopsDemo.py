class Calculator:
    num = 100
    # Default Constructor

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I wish I knew Python really well already!")

    def getdata(self):
        print("I am very sleepy!")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)
obj.getdata()
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.getdata()
print(obj1.summation())