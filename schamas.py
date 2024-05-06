# definir modelos estruturas no input

"""
MODELO ESPERADO NO BODY
{
"price":12325,
"to_currencuies": ['USD', 'GBP']
}


import re
from pydantic import BaseModel, model_validator, ValidationError
from typing import List

class ConverterInput(BaseModel):
    price: float
    to_currencies: List[str]

    @model_validator
    def validate_to_currencies(cls, to_currencies):
        for currency in to_currencies:
            if not re.match('^[A-Z]{3}$', currency):
                raise ValueError(f'Invalid currency {currency}')
        return {'to_currencies': to_currencies}

class ConvertOutput(BaseModel):
    message: str
    data: List[dict]
"""