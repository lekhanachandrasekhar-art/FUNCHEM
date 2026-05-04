from pydantic import BaseModel
from typing import List, Optional

class Element(BaseModel):
    name: str
    symbol: str
    atomic_number: int
    atomic_mass: float
    type: str
    bond_type: List[str]
    applications: List[str]

class Compound(BaseModel):
    name: str
    formula: str
    elements: List[str]
    balanced_equation: str
    reaction_type: str
    bond_type: str
    description: str