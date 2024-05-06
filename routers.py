from asyncio import gather #vai executar todas as funções coroutines de uma vez 
from fastapi import APIRouter, Path,Query
from converter import sync_converter, async_converter


from fastapi import Body #


router = APIRouter(prefix='/converter') 





#VERSAO SINCRONA decorator #endpoint
@router.get("/{from_currency}") 
def converter(from_currency: str, to_currencies: str, price: float): 
    to_currencies = to_currencies.split(',')
    result = []

    for currency in to_currencies: 
        response =  sync_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        ) 

        result.append(response)

    return result


# versão assincrona 
@router.get("/async/v2/{from_currency}")
async def async_converter_router(
    from_currency: str = Path(..., max_length=3, regex='^[A-Z]{3}$'),
    to_currencies: str = Query(..., regex='^[A-Z]{3}(,[A-Z]{3})*$'),
    price: float = Query(..., gt=0)
    
):
    to_currencies_list = to_currencies.split(',')  

    coroutines = []

    for currency in to_currencies_list:
        coro = async_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        coroutines.append(coro)

    result = await gather(*coroutines)
    return result
#convertoutput 
