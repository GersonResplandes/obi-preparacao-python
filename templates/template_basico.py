#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Template básico para problemas da OBI em Python

Dicas importantes:
1. Sempre leia o problema 3 vezes
2. Identifique o padrão antes de codificar
3. Teste com exemplos pequenos
4. Gerencie o tempo (máx 30 min por problema)
"""

import sys
import math
from collections import defaultdict, deque, Counter
from itertools import combinations, permutations
from typing import List, Tuple, Set

# ===== FUNÇÕES ÚTEIS =====

def ler_int() -> int:
    """Lê um inteiro da entrada padrão"""
    return int(input())

def ler_ints() -> List[int]:
    """Lê uma lista de inteiros da entrada padrão"""
    return list(map(int, input().split()))

def ler_string() -> str:
    """Lê uma string da entrada padrão"""
    return input().strip()

def imprimir_array(arr: List[int]) -> None:
    """Imprime um array separado por espaços"""
    print(*arr)

def maximo(a: int, b: int) -> int:
    """Retorna o máximo entre dois números"""
    return max(a, b)

def minimo(a: int, b: int) -> int:
    """Retorna o mínimo entre dois números"""
    return min(a, b)

def eh_par(n: int) -> bool:
    """Verifica se um número é par"""
    return n % 2 == 0

def eh_impar(n: int) -> bool:
    """Verifica se um número é ímpar"""
    return n % 2 == 1

def eh_primo(n: int) -> bool:
    """Verifica se um número é primo"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def mdc(a: int, b: int) -> int:
    """Calcula o MDC usando algoritmo de Euclides"""
    while b:
        a, b = b, a % b
    return a

def mmc(a: int, b: int) -> int:
    """Calcula o MMC usando MDC"""
    return (a * b) // mdc(a, b)

# ===== ESTRUTURA PRINCIPAL =====

def main():
    """Função principal"""
    
    # ===== LEITURA DA ENTRADA =====
    
    # Leitura básica
    n = ler_int()  # número de casos/testes
    
    # Leitura de array
    # arr = ler_ints()
    
    # Leitura de múltiplas linhas
    # for _ in range(n):
    #     linha = ler_ints()
    
    # ===== PROCESSAMENTO =====
    
    # Seu código aqui...
    resultado = 0
    
    # ===== SAÍDA =====
    
    # Saída básica
    print(resultado)
    
    # Saída formatada
    # print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
