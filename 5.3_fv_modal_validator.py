from pydantic import BaseModel,Field,EmailStr,model_validator
from typing import List, Dict, Optional , Annotated

class Validator(BaseModel):
    name : str
    email : EmailStr
    age : Annotated[int,Field(gt=0,strict=True)] 
    weight : float = Field(gt=0,lt=120)
    contact : Dict[str,str] 


    @model_validator(mode='after') # <- mode should be defined or will throw error
    def validate_emergency_contact(cls,model): #<-- whole model as imput
        if model.age > 60 and model.contact['emergency'] is not None:
            return model
        else :
            raise ValueError('Age greater than 60 must have enmergency contact')





raw_data = {
    'name': 'Kunal',
    'email':'Kunalwagh@hdfc.com',
    'age' : 61,
    'weight' : 82.5,
    'contact' : {
        'emergency' : '054534545',
        'contact': '9123445'
    }
}


pyd_model = Validator(**raw_data)

#------------------------------------------------------------------------
def display_values(pyd : Validator):
    return print(pyd)

display_values(pyd_model) 
#------------------------------------------------------------------------


