ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

sorted_ages = sorted(ages)
min_age = min(ages) 
max_age = max(ages) 
print(f"Sorted Ages: {sorted_ages}\nMin: {min_age}, Max: {max_age}")

modified_ages = ages + [min_age, max_age]
print(f"Modified Ages: {modified_ages}")

sorted_modified = sorted(modified_ages)
n = len(sorted_modified)
median = (sorted_modified[n//2 - 1] + sorted_modified[n//2]) / 2
print(f"Median Age: {median}")

average = sum(sorted_modified) / len(sorted_modified)
print(f"Average Age: {average:.2f}") 

age_range = max_age - min_age
print(f"Age Range: {age_range}")  

diff_min = abs(min_age - average)
diff_max = abs(max_age - average)
print(f"|Min - Average|: {diff_min:.2f} > |Max - Average|: {diff_max:.2f}")

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

middle_index = len(countries) // 2
print(f"Middle Country: {countries[middle_index]}")

split_index = (len(countries) + 1) // 2
first_half = countries[:split_index]
second_half = countries[split_index:]
print(f"First Half: {first_half}")
print(f"Second Half: {second_half}")

first_three, *scandic = countries[:3], countries[3:]
print(f"First Three: {first_three}") 
print(f"Scandic Countries: {countries[3:]}")