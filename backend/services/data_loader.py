import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_path = os.path.join(BASE_DIR, "data", "periodic_data.csv")

df = pd.read_csv(csv_path, encoding="latin1")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

def load_elements():
    elements = []

    for _, row in df.iterrows():
        element = {
    "name": row.get("element_name"),
    "symbol": row.get("element_symbol"),
    "atomic_number": row.get("atomic_number"),
    "atomic_mass": row.get("atomic_mass"),
    "oxidation_states": str(row.get("oxidation_states", "")),
    "valency":row.get("valency"),
    "bond_type": ["Ionic", "Covalent"]
}
        elements.append(element)

    return elements