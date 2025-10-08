from pydantic import BaseModel,Field,EmailStr,field_validator
from typing import List, Dict, Optional , Annotated

class Validator(BaseModel):
    name : str
    email : EmailStr
    age : Annotated[int,Field(gt=0,strict=True)] 
    weight : float = Field(gt=0,lt=120)
    contact : Dict[str,str] 

#---- validation -----------------------------------------------------
    @field_validator('email')
    @classmethod
    def email_validator(cls,value): # <- cls is like self and value is value of email
        valid_domains = ['hdfc.com','icici.com']
        if value.split('@')[-1] not in valid_domains:
            # print(f"Please insert valid domains {valid_domains}")
            raise ValueError(f'please insert proper value of mail {valid_domains}')
        else:
            return value
        
#---- transformation  -----------------------------------------------------    
    @field_validator('name',mode='after') # <--- value is getting after type cohersion
    @classmethod
    def capital_name(cls,value):
        return value.upper()
    


raw_data = {
    'name': 'Kunal',
    'email':'Kunalwagh@hdfc.com',
    'age' : 26,
    'weight' : 82.5,
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


