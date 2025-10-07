from pydantic import BaseModel,EmailStr,AnyUrl
from typing import List, Dict, Optional

class Validator(BaseModel):
    name : str
    email : EmailStr # <-- custom data type email validation
    linkidin_url : AnyUrl  # <-- custom data type URL 
    age : int
    weight : float
    married : Optional[bool] = None   
    allergies : Optional[List[str]] = None 
    contact : Dict[str,str] 


raw_data = {
    'name': 'Kunal',
    'email' : 'Kunal.wagh@zohomail.in',
    'linkidin_url' : 'http://kunalwagh.com',
    'age' : 26,
    'weight' : 82.5,
    # 'married': False,     # <-- this field will show None
    # 'allergies':['Dust','Smoke'], # <-- this field will show None
    'contact' : {
        'contact': '9123445'
    }
}


pyd_model = Validator(**raw_data)

#------------------------------------------------------------------------
def display_values(pyd : Validator):
    return print(pyd)

display_values(pyd_model) 
#------------------------------------------------------------------------


