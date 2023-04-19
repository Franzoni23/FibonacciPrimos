class Primos:
    def __init__(self):
        pass
    
    def valida_numero():
        while True:
            try:
                print("-"*100)
                numero = int(input("Ver números primos de 2 até "))
                if not numero > 1:
                    print("")
                    print('\033[31m' + "Erro! Digite um inteiro maior que 1!" + '\033[0;0m')
                    print("")
                else:
                    return numero
            except ValueError:
                print("")
                print('\033[31m' + "Erro! Digite um inteiro maior que 1!" + '\033[0;0m')
                print("")
        
    def linear(n):   
        primos = []
        for x in range(2, n+1):
            contador = 0
            for i in range(1, n+1):
                if x % i == 0:
                    contador += 1
            if contador <= 2:
                primos.append(x)
        return primos

    def recursivo(n):
        if n < 2:
            return []
        elif Primos.teste_primo(n):
            return Primos.recursivo(n-1) + [n]
        else:
            return Primos.recursivo(n-1)
    
    def teste_divisao(n, i, x):
        if i > x:
            return False
        elif n % i == 0:
            return True
        else:
            return Primos.teste_divisao(n, i+1, x)        
        
    def teste_primo(n):
        return n > 1 and not (Primos.teste_divisao(n, 2, n-1))
