# b = "Hello world!"
# print(b[-5:-2])

# text = "company12"

# x = text.isalpha()
# print(x)

# myDict = ['John','norway']
# myseparator = ""

# x = myseparator.join(myDict)

# txt = 'I could eat bananas all day'
# x = txt.partition('pizza')

# txt = "I like bananas"
# x = txt.replace("bananas", "apples")

# txt = "one one was a race horse, two two was one too."
# x = txt.replace("one", "three")

# txt = "one one was a race horse, two two was one too."
# x = txt.replace("one", "three", 2)

# text = 'apple#banana#cherry#orange'
# x = text.split('#', 1)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")


# thislist = ["apple", "banana", "cherry"]
# # thislist.remove("banana")
# del thislist[0] 
# print(thislist)

thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(f"{i} :{thislist[i]}")

# [print(x) for x in thislist]
# newlist = [x for x in range(10) if x % 2 != 0]
# print(newlist)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# for x in list2:
#     list1.append(x)

list1 += [x for x in list2]

# list1.extend(list2)

# print(list1)

# username = input("Enter username:")
# print("Username is: " + username)

# nums = []
# num = 0
# while(num != 'q'):
#     num = input("Enter a number (or 'q' to quit): ")
#     if num == 'q':
#         break
#     if(num.isdigit()):

#         nums.append(int(num))
#     else:
#         print("only numbers are allowed")


# print([num for num in nums if num % 2 == 0])
# print([num for num in nums if num % 2 != 0])
# print("You entered:", nums)

# list = ["apple", "banana", "orange", "melon", "mango"]

# print(list)
# print(len(list))

# list.append("grape")
# list.remove("banana")
# print(list)

# username = input("Enter username:")
# ages = input("Enter your age:")
# print("Hello: " + username + ", you are " + ages + " years old.")

# text = "Hello World!"

# print(text.lower())
# print(text.upper())
# print(text.count("o"))

# print(f"Hello {username}, you are {ages} years old. end test sentence.{text}")

fruits = ("apple", "banana", "cherry")
# (green, yellow, *red) = fruits
# mytuple = fruits * 2
# print(mytuple)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)

# set1 = {"apple", 1 , "banana",0 , "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# set3 = set1.difference(set2)

# set3 = set1.difference_update(set2)
# print(set3)

# a = 330 
# b = 330
# print('A') if a > b else print('=') if a == b else print('B')

# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("Recursion Example Results:")
# tri_recursion(6)

#q1
# tuple1 = ("kiwi", "banana", "cherry", "apple", "orange")


# # print(tuple1 )
# print(f"second item {tuple1[1]} and last {tuple1[-1]} ")
# xlist = list(tuple1)
# xlist[2] = "grape"
# tuple1 = tuple(xlist)
# print(tuple1)

# #q2
# set1 = {1, 2, 3, 4, 5}
# print(set1)
# set1.add(6)
# set1.remove(3)
# print(set1)

# #q3s

# num = input("Enter a number (or 'q' to quit): ")
# if num.isdigit() and int(num) % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")


# score = input("Enter your score: ")
# if score.isdigit():
#     score = int(score)
#     if score >= 90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     elif score >= 70:
#         grade = 'C'
#     elif score >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
#     print(f"Your grade is: {grade}")


# # q5 
# for i in range(1, 11):
#     print(i)

# result = 0
# #q6
# list = [1, 2, 3, 4, 5]
# for num in list:
#     result += num   
# print(f"Sum is: {result}")

# #q7
# def sum_calc(num1,num2):
#     return num1 + num2

# #q8
# def find_max(args):
#     max_value = args[0]
#     for num in args:
#         if num > max_value:
#             max_value = num
#     return max_value
#     # return max(args)

# print(sum_calc(10,20))
# print(find_max(list))

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# x = car.keys()
# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change

# x = car.items()
# print(x) #before the change

# car["year"] = 2020
# print(x) #after the change

myfamily = {
  "child1": {
    "name": "Kasumi",
    "year": 1983
  },
  "child2": {
    "name": "Kaori",
    "year": 1986
  },
  "child3": {
    "name": "Genki",
    "year": 1990
  } 
}

# print(myfamily["child2"]["name"])

# for x, obj in myfamily.items():
#     print(x)
#     for y in obj:
#         print(y + ": ", obj[y])

# x = ("key1", "key2", "key3")
# y = 0

# thisdict = dict.fromkeys(x, y)

# print(thisdict)

# x = car.get("price", 15000) #if the key doesn't exist, it will return 15000

# print(x)

import os
import filecmp as fc
# print("String format : ", os.getcwd())
# print("Byte string format :", os.getcwdb())

dir_1 = dir_2 = os.getcwd()

#creating object and invoking constuctor
# d = fc.dircmp(dir_1, dir_2, ignore=None, hide=None)

# print("comparison 1 :")

# d.report()

##q1
### r is read mode it supposed to read the file
### w is write mode it will create a new file or overwrite existing file
### a is append mode it will append to the end of the file

##q2
f = open("example.txt", "r")
# print(f.read())

#q3

if os.path.exists("example.txt"):
    r = open("example.txt", "r")
    print(r.read())


##q4 with - it can automatically close the file after the nested block of code
with open("example.txt", "r") as f:
    print(f.read())

###page2 q1
def writeFile(filename, content):
    with open(filename, "w") as f:
        for text in content:
            f.write(text)

writeFile("example.txt", ["Hello World!\n", "This is a test file.\n", "Goodbye!\n"])

###page2 q2
