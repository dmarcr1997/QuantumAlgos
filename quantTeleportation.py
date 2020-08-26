import random
import numpy as np
import cirq 
from cirq import H, CNOT, Y, X, CZ, measure

def make_quantum_tele_circuit(randX, randY):
    circuit = cirq.Circuit()
    msg, alice, bob = LineQubit.range(3)
    
    circuit.append([H(alice), CNOT(alice, bob)])

    circuit.append([X(msg)**randX, Y(msg)**randY])

    circuit.append([CNOT(msg, alice), H(msg)])
    circuit.append([measure(msg, alice)])

    circuit.append([CNOT(alice, bob), CZ(msg, bob)])

    return circuit


def main(seed=None):
    random.seed(seed)

    ranX = random.random()
    ranY = random.random()
    circuit = make_quantum_tele_circuit(ranX, ranY)

    print("Circuit:")
    print(circuit)

    sim = cirq.Simulator(seed=seed)

    # Run a simple simulation that applies the random X and Y gates that
    # create our message.
    q0 = cirq.LineQubit(0)
    message = sim.simulate(cirq.Circuit([cirq.X(q0)**ranX, cirq.Y(q0)**ranY]))

    print("\nBloch Sphere of Message After Random X and Y Gates:")
    # Prints the Bloch Sphere of the Message after the X and Y gates.
    expected = cirq.bloch_vector_from_state_vector(message.final_state_vector,
                                                    0)
    print("x: ", np.around(expected[0], 4), "y: ", np.around(expected[1], 4),
            "z: ", np.around(expected[2], 4))

    # Records the final state of the simulation.
    final_results = sim.simulate(circuit)

    print("\nBloch Sphere of Qubit 2 at Final State:")
    # Prints the Bloch Sphere of Bob's entangled qubit at the final state.
    teleported = cirq.bloch_vector_from_state_vector(
        final_results.final_state_vector, 2)
    print("x: ", np.around(teleported[0], 4), "y: ",
            np.around(teleported[1], 4), "z: ", np.around(teleported[2], 4))


if __name__ == '__main__':
    main()