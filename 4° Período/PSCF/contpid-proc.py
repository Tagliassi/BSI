#!/usr/bin/env python3

# Contador usando 2 processos

import os
import sys
from time import sleep
from multiprocessing import Process

def cont(n, t, nome):
    print(f"{nome} - PID = {os.getpid()}")
    print(f"{nome} - PID do PAI = {os.getppid()}")

    for i in range(n):
        print(f'{nome}: {i+1}')
        sleep(t)

def main():
    print(f"PID = {os.getpid()}")

    p1 = Process(target=cont, args=(10, 1, "  P1"))
    p2 = Process(target=cont, args=(20, 0.7, "    P2"))

    print("Iniciando processos")
    p1.start()
    p2.start()

    print("Aguardando fim dos processos")
    p1.join()
    p2.join()

    print("Fim do processo pai")

if __name__ == '__main__':
    main()
