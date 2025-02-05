def true(list):
    for i in range(len(list)-1):
        if list[i]==0 and list[i-1]==list[i] and list[i+1]==7:
            return True
    return False
list=[1,3,3,0,0,1]
print(true(list))