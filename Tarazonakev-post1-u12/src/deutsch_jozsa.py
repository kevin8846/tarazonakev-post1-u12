from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def oracle_constante(n):
    """
    Oráculo constante f(x)=0
    """
    return QuantumCircuit(n + 1)


def oracle_balanceada(n):
    """
    Oráculo balanceado
    """
    qc = QuantumCircuit(n + 1)

    for i in range(n):
        qc.cx(i, n)

    return qc


def deutsch_jozsa(oracle_qc, n, shots=1024):

    qc = QuantumCircuit(n + 1, n)

    # Ancilla en |1>
    qc.x(n)

    # Hadamard en todos
    qc.h(range(n + 1))

    # Aplicar oráculo
    qc.compose(oracle_qc, inplace=True)

    # Interferencia
    qc.h(range(n))

    # Medir
    qc.measure(range(n), range(n))

    simulator = AerSimulator()

    counts = simulator.run(
        qc,
        shots=shots
    ).result().get_counts()

    return counts


if __name__ == "__main__":

    n = 2

    counts_constante = deutsch_jozsa(
        oracle_constante(n),
        n
    )

    print("\nResultado Oráculo Constante:")
    print(counts_constante)

    counts_balanceada = deutsch_jozsa(
        oracle_balanceada(n),
        n
    )

    print("\nResultado Oráculo Balanceado:")
    print(counts_balanceada)

    assert "00" in counts_constante, \
        "Error: el oráculo constante no devolvió 00"

    assert "00" not in counts_balanceada, \
        "Error: el oráculo balanceado devolvió 00"

    print("\nOK: Deutsch-Jozsa verifica correctamente")