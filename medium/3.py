lst1= [1,2,4,2,3,9,7,6,2]
lst2= [1,5,3,2,8,1]

#method 1: Comprehension
print([x for x in lst1 if x in lst2])  #does not work if lists have duplicate elements

#method 2 : Use set
s1=set(lst1)
s2=set(lst2)
print([x for x in s1 if x in s2])

#method 3: Use intersection() method

print(s1.intersection(lst2))

#method 4: use filter method
print(list(filter(lambda x: x in lst2,lst1)))  #does not work with duplicates