from services.compound_data_service import get_compounds

def generate_compounds(e1, e2):
    e1 = e1.strip()
    e2 = e2.strip()

    print("🔥 FUNCTION RUNNING:", e1, e2)

    results = get_compounds(e1, e2)

    print("DATASET RESULT:", results)

    if not results:
        return {"message": "No compounds found"}

    return {
        "elements": [e1, e2],
        "possible_compounds": results
    }