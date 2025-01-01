# healthy=["kale chips","broccoli"]
# backpack=["pizza","nachos","kale chips","apple crisp"]
# print(id(backpack))
# # backpack=[item for item in backpack if item in healthy]# by using this we have created another list rather than changing same one 
# backpack[:]=[item for item in backpack if item in healthy]# this technique will replace item in same list.
# print(id(backpack))
# print(backpack)


#List comprehension
# squares=[i**2 for i in range(10) if i%2==0]
# print(squares)