from pydantic import BaseModel,Field
from typing import List, Dict, Optional , Annotated

class Validator(BaseModel):
    name : Annotated[str ,Field(title='Name of Patient',
                       description='This will be added as first name',
                        examples=['Kunal','Wagh'], max_length=50)]
    # Annotated[type,metadata]

    age : Annotated[int,Field(gt=0,strict=True)]  # no smart conversion 

    weight : float = Field(gt=0,lt=120) # greater than 0 and less than 120
    married : Optional[bool] = None   
    allergies : Optional[List[str]] = None 
    contact : Dict[str,str] 


raw_data = {
    'name': 'Kunal',
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


