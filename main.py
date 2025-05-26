from fastapi import FastAPI
import uvicorn
from funcoes import ler_cadastro, inserir_cadastro


app = FastAPI()

@app.get("/cadastro/{id}")
def minha_request(id: int):
    cad = ler_cadastro(id)
    if cad:
        return{"mensagem": f"Olá, {cad['nome']}, você tem {cad['idade']}!"}
    return{"mensagem": "Cadastro não encontrado"}

uvicorn.run(
    app = app
)