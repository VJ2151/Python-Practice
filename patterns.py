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


# GGGGG * GGGGG 
# GGGG * * GGGG 
# GGG * * * GGG 
# GG * * * * GG 
# G * * * * * G 
#  * * * * * *  
# G * * * * * G 
# GG * * * * GG 
# GGG * * * GGG 
# GGGG * * GGGG 
# GGGGG * GGGGG 
# GGGGGG GGGGGG 
for i in range(5):
    print("G"*(5-i),end=" ")
    for stars in range(i+1):
        print("*",end=" ")
    print("G"*(5-i),end=" ")
    print()
    
for i in range(7):
    print("G"*i,end=" ")
    for stars in range(5-i,-1,-1):
        print("*",end=" ")
    print("G"*i,end=" ")
    print()
