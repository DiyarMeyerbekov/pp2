lst=[]
set=set()
tuple=()
i=5
while i>0:
    a=int(input("Numb? "))
    lst.append(a)
    set.add(a)
    i-=1
for i in lst:
    print(i*2)
tuple=set
print(set)
print(tuple)