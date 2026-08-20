# gender = input("Enter your gender:")
# country = "France"
# print(gender, "of", country)
# #  Data types
# a = 25 #int
# b = 2.31 #float
# c = "Hello" #str
# d = 'hey' #str
# e = "123456" #str
# f = True  #bool
# g = False #bool
# h = None #NoneType
# i = ""   #str-blank
# j = " "  #str-Empty


# text = 'daicha'
# number = 25

# print(type(text))
# print(type(number))
# print(len(text))
# print(text.upper())
# print(number.bit_length())

# Create 5 variables- each with a different data type: age, height(with decimals), name, are you a studen? something with no value yet then print the values, data types, lenghts of all variables
# age = 21
# height = 5
# name = "Tila"
# p = True
# t = None

# print(age,height,name,p,t)
# print(type(age))
# print(type(height))
# print(type(name))
# print(type(p))
# print(type(t))


# print(len(name))
 
# Types
# name = "Prawjal"
# print(type(name))

# age = 28
# print(type(age))
# print("Your Age is:" + str(age))
# age = age + 5
# age = str(age)
# print(type(age))
# age = age + 5

# Math
password = "123  abc"
print(len(password))

if len(password) < 8:  #len() counts everything even spaces
   print("Your password is too short!")

text = """
Python is easy to learn.
Python is powerful.
Many people love pyhton.
"""
print(text.count("Python"))

# Transformations
# price = "1234,56"
# print(price.replace(",", "."))

# phone = "176-1234-56"
# print(phone.replace("-", "/"))

# price = "$1,299.99"
# print(price.replace("$",  "").replace(",", ""))

phone = "+49 (176) 123-4567"
print(phone.replace("+", "00",) .replace("").replace( "-", ""))
