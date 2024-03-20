from fastapi import FastAPI
from langchain_openai import ChatOpenAI

app = FastAPI()
llm = ChatOpenAI(openai_api_key="...")

@app.get("/")
def home(): 
    return {"message": "Bem-vindo à API de tradução"}

@app.post("/translate")
def translate_text(request: dict):
    text = request.get("text", "") 

    prompt = [
        {"role": "system", "content": "Você é um tradutor de classe mundial."},
        {"role": "user", "content": text}
    ]

    response = llm.invoke(prompt)

    translation = response.content# Acessando a tradução corrigida

    return {"translation": translation}
