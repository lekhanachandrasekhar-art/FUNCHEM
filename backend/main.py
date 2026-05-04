from fastapi import FastAPI, HTTPException
from services.element_service import get_all_elements, get_element, filter_elements
from services.compound_service import generate_compounds
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FUNCHEM API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 🔹 Get periodic table
@app.get("/elements")
def elements(type: str = None):
    if type:
        return filter_elements(type)
    return get_all_elements()


# 🔹 Get single element info
@app.get("/element")
def get_element_info(symbol: str):
    element = get_element(symbol)

    if not element:
        return {"error": "Element not found"}

    return element


# 🔹 Get ALL possible compounds from two elements
@app.get("/compounds")
def compounds(e1: str, e2: str):
    result = generate_compounds(e1, e2)

    if not result["possible_compounds"]:
        return {"message": "No compounds found"}

    return result