import os
import random
from tokenize import String

import string

mapa = "abcdefghijklmnopqrstuvwxyz"

class Sort():
    def __init__(self):
        pass
    def SortNum(self, pasta):
        try:
            arq = ""
            for diretorio, subpastas, arquivos in os.walk(pasta):
                for arquivo in arquivos:
                    #print(os.path.join(os.path.realpath(diretorio), arquivo))
                    arq = os.path.join(os.path.realpath(diretorio), arquivo)
                    teste = arq[len(pasta)+1:]
                    if teste[0:4].isnumeric() and teste[4] == '_':
                        teste = teste[5:]
                        print(f"Ja existia um numero aleatorio aqui")
                    if teste[-4:].lower() == '.mp3':
                        random.seed(None)
                        number = random.randrange(0, 9999)
                        numStr = str(number).zfill(4)
                        os.rename(arq, f'{pasta}/{numStr}_{teste}')
                    else:
                        print("Não é musica")
            return 0
        except:
            return -1

    def SortLetters(self, pasta):
        arq = ""
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                #print(os.path.join(os.path.realpath(diretorio), arquivo))
                arq = os.path.join(os.path.realpath(diretorio), arquivo)
                teste = arq[len(pasta)+1:]

                random.seed(None)
                number = random.randrange(0, 25)
                letters = mapa[number]
                number = random.randrange(0, 25)
                letters = letters+mapa[number]
                number = random.randrange(0, 25)
                letters = letters+mapa[number]
                number = random.randrange(0, 25)
                letters = letters+mapa[number]

                os.rename(arq, f'{pasta}/{letters}_{teste}')


    def RemoveNum(self, pasta):
        try:
            arq = ""
            for diretorio, subpastas, arquivos in os.walk(pasta):
                for arquivo in arquivos:
                    #print(os.path.join(os.path.realpath(diretorio), arquivo))
                    arq = os.path.join(os.path.realpath(diretorio), arquivo)
                    teste = arq[len(pasta)+1:]
                    if teste[0:4].isnumeric() and teste[4] == "_":
                        os.rename(arq, f'{pasta}/{teste[5:]}')
  
                    else:
                        print(f'Falha em remover numeros de {teste}')
            return 0
        except:
            return -1
    def RemoveLetters(self, pasta):
        arq = ""
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                #print(os.path.join(os.path.realpath(diretorio), arquivo))
                arq = os.path.join(os.path.realpath(diretorio), arquivo)
                teste = arq[len(pasta)+1:]
                if teste[4] == "_":
                    os.rename(arq, f'{pasta}/{teste[5:]}')
                else:
                    print(f'Falha em remover Letras de {teste}')
