
class ComplexNumber: 
    def __init__(self, real, imaginary):
        self.number = [real, imaginary]

    def multiply_real(self, num):
        self.number[0] *= num 
        self.number[1] *= num 

    
