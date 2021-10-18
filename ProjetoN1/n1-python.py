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

def incluiE_mail():
    endereco=input("Digite o e_mail completo : ")
    while endereco.count('@') == 0:
        endereco=input("e-mail inválido. Digite o e_mail completo : ")
    eMail.append(endereco)
    print("Cadastro realizado")
    time.sleep(2) 
    print("...")  
    time.sleep(2) 
    print("...") 
    return

def imprimirAlfabeto():
    alfabeto=sorted(nomeCompleto)
    
    for i in alfabeto :
        print (i)
    time.sleep(3)
    retornoMenuInicial()

def imprimir():
    for i in nomeCompleto :
        print (i)
    time.sleep(4) 
    print("...")  
    time.sleep(3) 
    print("...")     
    retornoMenuInicial()

def procuraNome ():
    nome=input("Digite o nome que está procurando : ")
    n=-1
    for i in nomeCompleto :
        if nome in i :
            print (i)
            n=1
            time.sleep(5)
            retornoMenuInicial()
    if n==-1 :
        print("Nome não encontrado ")
    return

def remove():
    e_mail=input("Digite o e-mail do usuario que deseja remover : ")
    x=-1
    for i in eMail :
        if e_mail==i :
            x=eMail.index(e_mail)
            eMail.remove(e_mail)
            nomeCompleto.pop(x)
            time.sleep(6)
            print("Foi removido o e-mail {} e usuario ". format(e_mail ))
            time.sleep(5)
    if x==-1 :
        print("Não foi encontrado o e-mail{} ".format(e_mail))
    print (eMail)
    time.sleep(5)
    print (nomeCompleto)
    time.sleep(3)
    retornoMenuInicial()
