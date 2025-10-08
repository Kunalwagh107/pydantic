from pydantic import BaseModel,Field,EmailStr,computed_field
from typing import List, Dict, Optional , Annotated

class Address(BaseModel):
    city : str
    state : str
    pincode : str

class Validator(BaseModel):
    name : str
    email : EmailStr
    address : Address #<--- feeding other pydantic class as input
#-----------------------------------------------------------------
raw_address_data = {
    'city' : 'Malegaon',
    'state' : 'Maharashtra',
    'pincode' : '423203'
}
address_model = Address(**raw_address_data)
#-----------------------------------------------------------------
raw_data = {
    'name': 'Kunal',
    'email':'Kunalwagh@hdfc.com',
    'address':address_model
} 
pyd_model = Validator(**raw_data)


temp = pyd_model.model_dump(include=['name']) # will only take name
print(temp)

temp2 = pyd_model.model_dump_json(exclude_unset=True) # <- default not populated
print(temp2)


