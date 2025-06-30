dog = {}
dog = dict()
print(dog)
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
print(dog)
student = {
    'first_name': 'Larry',
    'last_name': 'Cacananta',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'Philippines',
    'city': 'Manila',
    'address': 'Sta Rita East'
}
print(student)
length = len(student)
print(length) 
skills = student.get('skills')
print(skills)
print(type(skills))

student['skills'].append('Machine Learning')
student['skills'].extend(['Communication', 'Problem Solving'])

print(student['skills'])
keys_list = list(student.keys())
print(keys_list)
del dog