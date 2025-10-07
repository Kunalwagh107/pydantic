from pydantic import BaseModel

# 1. create pydantic class by inheriting from BaseModel --------------------------------------------------------
class Validator(BaseModel): 
    name : str #<-- any instance will match this type
    age : int

raw_data = {
    'name' : 'Kunal',
    'age'  : '30'  # <---smart int conversion 
}

# 2. create object of pydantic class -> if gets created then it's validated -------------------------------------
pydantic_object = Validator(**raw_data) # ** basically unpacks it as name = 'Kunal' and age = 30

# 3. use that model anywhere it is required ---------------------------------------------------------------------
def insert(pyd_obj : Validator):
    return print(f'{pyd_obj.name},{pyd_obj.age}')

insert(pydantic_object)



