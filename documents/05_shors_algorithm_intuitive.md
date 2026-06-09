# Physics StackExchange: An intuitive, non-textbook explanation of Shor's algorithm for programmers

**Question:** I'm a software engineer. Every explanation of Shor's Algorithm (the one that breaks RSA encryption) gets bogged down in quantum Fourier transforms and bra-ket notation. Can someone explain it in plain programming concepts?

**Answer:**
Think of RSA encryption like multiplying two massive prime numbers together. Multiplying is easy (fast), but factoring the result back into the two primes is impossibly hard (slow) for classical computers. 

Shor's algorithm cheats. It turns the factoring problem into a *period-finding* problem. 

Imagine you have a repeating sequence of numbers. A classical computer has to look at the numbers one by one to find the repeating pattern. Shor's algorithm uses a quantum computer to look at *all possible numbers at once* (superposition). 

Then, it uses a trick called the Quantum Fourier Transform (QFT). Think of QFT like a noise-canceling headphone. It causes the wrong answers to cancel each other out (destructive interference) and amplifies the correct answer (constructive interference). When you finally measure the quantum state, the only answer left standing is the period of the sequence.

Once you have the period, classical math takes over. You run the period through a simple classical algorithm (the Euclidean algorithm), and boom—you have the prime factors. RSA is broken. But don't panic, a quantum computer large enough and stable enough to run Shor's on a real 2048-bit RSA key doesn't exist yet, and likely won't for at least 10-15 years.