# Recently came across this interesting problem set
# Problem: 
# Write a python program to implement the following. Given a pattern and a string. If string matches the pattern return true else return false
# Ex: 
# Pattern – “abba”, String – “dog cat cat dog” will return true. 
# Pattern – “aba”, String – “dog dog cat” will return false.
# Explaination: Here the pattern is a code for the string, a=dog and b=cat hence first example is true and second false

# Naive approach

def getdata(string, pattern):
    # creating a map to store key - value pairs
    code={'a':'dog','b':'cat'}
   
    # Creating a new list str based on the pattern given
    str=[]
    for i in pattern:
        if i in code:
            str.append(code[i])

    # Converting the original string into list 
    str1=string.split()
    # print(str)
    # print(str1)

    # finally comparing both list if they are equal or not, if yes true else false        
    if str==str1:
        print("true")
    else:
        print("false")

# testcases
getdata("dog cat cat dog","abba")  # True
getdata("dog dog cat","aba")       # False
getdata("dog dog dog dog","aaaa")  # True
getdata("dog cat fish bird","abcd")  # false Error it should be true
getdata("dog dog dog dog","abba")  # False 

# ________________________________________________________________________________________________________________________#

# Better approach
# Lets try to make this more dynamic 

def wordPattern(pattern, str_):
    # Splitting the string based on spaces and storing it in words as list
    words = str_.split()
    
    # Early exit if lengths don't match
    if len(pattern) != len(words):
        return False
    
    # Two dictionaries to map pattern to word and word to pattern
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True

	
print(wordPattern("abba", "dog cat cat dog"))  # True
print(wordPattern("aba", "dog dog cat"))       # False
print(wordPattern("abba", "dog cat cat"))  # False
print(wordPattern("aaaa", "dog dog dog dog"))  # True
print(wordPattern("abcd", "dog cat fish bird"))  # True
print(wordPattern("abba", "dog dog dog dog"))  # False 

# Explaination:
# we are using zip as tuples are immutable so we cannot change mapping, if a = dog and b = cat, we connot change this mapping say b = dog