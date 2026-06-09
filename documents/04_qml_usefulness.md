# r/learnmachinelearning: Is Quantum Machine Learning actually useful yet?

**User: ML_Student_22**
I'm looking for a thesis topic. Is Quantum Machine Learning (QML) actually outperforming classical ML right now, or is it just hype?

**Comment: tensor_flow_rider**
Right now? Pure hype. There is currently no proven "quantum advantage" for machine learning on real, existing hardware. You can train a neural network much faster on an Nvidia A100 GPU than on any quantum computer available today. 

**Comment: qml_researcher**
It's true that classical GPUs win today, but that's not the point of research. The interesting part of QML is Quantum Support Vector Machines (QSVMs) and Quantum Neural Networks (QNNs). Quantum computers can process data in a high-dimensional Hilbert space exponentially faster than classical computers. The bottleneck is loading classical data *into* the quantum state (the I/O problem). If your data is already quantum (e.g., studying chemical reactions), QML is incredibly promising.

**Comment: data_cynic**
Beware of "quantum washing". A lot of companies claim to use QML, but what they really do is run a standard classical ML model, and maybe use a quantum simulator to generate one random feature. If you want a job in ML today, stick to PyTorch and classical transformers. If you want an academic career for the 2030s, study QML.