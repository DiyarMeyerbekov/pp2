def reversed(string:str):
    splitted = string.split()
    splitted.reverse()
    new_string = ""
    for i in splitted:
        new_string +=i
        new_string += " "
    return new_string
text=input("Write  a sentence ")
print(reversed(text))