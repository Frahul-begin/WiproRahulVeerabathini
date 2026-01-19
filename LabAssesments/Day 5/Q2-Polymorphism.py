class Calculator:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        print("Calculator Value:",self.value)

    #operator overloading
    def __add__(self, other):
        return Calculator(self.value + other.value)

class AdvancedCalculator(Calculator):
    def __init__(self, value):
        self.value = value
    #method overriding
    def calculate(self):
        print("AdvancedCalculator value:", self.value * 2)

c1 = Calculator(10)
c2= Calculator(20)

c3 = c1 + c2
c3.calculate()

a1 = AdvancedCalculator(25)
a1.calculate()