person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2] 
    print(f"The middle skill is: {middle_skill}")

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"Has Python skill: {has_python}")

if 'skills' in person:
    skills = person['skills']
    if {'JavaScript', 'React'}.issubset(skills) and len(skills) == 2:
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills) and len(skills) ==3:
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills) and len(skills) == 3:
        print('He is a fullstack developer')
    else:
        print('unknown title')



if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")