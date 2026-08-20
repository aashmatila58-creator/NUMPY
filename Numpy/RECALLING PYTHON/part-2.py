# ALL ABOUT STRING
# data types (Transformations)
# first_name = "Tila"
# last_name = "Chaudhary" #'string' + 'string'(operator) joins(concatinates) two stringsinto one.
# last_name = first_name + " " +last_name
# print(last_name)

# folder = "C:/Users/Baraa"
# file = "report.csv"  #use case-build file paths(build dynamic paths using folder and file variables)
# full_file_path = folder + file
# print(full_file_path)

# Data Transformations(f string)
#f-string(modern, super-easy way to format and build strings "f" stands for "formatted"
# and lets tou easliy put variables and expressions directly inside  string value)
# name = "Prawjal_Shrestha"
# age = 28
# is_student = False
# print("His name is " + name +", He is " + str(age) + " years old, and student status is " + str(is_student) + ".")
# print(f"His name is {name}, He is {age} years old, and student status is{is_student}.")

# print(f"2 + 8 = {2 +8}")
# print(f"{{This is me}}")


# Data Transformation(split()) - split(seperator) {string method , output: list of strings} breaks a string into smaller parts
# stamp = "2004-10-08"
# print(stamp.split("-"))
# another example:-
# csv_file = "1234,Max, USA,1988-06-11,M"
# print(csv_file.split(","))


# Data Transformation(String Repetition)
# 'string' * number {operator, output: string} (repeats the string multiple times)
# print("hi" * 3)
# print("================")  #use case- style your logs [use repeated characters to create clear sections in output]
# print("&" * 8)
# print("$" * 10)


# Data Extraction(Indexing and Slicing)
# Each character has a position number(index) we have positive index and negative index
# positive indexs(start from left to right) and negative indexs(start from the right to the left)
# Indedes & Slicing
# text ="Python"
# Extract the first character
# print(text[0])
# print(text[-6])

# Extract the last character
# print(text[5])
# print(text[-1])
# Extract h
# print(text[3])

# Example of Slicing
# date = "1997-06-07"
# Extract the year
# print(date[0:4])  #Open-ended slicing(if you leave the start empty, Python starts from index 0)
# print(date[:4])
# Extract the month
# print(date[5:7])
# Extract the day
# print(date[8:])
# print(date[-2:])

# Data cleaning[Whitespace cleaning]
# text = "  Airforce".lstrip() #l.strip()[removes spaces from the left side]
# print(text)

# text = "Airforce  ".rstrip() #rstrip()[removes spaces from the right side of a string]
# print(text)

# text = "  Airforce    ".strip()  #strip()[removes spaces from both ends][It removes tabs and multiple spaces]
# print(text)

# How do you check for spaces at the start or end without just looking?
# Use Case-Detect Extra Spaces(Check the length before and after strip() to find unwanted spaces)

# text = "Datascientist    "
# print(len(text))
# print(len(text.strip()))
# print(len(text) - len(text.strip()))

# nr_of_spaces = len(text) - len(text.strip())
# is_clean = len(text) == len(text.strip())
# print("Nr of spaces:", nr_of_spaces)
# print("Is my data clean?", is_clean)

# Case Conversions(part of data cleaning)  #Use Case-Standardize text case(make sure is always in lowercase)
# text = " python PROGRAMMING"
# print(text.lower())
# print(text.upper())  #Use case- clean Data for matching[lowercase all text to prevent case-based mismatches during search of comparison]

# search = "Email".lower()
# data = "email".lower()
# print(search == data) #Best Practicce - Clean Before Search[always trimm spaces and lowercase your data and search term before matching]



# Pyhton advance challenge
# Turn the messy string into a single clean summary with name, role, and age.
# "968-Maria, ( d@t@ Engineer ) ;;  27y  "
# clean the string
# name: maria | role: data engineer | age: 27

# STRING FUNCTION[Searching]
# search
# phone = "+49-176-12345"
# print(phone.startswith("+49"))  #startswith(substring)[checks if the string begins with a specific word]

# email = "tila@gmail.com"
# print(email.endswith("@gmail.com"))  #endswith[checks if the string ends with a specific word]

# 'substring' in 'string'[checks if word exist in the string]
# print("@ in email")

# url = "https://api.company.com/v1/data"
# print("/api" in url)

# find() is  great when combined with other methods to add dynamics
# phone1 = "+48-176-12345"
# phone2 = "48-654-16548"
# phone3 = "0048-654-16548"
# print(phone1[4:])  #or #print(phone1[phone1.find("-")+1:])
# print(phone2[3:]) #find()[returns the starting position of a word in the string]

# print(phone1.find("-"))

# STRING FUNCTION[Validation]
country = "France@"   #isalpha()[checks if the string has only letters]
print(country.isalpha())

phone = "3.19"
print(phone.isnumeric())  # isnumeric()[checks if the string has only numbers]





 




