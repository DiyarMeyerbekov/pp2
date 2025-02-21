class me:
    def __init__(self):
        self.name=str(input("What is ur name? "))
        self.surname=str(input("What is ur surname? "))
        self.age=int(input("Ur age? "))
    def out(self):
        print(f"{self.name} {self.surname} born in {2025-self.age}")
x=me()
x.out()