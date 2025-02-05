class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2
square_obj = Square(int(input("length? ")))
print(f"{square_obj.area()}")
# 3
class rectangle(Shape):
    def __init__(self,leng=0,width=0):
        self.leng=int(input("What is the leng? "))
        self.width=int(input("What is the width? "))
    def area(self):
        return self.leng*self.width
obj=rectangle()
print(obj.area())