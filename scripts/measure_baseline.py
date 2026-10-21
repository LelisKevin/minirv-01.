# exemplo: scripts/measure_baseline.py
import json, time, tracemalloc
from pathlib import Path

def executar_benchmark():
    # Substitua este bloco pelo comando real do simulador.
    total = 0
    for i in range(100000):
        total += i % 7
    return {"amostras": 100000, "checksum": total}

resultados = []
for repeticao in range(1, 4):
    tracemalloc.start()
    inicio = time.perf_counter()
    saida = executar_benchmark()
    tempo = time.perf_counter() - inicio
    atual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    resultados.append({
        "repeticao": repeticao,
        "tempo_decorrido_s": tempo,
        "memoria_pico_bytes": pico,
        "saida": saida
    })

Path("benchmarks/baseline").mkdir(parents=True, exist_ok=True)
Path("benchmarks/baseline/resultados-brutos.json").write_text(
    json.dumps(resultados, indent=2, ensure_ascii=False),
    encoding="utf-8"
)
