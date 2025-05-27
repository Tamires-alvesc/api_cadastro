from fastapi import FastAPI
import uvicorn
from funcoes import ler_cadastro, inserir_cadastro, modificar_cadastro


app = FastAPI()

@app.get("/cadastro/{id}")
def minha_request(id: int):
    cad = ler_cadastro(id)
    if cad:
        return{"mensagem": f"Olá, {cad['nome']}, você tem {cad['idade']} anos!"}
    return{"mensagem": "Cadastro não encontrado"}

@app.get("/novo_cadastro/")
def inserir_novo_cadastro(nome: str,idade: int):
    cad_novo = inserir_cadastro(nome,idade)
    if cad_novo:
        return{"mensagem": f"Inserido o cadastro de {nome}, que tem {idade} anos!"}
    return{"mensagem": "Não foi possível inserir o cadastro"}

@app.get("/alterar_cadastro/{id}")
def modificar_um_cadastro(id: int, nome: str, idade: int):
    resultado = modificar_cadastro(id,nome,idade)
    return resultado

uvicorn.run(
    app = app
)