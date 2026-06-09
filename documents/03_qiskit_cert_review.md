# My Honest Review of the IBM Qiskit Developer Certification

I recently took the IBM Qiskit Developer Certification exam (exam code C1000-112). At $200, it's not cheap, so here is my unfiltered take on whether it's worth it and how to pass.

**Is it worth it?**
If you have zero professional experience in quantum computing and want to get your resume noticed by recruiters, yes. It proves you understand the basics of quantum circuits and can write code using IBM's framework. However, it will *not* get you a job on its own. It's a stepping stone.

**The Exam Format**
It's a 60-question multiple-choice test. You have 90 minutes. You need roughly a 68% to pass. It is heavily focused on Qiskit syntax. You aren't just asked "what does a Hadamard gate do?", you are asked "which of these 4 code snippets correctly applies a Hadamard gate to qubit 0 and measures it into classical bit 1?"

**How to Study**
Do not bother reading textbooks on quantum physics for this. The best resource is the official Qiskit Textbook (the online, interactive one). Specifically, memorize the syntax for `QuantumCircuit`, `execute`, and `Aer` simulators. 

A huge gotcha: IBM frequently updates Qiskit. Make sure you are studying the version of Qiskit that the exam is currently testing! When I took it, the exam was testing Qiskit 0.28, even though 0.39 was already out, meaning some functions on the test were actually deprecated in the real world. Check the syllabus carefully.