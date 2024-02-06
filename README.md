# D-Alg: Deutsch's Algorithm

## Overview

This GitHub repository, named D-Alg, focuses on Deutsch's Algorithm, a fundamental quantum computing concept. The provided Python code implements the algorithm using the Qiskit library. Below is an overview of the code and its underlying principles.

## Concept

Deutsch's Algorithm is a quantum algorithm designed to solve a specific problem efficiently. The problem involves determining whether a given quantum function is constant or balanced. The algorithm achieves this with only one query to the function, showcasing the power of quantum parallelism.

The algorithm considers four possible cases for a Deutsch function (f: {0,1} -> {0,1}):

1. **Constant 0**: The function always outputs 0.
2. **Identity**: The function outputs the input itself.
3. **Negation**: The function outputs the opposite of the input.
4. **Constant 1**: The function always outputs 1.

Each case is represented by a quantum circuit, and the code provides a Python function, `dfunctions`, to simulate these circuits based on the given case.

## Code Structure

The code is divided into three main functions:

1. **dfunctions**: Simulates the Deutsch function circuit for a specified case (1 to 4). Returns the corresponding quantum circuit.

2. **circuit**: Constructs the full Deutsch algorithm circuit using the Deutsch function. The input is set to |0⟩ for the first qubit, and |1⟩ is created using the X gate. The circuit includes Hadamard gates, function application, and measurements.

3. **dalg**: Combines the previous functions to execute Deutsch's Algorithm and determine whether the given function is constant or balanced.

## Usage

To use this code, ensure you have the necessary packages installed. You can set up your environment by installing the required packages using the following command:

```bash
pip install qiskit qiskit_aer
```

The main functionality is provided by the `dalg` function, which prints the measurements and indicates whether the function is constant or balanced.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/WuiiiGithub/D-Alg.git
cd D-Alg
cd "Deutsch's Algorithm"
```

2. Install dependencies:

```bash
pip install qiskit
pip install qiskit_aer
```

3. Run the code:

```bash
python main.py
```
