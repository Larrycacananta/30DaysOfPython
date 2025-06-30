total_sum = 0
for i in range(101):
    total_sum += i

print(f"The sum of all numbers is {total_sum}.")
sum_evens = 0
sum_odds = 0

for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i

print(f"The sum of all evens is {sum_evens}. And the sum of all odds is {sum_odds}.")