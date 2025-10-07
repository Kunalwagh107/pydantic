# problem -> type and data validation 

def insert_name(name:str,age:int): # <- type hinting -> but even that it will produce error
    return print(f'{name} and {age} enterted in DB')

insert_name('Kunal','40') # <-- it will still work 
#-----------------------------------------------------
def insert_name(name,age):
    if type(name)==str and type(age)==int:
        if age > 0: # <--- data validation 
            return print(f'{name} and {age} enterted in DB')
    else:
        raise TypeError('Please insert proper type of data')
# insert_name('Kunal','40') # <-- now this will throw error

# This code is not scalable and need to write the same validation in each CRUD command


