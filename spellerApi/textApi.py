import json
from spellerApi.apisend import json_return

async def json_to_text(text:str):
    data = await json_return(text=text)
    data = json.loads(data)
    print(text)
    for i in data:
        text = text.replace(i.get("word"),i.get("s")[0])
    text = text.replace("+"," ")
    return text
