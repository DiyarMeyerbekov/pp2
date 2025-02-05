def prime(list):
        new_list=[]
        for i in list:
            if i<2:
                continue
            isprime=True
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    isprime=False
                    break
            if isprime:
                new_list.append(i)
        print(new_list)
list=[0,1,2,3,4,5,6,7,8,9]
prime(list)