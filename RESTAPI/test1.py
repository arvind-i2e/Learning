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

## Function caching in python
from functools import lru_cache
import time
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

### First computation it will store info 
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
## In second for same data it will store result in cache(memo).
print(fx(20))
print("Done for 20")
print(fx(2))
print("Done for 2")
## If we pass new data it will take time because it doesn't stored the new result in cache.
print(fx(51))
print("Done for 51")