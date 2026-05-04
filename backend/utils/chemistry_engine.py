import re
from math import gcd

VALENCY = {
    # Group 1
    "Li": [1], "Na": [1], "K": [1], "Rb": [1], "Cs": [1],

    # Group 2
    "Be": [2], "Mg": [2], "Ca": [2], "Sr": [2], "Ba": [2],

    # Halogens
    "F": [-1], "Cl": [-1], "Br": [-1], "I": [-1],

    # Oxygen family
    "O": [-1,-2], "S": [-2, 4, 6],

    # Hydrogen
    "H": [1, -1],

    # Nitrogen family
    "N": [-3, 3, 5], "P": [-3, 3, 5],

    # Carbon
    "C": [-4, 4],

    # Transition metals (common ones)
    "Fe": [2, 3],
    "Cu": [1, 2],
    "Zn": [2],
    "Ag": [1],
    "Au": [1, 3],
    "Ni": [2, 3],
    "Co": [2, 3],
    "Cr": [2, 3, 6],
    "Mn": [2, 3, 4, 6, 7],

    # Aluminium
    "Al": [3],
}


# 🔹 Metals list (GLOBAL so all functions can use it)
METALS = [
    "Li","Na","K","Rb","Cs","Fr",
    "Be","Mg","Ca","Sr","Ba","Ra",
    "Al","Fe","Cu","Zn","Ag","Au",
    "Ni","Co","Cr","Mn"
]


# 🔹 Order elements (metal first)
def order_elements(e1, e2):
    if e1 in METALS and e2 not in METALS:
        return e1, e2
    elif e2 in METALS and e1 not in METALS:
        return e2, e1
    return e1, e2

# 🔹 Extract elements
def extract_elements(formula):
    return re.findall(r'[A-Z][a-z]?', formula)

# 🔹 Parse formula → [('Na',1), ('Cl',1)]
def parse_formula(formula):
    parts = re.findall(r'([A-Z][a-z]?)(\d*)', formula)
    return [(el, int(num) if num else 1) for el, num in parts]

# 🔹 Remove known junk compounds
def is_known_invalid(formula):
    return formula in ["HO", "H3O3", "H2O3", "H3O2"]

# 🔹 Basic validation (dataset filter)
def is_valid_compound(formula, e1, e2):
    elements = extract_elements(formula)

    if set(elements) != set([e1, e2]):
        return False

    parts = parse_formula(formula)
    counts = [c for _, c in parts]

    # Reject very large unrealistic numbers
    if max(counts) > 5:
        return False

    return True

# 🔹 Chemical correctness (charge balance)
def is_chemically_valid(formula, e1, e2):
    if is_known_invalid(formula):
        return False

    parts = parse_formula(formula)

    if len(parts) != 2:
        return False

    (el1, n1), (el2, n2) = parts

    if set([el1, el2]) != set([e1, e2]):
        return False

    # Special valid compounds
    special_valid = ["H2O2", "Na2O2", "Mn3O4"]
    if formula in special_valid:
        return True

    states1 = VALENCY.get(el1, [])
    states2 = VALENCY.get(el2, [])

    for v1 in states1:
        for v2 in states2:
            if (v1 * n1 + v2 * n2) == 0:
                return True

    return False

# 🔹 Normalize formula (ClNa → NaCl)
def normalize_formula(formula, e1, e2):
    parts = parse_formula(formula)
    data = {el: count for el, count in parts}

    e1, e2 = order_elements(e1, e2)

    return f"{e1}{data.get(e1,1) if data.get(e1,1)>1 else ''}" + \
           f"{e2}{data.get(e2,1) if data.get(e2,1)>1 else ''}"

# 🔹 Bond type
def get_bond_type(e1, e2):
    if (e1 in METALS and e2 not in METALS) or (e2 in METALS and e1 not in METALS):
        return "Ionic"
    return "Covalent"