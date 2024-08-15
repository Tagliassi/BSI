#!/usr/bin/env python3

#
# von Neumann - Arquitetura Básica
# Todos as classes em um mesmo arquivo
# PSCF - BSI - Prof. Luiz Lima Jr.
#
# Arquitetura formada de 3 componentes básicos:
#
# 1. Memória => RAM
# 2. CPU
# 3. Entrada e Saída (IO)
#

class IO:
    def output(self, s):
        print(s, end='')

    def input(self, prompt):
        return input(prompt)


# Exceção (erro)
class EnderecoInvalido(Exception):
    def __init__(self, ender):
        self.ender = ender


class RAM:
    def __init__(self, k):
        self.tamanho = 2**k
        self.memoria = [0] * self.tamanho

    def verifica_endereco(self, ender):
        if (ender < 0) or (ender >= self.tamanho):
            raise EnderecoInvalido(ender)

    def capacidade(self):
        return self.tamanho

    def read(self, ender):
        self.verifica_endereco(ender)
        return self.memoria[ender]

    def write(self, ender, val):
        self.verifica_endereco(ender)
        self.memoria[ender] = val

class CacheSimples:
    def __init__(self, kc, ram):
        self.tamanho_cach = 2**kc
        self.dados = [0] * self.tamanho_cach
        self.bloco = -1
        self.modif = False
    
    def read(self, ender):
        bloco_ender = int(ender / self.tamanho_cach)
        if bloco_ender == self.bloco:
            print("Cache hit")
            pos = ender - self.bloco * self.tamanho_cach
            return self.dados[pos]
        print("Cache miss")
    
    def write(self, ender, val):
        #cache foi modificada? -> atualiza a RAM
        #cache miss -> atualiza a cache a partir do bloco da RAM contendo o endereco
        #return...
        pass
        
class CPU:
    def __init__(self, mem, io):
        self.mem = mem
        self.io = io
        self.PC = 0                    # program counter
        self.A = self.B = self.C = 0   # registradores auxiliares

    def run(self, ender):
        self.PC = ender
        # lê "instrução" no endereço PC
        self.A = self.mem.read(self.PC)
        self.PC += 1
        self.B = self.mem.read(self.PC)
        self.PC += 1

        self.C = 1
        while self.A <= self.B:
            self.mem.write(self.A, self.C)
            self.io.output(f"{self.A} -> {self.C}\n")
            self.C += 1
            self.A += 1

# Programa Principal

try:
    io = IO()
    ram = RAM(7)
    cache = CacheSimples(3, ram)
    cpu = CPU(cache, io)

    endereco = 10
    ram.write(endereco, 120)
    ram.write(endereco+1, 130)
    cpu.run(endereco)

except EnderecoInvalido as e:
    print("Endereco invalido:", e.ender)