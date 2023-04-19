class Fibonacci:
    def __init__(self):
        pass

    def valida_posicao():
        while True:
            try:
                print("-"*100)
                posicao_escolhida = int(input("Digite a posição de fibonacci que deseja encontrar: "))
                if not posicao_escolhida >= 0:
                    print("")
                    print('\033[31m' + "Erro! Digite um inteiro maior ou igual a 0!" + '\033[0;0m')
                    print("")
                else:
                    return posicao_escolhida
            except ValueError:
                print("")
                print('\033[31m' + "Erro! Digite um inteiro maior ou igual a 0!" + '\033[0;0m')
                print("")
    
    def linear(n):
        penultimo = 1
        ultimo = 1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            contador = 3
            while contador <= n:
                soma = ultimo + penultimo
                penultimo = ultimo
                ultimo = soma
                contador += 1
            return soma

    def recursivo(n):                            
        if n <= 1:                                 
            return n                             
        else:                                    
            return Fibonacci.recursivo(n-1) + Fibonacci.recursivo(n-2)
