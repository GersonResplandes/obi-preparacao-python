#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo 1: Arrays e Listas Básicas
==================================

Neste módulo você aprenderá:
1. Como criar e manipular listas em Python
2. Operações básicas com arrays
3. Técnicas de iteração
4. Problemas comuns da OBI

Conceitos fundamentais para TODOS os outros módulos!
"""

# ===== 1. CRIANDO LISTAS =====

def criar_listas():
    """Demonstra diferentes formas de criar listas"""
    
    # Lista vazia
    lista_vazia = []
    
    # Lista com valores
    numeros = [1, 2, 3, 4, 5]
    
    # Lista usando range
    lista_range = list(range(1, 6))  # [1, 2, 3, 4, 5]
    
    # Lista com repetição
    lista_zeros = [0] * 5  # [0, 0, 0, 0, 0]
    
    # Lista 2D (matriz)
    matriz = [[0] * 3 for _ in range(3)]  # 3x3 de zeros
    
    return numeros, matriz

# ===== 2. OPERAÇÕES BÁSICAS =====

def operacoes_basicas():
    """Demonstra operações básicas com listas"""
    
    numeros = [1, 2, 3, 4, 5]
    
    # Acessando elementos
    primeiro = numeros[0]      # 1
    ultimo = numeros[-1]       # 5
    segundo = numeros[1]       # 2
    
    # Modificando elementos
    numeros[0] = 10            # [10, 2, 3, 4, 5]
    
    # Adicionando elementos
    numeros.append(6)          # [10, 2, 3, 4, 5, 6]
    numeros.insert(1, 7)       # [10, 7, 2, 3, 4, 5, 6]
    
    # Removendo elementos
    numeros.pop()              # Remove o último: 6
    numeros.pop(0)             # Remove o primeiro: 10
    
    # Tamanho da lista
    tamanho = len(numeros)     # 5
    
    return numeros

# ===== 3. ITERAÇÃO =====

def iteracao_listas():
    """Demonstra diferentes formas de iterar sobre listas"""
    
    numeros = [1, 2, 3, 4, 5]
    
    # 1. Iteração por índice
    print("Por índice:")
    for i in range(len(numeros)):
        print(f"Posição {i}: {numeros[i]}")
    
    # 2. Iteração direta (mais pythonico)
    print("\nDireta:")
    for num in numeros:
        print(f"Valor: {num}")
    
    # 3. Iteração com enumerate
    print("\nCom enumerate:")
    for i, num in enumerate(numeros):
        print(f"Posição {i}: {num}")
    
    # 4. Iteração reversa
    print("\nReversa:")
    for num in reversed(numeros):
        print(f"Valor: {num}")

# ===== 4. FUNÇÕES ÚTEIS =====

def funcoes_uteis():
    """Demonstra funções úteis para listas"""
    
    numeros = [3, 1, 4, 1, 5, 9, 2, 6]
    
    # Soma
    soma = sum(numeros)        # 31
    
    # Máximo e mínimo
    maximo = max(numeros)      # 9
    minimo = min(numeros)      # 1
    
    # Média
    media = soma / len(numeros)  # 3.875
    
    # Contagem de elementos
    contagem_1 = numeros.count(1)  # 2
    
    # Encontrar índice
    indice_5 = numeros.index(5)    # 4
    
    return soma, maximo, minimo, media

# ===== 5. PROBLEMAS PRÁTICOS =====

def problema_soma_array():
    """
    Problema: Dado um array de N números, calcule a soma de todos os elementos.
    
    Entrada:
    5
    1 2 3 4 5
    
    Saída:
    15
    """
    
    # Simulando entrada
    n = 5
    numeros = [1, 2, 3, 4, 5]
    
    # Solução 1: Loop tradicional
    soma = 0
    for num in numeros:
        soma += num
    
    # Solução 2: Usando sum() (mais pythonico)
    soma_pythonica = sum(numeros)
    
    print(f"Soma: {soma}")
    return soma

def problema_maior_elemento():
    """
    Problema: Dado um array de N números, encontre o maior elemento.
    
    Entrada:
    5
    3 7 2 9 1
    
    Saída:
    9
    """
    
    numeros = [3, 7, 2, 9, 1]
    
    # Solução 1: Loop tradicional
    maior = numeros[0]
    for num in numeros:
        if num > maior:
            maior = num
    
    # Solução 2: Usando max() (mais pythonico)
    maior_pythonico = max(numeros)
    
    print(f"Maior elemento: {maior}")
    return maior

def problema_contar_pares():
    """
    Problema: Dado um array de N números, conte quantos são pares.
    
    Entrada:
    6
    1 2 3 4 5 6
    
    Saída:
    3
    """
    
    numeros = [1, 2, 3, 4, 5, 6]
    
    # Solução 1: Loop tradicional
    contador = 0
    for num in numeros:
        if num % 2 == 0:
            contador += 1
    
    # Solução 2: Usando list comprehension
    contador_pythonico = sum(1 for num in numeros if num % 2 == 0)
    
    print(f"Números pares: {contador}")
    return contador

# ===== 6. EXERCÍCIOS PARA PRATICAR =====

def exercicio_1():
    """
    Exercício 1: Soma de elementos em posições pares
    
    Dado um array, calcule a soma dos elementos nas posições 0, 2, 4, ...
    
    Entrada: [1, 2, 3, 4, 5, 6]
    Saída: 9 (1 + 3 + 5)
    """
    
    numeros = [1, 2, 3, 4, 5, 6]
    
    # Sua solução aqui
    soma = 0
    for i in range(0, len(numeros), 2):  # Pula de 2 em 2
        soma += numeros[i]
    
    print(f"Soma em posições pares: {soma}")
    return soma

def exercicio_2():
    """
    Exercício 2: Inverter array
    
    Dado um array, crie uma versão invertida.
    
    Entrada: [1, 2, 3, 4, 5]
    Saída: [5, 4, 3, 2, 1]
    """
    
    numeros = [1, 2, 3, 4, 5]
    
    # Solução 1: Usando slice
    invertido = numeros[::-1]
    
    # Solução 2: Loop tradicional
    invertido_manual = []
    for i in range(len(numeros) - 1, -1, -1):
        invertido_manual.append(numeros[i])
    
    print(f"Original: {numeros}")
    print(f"Invertido: {invertido}")
    return invertido

# ===== FUNÇÃO PRINCIPAL =====

def main():
    """Executa todos os exemplos e exercícios"""
    
    print("=== MÓDULO 1: ARRAYS E LISTAS BÁSICAS ===\n")
    
    print("1. Criando listas:")
    numeros, matriz = criar_listas()
    print(f"   Números: {numeros}")
    print(f"   Matriz 3x3: {matriz}\n")
    
    print("2. Operações básicas:")
    resultado = operacoes_basicas()
    print(f"   Resultado: {resultado}\n")
    
    print("3. Iteração:")
    iteracao_listas()
    print()
    
    print("4. Funções úteis:")
    soma, maximo, minimo, media = funcoes_uteis()
    print(f"   Soma: {soma}, Máximo: {maximo}, Mínimo: {minimo}, Média: {media:.2f}\n")
    
    print("5. Problemas práticos:")
    problema_soma_array()
    problema_maior_elemento()
    problema_contar_pares()
    print()
    
    print("6. Exercícios:")
    exercicio_1()
    exercicio_2()
    print()
    
    print("=== PRÓXIMO PASSO ===")
    print("Agora pratique esses conceitos com problemas reais!")
    print("Tente resolver os problemas na pasta 'problemas/nivel1/'")

if __name__ == "__main__":
    main()
