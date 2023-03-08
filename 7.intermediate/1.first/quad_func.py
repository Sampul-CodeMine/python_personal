import math

class Quadratic:
    
    def __init__(self, valA, valB, valC):
        self.valA = valA
        self.valB = valB
        self.valC = valC


    def square(self, param):
        return param * param


    def square_root(self, param):
        return math.sqrt(param)


    def find_result(self):

        arg = (self.square(self.valB) - (4 * self.valA * self.valC))
        if arg < 0:
            return 'Invalid Input. No root available'
        else:
            square_val = self.square_root(arg)

        if square_val == 0:
            only_root = (-self.valB) / (2 * self.valA)
            return 'The only root is = %0.2f' % only_root
        elif square_val > 0:
            var_one = -self.valB + square_val
            var_two = -self.valB - square_val
            first_root = var_one / (2 * self.valA)
            second_root = var_two / (2 * self.valA)
            ans = 'First Root = %0.2f and the Second Root = %0.2f' % (first_root, second_root)
            return ans