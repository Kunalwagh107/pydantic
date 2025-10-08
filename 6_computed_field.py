from pydantic import BaseModel,Field,EmailStr,computed_field
from typing import List, Dict, Optional , Annotated

class Validator(BaseModel):
    name : str
    email : EmailStr
    age : Annotated[int,Field(gt=0,strict=True)] 
    weight : float = Field(gt=0,lt=120)
    height : float


    @computed_field
    @property
    def bmi_calculation(self) -> float: #perticular as instance and type is float
         bmi = round(self.weight/self.height**2,3)
         return bmi

raw_data = {
    'name': 'Kunal',
    'email':'Kunalwagh@hdfc.com',
    'age' : 61,
    'weight' : 82.5,
    'height' : 2
} 


pyd_model = Validator(**raw_data)

#------------------------------------------------------------------------
def display_values(pyd : Validator):
    return print(pyd)

display_values(pyd_model) 
#------------------------------------------------------------------------


