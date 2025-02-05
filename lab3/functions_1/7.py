def true(list):
    for i in range(len(list)-1):
        if list[i]==3 and list[i]==list[i+1]:
            return True
    return False
list=[1,3,3]
print(true(list))