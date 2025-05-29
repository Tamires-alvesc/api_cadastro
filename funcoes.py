def ler_cadastro(id):
    with open("cadastros.csv", "r") as arquivo:
        conteudo = arquivo.readlines()

    lista =[]
    for linha in conteudo:
        if linha.strip() == "":
            continue
        dados = linha.strip().split(",")
        cad = {
            "id": int(dados[0]),
            "nome": dados[1],
            "idade": int(dados[2])
        }
        lista.append(cad)

    for cad in lista:
        if cad["id"] == id:
            return cad
    return None



def inserir_cadastro(nome, idade):
    try:
        with open("cadastros.csv", "r") as arquivo:
            conteudo = arquivo.readlines()
            id_atual = len(conteudo)
            id_novo = id_atual + 1
    except FileNotFoundError:
        id_novo = 1
    
    with open("cadastros.csv", "a") as arquivo:
        linha = f"{id_novo},{nome},{idade}\n"
        arquivo.write(linha)

    return {"mensagem": f"Cadastro da pessoa atualizado"}


    
def modificar_cadastro(id,nome,idade):
    cadastro = ler_cadastro(id)
    if cadastro:
        cadastro["nome"] = nome
        cadastro["idade"] = idade
        with open("cadastros.csv", "r") as arquivo:
            conteudo = arquivo.readlines()
        conteudo = [linha.strip() for linha in conteudo]
        conteudo_atualizado = []
        for linha in conteudo:
            if linha.strip() == "":
                continue
            if linha.startswith(str(id)):
                conteudo_atualizado.append(f"{cadastro['id']},{cadastro['nome']},{cadastro['idade']}")
            else:
                conteudo_atualizado.append(linha)
        with open("cadastros.csv", "w") as arquivo:
            conteudo = "\n".join(conteudo_atualizado)
            arquivo.write(conteudo)

            return{"mensagem": f"Dados do cadastro atualizados com sucesso"}
    else:
        return{"mensagem": "Cadastro não encontrado"}
    

def excluir_cadastro(id):
    cadastro = ler_cadastro(id)
    if cadastro:
        with open("cadastros.csv", "r") as arquivo:
            linhas = arquivo.readlines()        
        conteudo_atualizado = []
        for linha in linhas:
            if linha.strip() == "":
                continue
            partes = linha.strip().split(',')
            if int(partes[0]) != id:
                conteudo_atualizado.append(linha.strip()) 
            
        with open("cadastros.csv", "w") as arquivo:
            conteudo = "\n".join(conteudo_atualizado) + "\n"
            arquivo.write(conteudo)

            return{"mensagem": f"Cadastro id {id} apagado com sucesso"}
    else:
        return{"mensagem": "Cadastro não encontrado"}