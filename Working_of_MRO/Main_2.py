class A:
    def __init__(self):
        self.x = 10

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 20

class C(A):
    def __init__(self):
        super().__init__()
        self.y = 30

# class D(B,C):
#     def __init__(self):
#         super().__init__()

class D(C,B):
    def __init__(self):
        super().__init__()

d1 = D()
print("When D(C,B) is the class being called the values of x and y are as follows")
print(d1.x,"\n",d1.y)