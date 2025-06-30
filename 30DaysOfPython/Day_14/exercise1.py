from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(x):
  return x*x

def is_even(x):
  return x%2 == 0

def add(x,y):
  return x+y

squared_numbers = list(map(square, numbers))
even_numbers = list(filter(is_even, numbers))
sum_of_numbers = reduce(add, numbers)

print("Squared Numbers:", squared_numbers)
print("Even Numbers:", even_numbers)
print("Sum of Numbers:", sum_of_numbers)


def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print("Closure Example:", add_five(3))

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

print("\nDecorator Example:")
greet()

print("\nCountries:")
for country in countries:
    print(country)

print("\nNames:")
for name in names:
    print(name)

print("\nNumbers:")
for number in numbers:
    print(number)