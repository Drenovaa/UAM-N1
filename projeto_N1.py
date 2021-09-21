
import random
import time

plays = 0
sala = 1
jogada = 0
LIMIT_PLAYS = 7
cont = 0
def res():
    global plays
    global sala
    global jogada
    print("Voce deseja reiniciar  o game ? ")
    print("[1]- Para Reiniciar ")
    print("[2]- Para Sair")
    rest = int(input())
    if (rest == 1):
        plays = 0
        sala = 1
        jogada = 0
        main()
    else:
        exit(0)


def main():
    
    global cont
    global jogada
    while (plays < LIMIT_PLAYS): 
        print("Você está na sala {} ".format(sala))
        print("Escolha Seu caminho:")
        print("[1]- Caminho Vermelho")
        print("[2]- Caminho Preto")
        jogada = int(input()) 
        if jogada == 1  or jogada==2 :   
                verif()     
        else:
            print("Voce digitou um valor invalido")
            time.sleep(1)

    print("Game Over!") 
    res ()                       
                
  

def verif():
    global sala
    global jogada 
    global plays
    
    if (sala == 8 and jogada == 2):
        print("Voce acabou de entrar em um portal")
        print("Loading")
        time.sleep(2) 
        print("...")  
        time.sleep(2) 
        print("...")  
        sala = random.randrange(1,6)
        sala=sala-jogada 
    sala = sala + jogada
    plays += 1
    
    if (sala == 6):
        print("Você está na sala {}".format(sala))
        print("Voce só pode seguir a esquerda:")
        print("Seguindo para a esquerda")
        time.sleep(2) 
        print("...")  
        time.sleep(2) 
        print("...") 
        time.sleep(2) 
        print("...")  
        sala += 2
    if (sala == 9):      
        print("You Win! ")  
        res()        
    

main()