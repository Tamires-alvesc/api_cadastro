def ler_cadastro(id):
    with open("cadastros.csv", "r") as arquivo:
        conteudo = arquivo.readlines()

    lista =[]
    for linha in conteudo:
        if not linha:
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
    with open("cadastros.csv", "r") as arquivo:
        conteudo = arquivo.readlines()

        id_atual = len(conteudo)
        id_novo = id_atual + 1
        conteudo_atualizado = []
        conteudo_atualizado.append(id_novo,nome,idade)
    with open("cadastros.csv", "w") as arquivo:
        conteudo = "\n".join(conteudo_atualizado)
        arquivo.write(conteudo)

    return {"mensagem": f"Cadastro da pessoa atualizado"}


    

