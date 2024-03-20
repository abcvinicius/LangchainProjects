from fastapi import FastAPI
from langchain import TranslationClient

app = FastAPI()
client = TranslationClient()

@app.post("/translate")
async def translate(text: str):
    translation = await client.translate(text, target_language='pt')
    return {"translation": translation}