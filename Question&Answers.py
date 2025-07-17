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
def fibonacci():
    num = int(input("enter number till you want fibonacci series: "))
    a,b = 0,1
    print("Fibonacci Series:", end=' ')
    for i in range(num):
        print(a, end=' ')
        a,b = b, a+b
fibonacci()
