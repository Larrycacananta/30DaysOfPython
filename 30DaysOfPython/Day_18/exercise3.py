import re
from collections import Counter

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text: str) -> str:
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()

def most_frequent_words(text: str, n=3):
    words = text.lower().split()
    counts = Counter(words)
    return counts.most_common(n)
cleaned_text = clean_text(sentence)
print(cleaned_text)
top_words = most_frequent_words(cleaned_text)
print(top_words)