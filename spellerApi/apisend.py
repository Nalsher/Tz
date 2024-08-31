import requests
from spellerApi.create_link import create_link

async def json_return(text:str):
    link = await create_link(text)
    request = requests.get(url=link)
    return request.text