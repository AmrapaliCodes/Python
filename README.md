# Python
Beginning with python

Day1: Lets understand very useful function in python: zip()

- The zip() function in Python is used to combine elements from two or more iterables (like lists, tuples, etc.) into tuples.
- It "zips" them together, creating pairs (or more, depending on the number of iterables) of corresponding elements from each iterable.
- If the input iterables are of different lengths, zip() stops creating tuples when the shortest iterable is exhausted.

Syntax: zip(*iterables)
*iterables: This can be any number of iterables (lists, tuples, etc.) that you want to zip together.

Example:
1. Two Iterables:

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))

Output: [(1, 'a'), (2, 'b'), (3, 'c')]

2. Different Lengths:

list1 = [1, 2, 3]
list2 = ['a', 'b']

zipped = zip(list1, list2)
print(list(zipped))

Output: [(1, 'a'), (2, 'b')]

3. Multiple Iterables

list1 = [1, 2]
list2 = ['a', 'b']
list3 = ['alpha', 'beta']

zipped = zip(list1, list2, list3)
print(list(zipped))

Output: [(1, 'a', 'alpha'), (2, 'b', 'beta')]

Common Use Case Example:

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

Output: 
Alice scored 85
Bob scored 90
Charlie scored 95

Unzipping: You can also unzip a zipped object using zip(*zipped_object).

Example:
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)

print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')

Day1: why we are using _ after a variable in python?
# single_trailing_underscore_ : used by convention to avoid conflicts with Python keyword
---------------------------------------------------------------------------------------------------------------------------



