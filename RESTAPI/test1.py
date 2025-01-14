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
# from functools import lru_cache
# import time
# @lru_cache(maxsize=None)
# def fx(n):
#     time.sleep(5)
#     return n*5

# ### First computation it will store info 
# print(fx(20))
# print("Done for 20")
# print(fx(2))
# print("Done for 2")
# ## In second for same data it will store result in cache(memo).
# print(fx(20))
# print("Done for 20")
# print(fx(2))
# print("Done for 2")
# ## If we pass new data it will take time because it doesn't stored the new result in cache.
# print(fx(51))
# print("Done for 51")

### Exception handling
# try:
#     num=int(input("Enter a number: "))
#     a=[6,4]
#     print(a[num])
# except ValueError:
#     print("Invalid value type")
# except IndexError:
#     print("Invalid Index") 
# try:
#     answer=10/int(input("Enter a number"))
# except ZeroDivisionError as e:
#     print(e)
# except:
#     print("Invalid input")       ## big no-no(use) 

## dictionary      
# test_grades={
#     "Elliot":"B+",
#     "Stanley":"C",
#     "Ryan":"A",
#     3:95.2
# }
# print(test_grades["Elliot"])
# print(test_grades.get("Bob","No student Found"))
# print(test_grades[3])

## Oops Concept
# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def read_book(self):
#         print(f"Reading {self.title} by {self.author}")

# book1=Book("harry potter","JK Rowling")
# book1.title="Half blood prince"
# print(book1.title)
# book1.read_book()    
## Getter & Setters
# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     @property
#     def title(self):
#         print("Getting title")
#         return self._title  ## Underscore signifies that title is private attribute
#     @title.setter
#     def title(self,value):
#         print("Setting title")
#         self._title=value
#     @title.deleter
#     def title(self):
#         del self._title
    
#     def read_book(self):
#         print(f"Reading {self.title} by {self.author}")
    
# book1=Book("harry potter","JK Rowling")
# # book1.title="Half blood prince"
# print(book1.title)
# book1.read_book()

## Inheritance  
                  