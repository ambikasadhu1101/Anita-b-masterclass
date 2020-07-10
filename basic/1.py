s=input("Enter a string ")

#Method 1 ---> Using loop
for i in range(len(s)):
    if(i%2==0): #zero based indexing
        print(s[i],end='')

#Method 2--> slicing
print(s[::2])
