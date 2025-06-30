integer_var = 10
float_var = 3.14
complex_var = 2 + 3j
print(f"Integer: {integer_var}, Float: {float_var}, Complex: {complex_var}")
string_var = "Hello, Python!"
print(f"String: {string_var}")
boolean_var = True
print(f"Boolean: {boolean_var}")
list_var = [1, 2, 3, "apple", "banana"]
print(f"List: {list_var}")
tuple_var = (1, 2, 3, "apple", "banana")
print(f"Tuple: {tuple_var}")
set_var = {1, 2, 3, "apple", "banana"}
print(f"Set: {set_var}")
dictionary_var = {"name": "Larry", "age": 21, "city": "Philippines"}
print(f"Dictionary: {dictionary_var}")

import math

x1, y1 = 2, 3
x2, y2 = 10, 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")