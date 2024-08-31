

async def create_link(text:str):
    link = "https://speller.yandex.net/services/spellservice.json/checkText?text="
    return link+text
