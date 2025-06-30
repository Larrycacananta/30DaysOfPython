empty_list = []
print("Empty list:", empty_list)  

my_list = [10, 20, 30, 40, 50, 60, 70]
print("List with more than 5 items:", my_list)

print("Length of my_list:", len(my_list)) 

first_item = my_list[0]
middle_index = len(my_list) // 2
middle_item = my_list[middle_index]
last_item = my_list[-1]
print("First item:", first_item) 
print("Middle item:", middle_item)  
print("Last item:", last_item)

mixed_data_types = ["Larry", 30, 5.9, False, "1234 Elm Street"]
print("Mixed data types list:", mixed_data_types)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print("IT companies:", it_companies)

print("Number of IT companies:", len(it_companies))  

first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print("First company:", first_company)  
print("Middle company:", middle_company) 
print("Last company:", last_company)     

it_companies[3] = "Tesla"  
print("Modified IT companies:", it_companies)

it_companies.append("Netflix")
print("After adding Netflix:", it_companies)

middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "Adobe")
print("After inserting Adobe in the middle:", it_companies)

for i, company in enumerate(it_companies):
    if company != "IBM":
        it_companies[i] = company.upper()
        break
print("After changing one company to uppercase (except IBM):", it_companies)

joined_companies = '#;  '.join(it_companies)
print("Joined companies:", joined_companies)

company_to_check = "GOOGLE"
print(f"Does {company_to_check} exist in the list?", company_to_check in it_companies)

it_companies.sort()
print("Sorted IT companies:", it_companies)

it_companies.reverse()
print("Reversed IT companies:", it_companies)

first_three = it_companies[:3]
print("First 3 companies:", first_three)

last_three = it_companies[-3:]
print("Last 3 companies:", last_three)

length = len(it_companies)
if length % 2 == 0:
    middle_companies = it_companies[length//2 - 1:length//2 + 1]
else:
    middle_companies = [it_companies[length//2]]
print("Middle company/companies:", middle_companies)

removed_first = it_companies.pop(0)
print("Removed first company:", removed_first)
print("List after removing first company:", it_companies)

length = len(it_companies)
if length % 2 == 0:

    mid1 = length//2 - 1
    mid2 = length//2
    removed_middle = it_companies[mid1:mid2+1]
    del it_companies[mid1:mid2+1]
else:

    mid = length//2
    removed_middle = [it_companies[mid]]
    del it_companies[mid]
print("Removed middle company/companies:", removed_middle)
print("List after removing middle company/companies:", it_companies)

removed_last = it_companies.pop()
print("Removed last company:", removed_last)
print("List after removing last company:", it_companies)

it_companies.clear()
print("List after removing all companies:", it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print("Joined front_end and back_end:", joined_list)

full_stack = joined_list.copy()
index_redux = full_stack.index('Redux')
full_stack.insert(index_redux + 1, 'Python')
full_stack.insert(index_redux + 2, 'SQL')
print("Full stack after inserting Python and SQL:", full_stack)