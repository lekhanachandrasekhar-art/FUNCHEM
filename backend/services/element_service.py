from services.data_loader import load_elements

elements = load_elements()

def get_all_elements():
    return elements

def get_element(symbol: str):
    for el in elements:
        if el["symbol"].lower() == symbol.lower():
            return el
    return None

def filter_elements(element_type: str):
    return [el for el in elements if element_type.lower() in str(el["type"]).lower()]