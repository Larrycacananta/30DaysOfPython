numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_or_zero = [num for num in numbers if num <= 0]
print("Negative or zero numbers:", negative_or_zero)
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print("Flattened list:", flattened)
list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("List of tuples:", list_of_tuples)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[c.upper(), c[:3].upper(), ci.upper()] for country in countries for c, ci in country]
print("Flattened countries:", flattened_countries)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_dicts = [{'country': c.upper(), 'city': ci.upper()} for country in countries for c, ci in country]
print("List of dictionaries:", list_of_dicts)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{first} {last}" for name_list in names for first, last in name_list]
print("Concatenated names:", concatenated_names)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else "Undefined slope (vertical line)"
y_intercept = lambda m, x, y: y - m * x
m = slope(1, 2, 3, 4)
b = y_intercept(m, 1, 2)
print(f"Slope: {m}, Y-intercept: {b}")