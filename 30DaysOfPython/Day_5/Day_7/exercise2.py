A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
union_set = A.union(B)
union_set = A | B
print(union_set)
intersection_set = A.intersection(B)
intersection_set = A & B
print(intersection_set)
is_subset = A.issubset(B)
print(is_subset)
are_disjoint = A.isdisjoint(B)
print(are_disjoint)
join_A_B = A.union(B)
join_B_A = B.union(A)
print(join_A_B == join_B_A)
print(join_A_B)
sym_diff = A.symmetric_difference(B)
sym_diff = A ^ B
print(sym_diff)
del A
del B