str1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(str1)

str2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(str2)

company = "Coding For All"

print(company)

print(len(company)) 

print(company.upper()) 

print(company.lower())  

print(company.capitalize()) 
print(company.title())   
print(company.swapcase())   

first_word = company.split()[0]
print(first_word) 

print(company.find('Coding') != -1)

print(company.index('Coding')) 

print(company.replace('Coding', 'Python'))

sentence = "Python for Everyone"
print(sentence.replace('Everyone', 'All'))

print(company.split())

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print([c.strip() for c in companies.split(',')])

print(company[0]) 

print(len(company) - 1)
print(company[10])

phrase1 = "Python For Everyone"
acronym1 = ''.join(word[0].upper() for word in phrase1.split())
print(acronym1)

phrase2 = "Coding For All"
acronym2 = ''.join(word[0].upper() for word in phrase2.split())
print(acronym2) 

print(company.index('C'))

print(company.index('F'))

string_extended = "Coding For All People"
print(string_extended.rfind('l'))

sentence2 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence2.find('because')) 

print(sentence2.rindex('because')) 

start = sentence2.find('because')
end = sentence2.rindex('because') + len('because')
print(sentence2[start:end]) 

print(sentence2.find('because'))  

print(sentence2[start:end])  

print(company.startswith('Coding'))  

print(company.endswith('coding'))  

str_with_spaces = '   Coding For All      '
print(str_with_spaces.strip())  

var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier()) 
print(var2.isidentifier()) 

libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libs))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 * 6 = {8 ** 6}")