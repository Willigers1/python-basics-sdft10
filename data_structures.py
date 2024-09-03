# PYTHON DATA STURUCTURES - LISTS, TUPLES, DICTIONARIES, SETS

# Lists - ordered, mutable, allows duplicate elements
# syntax - list_name = [element1, element2, element3]

# List example 
my_list = [1, 2, 3, 4, 5]
my_list_two = [(1,2,4), 4,7,2]
my_tuples = ((1,2,4), 4,7,2)
print(my_list_two)
print(my_list)

# Accessing elements in a list
# syntax - list_name[index] (index starts from 0)
print(my_list[2]) # 3

# Negative indexing
# syntax - list_name[-index]
print(my_list[-2]) # 4

# Slicing
# syntax - list_name[start_index:end_index] 
# Access a range of elements in a list
print(my_list[1:3]) # [2, 3]

# Change an element in a list
my_list[2] = 10
print(my_list) # [1, 2, 10, 4, 5]

# Add an element to a list in the end 
# syntax - list_name.append(element)
my_list.append(6)
print(my_list) # [1, 2, 10, 4, 5, 6]

#Add an element to a list in the start
# syntax - list_name.insert(index, element)
my_list.insert(0, 100)
print(my_list) # [100, 1, 2, 10, 4, 5, 6]

# Remove an element from a list
# syntax - list_name.remove(element)
my_list.remove(10)
print(my_list) # [100, 1, 2, 4, 5, 6]

# Remove the last element from a list
# syntax - list_name.pop()
my_list.pop()
print(my_list) # [100, 1, 2, 4, 5]

# Remove an element at a specific index
# syntax - list_name.pop(index)
my_list.pop(2)
print(my_list) # [100, 1, 4, 5]


# Tuples - ordered, immutable, allows duplicate elements
# syntax - tuple_name = (element1, element2, element3)

# Tuple example
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Accessing elements in a tuple
# syntax - tuple_name[index] (index starts from 0)
print(my_tuple[2]) # 3

# Negative indexing
# syntax - tuple_name[-index]
print(my_tuple[-2]) # 4

# Slicing
# syntax - tuple_name[start_index:end_index]
# Access a range of elements in a tuple
print(my_tuple[1:3]) # (2, 3)



# Dictionaries - unordered, mutable, indexed, no duplicate elements
# syntax - dict_name = {key1: value1, key2: value2, key3: value3}

# Dictionary example    
my_dict = {"name": "John", "age": 25}
print(my_dict)

# Accessing elements in a dictionary
# syntax - dict_name[key]
print(my_dict["name"]) # John

# Change the value of a key in a dictionary
my_dict["age"] = 30
print(my_dict) # {'name': 'John', 'age': 30}

# Add a new key-value pair to a dictionary
my_dict["city"] = "New York"
print(my_dict) # {'name': 'John', 'age': 30, 'city': 'New York'}

# Remove a key-value pair from a dictionary
# syntax - dict_name.pop(key)
my_dict.pop("age")
print(my_dict) # {'name': 'John', 'city': 'New York'}

# Remove the last key-value pair from a dictionary
# syntax - dict_name.popitem()
my_dict.popitem()
print(my_dict) # {'name': 'John'}

# Remove a key-value pair from a dictionary using del keyword
# syntax - del dict_name[key]
del my_dict["name"]
print(my_dict) # {}

person_one = {"name": "John", "age": 25, "city": "New York"}
person_two = {"name": "Jane", "age": 30}

#merge the two dictionaries
# syntax - dict_name.update(dict_name)
person_one.update(person_two)
print(person_one) # {'name': 'Jane', 'age': 30}

people = {"person1": person_one, "person2": person_two}
print(people) # {'person1': {'name': 'Jane', 'age': 30}, 'person2': {'name': 'Jane', 'age': 30}}
# Sets - unordered, mutable, no duplicate elements


