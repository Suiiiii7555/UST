def linear_model(a,b,x):
    return (a*x) + b

class Linear_Model():
    def __init__(self, a , b):
          self.a = a
          self.b = b
        
    def compute(self, x):
        output = (self.a * x) + self.b
        return output
    
    def __call__(self, x):
        output = (self.a * x) + self.b
        return output         
    
lm = Linear_Model(2,3)
lm(0)
# output_1 = lm.compute(0)
lm(10)
# output_2 = lm.compute(10)

print("Output 1 :",lm(0))
print("Output 2 :",lm(10))