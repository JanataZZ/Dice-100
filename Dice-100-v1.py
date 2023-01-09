import random
#import pandas
v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0

for i in range (1,1001):
    sum = 0
    while sum <= 100:
        sum += random.randint(1,6)
    if sum == 101:
        v1 = v1 + 1    
    if sum == 102:
        v2 = v2 + 1    
    if sum == 103:
        v3 = v3 + 1    
    if sum == 104:
        v4 = v4 + 1    
    if sum == 105:
        v5 = v5 + 1    
    if sum == 106:
        v6 = v6 + 1    
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
print(v6)
        
    



