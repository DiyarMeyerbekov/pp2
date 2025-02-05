def palidrom(str):
    for i in range(len(str)//2):
        if str[i]==str[len(str)-i-1]:
            return True
    return False
str=str(input("Write palid... "))
print(palidrom(str))