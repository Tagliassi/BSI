import multiprocessing
import time

# Função que realiza a contagem
def conta(nome, n, t, contador, mutex, semaforo_inicio=None, semaforo_inicio2=None, semaforo_fim=None):  
    # Atraso baseado no temporizador do processo
    if semaforo_inicio:
        semaforo_inicio.acquire()  
    

    if semaforo_inicio2:
        semaforo_inicio2.acquire()

    print(f"{nome} : Iniciando contagem ( n = {n}, t = {t})")

    for i in range(n):
        with mutex:  
            contador.value += 1  # Incrementa o contador
      
        time.sleep(t)  # Espera o intervalo especificado no processo
        print(f"{multiprocessing.current_process().name}: {contador.value}")

    if semaforo_fim:
        semaforo_fim.release()  # Libera o semáforo para o próximo processo
        print(f"{multiprocessing.current_process().name}: Finalizando")  # Imprime mensagem de finalização

if __name__ == '__main__':

    # Mutex para garantir que a seção crítica seja segura
    mutex = multiprocessing.Lock()

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
    processo_A = multiprocessing.Process(target=conta, args=("Processo A", qtd_A, t_A, contador_A, mutex, None, None, semaforo_A), name='Processo A')

    processo_B = multiprocessing.Process(target=conta, args=("Processo B", qtd_B, t_B, contador_B, mutex, semaforo_A, None, semaforo_B), name='----Processo B')
    processo_C = multiprocessing.Process(target=conta, args=("Processo C", qtd_C, t_C, contador_C, mutex, semaforo_A, None, semaforo_C), name='--------Processo C')

    processo_D = multiprocessing.Process(target=conta, args=("Processo D", qtd_D, t_D, contador_D, mutex, semaforo_B, semaforo_C, semaforo_D), name='------------Processo D')

    # Início dos processos
    processo_A.start()
    processo_B.start()
    processo_C.start()
    processo_D.start()

    # Aguardar todos os processos terminarem
    processo_A.join()
    semaforo_A.release()  # Libera semáforo para B e C começarem após A

    processo_B.join()  
    processo_C.join()  

    semaforo_B.release()
    semaforo_C.release()  
