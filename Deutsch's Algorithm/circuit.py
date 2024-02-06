from qiskit import QuantumCircuit as qcir

def circuit(function: qcir):
    """
    This is a function which makes the full circuit.
    It takes the deutch function to use as a parameter.
    Yea, the same function which we created.
    
    Now, we will make a 2 input Quantum Circuit.
    And we will have one classical bit to measure our output.
    This is as per our Deutch Algorithm Circuit.
    """
    
    #making the circuit as said
    qc=qcir(2,1)
    
    #now setting input as q0 as already 0 by default
    #And for q1 we use X gate to make 1
    qc.x(0)
    
    #Lets apply a line to do proper cegrigation
    qc.barrier()
    
    #Applying hadarmard gate to create superposition on all qubits
    qc.h([0,1])
    
    #Now after hadarmard. Lets apply cegrigation and go to next state
    qc.barrier()
    
    #Now lets add our function
    #We do that using compose method of quantum circuit object
    qc.compose(function, inplace=True)
    
    #Now, to indicate function is over lets apply one more cegrigator or barrier
    qc.barrier()
    
    #Now again lets apply hadarmard to all inputs
    qc.h(0)
        
    #Now lets apply a measure gate to measure the output
    qc.measure(0,0)
    
    #Now lets return this circuit to make everything like done
    return qc
