list = [3,8,10,4,6,7,1,2,5,9]

for i in range(10):
    a = list[5]
    if(a < list[i]):
        list[5] = list[i-1]
        list[i-1] = a
         

print (list)