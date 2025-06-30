it_companies = {'Facebook', 'Google', 'Microsoft','Apple'}
num_companies =len(it_companies)
length = len (it_companies)
print(f"The number of IT companies in the set is:{num_companies}")
it_companies.add('Twitter')
print(it_companies)
new_companies = {'LinkedIn', 'Snapchat', 'Tiktok'}
it_companies.update(new_companies)
print(it_companies)
it_companies.remove('IBM')
print(it_companies)
it_companies.discard('IBM') 
it_companies.remove('IBM')