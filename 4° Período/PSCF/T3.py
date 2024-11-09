import multiprocessing
import time

# Funções up e down para controlar o semáforo
def down(s):
    s.acquire()

def up(s):
    s.release()

# Função que realiza a contagem
def conta(n, t, contador, semaforo_inicio=None, semaforo_inicio2=None, semaforo_fim=None):  
    if semaforo_inicio:
        down(semaforo_inicio)  # Usa a função down para adquirir o semáforo
    
    if semaforo_inicio2:
        down(semaforo_inicio2)  # Usa a função down para adquirir o segundo semáforo, se necessário

    print(f"{multiprocessing.current_process().name} : Iniciando contagem (n = {n}, t = {t})")

    for i in range(n):
        contador.value += 1  # Incrementa o contador sem mutex
      
        time.sleep(t)  # Espera o intervalo especificado no processo
        print(f"{multiprocessing.current_process().name}: {contador.value}")

    if semaforo_fim:
        up(semaforo_fim)  # Usa a função up para liberar o próximo processo
        print(f"{multiprocessing.current_process().name}: Finalizando")  # Imprime mensagem de finalização

if __name__ == '__main__':
    qtd_A = int(input("Digite a contagem de A: "))
    t_A = float(input("Digite o temporizador de A: "))

    qtd_B = int(input("Digite a contagem de B: "))
    t_B = float(input("Digite o temporizador de B: "))

    qtd_C = int(input("Digite a contagem de C: "))
    t_C = float(input("Digite o temporizador de C: "))

    qtd_D = int(input("Digite a contagem de D: "))
    t_D = float(input("Digite o temporizador de D: "))

    # Criação dos semáforos para controlar a ordem de execução
    semaforo_A = multiprocessing.Semaphore(0)  
    semaforo_B = multiprocessing.Semaphore(0)  
    semaforo_C = multiprocessing.Semaphore(0)  
    semaforo_D = multiprocessing.Semaphore(0)  

    contador_A = multiprocessing.Value('i', 0)
    contador_B = multiprocessing.Value('i', 0)
    contador_C = multiprocessing.Value('i', 0)
    contador_D = multiprocessing.Value('i', 0)

    # Definição dos processos
    processo_A = multiprocessing.Process(target=conta, args=( qtd_A, t_A, contador_A, None, None, semaforo_A), name='Processo A')
    processo_B = multiprocessing.Process(target=conta, args=( qtd_B, t_B, contador_B, semaforo_A, None, semaforo_B), name='----Processo B')
    processo_C = multiprocessing.Process(target=conta, args=( qtd_C, t_C, contador_C, semaforo_A, None, semaforo_C), name='--------Processo C')
    processo_D = multiprocessing.Process(target=conta, args=( qtd_D, t_D, contador_D, semaforo_B, semaforo_C, semaforo_D), name='------------Processo D')

    # Início dos processos
    processo_A.start()
    processo_B.start()
    processo_C.start()
    processo_D.start()

    # Aguardar todos os processos terminarem
    processo_A.join()
    up(semaforo_A)  # Libera semáforo para B e C começarem após A

    processo_B.join()  
    processo_C.join()  

    up(semaforo_B)
    up(semaforo_C)
    processo_D.join()