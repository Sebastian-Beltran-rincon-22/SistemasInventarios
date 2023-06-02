from pydantic import BaseModel, Field
from typing import Optional


class Supplier (BaseModel):
    id : Optional[int]
    sub_name : str = Field(max_length=40,min_length=2,description="name supplier")
    address : str = Field(max_length=40,min_length=2,description="fitting room address")
    phone : int = Field(ge=5)
    email : str = Field(max_length=40,min_length=2,description="provider email")
    
    class config:
        schemas_extra = {
            "example":{
                "id":1,
                "sub_name":"ramo",
                "address":"nose cual",
                "phone":3053232233,
                "email":"probando@gmail.com"            
            }
        }