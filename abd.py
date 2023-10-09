# abdullah shahid
# NIM-BSCS-2021-07

"""
in this file i am going to make
a calculator
"""

class Calculator:

    def __init__(self, n1, n2, operation):
        self.n1 = n1
        self.n2 = n2
        self.operation = operation
    def run(self):
        if self.operation == '+':
            return self.sum()
        elif self.operation == '-':
            return self.minus()
        elif self.operation == '*':
            return self.multiply()
        
    def sum(self):
        return self.n1 + self.n2
    
    def minus(self):
        return self.n1 - self.n2
    
    def multiply(self):
        return self.n1 * self.n2
     
    
cal = Calculator(12, 15, '+')
print(cal.run())
