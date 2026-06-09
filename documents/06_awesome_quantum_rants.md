# Awesome Quantum: The Opinionated List
*A community-curated list of quantum computing resources, with actual honest commentary.*

## Frameworks
*   **IBM Qiskit**: The elephant in the room. It has the biggest community and the most tutorials. **Hot take:** It's also bloated, incredibly slow for large simulations, and the API changes constantly. But you have to learn it because it's the industry standard.
*   **Google Cirq**: Google's framework. **Hot take:** Much cleaner Python code than Qiskit, designed by actual software engineers. However, the documentation is sparse, and the community is much smaller.
*   **Pennylane**: Built by Xanadu. **Hot take:** The absolute best framework if you specifically want to do Quantum Machine Learning (QML). It integrates natively with PyTorch and NumPy. 

## Simulators (When you don't have real quantum hardware)
*   **QuTiP**: A fast, C++ based simulator. Excellent for simulating noise and decoherence.
*   **Aer (Qiskit's simulator)**: Good enough for beginners, but terrible memory management if you try to simulate more than 24 qubits on your laptop. Your computer will crash.

## Books
*   **Quantum Computation and Quantum Information (Nielsen & Chuang)**: Known as "Mike and Ike". **Hot take:** This is the holy bible of the field, but it is TERRIBLE for beginners. It's a dense physics textbook. Do not start here unless you love math.
*   **Dancing with Qubits (Robert S. Sutor)**: The best actual entry-level book for developers. It walks you through the math gently.