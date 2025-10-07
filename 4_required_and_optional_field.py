from pydantic import BaseModel
from typing import List, Dict, Optional

class Validator(BaseModel):
    name : str
    age : int
    weight : float
    married : Optional[bool] = None   #<-- optional field
    allergies : Optional[List[str]] = None    #<-- optional field
    contact : Dict[str,str] 

#------------------------------------------------------------------------
raw_data = {
    'name': 'Kunal',
    'age' : 26,
    'weight' : 82.5,
    # 'married': False,     # <-- this field will show None
    # 'allergies':['Dust','Smoke'], # <-- this field will show None
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


