from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os

def bell_state_experiment(shots=1024):
    """
    Prepara el estado de Bell |Φ+> y mide los resultados.
    """

    os.makedirs("capturas", exist_ok=True)

    qc = QuantumCircuit(2, 2)

    # Superposición
    qc.h(0)

    # Entrelazamiento
    qc.cx(0, 1)

    # Medición
    qc.measure([0, 1], [0, 1])

    simulator = AerSimulator()

    job = simulator.run(qc, shots=shots)
    result = job.result()

    counts = result.get_counts()

    print(f"\nResultados Bell |Φ+> ({shots} shots):\n")

    for state, count in sorted(counts.items()):
        porcentaje = count / shots * 100
        print(f"|{state}> : {count:4d} ({porcentaje:.1f}%)")

    assert "01" not in counts and "10" not in counts, \
        "ERROR: aparecieron estados no entrelazados"

    print("\nOK: correlación perfecta verificada")

    fig = plot_histogram(counts)
    fig.savefig("capturas/bell_histogram.png", dpi=150)

    plt.close()

    return counts


if __name__ == "__main__":
    bell_state_experiment()