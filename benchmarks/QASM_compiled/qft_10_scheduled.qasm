qubits 10

.qft_10
    h q0 
    qwait 1
    cnot q0,q1 
    qwait 3
    cnot q0,q1 
    qwait 3
    cnot q0,q2 
    qwait 3
    cnot q0,q2 
    qwait 1
    h q1 
    qwait 1
    { cnot q1,q2  | cnot q0,q3  }
    qwait 3
    { cnot q1,q2  | cnot q0,q3  }
    qwait 3
    { cnot q1,q3  | cnot q0,q4  }
    qwait 3
    { cnot q1,q3  | cnot q0,q4  }
    qwait 1
    h q2 
    qwait 1
    { cnot q2,q3  | cnot q1,q4  | cnot q0,q5  }
    qwait 3
    { cnot q2,q3  | cnot q1,q4  | cnot q0,q5  }
    qwait 3
    { cnot q2,q4  | cnot q1,q5  | cnot q0,q6  }
    qwait 3
    { cnot q2,q4  | cnot q1,q5  | cnot q0,q6  }
    qwait 1
    h q3 
    qwait 1
    { cnot q3,q4  | cnot q2,q5  | cnot q1,q6  | cnot q0,q7  }
    qwait 3
    { cnot q3,q4  | cnot q2,q5  | cnot q1,q6  | cnot q0,q7  }
    qwait 3
    { cnot q3,q5  | cnot q2,q6  | cnot q1,q7  | cnot q0,q8  }
    qwait 3
    { cnot q3,q5  | cnot q2,q6  | cnot q1,q7  | cnot q0,q8  }
    qwait 1
    h q4 
    qwait 1
    { cnot q4,q5  | cnot q3,q6  | cnot q2,q7  | cnot q1,q8  | cnot q0,q9  }
    qwait 3
    { cnot q4,q5  | cnot q3,q6  | cnot q2,q7  | cnot q1,q8  | cnot q0,q9  }
    qwait 3
    { cnot q4,q6  | cnot q3,q7  | cnot q2,q8  | cnot q1,q9  }
    qwait 3
    { cnot q4,q6  | cnot q3,q7  | cnot q2,q8  | cnot q1,q9  }
    qwait 1
    h q5 
    qwait 1
    { cnot q5,q6  | cnot q4,q7  | cnot q3,q8  | cnot q2,q9  }
    qwait 3
    { cnot q5,q6  | cnot q4,q7  | cnot q3,q8  | cnot q2,q9  }
    qwait 3
    { cnot q5,q7  | cnot q4,q8  | cnot q3,q9  }
    qwait 3
    { cnot q5,q7  | cnot q4,q8  | cnot q3,q9  }
    qwait 1
    h q6 
    qwait 1
    { cnot q6,q7  | cnot q5,q8  | cnot q4,q9  }
    qwait 3
    { cnot q6,q7  | cnot q5,q8  | cnot q4,q9  }
    qwait 3
    { cnot q6,q8  | cnot q5,q9  }
    qwait 3
    { cnot q6,q8  | cnot q5,q9  }
    qwait 1
    h q7 
    qwait 1
    { cnot q7,q8  | cnot q6,q9  }
    qwait 3
    { cnot q7,q8  | cnot q6,q9  }
    qwait 3
    cnot q7,q9 
    qwait 3
    cnot q7,q9 
    qwait 1
    h q8 
    qwait 1
    cnot q8,q9 
    qwait 3
    cnot q8,q9 
    qwait 3
    h q9 
    qwait 1
    { h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1

