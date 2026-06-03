from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os


def grover_2qubits(target="11", shots=1024):

    os.makedirs("capturas", exist_ok=True)

    qc = QuantumCircuit(2, 2)

    # Superposición uniforme
    qc.h([0, 1])

    # Oráculo
    if target == "11":
        qc.cz(0, 1)

    elif target == "00":
        qc.x([0, 1])
        qc.cz(0, 1)
        qc.x([0, 1])

    elif target == "01":
        qc.x(0)
        qc.cz(0, 1)
        qc.x(0)

    elif target == "10":
        qc.x(1)
        qc.cz(0, 1)
        qc.x(1)

    # Difusor
    qc.h([0, 1])

    qc.x([0, 1])

    qc.cz(0, 1)

    qc.x([0, 1])

    qc.h([0, 1])

    # Medición
    qc.measure([0, 1], [0, 1])

    simulator = AerSimulator()

    counts = simulator.run(
        qc,
        shots=shots
    ).result().get_counts()

    print(f"\nGrover buscando |{target}>")

    for state, count in sorted(counts.items()):
        porcentaje = count / shots * 100
        print(f"|{state}> : {count:4d} ({porcentaje:.1f}%)")

    estado_mas_probable = max(
        counts,
        key=counts.get
    )

    print(
        f"\nEstado más probable: |{estado_mas_probable}>"
    )

    fig = plot_histogram(counts)

    fig.savefig(
        f"capturas/grover_{target}.png",
        dpi=150
    )

    plt.close()

    return counts


if __name__ == "__main__":

    objetivos = [
        "00",
        "01",
        "10",
        "11"
    ]

    for objetivo in objetivos:

        grover_2qubits(
            target=objetivo
        )

        print("-" * 40)