marks= [10,100,30,40,99,98,55,43,88,76,74,98,24,95]

#method 1: Loop
for mark in marks:
    if mark > 75:
        print(mark)

#method 2: List comprehension
print([mark for mark in marks if mark > 75])

#method 3: Using filter and lambda

result= list(filter(lambda x: x>75,marks))
print(result)