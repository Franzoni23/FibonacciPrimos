from Fibonacci import *
from Primos import *
from Layout import *
import time

while True:
    opcao_escolhida = menu (["Calcular Fibonacci", "Descobrir Primos", "Finalizar Programa"])
    if opcao_escolhida == 1:
        posicao_escolhida = Fibonacci.valida_posicao()
        inicio = time.time()
        resultado1 = Fibonacci.linear(posicao_escolhida)
        fim = time.time()
        inicio2 = time.time()
        resultado2 = Fibonacci.recursivo(posicao_escolhida)
        fim2 = time.time()
        resultado_fibonacci(posicao_escolhida, resultado1, resultado2)
        tempo_execucao(fim, inicio, fim2, inicio2)
    if opcao_escolhida == 2:
        numero = Primos.valida_numero()
        inicio = time.time()
        resultado1 = Primos.linear(numero)
        fim = time.time()
        inicio2 = time.time()
        resultado2 = Primos.recursivo(numero)
        fim2 = time.time()
        resultado_primos(numero, resultado1, resultado2)
        tempo_execucao(fim, inicio, fim2, inicio2)
    if opcao_escolhida == 3:
        finaliza()
        break
