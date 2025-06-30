print("Hello, World!")

name = "Larry"
print(f"My name is {name}")

age = 21
print(f"{name} is {age} years old.")

x = 10
y = 5
sum_xy = x + y
print(f"The sum of {x} and {y} is: {sum_xy}")

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero!")