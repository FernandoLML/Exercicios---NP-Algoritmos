from typing import Dict, List
from config import CAPACIDADE

def avaliar_solucao(individuo: List[int], tarefas: List[Dict], capacidade: int) -> int:
    """
    Retorna o valor total da solução se o custo couber na capacidade,
    ou 0 se ultrapassar (solução inválida).
    """
    custo_total = sum(tarefas[i]["custo"] for i in range(len(tarefas)) if individuo[i] == 1)
    valor_total = sum(tarefas[i]["valor"] for i in range(len(tarefas)) if individuo[i] == 1)
    return valor_total if custo_total <= capacidade else 0

def exibir_solucao(individuo: List[int], tarefas: List[Dict], label: str = "") -> None:
    """Imprime as tarefas selecionadas, custo e valor total."""
    selecionadas = [tarefas[i] for i in range(len(tarefas)) if individuo[i] == 1]
    custo = sum(t["custo"] for t in selecionadas)
    valor = sum(t["valor"] for t in selecionadas)
    
    print(f"\n{'─'*50}")
    if label:
        print(f"  {label}")
    print(f"{'─'*50}")
    for t in selecionadas:
        print(f"  [{t['custo']:>2} SP | ROI {t['valor']:>3}]  {t['nome']}")
    print(f"{'─'*50}")
    print(f"  Custo total : {custo} / {CAPACIDADE} SP")
    print(f"  Valor total : {valor}")
    print(f"{'─'*50}")