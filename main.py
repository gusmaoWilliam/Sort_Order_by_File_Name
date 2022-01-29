import os
import random
from tokenize import String

import string


def Sort():
    pasta = input("Cole o diretorio aqui: ")
    arq = ""
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            #print(os.path.join(os.path.realpath(diretorio), arquivo))
            arq = os.path.join(os.path.realpath(diretorio), arquivo)
            teste = arq[len(pasta)+1:]
            random.seed(None)
            number = random.randrange(0, 9999)
            numStr = str(number).zfill(4)
            os.rename(arq, f'{pasta}/{numStr}_{teste}')
    print("Finshed!")

def Remove():
    pasta = input("Cole o diretorio aqui: ")
    arq = ""
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            #print(os.path.join(os.path.realpath(diretorio), arquivo))
            arq = os.path.join(os.path.realpath(diretorio), arquivo)
            teste = arq[len(pasta)+6:]
            random.seed(None)
            os.rename(arq, f'{pasta}/{teste}')
    print("Finshed!")



x = input("Digite (1) para sortear e (2) para remover numeros: ")

if x == "1":
    Sort()
if x == "2":
    Remove()
