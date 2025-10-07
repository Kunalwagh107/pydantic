from pydantic import BaseModel
from typing import List, Dict #<-- this is for 2 level validation

class Validator(BaseModel):
    name : str
    age : int
    weight : float
    married : bool
    allergies : List[str] # <- complex validation -> list of string
    contact : Dict[str,str] # <-- dict of key:value as string:string

#------------------------------------------------------------------------
raw_data = {
    'name': 'Kunal',
    'age' : 26,
    'weight' : 82.5,
    'married': False,
    'allergies':['Dust','Smoke'],
    'contact' : {
        'email' : 'Kunal.wagh@zohomail.in',
        'contact': '9123445'
    }
}

pyd_model = Validator(**raw_data)

#------------------------------------------------------------------------
def display_values(pyd : Validator):
    return print(pyd)

display_values(pyd_model) 
#------------------------------------------------------------------------


