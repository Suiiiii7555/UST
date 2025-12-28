class Sample:
    x = 0
    def __init__(self):
        self.y = 10

    ## Instance Method
    def change_object(self , new_x , new_y):
        print(self.y)
        self.y = new_y

        print("class :",self.__class__)
        print("Class Attribute x :",self.__class__.x)
        self.__class__.x = new_x

    ## Class Method
    @classmethod
    def change_class(cls):
        print("Class Attribute X :",cls.x)
        cls.x = 200

    ## Static Method
    @staticmethod
    def auxillary_method():
        print("Inside auxillary method")

## THE BELOW 4 LINES ARE CODE FOR CALLING THE INSTANCE METHOD
# print("Class attribute x :",Sample.x)
# obj = Sample()
# obj.change_object(10,20)
# print("Class Attribute X :",Sample.x)
# print("Instance Attribute Y :",obj.y)

## THE BELOW CODES ARE FOR CALLING THE CLASS METHOD
# print("Value of class attribute X before calling of class method :",Sample.x)
# Sample.change_class()
# print("Value of class attribute X after calling of class method :",Sample.x)

## THE BELOW CODES ARE FOR CALLING STATIC METHOD
Sample.auxillary_method()
obj = Sample()
obj.auxillary_method()