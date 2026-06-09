# Unofficial FAQ: MIT Quantum Hackathon (Discord Archive)

**Q: Do I need to know quantum physics to participate?**
A: No! Every team needs a mix of skills. We need UI/UX designers to build frontends for quantum apps, classical backend devs to handle the APIs, and presenters. Only 1-2 people on a 4-person team actually need to know how to write the Qiskit code.

**Q: Will we run our code on real quantum computers?**
A: Yes and No. You will develop and test your code on local simulators (like Qiskit Aer) because it's fast. For your final submission, you will be given API credits to send ONE run to an actual IBM quantum machine. Expect a queue time of 2-4 hours, so submit your final run early on Sunday! Do not wait until the last minute.

**Q: What makes a winning project?**
A: Don't try to invent a new quantum algorithm; you only have 48 hours. The winning projects usually take an existing algorithm (like QAOA or VQE) and apply it to a cool, visual use case. Last year's winner used a quantum algorithm to generate procedural music, and built a really slick web app to play it. 

**Q: Why are my simulator results perfect, but the real hardware results are trash?**
A: Welcome to the NISQ era! Real qubits are noisy. They suffer from thermal relaxation and gate errors. If your circuit has a depth of more than 30 gates, the noise will overwhelm the signal. You must use error mitigation techniques (like Zero Noise Extrapolation) or keep your circuits very shallow. 

**Q: Where is the free food?**
A: Pizza arrives at 7 PM on Friday in the main lobby. The Red Bull is locked in the sponsor room and is supposedly for mentors only, but if you ask nicely, they'll give you one.