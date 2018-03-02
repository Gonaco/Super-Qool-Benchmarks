qubits 13

.ising_model_13
    { h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1
    { cnot q10,q11  | cnot q8,q9  | cnot q6,q7  | cnot q4,q5  | cnot q2,q3  | cnot q0,q1  }
    qwait 3
    { cnot q10,q11  | cnot q8,q9  | cnot q6,q7  | cnot q4,q5  | cnot q2,q3  | cnot q0,q1  }
    qwait 1
    h q12 
    qwait 1
    { cnot q11,q12  | cnot q9,q10  | cnot q7,q8  | cnot q5,q6  | cnot q3,q4  | cnot q1,q2  }
    qwait 3
    { cnot q11,q12  | cnot q9,q10  | cnot q7,q8  | cnot q5,q6  | cnot q3,q4  | cnot q1,q2  }
    qwait 3
    { h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1
    { h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1
    { cnot q10,q11  | cnot q8,q9  | cnot q6,q7  | cnot q4,q5  | cnot q2,q3  | cnot q0,q1  }
    qwait 3
    { cnot q10,q11  | cnot q8,q9  | cnot q6,q7  | cnot q4,q5  | cnot q2,q3  | cnot q0,q1  | h q12  }
    qwait 1
    h q12 
    qwait 1
    { cnot q11,q12  | cnot q9,q10  | cnot q7,q8  | cnot q5,q6  | cnot q3,q4  | cnot q1,q2  }
    qwait 3
    { cnot q11,q12  | cnot q9,q10  | cnot q7,q8  | cnot q5,q6  | cnot q3,q4  | cnot q1,q2  }
    qwait 3
    { h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1
    { h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1
    { cnot q10,q11  | cnot q8,q9  | cnot q6,q7  | cnot q4,q5  | cnot q2,q3  | cnot q0,q1  }
    qwait 3
    { cnot q10,q11  | cnot q8,q9  | cnot q6,q7  | cnot q4,q5  | cnot q2,q3  | cnot q0,q1  | h q12  }
    qwait 1
    h q12 
    qwait 1
    { cnot q11,q12  | cnot q9,q10  | cnot q7,q8  | cnot q5,q6  | cnot q3,q4  | cnot q1,q2  }
    qwait 3
    { cnot q11,q12  | cnot q9,q10  | cnot q7,q8  | cnot q5,q6  | cnot q3,q4  | cnot q1,q2  }
    qwait 3
    { h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1
    { h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1
    { cnot q10,q11  | cnot q8,q9  | cnot q6,q7  | cnot q4,q5  | cnot q2,q3  | cnot q0,q1  }
    qwait 3
    { cnot q10,q11  | cnot q8,q9  | cnot q6,q7  | cnot q4,q5  | cnot q2,q3  | cnot q0,q1  | h q12  }
    qwait 1
    h q12 
    qwait 1
    { cnot q11,q12  | cnot q9,q10  | cnot q7,q8  | cnot q5,q6  | cnot q3,q4  | cnot q1,q2  }
    qwait 3
    { cnot q11,q12  | cnot q9,q10  | cnot q7,q8  | cnot q5,q6  | cnot q3,q4  | cnot q1,q2  }
    qwait 3
    { h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1
    { h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1
    { cnot q10,q11  | cnot q8,q9  | cnot q6,q7  | cnot q4,q5  | cnot q2,q3  | cnot q0,q1  }
    qwait 3
    { cnot q10,q11  | cnot q8,q9  | cnot q6,q7  | cnot q4,q5  | cnot q2,q3  | cnot q0,q1  | h q12  }
    qwait 1
    h q12 
    qwait 1
    { cnot q11,q12  | cnot q9,q10  | cnot q7,q8  | cnot q5,q6  | cnot q3,q4  | cnot q1,q2  }
    qwait 3
    { cnot q11,q12  | cnot q9,q10  | cnot q7,q8  | cnot q5,q6  | cnot q3,q4  | cnot q1,q2  }
    qwait 3
    { h q12  | h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1
    { h q12  | h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1

