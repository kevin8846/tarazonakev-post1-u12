# Post-Contenido 1 - Unidad 12
## Computación Emergente y Tendencias

### Autor
Kevin Alejandro Tarazona Martínez

### Descripción

En este laboratorio se implementan tres experimentos fundamentales de computación cuántica utilizando Qiskit:

1. Estado de Bell (Entrelazamiento Cuántico)
2. Algoritmo de Deutsch-Jozsa
3. Algoritmo de Grover para 2 qubits

Todos los experimentos son ejecutados mediante el simulador AerSimulator de Qiskit.

---

# Requisitos

- Python 3.9 o superior
- Qiskit
- Qiskit Aer
- Matplotlib

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# Estructura del Proyecto

```text
apellido-post1-u12/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── bell_state.py
│   ├── deutsch_jozsa.py
│   └── grover.py
│
└── capturas/
    ├── bell_histogram.png
    ├── grover_00.png
    ├── grover_01.png
    ├── grover_10.png
    └── grover_11.png
```

---

# Experimento 1: Estado de Bell

## Objetivo

Construir el estado de Bell:

|Φ⁺⟩ = (|00⟩ + |11⟩)/√2

para demostrar el fenómeno de entrelazamiento cuántico.

## Procedimiento

1. Aplicar una puerta Hadamard al primer qubit.
2. Aplicar una puerta CNOT.
3. Medir ambos qubits.
4. Ejecutar 1024 simulaciones.

## Ejecución

```bash
python src/bell_state.py
```

## Resultado Esperado

```text
|00> ≈ 50%
|11> ≈ 50%
```

Los estados:

```text
|01>
|10>
```

no deben aparecer.

## Interpretación

Los resultados muestran que ambos qubits se encuentran entrelazados. Cuando uno de ellos es medido, el otro presenta una correlación perfecta con el primero.

---

# Experimento 2: Algoritmo de Deutsch-Jozsa

## Objetivo

Determinar si una función es:

- Constante
- Balanceada

utilizando una única evaluación del oráculo.

## Ejecución

```bash
python src/deutsch_jozsa.py
```

## Resultado Esperado

### Oráculo Constante

```text
{'00': 1024}
```

### Oráculo Balanceado

```text
{'01': ..., '10': ...}
```

Sin aparición del estado:

```text
00
```

## Interpretación

El algoritmo cuántico permite determinar la naturaleza de la función con una sola evaluación del oráculo.

En un algoritmo clásico para n=2 podrían requerirse hasta 3 evaluaciones.

---

# Experimento 3: Algoritmo de Grover

## Objetivo

Encontrar un elemento marcado dentro de un espacio de búsqueda de cuatro estados:

```text
00
01
10
11
```

utilizando amplificación de amplitudes.

## Ejecución

```bash
python src/grover.py
```

## Resultados Esperados

| Objetivo | Estado Más Probable |
|-----------|--------------------|
| 00 | 00 |
| 01 | 01 |
| 10 | 10 |
| 11 | 11 |

Con probabilidades superiores al 90%.

## Interpretación

Grover incrementa la probabilidad de encontrar el estado objetivo mediante:

1. Superposición uniforme.
2. Aplicación del oráculo.
3. Difusor o inversión alrededor de la media.

Para un sistema de 2 qubits solo se necesita una iteración para maximizar la probabilidad de éxito.

---

# Capturas de Evidencia

## Estado de Bell

![Bell](capturas/bell_histogram.png)

## Grover - Objetivo 00

![Grover00](capturas/grover_00.png)

## Grover - Objetivo 01

![Grover01](capturas/grover_01.png)

## Grover - Objetivo 10

![Grover10](capturas/grover_10.png)

## Grover - Objetivo 11

![Grover11](capturas/grover_11.png)

---

# Conclusiones

- Se implementó exitosamente el estado de Bell demostrando el entrelazamiento cuántico.
- Se verificó el funcionamiento del algoritmo de Deutsch-Jozsa para distinguir funciones constantes y balanceadas.
- Se implementó el algoritmo de Grover para localizar correctamente los cuatro estados posibles en un espacio de búsqueda de dos qubits.
- Los resultados obtenidos coinciden con el comportamiento teórico esperado de cada algoritmo.

---

# Commits Realizados

```bash
git commit -m "feat: estado de Bell con verificación de correlación cuántica"

git commit -m "feat: Deutsch-Jozsa con oráculos constante y balanceado para n=2"

git commit -m "feat: Grover 2 qubits — búsqueda de los 4 estados objetivo"
```

---
