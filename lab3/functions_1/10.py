def unique(list):
    new_list=[]
    for i in list:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

list=[1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
unique(list)