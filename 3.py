def sq(a):
    return a**2
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old.")
print(sq(2))
obj=person("fi",13)
obj.print()