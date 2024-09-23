import json
import os


def criar_produto(nome, preco, quantidade):
    produto_qntd = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }

    if os.path.exists('produtos.json'): #Verificando se o arquivo ja existe
        with open('produtos.json', 'r') as produtos: # se existir, abriremos o arquivo
            lista_produtos = json.load(produtos) #Aqui estamos jogando as informações do json para uma lista
    else:
        lista_produtos = [] #Se o arquivo não existir, criaremos uma lista vazia

    lista_produtos.append(produto_qntd) #adicionamos o dicionario para uma lista de dicionarios

    with open('produtos.json', 'w') as produtos:
        json.dump(lista_produtos, produtos, indent=3) #Jogamos a lsita de dicionarios para o Json


criar_produto('Aveia em flocos', 3.80, 30)
criar_produto('Coca-cola zero', 5.0, 10)