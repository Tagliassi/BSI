def input_set():
    while True:
        input_str = input("Digite os elementos do conjunto separados por vírgula: ").strip()
        if not input_str:
            print("Entrada inválida. Por favor, tente novamente.")
            continue
        elements = input_str.split(',')
        return set(elements)

def sets():

    while True:
        print("\nMenu Principal:")
        print("1) Modificar conjunto A")
        print("2) Modificar conjunto B")
        print("3) Sair")

        main_choice = input("Escolha uma opção: ")

        if main_choice == '1':
            print("Conjunto A:")
            modify_set(set_a)
        elif main_choice == '2':
            print("Conjunto B:")
            modify_set(set_b)
        elif main_choice == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

    print("Programa encerrado.")

def modify_set(existing_set):
    print("1) Adicionar elementos ao conjunto")
    print("2) Remover elementos do conjunto")
    print("3) Voltar ao menu principal")

    modification_choice = input("Escolha uma opção: ")

    if modification_choice == '1':
        new_elements = input("Digite os elementos a serem adicionados separados por vírgula: ").strip().split(',')
        existing_set.update(new_elements)
        print("Elementos adicionados ao conjunto.")
        print("Conjunto atual:", existing_set)
        
    elif modification_choice == '2':
        elements_to_remove = input("Digite os elementos a serem removidos separados por vírgula: ").strip().split(',')
        existing_set.difference_update(elements_to_remove)
        print("Elementos removidos do conjunto.")
        print("Conjunto atual:", existing_set)
    elif modification_choice == '3':
        return
    else:
        print("Opção inválida.")

def print_set_operation_result(result_set):
    print("Resultado da operação:", result_set)

set_a = input_set()
set_b = input_set()

def main():

    while True:
        print("\nMenu de Operações:")
        print("1) Modificar conjuntos")
        print("a) União A e B")
        print("b) Intersecção A e B")
        print("c) Diferença A e B")
        print("d) Produto cartesiano A e B")
        print("e) Verificação se A é subconjunto de B")
        print("f) Verificação se B é subconjunto de A")
        print("g) Intersecção B e A")
        print("j) Diferença B e A")
        print("k) Produto cartesiano B e A")
        print("s) Sair")

        choice = input("Escolha uma opção: ").lower()

        if choice == 's':
            print("Encerrando o programa.")
            break
        elif choice == '1':
            sets()
        elif choice in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'j', 'k'):
            if choice == 'a':
                result = set_a.union(set_b)
            elif choice == 'b':
                result = set_a.intersection(set_b)
            elif choice == 'c':
                result = set_a.difference(set_b)
            elif choice == 'd':
                result = {(x, y) for x in set_a for y in set_b}
            elif choice == 'e':
                result = set_a.issubset(set_b)
                print("É subconjunto de B:", result)
                continue
            elif choice == 'f':
                result = set_b.issubset(set_a)
                print("É subconjunto de A:", result)
                continue
            elif choice == 'g':
                result = set_b.intersection(set_a)
            elif choice == 'j':
                result = set_b.difference(set_a)
            elif choice == 'k':
                result = {(x, y) for x in set_b for y in set_a}

            print_set_operation_result(result)

        else:
            print("Opção inválida. Por favor, escolha novamente.")

    print("Programa encerrado.")

if __name__ == "__main__":
    main()