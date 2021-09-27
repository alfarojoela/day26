numbers = [1, 2, 3]

#example of creating a list with list comprehension:
#new_list = [new_item for item in list]  #this uses keywords to help with syntax understanding
new_list = [n + 1 for n in numbers]
#print(new_list)

#the below process accomplishes the same as above code.  but does not use list comprehension process
#above is far more succinct.  below resembles more of a C++ methodology
new_list_other_way = []
for n in numbers:
    n = n+1
    new_list_other_way.append(n)
#print(new_list_other_way)

double_list = [(index*2) for index in range(1,5)]
#print(double_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name_item.upper() for name_item in names if len(name_item) >= 5]
#print(short_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number * number for number in numbers]

#Write your code 👆 above:

#print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:
#result = [new_item for item in list if test]
result = [number for number in numbers if number%2 == 0]

#Write your code 👆 above:

#print(result)



# numbers1 = open(".file1.txt")
#
# numbers1_list = numbers1.readlines()

with open("file1.txt") as numbers1_file:
    numbers1 = numbers1_file.readlines()

with open("file2.txt") as numbers2_file:
    numbers2 = numbers2_file.readlines()


#converts num variables to be added to result list to ints
#second reference to num is iteration of numbers1 list
#if condition checks if num elements in numbers2 list.

#newlist = [newlistitems for items in list1 if items are in list2
result = [int(num) for num in numbers1 if num in numbers2]

# print(result_in_string)
# Write your code above 👆
#print("LIST OF NUMBERS IN COMMON BETWEEN file1 and file2")
#print(result)

#DICTIONARY COMPREHENSION
#new_dict = {new_key:new_value for item in list}
#another way:
##new_dict = {new_key:new_value for (key,value) in dict.items()}
##new_dict = {new_key:new_value for (key,value) in dict.items() if test}


#DICTIONARY PRACTICE
import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# students_scores = {new_key:new_value for item in list_or_tuple_or_range_or_string}
student_scores = {student:random.randint(1, 100) for student in names}

#print(names)
#print(student_scores)

#passed_student = {new_key:new_value for (key, value) in dictionary.items() if test}
passed_students = {student:score for (student, score) in student_scores.items() if score >=60}

#dictionary.items()  #####this appears to get all key values from the dictionary

#print("PASSED STUDENTS:")
#print(passed_students)
#print(student_scores.items())

############
#MORE DICTIONARY EXERCISES
############

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
#TEMPLATE:
# passed_students = {student:score for (student, score) in student_scores.items() if score >=60}

#split up string into list:
sentence_list = list(sentence.split(" "))
#print(sentence_list)

#result = {new_key:new_value for item in list}
#was mostly on track but prior code was
#result = {word:len(word) for word, len(word) in sentence_list}
result = {word:len(word) for word in sentence.split()}
#print(result)
import math
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
def temp_conversion(temp):
    return (temp * 9/5) +32

#passed_student = {new_key:new_value for (key, value) in dictionary.items() if test}
#prior code was in error.  did not use items() method.
weather_f = {day:((temp*(9/5))+32) for (day, temp) in weather_c.items()}


print(weather_f)

#how to iterate over data frame:
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for(key, value) in student_dict.items():
#     print(key)
#     print(value)

import pandas

#create dataframe from dictionary
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through a data frame BUT not using pandas library
for(key, value) in student_data_frame.items():
    print(key)
    print(value)

#loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)


#print(result)

