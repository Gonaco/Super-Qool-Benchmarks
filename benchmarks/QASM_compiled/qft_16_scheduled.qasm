qubits 16

.qft_16
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
    { cnot q4,q6  | cnot q3,q7  | cnot q2,q8  | cnot q1,q9  | cnot q0,q10  }
    qwait 3
    { cnot q4,q6  | cnot q3,q7  | cnot q2,q8  | cnot q1,q9  | cnot q0,q10  }
    qwait 1
    h q5 
    qwait 1
    { cnot q5,q6  | cnot q4,q7  | cnot q3,q8  | cnot q2,q9  | cnot q1,q10  | cnot q0,q11  }
    qwait 3
    { cnot q5,q6  | cnot q4,q7  | cnot q3,q8  | cnot q2,q9  | cnot q1,q10  | cnot q0,q11  }
    qwait 3
    { cnot q5,q7  | cnot q4,q8  | cnot q3,q9  | cnot q2,q10  | cnot q1,q11  | cnot q0,q12  }
    qwait 3
    { cnot q5,q7  | cnot q4,q8  | cnot q3,q9  | cnot q2,q10  | cnot q1,q11  | cnot q0,q12  }
    qwait 1
    h q6 
    qwait 1
    { cnot q6,q7  | cnot q5,q8  | cnot q4,q9  | cnot q3,q10  | cnot q2,q11  | cnot q1,q12  | cnot q0,q13  }
    qwait 3
    { cnot q6,q7  | cnot q5,q8  | cnot q4,q9  | cnot q3,q10  | cnot q2,q11  | cnot q1,q12  | cnot q0,q13  }
    qwait 3
    { cnot q6,q8  | cnot q5,q9  | cnot q4,q10  | cnot q3,q11  | cnot q2,q12  | cnot q1,q13  | cnot q0,q14  }
    qwait 3
    { cnot q6,q8  | cnot q5,q9  | cnot q4,q10  | cnot q3,q11  | cnot q2,q12  | cnot q1,q13  | cnot q0,q14  }
    qwait 1
    h q7 
    qwait 1
    { cnot q7,q8  | cnot q6,q9  | cnot q5,q10  | cnot q4,q11  | cnot q3,q12  | cnot q2,q13  | cnot q1,q14  | cnot q0,q15  }
    qwait 3
    { cnot q7,q8  | cnot q6,q9  | cnot q5,q10  | cnot q4,q11  | cnot q3,q12  | cnot q2,q13  | cnot q1,q14  | cnot q0,q15  }
    qwait 3
    { cnot q7,q9  | cnot q6,q10  | cnot q5,q11  | cnot q4,q12  | cnot q3,q13  | cnot q2,q14  | cnot q1,q15  }
    qwait 3
    { cnot q7,q9  | cnot q6,q10  | cnot q5,q11  | cnot q4,q12  | cnot q3,q13  | cnot q2,q14  | cnot q1,q15  }
    qwait 1
    h q8 
    qwait 1
    { cnot q8,q9  | cnot q7,q10  | cnot q6,q11  | cnot q5,q12  | cnot q4,q13  | cnot q3,q14  | cnot q2,q15  }
    qwait 3
    { cnot q8,q9  | cnot q7,q10  | cnot q6,q11  | cnot q5,q12  | cnot q4,q13  | cnot q3,q14  | cnot q2,q15  }
    qwait 3
    { cnot q8,q10  | cnot q7,q11  | cnot q6,q12  | cnot q5,q13  | cnot q4,q14  | cnot q3,q15  }
    qwait 3
    { cnot q8,q10  | cnot q7,q11  | cnot q6,q12  | cnot q5,q13  | cnot q4,q14  | cnot q3,q15  }
    qwait 1
    h q9 
    qwait 1
    { cnot q9,q10  | cnot q8,q11  | cnot q7,q12  | cnot q6,q13  | cnot q5,q14  | cnot q4,q15  }
    qwait 3
    { cnot q9,q10  | cnot q8,q11  | cnot q7,q12  | cnot q6,q13  | cnot q5,q14  | cnot q4,q15  }
    qwait 3
    { cnot q9,q11  | cnot q8,q12  | cnot q7,q13  | cnot q6,q14  | cnot q5,q15  }
    qwait 3
    { cnot q9,q11  | cnot q8,q12  | cnot q7,q13  | cnot q6,q14  | cnot q5,q15  }
    qwait 1
    h q10 
    qwait 1
    { cnot q10,q11  | cnot q9,q12  | cnot q8,q13  | cnot q7,q14  | cnot q6,q15  }
    qwait 3
    { cnot q10,q11  | cnot q9,q12  | cnot q8,q13  | cnot q7,q14  | cnot q6,q15  }
    qwait 3
    { cnot q10,q12  | cnot q9,q13  | cnot q8,q14  | cnot q7,q15  }
    qwait 3
    { cnot q10,q12  | cnot q9,q13  | cnot q8,q14  | cnot q7,q15  }
    qwait 1
    h q11 
    qwait 1
    { cnot q11,q12  | cnot q10,q13  | cnot q9,q14  | cnot q8,q15  }
    qwait 3
    { cnot q11,q12  | cnot q10,q13  | cnot q9,q14  | cnot q8,q15  }
    qwait 3
    { cnot q11,q13  | cnot q10,q14  | cnot q9,q15  }
    qwait 3
    { cnot q11,q13  | cnot q10,q14  | cnot q9,q15  }
    qwait 1
    h q12 
    qwait 1
    { cnot q12,q13  | cnot q11,q14  | cnot q10,q15  }
    qwait 3
    { cnot q12,q13  | cnot q11,q14  | cnot q10,q15  }
    qwait 3
    { cnot q12,q14  | cnot q11,q15  }
    qwait 3
    { cnot q12,q14  | cnot q11,q15  }
    qwait 1
    h q13 
    qwait 1
    { cnot q13,q14  | cnot q12,q15  }
    qwait 3
    { cnot q13,q14  | cnot q12,q15  }
    qwait 3
    cnot q13,q15 
    qwait 3
    cnot q13,q15 
    qwait 1
    h q14 
    qwait 1
    cnot q14,q15 
    qwait 3
    cnot q14,q15 
    qwait 3
    h q15 
    qwait 1
    { h q15  | h q14  | h q13  | h q12  | h q11  | h q10  | h q9  | h q8  | h q7  | h q6  | h q5  | h q4  | h q3  | h q2  | h q1  | h q0  }
    qwait 1

