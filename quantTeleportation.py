import random
import numpy as np
import cirq 
from cirq import H, CNOT, Y, X, CZ, measure

def mak_quantum_tele_circuit(randX, randY):
    circuit = cirq.Circuit()
    msg, alice, bob = cirq.LineQubit.range(3)
    
    circuit.append([H(alice), CNOT(alice, bob)])

    circuit.append([X(msg)**randX, Y(msg)**randY])

    circuit.append([CNOT(msg, alice), H(msg)])
    circuit.append([measure(msg, alice)])

    circuit.append([CNOT(alice, bob), CZ(msg, bob)])

    return circuit