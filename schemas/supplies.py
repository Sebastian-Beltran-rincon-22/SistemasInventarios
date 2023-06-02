from pydantic import BaseModel, Field
from typing import Optional

class Supplies(BaseModel):
    id : Optional [int] = None
    product_id : int = Field(ge=1)
    supplies_id : int = Field(ge=1)
    purchase_price : float = Field(ge=1)

    class Config:
        schema_extra = {
            "example":{
                'product_id': 1,
                'supplies_id': 1,
                'purchase_price':1,
            }
        }