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

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)

set1 = {"apple", 1 , "banana",0 , "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)