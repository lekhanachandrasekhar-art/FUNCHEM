import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "COMPOUND_NAME.csv")

df = pd.read_csv(csv_path)

# Normalize columns
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

def get_compounds(e1, e2):
    e1 = e1.strip()
    e2 = e2.strip()

    results = []
    seen = set()  

    for _, row in df.iterrows():
        el1 = row["element1"]
        el2 = row["element2"]

        if (e1 == el1 and e2 == el2) or (e1 == el2 and e2 == el1):

            formula = row["formula"]

            # skip duplicate
            if formula in seen:
                continue

            seen.add(formula)

            results.append({
                "formula": row["formula"],
                "name": row["name"],
                "bond_type": row["bond_type"],
                "state": row["state"],
                "color": row["color"],
                "uses": row["uses"],
                "description": row["description"]
            })

    return results