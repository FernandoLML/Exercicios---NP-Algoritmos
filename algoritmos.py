import itertools
import random
from typing import Dict, List, Optional, Tuple
from utils import avaliar_solucao

# ══════════════════════════════════════════════
# EXERCÍCIO 1 — Busca Exaustiva (Brute Force)
# ══════════════════════════════════════════════
def busca_exaustiva(tarefas: List[Dict], capacidade: int) -> Tuple[List[int], int]:
    n = len(tarefas)
    melhor_individuo = [0] * n
    melhor_valor = 0

    for combo in itertools.product([0, 1], repeat=n):
        individuo = list(combo)
        valor = avaliar_solucao(individuo, tarefas, capacidade)
        if valor > melhor_valor:
            melhor_valor = valor
            melhor_individuo = individuo[:]

    return melhor_individuo, melhor_valor

# ══════════════════════════════════════════════
# EXERCÍCIO 2 — Heurística Gulosa (Greedy)
# ══════════════════════════════════════════════
def greedy_knapsack(tarefas: List[Dict], capacidade: int) -> Tuple[List[int], int]:
    n = len(tarefas)
    individuo = [0] * n
    capacidade_restante = capacidade

    indices = sorted(
        range(n),
        key=lambda i: tarefas[i]["valor"] / tarefas[i]["custo"],
        reverse=True
    )

    for i in indices:
        if tarefas[i]["custo"] <= capacidade_restante:
            individuo[i] = 1
            capacidade_restante -= tarefas[i]["custo"]

    valor_total = sum(tarefas[i]["valor"] for i in range(n) if individuo[i] == 1)
    return individuo, valor_total

# ══════════════════════════════════════════════
# EXERCÍCIO 4 — Hill Climbing (Busca Local)
# ══════════════════════════════════════════════
def gerar_vizinhos(individuo: List[int]) -> List[List[int]]:
    vizinhos = []
    for i in range(len(individuo)):
        vizinho = individuo[:]
        vizinho[i] = 1 - vizinho[i]
        vizinhos.append(vizinho)
    return vizinhos

def hill_climbing(
    tarefas: List[Dict],
    capacidade: int,
    solucao_inicial: Optional[List[int]] = None,
    max_iter: int = 1000,
    verbose: bool = False
) -> Tuple[List[int], int, int]:
    
    if solucao_inicial is None:
        atual, _ = greedy_knapsack(tarefas, capacidade)
    else:
        atual = solucao_inicial[:]

    atual_valor = avaliar_solucao(atual, tarefas, capacidade)
    n_iter = 0

    for it in range(max_iter):
        vizinhos = gerar_vizinhos(atual)
        melhor_viz = max(vizinhos, key=lambda v: avaliar_solucao(v, tarefas, capacidade))
        melhor_viz_valor = avaliar_solucao(melhor_viz, tarefas, capacidade)

        if melhor_viz_valor > atual_valor:
            atual = melhor_viz
            atual_valor = melhor_viz_valor
            n_iter = it + 1
            if verbose:
                print(f"    iter {it+1:>4}: valor = {atual_valor}")
        else:
            n_iter = it
            break

    return atual, atual_valor, n_iter

def hill_climbing_com_restart(
    tarefas: List[Dict],
    capacidade: int,
    n_restarts: int = 5
) -> Tuple[List[int], int]:
    n = len(tarefas)
    melhor_global_ind = [0] * n
    melhor_global_val = 0

    for r in range(n_restarts):
        inicio = [random.randint(0, 1) for _ in range(n)]
        ind, val, iters = hill_climbing(tarefas, capacidade, solucao_inicial=inicio)
        status = "✓ novo melhor!" if val > melhor_global_val else ""
        print(f"  Restart {r+1}: valor = {val:>3}  ({iters} iters) {status}")
        
        if val > melhor_global_val:
            melhor_global_val = val
            melhor_global_ind = ind[:]

    return melhor_global_ind, melhor_global_val