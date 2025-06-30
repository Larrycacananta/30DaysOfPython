from collections import Counter
import re

paragraph = '''I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities 
to develop an application what else can you love.'''
words = re.findall(r'\b\w+\b', paragraph.lower())
word_counts = Counter(words)
most_common_word, frequency = word_counts.most_common(1)[0]
print(f"Most frequent word: '{most_common_word}' with {frequency} occurrences")
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
points_int = list(map(int, points))
points_int.sort()
distance = points_int[-1] - points_int[0]
print(f"Particle positions (sorted): {points_int}")
print(f"Distance between the two furthest particles: {distance}")