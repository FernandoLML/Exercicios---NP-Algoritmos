import random
import time
from typing import Dict, List
from algoritmos import busca_exaustiva, greedy_knapsack, hill_climbing
from utils import exibir_solucao

def medir_complexidade(
    tamanhos: List[int],
    capacidade: int = 30,
    repeticoes: int = 3
) -> Dict[int, float]:
    resultados = {}
    for n in tamanhos:
        tempos = []
        for _ in range(repeticoes):
            tarefas_rand = [
                {"custo": random.randint(1, 10), "valor": random.randint(5, 50)}
                for _ in range(n)
            ]
            t0 = time.perf_counter()
            busca_exaustiva(tarefas_rand, capacidade)
            tempos.append((time.perf_counter() - t0) * 1000)

        resultados[n] = sum(tempos) / len(tempos)
    return resultados

def calcular_razoes_crescimento(tempos: Dict[int, float]) -> None:
    ns = sorted(tempos.keys())
    print(f"\n{'─'*55}")
    print(f"  {'n':>4}  {'Tempo (ms)':>12}  {'Razão':>8}  {'2^n':>12}")
    print(f"{'─'*55}")

    for idx, n in enumerate(ns):
        t = tempos[n]
        razao = f"{t / tempos[ns[idx-1]]:.2f}x" if idx > 0 else "  —"
        print(f"  {n:>4}  {t:>12.3f}  {razao:>8}  {2**n:>12,}")

    print(f"{'─'*55}")
    print(
        "\n  Conclusão: quando a razão se estabiliza em ~4x ao incrementar n em 2,\n"
        "  confirmamos crescimento O(2^n). Cada +2 em n dobra duas vezes o trabalho."
    )

def comparar_abordagens(tarefas: List[Dict], capacidade: int) -> None:
    t0 = time.perf_counter()
    ind_bf, val_bf = busca_exaustiva(tarefas, capacidade)
    t_bf = (time.perf_counter() - t0) * 1000

    t0 = time.perf_counter()
    ind_gr, val_gr = greedy_knapsack(tarefas, capacidade)
    t_gr = (time.perf_counter() - t0) * 1000

    t0 = time.perf_counter()
    ind_hc, val_hc, iters_hc = hill_climbing(tarefas, capacidade)
    t_hc = (time.perf_counter() - t0) * 1000

    print(f"\n{'═'*60}")
    print("  COMPARAÇÃO DAS ABORDAGENS")
    print(f"{'═'*60}")
    print(f"  {'Abordagem':<18} {'Valor':>6}  {'Tempo':>10}  {'Ótimo?'}")
    print(f"{'─'*60}")
    print(f"  {'Brute Force':<18} {val_bf:>6}  {t_bf:>9.2f}ms  ✅ Garante")
    print(f"  {'Greedy':<18} {val_gr:>6}  {t_gr:>9.2f}ms  ⚠ Sub-ótimo")
    print(f"  {'Hill Climbing':<18} {val_hc:>6}  {t_hc:>9.2f}ms  ⚠ Mínimo local")
    print(f"{'═'*60}")
    print(f"  Gap Greedy    : {val_bf - val_gr:+d} em relação ao ótimo")
    print(f"  Gap HC        : {val_bf - val_hc:+d} em relação ao ótimo")
    print(f"{'═'*60}\n")

    exibir_solucao(ind_bf, tarefas, "Brute Force — Solução Ótima")
    exibir_solucao(ind_gr, tarefas, "Greedy — Solução Heurística")
    exibir_solucao(ind_hc, tarefas, f"Hill Climbing — {iters_hc} iterações")