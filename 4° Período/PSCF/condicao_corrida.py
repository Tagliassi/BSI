#!/usr/bin/env python3

# PSCF Experimentos
# com Programação Concorrente

from time import time, sleep
from os import getpid, getppid
from multiprocessing import Process, Value

def conta(n,vc):
    for i in range(n):
        vc.value += 1

def main():
    vc = Value("i",0,lock=False) # variável compartilhada
    # cria 2 processos filho
    filho1 = Process(target=conta, args=[1000000,vc])
    filho2 = Process(target=conta, args=[1000000,vc])
    # inicia execução dos 2 processos
    filho1.start()
    filho2.start();
    
    print("aguardando filhos")
    filho1.join()
    filho2.join()
    
    print("resultado =", vc.value)

if __name__ == "__main__":
    main()
