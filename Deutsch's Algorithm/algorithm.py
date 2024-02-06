from qiskit import QuantumCircuit as qcir
from qiskit_aer import AerSimulator as simulator
from circuit import circuit

def dalg(function: qcir):
    """
    dalg: Deutch's Algorithm
    Now, to our already done work,
    we will accumulate everything.
    And then run the circuit.
    This run is using a simulator.
    (Simulator: AerSimulator)
    Its a popular simulator.
    It even models noise.
    """
    
    #getting ready with whole circuit
    qc=circuit(function)
    
    #storing the result after running the simulator
    result=simulator().run(qc, shots=1, memory=True).result()
    """
    I know that the upper line is a bit too much or sudden.
    Let me explain that to you.
    Here, we are using a quantum simulator to simulate our circuit.
    To run our circuit in simulator,
        we provide it .i.e. 'qc' here as an argument.
        No. of times it has to run or shots = 1 (once)
        Should it store detail information about the shot?
            For the sake of debugging and much more, we do store
            This stores the detail information in result object
            if its false then it dosen't
        After providing all of this circuit runs.
    The circuit stores its run's result information in result object.
    This object contains so many other values too.
    We will only use those which we require.
    """
    
    #checking the data stroed in classical bit after execution.
    measurements=result.get_memory()
    
    #For our understanding lets print this measurement varaible.
    print("The mesurements made are:", measurements)
    
    if measurements[0]=="0":
        return "The function is constant."
    
    return "The function is balanced."
    
