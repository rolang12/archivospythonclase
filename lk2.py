lst=[0,1]
lst2=[i for i in lst]
i=0
x=0
while i < len(lst):
    if lst2[x]==0:
        lst[i]=0
        i+=1
        if i<=len(lst):
            lst[i]=0
    else:
        lst[i]=lst2[x]
    x+=1
    i+=1
print(lst)