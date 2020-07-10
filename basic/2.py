lst= [10,2,20,4,5,7]  #sample list

#1.Divisible by 5
#Method 1: Loop
for i in lst:
    if(i%5==0):
        print(i)

#Method 2: List comprehension
print([x for x in lst if x%5==0])

#2. Square of each number
print([x**2 for x in lst])
