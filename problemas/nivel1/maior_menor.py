#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problema de Treino: Maior e Menor Elemento
===========================================

Problema: Dado um array de N números inteiros, encontre o maior e o menor elemento.

Entrada:
- Primeira linha: um inteiro N (1 ≤ N ≤ 100)
- Segunda linha: N inteiros separados por espaço

Saída:
- Duas linhas: o maior elemento na primeira linha e o menor na segunda

Exemplo:
Entrada:
5
3 7 2 9 1

Saída:
9
1

Dica: Use as funções max() e min() do Python ou loops para encontrar os valores.
"""

def resolver():
    """Solução para o problema"""
    
    # Lendo a entrada
    n = int(input())  # Número de elementos
    numeros = list(map(int, input().split()))  # Array de números
    
    # Verificando se o tamanho está correto
    assert len(numeros) == n, f"Esperado {n} números, mas recebido {len(numeros)}"
    
    # Encontrando o maior e menor elemento
    maior = max(numeros)
    menor = min(numeros)
    
    # Imprimindo os resultados
    print(maior)
    print(menor)

if __name__ == "__main__":
    resolver()
