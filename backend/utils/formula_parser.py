import re

def extract_elements(formula):
    return re.findall(r'[A-Z][a-z]?', formula)

def is_valid_compound(formula):
    elements = extract_elements(formula)
    return len(set(elements)) >= 2