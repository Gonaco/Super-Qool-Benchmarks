# Circuit generated by QLib
# Multiplier circuit
.qubit 11
qubit b0
qubit b1
qubit a0
qubit a1
qubit a2
qubit a3
qubit out0
qubit out1
qubit out2
qubit out3
qubit anc0
Prep0 a2
Prep0 a3
Prep0 out0
Prep0 out1
Prep0 out2
Prep0 out3
Prep0 anc0

.begin
Toffoli b0 a0 out0
CNOT a0 anc0
Toffoli anc0 out0 a0
Toffoli b0 a1 out1
CNOT a1 a0
Toffoli a0 out1 a1
Toffoli b0 a1 out2
Toffoli a0 out1 a1
CNOT a1 a0
Toffoli b0 a0 out1
Toffoli anc0 out0 a0 
CNOT a0 anc0
Toffoli b0 anc0 out0 
SWAP a3 a2
SWAP a2 a1
SWAP a1 a0
Toffoli b1 a0 out0
CNOT a0 anc0
Toffoli anc0 out0 a0
Toffoli b1 a1 out1
CNOT a1 a0
Toffoli a0 out1 a1
Toffoli b1 a2 out2
CNOT a2 a1
Toffoli a1 out2 a2
Toffoli b1 a2 out3
Toffoli a1 out2 a2
CNOT a2 a1
Toffoli b1 a1 out2
Toffoli a0 out1 a1
CNOT a1 a0
Toffoli b1 a0 out1
Toffoli anc0 out0 a0 
CNOT a0 anc0
Toffoli b1 anc0 out0 
SWAP a0 a1
SWAP a1 a2
SWAP a2 a3
.end