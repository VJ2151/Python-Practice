#Converting an Integer into Decimals
# import decimal
# num = input("Enter any number: ")
# new=decimal.Decimal(num)
# print(type(new))

# Reverse each word in the input string
# text = input("Enter any text: ")
# words = text.split()
# reversed_text = [word[::-1] for word in words]
# print(" ".join(reversed_text))

#  Counting Vowels in a Given Word:
# vowels = ['a','e','i','o','u']
# text = input("Enter any word: ")
# count= 0
# for ch in text:
#     if ch in vowels:
#         count += 1
#     else:
#         pass
# print("Total count of vowels present in word : ",count)

# Counting the Number of Occurrences of a Character in a String
# text = input("Enter any string: ")
# ch = 'e'
# occurence = 0
# for i in text:
#     if i.lower() == ch.lower():
#         occurence += 1
# print(occurence)

# Writing Fibonacci Series:   0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# def fibonacci():
#     a,b = 0,1
#     num = int(input("enter any no. : "))
#     for i in range(num):
#         print(a,end=" ")
#         a,b = b, a+b
# fibonacci()


# Finding the Maximum Number in a List:
# list1 = input("Enter items in a list: ").split()
# biggest = 0
# for i in list1:
#     if (int(i) > biggest):
#         biggest = int(i)
# print(biggest)

# Finding the minimum Number in a List:
# list1 = input("Enter items in a list: ").split()
# smallest = 100
# for i in list1:
#     if (int(i) < smallest):
#         biggest = int(i)
# print(smallest)

# Finding the 2nd maximum Number in a List:
# list1 = input("Enter items in a list: ").split()
# biggest = int(list1[0])
# second_biggest = int(list1[1])
# if (second_biggest > biggest):
#     biggest, second_biggest = second_biggest, biggest
# else:
#     pass
# for i in list1[2:]:
#     num = int(i)
#     if num > biggest:
#         second_biggest = biggest
#         biggest = num
#     elif num > second_biggest:
#         second_biggest = num
# print("biggest : ",biggest)
# print("second_biggest : ",second_biggest)

# Finding the Middle Element in a List:
# list1 = input("Enter items for a list separated by spaces: ").split()
# n = len(list1)

# if n % 2 == 1:
#     print("Middle element:", list1[n // 2])
# else:
#     print("Middle elements:", list1[(n // 2) - 1], "and", list1[n // 2])

# Converting a List into a String:
# list1 = ['Hello,', 'My', 'Name', 'is', 'vijay', 'Rajage']
# str = ' '.join(list1)
# print(str)

# Adding Two List Elements Together:
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6] 
# added_list =[]
# for i in range(0,len(lst1)):
#         add = lst1[i]+lst2[i]
#         added_list.append(add)
# print(added_list)

# Comparing Two Strings for Anagrams:
# str1 = "Listen"
# str2 = "Silent"
# if sorted(str1.upper()) == sorted(str2.upper()):
#     print("anagrams")
# else:
#     print("not anagrams")

# Palindrome(A palindrome is a word, number, phrase, or sequence that reads the same backward as forward.):
# str1 = "Kayak".lower()
# str2 = "kayak".lower()
# if str1[::-1]==str2:
#     print("palindrome")
# else:
#     print("not palindrome")

# Counting the White Spaces in a String
# string = "P r ogramm in g "
# print(string.count(' '))

# Removing All Whitespace in a String:
# string = "C O D E"
# str=string.split()
# print(''.join(str))

# Building a Pyramid in Python:
# rows = 6
# for i in range(rows):
#     print("_" * (rows - i - 1), end="")           # Print spaces 
#     print("*" * (2 * i + 1))                      # Print stars

# FACTORIAL
# num = int(input("enter a n0. to find it's factorial: "))
# def fact(num):
#     if num < 0:
#         return "please provide a positive number"
#     elif num == 0:
#         return 1
#     else:
#         return num * fact(num-1)
# print(fact(num))

# Find the First Non-Repeating Character
# ch = input("enter any word: ")
# for i in ch:
#     if ch.count(i) == 1:
#         print (i,"is the first non repeating character")
#         break
# else:
#     print("no")






























