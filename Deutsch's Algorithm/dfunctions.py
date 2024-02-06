from qiskit import QuantumCircuit as qcir

def dfunctions(case: int):
    """
    This is a python function simulating a deutch function.
    i.e. It will imitate all the possibilities of a f:{0,1}->{0,1}
    
    The functions based on their input output pairs will be of 4 possibilities.
    Lets take the input 0:
    then we have, f(0)=0 or f(0)=1
    Similarly,
    For input of 1:
    We have, f(1)=1 or f(1)=0
    
    We can now see this functions in detail as:
    case 1:
        f(0)=0 and f(1)=0
        Literally, no operation is happening.
        if we vissulaize this as a circuit.
        Because, irrespective of the input, ouput=0.
    case 2: 
        f(0)=0 and f(1)=1
        Here, its bit different.
        Input=Ouput here. 
    case 3:
        f(0)=1 and f(1)=0
        Here, it looks like NOT(Input)
    case 4:
        f(0)=1 and f(1)=1
        Again, no operation is happening.
        if we vissulaize this as a circuit.
        Because, irrespective of the input, ouput=1.
        
    Lets summarise what we saw:
    case 1: 
        Alaways output is zero.
        Thinking of practical implementation:
            And default for any circuit, input=0
            So, its better to leave it off.
            Like no input is provided.
            So, let it be zero.
    case 2: 
        Alaways output=input.
        Thinking of practical implementation:
            Here, we have a difference.
            It is that, our output is not fixed.
            (like in earlier case).
            So, we need some kinda measure.
            To change the output as per the input,
            We can use the CNOT gate.
            Here, we can manipulate output by this.
            If we keep it to |0> then we are done.
            i.e. it will be input = ouput.
    case 3: 
        Alaways output is opposit of input.
        Thinking of practical implementation:
            We have this similar to case 2.
            Just the difference is that,
            we have to apply X gate after CNOT
            (x gate acts as not)
    case 4: 
        Alaways output is one.
        Thinking of practical implementation:
            And default for any circuit, input=0
            So, lets add X gate to keep it 1.
            
    Then we will add this to Quantum Circuit.
    The Quantum Circuit will implement Deutch's Algorithm.
    """
    if case not in [1,2,3,4]:
        raise ValueError(f"Case {case} is not a valid case.\nThe input is expected between 1 to 4.")
    
    f=qcir(2) #2 Quantum Bit space and no classical bits for measuring.
    
    if case in [2,3]: #here CNOT operation for cases 2 and 3.
        f.cx(0,1)
    if case in [3,4]: #here 3 is once again because of CNOT and then X gate
        f.x(1) #X gate is applied on 3 and 4 to perform classical equivalent NOT operation
        
    return f #function being returned.

