family_members = ('Ranial', 'Adonis', 'Vince', 'Nikko', 'Larry', 'Alberto', 'Lilia')
*all_siblings, father, mother = family_members
siblings = tuple(all_siblings)
parents = (father, mother)
print("Siblings:", siblings)
print("Parents:", parents)
fruits = ('Apple', 'Banana')
vegetables = ('Carrot', 'Tomato')
animal_products = ('Milk', 'Eggs')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print("\nFood Stuff List:", food_stuff_lt)

mid = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 0:
    middle_items = food_stuff_tp[mid-1:mid+1]
else:
    middle_items = (food_stuff_tp[mid],)
print("Middle Item(s):", middle_items)

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("\nFirst Three:", first_three) 
print("Last Three:", last_three)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("\n'Estonia' is Nordic:", 'Estonia' in nordic_countries) 
print("'Iceland' is Nordic:", 'Iceland' in nordic_countries) 