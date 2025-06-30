age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print("Length of list:", len(age)) 
print("Length of set:", len(age_set))
if len(age) > len(age_set):
    print("List is bigger because it contains duplicates.")
elif len(age) < len(age_set):
    print("Set is bigger.")
else:
    print("Both are equal in length.")
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.lower().split()
unique_words = set(words)

print("Words:", words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))