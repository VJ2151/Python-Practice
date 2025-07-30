# PATTERN : 1 2 3 4 5 * * * * * 11 12 13 14 15 * * * * *

n=5
loop = 20
count=1

while count<loop:
    for i in range(n):
        if count>loop:
            break
        print(count,end=" ")
        count+=1
    for j in range(n):
        if count>loop:
            break
        print("*",end=" ")
        count+=1
