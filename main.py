numbers = [1, 2, 3]

#example of creating a list with list comprehension:
#new_list = [new_item for item in list]  #this uses keywords to help with syntax understanding
new_list = [n + 1 for n in numbers]
print(new_list)

#the below process accomplishes the same as above code.  but does not use list comprehension process
#above is far more succinct.  below resembles more of a C++ methodology
new_list_other_way = []
for n in numbers:
    n = n+1
    new_list_other_way.append(n)
print(new_list_other_way)