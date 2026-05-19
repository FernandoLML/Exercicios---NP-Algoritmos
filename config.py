from typing import Dict, List


# DADOS DO PROBLEMA


TAREFAS: List[Dict] = [
    {"nome": "Auth OAuth2",         "custo": 8,  "valor": 40},
    {"nome": "Dashboard métricas",  "custo": 13, "valor": 55},
    {"nome": "Exportar CSV",        "custo": 5,  "valor": 20},
    {"nome": "Refactor serviço X",  "custo": 20, "valor": 35},
    {"nome": "API notificações",    "custo": 10, "valor": 60},
    {"nome": "Upgrade deps",        "custo": 3,  "valor": 15},
    {"nome": "Testes E2E checkout", "custo": 8,  "valor": 50},
    {"nome": "Rate limiting",       "custo": 6,  "valor": 45},
    {"nome": "Docs OpenAPI",        "custo": 4,  "valor": 25},
    {"nome": "Cache Redis",         "custo": 12, "valor": 70},
]

CAPACIDADE: int = 40  # Story Points máximos na Sprint