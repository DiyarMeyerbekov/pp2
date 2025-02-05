class String:
    def __init__(self):
        self.newstr = ""
    def get_string(self):
        self.newstr = input("Write a string: ")
    def upper(self):
        print(self.newstr.upper())
p1 = String()
p1.get_string()
p1.upper()
