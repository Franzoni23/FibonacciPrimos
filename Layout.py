def linha():
    return "-" * 100

def espaco():
    return " "

def cabecalho(titulo):
    print(linha())
    print(titulo.center(100))
    print(linha())

def menu(opcoes):
    cabecalho("MENU PRINCIPAL")
    numero = 1
    for item in opcoes:
        print(f'{numero} - {item}')
        numero += 1
    print(linha())
    opcao_escolhida = valida_opcao()
    return opcao_escolhida

def valida_opcao():
    while True:
        try:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1 or opcao == 2 or opcao == 3:
                return opcao
            else:
                print(espaco())
                print('\033[31m' + "Erro! Digite uma opção válida!" +'\033[0;0m')
                print(espaco())
        except ValueError:
            print(espaco())
            print('\033[31m' + "Erro! Digite uma opção válida!" +'\033[0;0m')
            print(espaco())

def resultado_fibonacci(posicaoescolhida, resultado1, resultado2):
    cabecalho("RESULTADO")
    print("Código linear -> fib(" + str(posicaoescolhida) + "): " + str(resultado1))
    print(espaco())
    print("Código recursivo -> fib(" + str(posicaoescolhida) + "): " + str(resultado2))
    print(espaco())

def resultado_primos(numero, resultado1, resultado2):
    cabecalho("RESULTADO")
    print("Código linear -> p(" + str(numero) + "): " + str(resultado1))
    print(espaco())
    print("Código recursivo -> p(" + str(numero) + "): " + str(resultado2))
    print(espaco())

def tempo_execucao(fim, inicio, fim2, inicio2):
    print("Tempo de execução do código em segundos:")
    print("Código linear:", float(fim-inicio))
    print("Código recursivo:", float(fim2-inicio2))

def finaliza():
    print(linha())
    print(espaco())
    print("PROGRAMA FINALIZADO.")
    print(espaco())
    print(linha())
