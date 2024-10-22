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
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Day3: Lets understand some useful concepts and differences

What is the difference between msg[i] and msg.value in the dictionary, say msg?
msg[i]: Accesses a specific value by key in the dictionary.
msg.values(): Returns all values in the dictionary.

What is the difference between extend and append() in list?
append():
Adds a single element to the end of the list.
The element can be of any data type (including another list, which will be added as a single object).

extend(): 
Adds multiple elements to the end of the list.
Takes an iterable (like a list, tuple, or string) and adds each element of that iterable to the list individually

Example
append():

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

my_list.append([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, [5, 6]]

extend():

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list.extend((6, 7))
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7]

my_list.extend(6)
print(my_list)  # Output: TypeError: 'int' object is not iterable

Example from the code:
msg={
    1: "my phonenumber is 9012912012",
    2: "my email id is xyz.com and my phone no is 9012912041 ",
    3: "hey there 321345532",
    4: "890076"
    }

# using append
list=[]
for i in msg:
    list.append(msg[i].split())
print(list) 
# Output: [['my', 'phonenumber', 'is', '9012912012'], ['my', 'email', 'id', 'is', 'xyz.com', 'and', 'my', 'phone', 'no', 'is', '9012912041'], ['hey', 'there', '321345532'], ['890076']]

# using extend
list=[]
for i in msg:
    list.extend(msg[i].split())
print(list)
# Output: ['my', 'phonenumber', 'is', '9012912012', 'my', 'email', 'id', 'is', 'xyz.com', 'and', 'my', 'phone', 'no', 'is', '9012912041', 'hey', 'there', '321345532', '890076']

what is isdigit() in python?
The isdigit() method in Python is a string method that checks if all characters in a string are digits. It returns True if the string contains only digit characters (0-9) and is not empty; otherwise, it returns False

Example
num_str1 = "12345"
num_str2 = "123a5"
num_str3 = ""
num_str4 = " 12345 "
num_str5 = "١٢٣٤٥"  # Arabic digits
print(num_str1.isdigit())  # Output: True
print(num_str2.isdigit())  # Output: False
print(num_str3.isdigit())  # Output: False
print(num_str4.isdigit())  # Output: False
print(num_str5.isdigit())  # Output: True


what is list and dict comprehension?
List comprehension and dictionary comprehension are concise ways to create lists and dictionaries in Python

Syntax:
list comprehension
[expression for item in iterable if condition]

dict comprehension
{key_expression: value_expression for item in iterable if condition}


Example

list comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]

dict comprehension
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

Breakdown of code logic:
phone_list = ['+91' + word for line in msg.values() for word in line.split() if word.isdigit() and len(word)<=10]

1. phone_list=[line for line in msg.values()] #Extracting all values(lines) from dict msg
   print(phone_list) #['my phonenumber is 9012912012', 'my email id is xyz.com and my phone no is 9012912041 ', 'hey there 321345532', '890076']

2. phone_list=[word for line in msg.values() for word in line.split()] #Extracting all words from all lines
   print(phone_list) #['my', 'phonenumber', 'is', '9012912012', 'my', 'email', 'id', 'is', 'xyz.com', 'and', 'my', 'phone', 'no', 'is', '9012912041', 'hey', 'there', '321345532', '890076']

3. phone_list=[word for line in msg.values() for word in line.split() if word.isdigit() and len(word)<=10] # Checking if each word is a digit and word len<=10
   print(phone_list) #['9012912012', '9012912041', '321345532', '890076']

4. phone_list=[word for line in msg.values() for word in line.split() if word.isdigit() and len(word)<=10] # Finally concating +91
   print(phone_list) #['+919012912012', '+919012912041', '+91321345532', '+91890076']

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
