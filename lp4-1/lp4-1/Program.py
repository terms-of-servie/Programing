﻿copies = int(input("Enter # of copies to print: "))
price = 0.0
cost = 0.0

if copies > 0 and copies <= 99 :
    price = 0.30
elif copies > 99 and copies <= 499:
    price = 0.28
elif copies > 499 and copies <= 749:
    price = 0.27
elif copies > 749 and copies <= 1000:
    price = 0.26   
elif copies > 1000:
    price = 0.25  
else:
    print ("Invalid # of copies")
    
cost = copies * price
print ("Price per copy is $" +str(price))
print ("Total cost is" + str (Round(cost,2)))
input()