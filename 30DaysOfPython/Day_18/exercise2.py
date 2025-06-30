import re
import keyword

def is_valid_variable(name: str) -> bool:
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, name)) and not keyword.iskeyword(name)
print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name')) 
print(is_valid_variable('firstname'))
print(is_valid_variable('for')) 