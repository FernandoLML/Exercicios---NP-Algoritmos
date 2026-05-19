import random
import time
from config import TAREFAS, CAPACIDADE
from utils import exibir_solucao
from algoritmos import (
    busca_exaustiva, greedy_knapsack, 
    hill_climbing, hill_climbing_com_restart
)
from analise import medir_complexidade, calcular_razoes_crescimento, comparar_abordagens

if __name__ == "__main__":
    random.seed(42)

    # ── Ex 1 ──────────────────────────────────
    print("\n" + "═"*60)
    print("  EXERCÍCIO 1 — Busca Exaustiva")
    print("═"*60)
    ind1, val1 = busca_exaustiva(TAREFAS, CAPACIDADE)
    exibir_solucao(ind1, TAREFAS, "Brute Force")
    assert val1 > 0, "Ex1: valor deve ser positivo"
    custo1 = sum(TAREFAS[i]["custo"] for i in range(len(TAREFAS)) if ind1[i] == 1)
    assert custo1 <= CAPACIDADE, "Ex1: custo não pode exceder capacidade"
    print("  ✅ Ex 1 OK")

    # ── Ex 2 ──────────────────────────────────
    print("\n" + "═"*60)
    print("  EXERCÍCIO 2 — Heurística Gulosa (Greedy)")
    print("═"*60)
    ind2, val2 = greedy_knapsack(TAREFAS[:6], CAPACIDADE)
    ind2_bf, val2_bf = busca_exaustiva(TAREFAS[:6], CAPACIDADE)
    exibir_solucao(ind2, TAREFAS[:6], f"Greedy    → valor {val2}")
    exibir_solucao(ind2_bf, TAREFAS[:6], f"BruteForce → valor {val2_bf} (ótimo)")
    print(f"\n  Gap Greedy vs Ótimo: {val2_bf - val2:+d}")
    assert val2 > 0
    print("  ✅ Ex 2 OK")

    # ── Ex 3 ──────────────────────────────────
    print("\n" + "═"*60)
    print("  EXERCÍCIO 3 — Análise Empírica de Complexidade")
    print("═"*60)
    tamanhos = [5, 8, 10, 12, 14, 16]
    tempos = medir_complexidade(tamanhos, capacidade=30, repeticoes=3)
    calcular_razoes_crescimento(tempos)

    print("\n  [Desafio] Greedy vs BruteForce, n=15:")
    tarefas15 = [{"custo": random.randint(1,10), "valor": random.randint(5,50)} for _ in range(15)]
    t0 = time.perf_counter(); busca_exaustiva(tarefas15, 30); t_bf15 = (time.perf_counter()-t0)*1000
    t0 = time.perf_counter(); greedy_knapsack(tarefas15, 30); t_gr15 = (time.perf_counter()-t0)*1000
    print(f"    BruteForce: {t_bf15:.2f} ms | Greedy: {t_gr15:.4f} ms")
    print("  ✅ Ex 3 OK")

    # ── Ex 4 ──────────────────────────────────
    print("\n" + "═"*60)
    print("  EXERCÍCIO 4 — Hill Climbing")
    print("═"*60)
    ind4, val4, iters4 = hill_climbing(TAREFAS, CAPACIDADE, verbose=True)
    exibir_solucao(ind4, TAREFAS, f"Hill Climbing — {iters4} iterações")
    assert val4 > 0
    custo4 = sum(TAREFAS[i]["custo"] for i in range(len(TAREFAS)) if ind4[i] == 1)
    assert custo4 <= CAPACIDADE
    print("  ✅ Ex 4 OK")

    print("\n  [Desafio] Hill Climbing com 5 restarts aleatórios:")
    ind4r, val4r = hill_climbing_com_restart(TAREFAS, CAPACIDADE, n_restarts=5)
    exibir_solucao(ind4r, TAREFAS, f"Melhor restart → valor {val4r}")

    # ── Debrief final ─────────────────────────
    print("\n" + "═"*60)
    print("  DEBRIEF — Comparação das Abordagens")
    print("═"*60)
    comparar_abordagens(TAREFAS, CAPACIDADE)