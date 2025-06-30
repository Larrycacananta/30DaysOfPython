from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


upper_countries = list(map(str.upper, countries))
print("Uppercase countries:", upper_countries)

squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

upper_names = list(map(str.upper, names))
print("Uppercase names:", upper_names)

countries_with_land = list(filter(lambda country: 'land' in country, countries))
print("Countries with 'land':", countries_with_land)

six_letter_countries = list(filter(lambda country: len(country) == 6, countries))
print("Countries with six letters:", six_letter_countries)

countries_six_or_more = list(filter(lambda country: len(country) >= 6, countries))
print("Countries with six or more letters:", countries_six_or_more)

countries_starting_with_E = list(filter(lambda country: country.startswith('E'), countries))
print("Countries starting with 'E':", countries_starting_with_E)

chained_result = list(map(str.upper, countries).filter(lambda country: len(country) > 6))

print("Chained result:", chained_result)


def get_string_lists(data):
    return [item for item in data if isinstance(item, str)]

mixed_list = [1, 'hello', 2, 'world', 3]
string_list = get_string_lists(mixed_list)
print("String list:", string_list)

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)

concatenated_countries = reduce(lambda x, y: f"{x}, {y}", countries)
print("Concatenated countries:", f"{concatenated_countries} are north European countries")



def categorize_countries(countries, pattern):
    return [country for country in countries if pattern in country]

countries_with_ia = categorize_countries(countries, 'ia')
print("Countries with 'ia':", countries_with_ia)



def count_starting_letters(countries):
    counts = {}
    for country in countries:
        first_letter = country[0].upper()
        counts[first_letter] = counts.get(first_letter, 0) + 1
    return counts

letter_counts = count_starting_letters(countries)
print("Starting letter counts:", letter_counts)



def get_first_ten_countries(countries):
    return countries[:10]

def get_last_ten_countries(countries):
    return countries[-10:]

first_ten = get_first_ten_countries(countries)
last_ten = get_last_ten_countries(countries) 

print("First ten countries:", first_ten)
print("Last ten countries:", last_ten)