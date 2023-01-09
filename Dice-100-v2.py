import random
#import pandas
result = []
for i in range (1,1001):
    sum = 0
    while sum <= 100:
        sum += random.randint(1,6)
       
    result.append(sum)
print(type(result))
print(type(result[0]))
print(result.count(101), result.count(102), result.count(103))

        
    



