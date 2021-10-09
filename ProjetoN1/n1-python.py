import time 
global nomeCompleto
global eMail

nomeCompleto = ['Tulio felipe', 'João da silva','Maria filomena','Carlos da Silva','Sandra souza']
eMail=['tulio.felipe@hotmail.com','joao.silva@gmail.com', 'mariafilo@globo.com', 'carlos.silva@amazon','sansou@netflix.com.br']

def retornoMenuInicial():
    print("[1]--Retornar ao Menu Inicial")
    print("[2]--Sair")
    resposta = int(input())
    if resposta == 1:
        menu()
    elif resposta == 2:
        exit(0)
    else:
        print("Resposta invalida")
        return resposta


def incluiNome ():
    nome=input("Digite o nome completo : ")
    nomeCompleto.append(nome)
    return
