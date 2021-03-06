# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""
Simulator instruction to save unitary matrix.
"""

from qiskit.circuit import QuantumCircuit
from .save_data import SaveSingleData, default_qubits


class SaveUnitary(SaveSingleData):
    """Save Unitary"""
    def __init__(self, key, num_qubits, pershot=False):
        """Create new instruction to save the unitary simulator state.

        Args:
            key (str): the key for retrieving saved data from results.
            num_qubits (int): the number of qubits of the
            pershot (bool): if True save a list of unitaries for each
                            shot of the simulation rather than a single
                            statevector [Default: False].

        .. note::

            This save instruction must always be performed on the full width of
            qubits in a circuit, otherwise an exception will be raised during
            simulation.
        """
        super().__init__('save_unitary',
                         key,
                         num_qubits,
                         pershot=pershot)


def save_unitary(self, key, pershot=False):
    """Save the current state of the unitary simulator.

    Args:
        key (str): the key for retrieving saved data from results.
        pershot (bool): if True save a list of unitaries for each
                        shot of the simulation [Default: False].

    Returns:
        QuantumCircuit: with attached instruction.

    .. note:

        This instruction is always defined across all qubits in a circuit.
    """
    qubits = default_qubits(self)
    instr = SaveUnitary(key,
                        len(qubits),
                        pershot=pershot)
    return self.append(instr, qubits)


QuantumCircuit.save_unitary = save_unitary
