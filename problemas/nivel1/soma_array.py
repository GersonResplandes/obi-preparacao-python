#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problema de Treino: Soma de Array
==================================

Problema: Dado um array de N números inteiros, calcule a soma de todos os elementos.

Entrada:
- Primeira linha: um inteiro N (1 ≤ N ≤ 100)
- Segunda linha: N inteiros separados por espaço

Saída:
- Um inteiro representando a soma de todos os elementos

Exemplo:
Entrada:
5
1 2 3 4 5

Saída:
15

Dica: Use a função sum() do Python ou um loop para somar os elementos.
"""

def resolver():
    """Solução para o problema"""
    
    # Lendo a entrada
    n = int(input())  # Número de elementos
    numeros = list(map(int, input().split()))  # Array de números
    
    # Verificando se o tamanho está correto
    assert len(numeros) == n, f"Esperado {n} números, mas recebido {len(numeros)}"
    
    # Calculando a soma
    soma = sum(numeros)
    
    # Imprimindo o resultado
    print(soma)

if __name__ == "__main__":
    resolver()
