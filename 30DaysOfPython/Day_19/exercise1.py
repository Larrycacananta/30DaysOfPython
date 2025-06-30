import os
import json
import re
from collections import defaultdict, Counter

def count_file_stats(filename):
    """Count lines and words in a text file"""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(re.findall(r'\b\w+\b', line)) for line in lines)
        return {'lines': num_lines, 'words': num_words}

def analyze_speeches():
    """Analyze all speech files in the data directory"""
    speech_files = [
        'obama_speech.txt',
        'michelle_obama_speech.txt',
        'donald_speech.txt',
        'melina_trump_speech.txt'
    ]
    
    for file in speech_files:
        path = os.path.join('data', file)
        if os.path.exists(path):
            stats = count_file_stats(path)
            print(f"\n{file} analysis:")
            print(f"Lines: {stats['lines']}, Words: {stats['words']}")

def most_spoken_languages(filename, top_n=10):
    """Find top N most spoken languages with tie handling"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        language_counts = defaultdict(int)
        
        for country in data:
            for lang in country['languages']:
                language_counts[lang] += 1
                
        sorted_langs = sorted(language_counts.items(), 
                            key=lambda x: (-x[1], x[0]))
        
        if not sorted_langs:
            return []
        
        threshold = sorted_langs[min(top_n, len(sorted_langs))-1][1]
        return [(count, lang) for lang, count in sorted_langs 
               if count >= threshold]

def most_populated_countries(filename, top_n=10):
    """Find top N most populated countries"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        sorted_countries = sorted(data, 
                                key=lambda x: x['population'], 
                                reverse=True)
        return [{'country': c['name'], 'population': c['population']} 
               for c in sorted_countries[:top_n]]

if __name__ == "_main_":
    
    analyze_speeches()

    data_path = os.path.join('data', 'countries_data.json')
    
    print("\nMost spoken languages:")
    print(most_spoken_languages(data_path, 10))
    
    print("\nMost populated countries:")
    print(most_populated_countries(data_path, 10))
