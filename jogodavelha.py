import os
import time
def Jogador(jogador):
    if jogador == "X":
        return "O"
    else:
        return "X"

def ganhador(tabuleiro,jogador):
    c = 0
    for i in range(len(tabuleiro)):
        c+= tabuleiro[i].count("_") 
        if tabuleiro[i].count("X") == 3 or tabuleiro[i].count("O") == 3 :
            print(f"(/◕ヮ◕)/ JOGADOR '{jogador}' é o GANHADOR! (/◕ヮ◕)/")
            time.sleep(5)
            return False
       
        if tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i]!= '_' and tabuleiro[1][i] == tabuleiro[2][i]:
            print(f"(/◕ヮ◕)/ JOGADOR '{jogador}' é o GANHADOR! (/◕ヮ◕)/")
            time.sleep(5)
            return False

        if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1]!= '_' and tabuleiro[1][1] == tabuleiro[2][2]:
            print(f"(/◕ヮ◕)/ JOGADOR '{jogador}' é o GANHADOR! (/◕ヮ◕)/")
            time.sleep(5)
            return False

        if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1]!= '_' and tabuleiro[1][1] == tabuleiro[2][0]:
            print(f"(/◕ヮ◕)/ JOGADOR '{jogador}' é o GANHADOR! (/◕ヮ◕)/")
            time.sleep(5)
            return False
 
    if c == 0:
    	print("Velha ")
    	time.sleep(5)
    	return False
    return True

def posicao(tabuleiro,jogador,row,column):
    if tabuleiro[row][column] == "_":
        tabuleiro[row][column] = jogador
        return tabuleiro, True
    else:
        return tabuleiro, False

tabuleiro = [["_"]*3 for i in range(3)]
jogador = "X"
Finalizar = True
while Finalizar:
    print(f"Jogador {jogador}")
    for i in tabuleiro:
        print(i)
    if Finalizar == False:
        break
    row = int(input("Linha: "))
    column = int(input("Coluna: "))
    tabuleiro, *res = posicao(tabuleiro,jogador,row,column)
    Finalizar = ganhador(tabuleiro,jogador)
    if res[0] == True:
        jogador = Jogador(jogador)
    else:
        print("Já Possue Valor nessa Posição, Tente Novamente")
        time.sleep(2)
    os.system('cls')
