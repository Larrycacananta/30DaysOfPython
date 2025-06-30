import json

def count_lines_words(filepath):
    """Counts the number of lines and words in a text file."""
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            words = []
            for line in lines:
                words.extend(line.strip().split())  
            num_words = len(words)
            return num_lines, num_words

    except FileNotFoundError:
        return 0, 0  


def most_spoken_languages(filename, n):
    """Finds the n most spoken languages from a JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            languages = {}
            for country in data:
                for lang in country['languages']:
                    languages[lang] = languages.get(lang, 0) + country['population']

            sorted_languages = sorted(languages.items(), key=lambda item: item[1], reverse=True)
            return sorted_languages[:n]
    except FileNotFoundError:
        return []


def most_populated_countries(filename, n):
    """Finds the n most populated countries from a JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            sorted_countries = sorted(data, key=lambda country: country['population'], reverse=True)
            return sorted_countries[:n]
    except FileNotFoundError:
        return []

files = ['obama_speech.txt', 'michelle_obama_speech.txt', 'donald_speech.txt', 'melina_trump_speech.txt']
data_dir = './data/'

for file in files:
    filepath = data_dir + file
    lines, words = count_lines_words(filepath)
    print(f"File: {file}, Lines: {lines}, Words: {words}")


print(most_spoken_languages(filename='./data/countries_data.json',))
print(most_spoken_languages(filename='./data/countries_data.json',))
print(most_populated_countries(filename='./data/countries_data.json',))
print(most_populated_countries(filename='./data/countries_data.json',))