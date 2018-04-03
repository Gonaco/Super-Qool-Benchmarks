# Circuit generated by QLib
# Cuccaro's Adder
# arXiv:quant-ph/0410184v1 
# 43 bit quantum adder

.qubit 88

qubit c0
qubit a0
qubit b0
qubit a1
qubit b1
qubit a2
qubit b2
qubit a3
qubit b3
qubit a4
qubit b4
qubit a5
qubit b5
qubit a6
qubit b6
qubit a7
qubit b7
qubit a8
qubit b8
qubit a9
qubit b9
qubit a10
qubit b10
qubit a11
qubit b11
qubit a12
qubit b12
qubit a13
qubit b13
qubit a14
qubit b14
qubit a15
qubit b15
qubit a16
qubit b16
qubit a17
qubit b17
qubit a18
qubit b18
qubit a19
qubit b19
qubit a20
qubit b20
qubit a21
qubit b21
qubit a22
qubit b22
qubit a23
qubit b23
qubit a24
qubit b24
qubit a25
qubit b25
qubit a26
qubit b26
qubit a27
qubit b27
qubit a28
qubit b28
qubit a29
qubit b29
qubit a30
qubit b30
qubit a31
qubit b31
qubit a32
qubit b32
qubit a33
qubit b33
qubit a34
qubit b34
qubit a35
qubit b35
qubit a36
qubit b36
qubit a37
qubit b37
qubit a38
qubit b38
qubit a39
qubit b39
qubit a40
qubit b40
qubit a41
qubit b41
qubit a42
qubit b42
qubit z

.begin
CNOT a0 b0
CNOT a0 c0
Toffoli c0 b0 a0
CNOT a1 b1
CNOT a1 a0
Toffoli a0 b1 a1
CNOT a2 b2
CNOT a2 a1
Toffoli a1 b2 a2
CNOT a3 b3
CNOT a3 a2
Toffoli a2 b3 a3
CNOT a4 b4
CNOT a4 a3
Toffoli a3 b4 a4
CNOT a5 b5
CNOT a5 a4
Toffoli a4 b5 a5
CNOT a6 b6
CNOT a6 a5
Toffoli a5 b6 a6
CNOT a7 b7
CNOT a7 a6
Toffoli a6 b7 a7
CNOT a8 b8
CNOT a8 a7
Toffoli a7 b8 a8
CNOT a9 b9
CNOT a9 a8
Toffoli a8 b9 a9
CNOT a10 b10
CNOT a10 a9
Toffoli a9 b10 a10
CNOT a11 b11
CNOT a11 a10
Toffoli a10 b11 a11
CNOT a12 b12
CNOT a12 a11
Toffoli a11 b12 a12
CNOT a13 b13
CNOT a13 a12
Toffoli a12 b13 a13
CNOT a14 b14
CNOT a14 a13
Toffoli a13 b14 a14
CNOT a15 b15
CNOT a15 a14
Toffoli a14 b15 a15
CNOT a16 b16
CNOT a16 a15
Toffoli a15 b16 a16
CNOT a17 b17
CNOT a17 a16
Toffoli a16 b17 a17
CNOT a18 b18
CNOT a18 a17
Toffoli a17 b18 a18
CNOT a19 b19
CNOT a19 a18
Toffoli a18 b19 a19
CNOT a20 b20
CNOT a20 a19
Toffoli a19 b20 a20
CNOT a21 b21
CNOT a21 a20
Toffoli a20 b21 a21
CNOT a22 b22
CNOT a22 a21
Toffoli a21 b22 a22
CNOT a23 b23
CNOT a23 a22
Toffoli a22 b23 a23
CNOT a24 b24
CNOT a24 a23
Toffoli a23 b24 a24
CNOT a25 b25
CNOT a25 a24
Toffoli a24 b25 a25
CNOT a26 b26
CNOT a26 a25
Toffoli a25 b26 a26
CNOT a27 b27
CNOT a27 a26
Toffoli a26 b27 a27
CNOT a28 b28
CNOT a28 a27
Toffoli a27 b28 a28
CNOT a29 b29
CNOT a29 a28
Toffoli a28 b29 a29
CNOT a30 b30
CNOT a30 a29
Toffoli a29 b30 a30
CNOT a31 b31
CNOT a31 a30
Toffoli a30 b31 a31
CNOT a32 b32
CNOT a32 a31
Toffoli a31 b32 a32
CNOT a33 b33
CNOT a33 a32
Toffoli a32 b33 a33
CNOT a34 b34
CNOT a34 a33
Toffoli a33 b34 a34
CNOT a35 b35
CNOT a35 a34
Toffoli a34 b35 a35
CNOT a36 b36
CNOT a36 a35
Toffoli a35 b36 a36
CNOT a37 b37
CNOT a37 a36
Toffoli a36 b37 a37
CNOT a38 b38
CNOT a38 a37
Toffoli a37 b38 a38
CNOT a39 b39
CNOT a39 a38
Toffoli a38 b39 a39
CNOT a40 b40
CNOT a40 a39
Toffoli a39 b40 a40
CNOT a41 b41
CNOT a41 a40
Toffoli a40 b41 a41
CNOT a42 b42
CNOT a42 a41
Toffoli a41 b42 a42
CNOT a42 z
Toffoli a41 b42 a42
CNOT a42 a41
CNOT a41 b42
Toffoli a40 b41 a41
CNOT a41 a40
CNOT a40 b41
Toffoli a39 b40 a40
CNOT a40 a39
CNOT a39 b40
Toffoli a38 b39 a39
CNOT a39 a38
CNOT a38 b39
Toffoli a37 b38 a38
CNOT a38 a37
CNOT a37 b38
Toffoli a36 b37 a37
CNOT a37 a36
CNOT a36 b37
Toffoli a35 b36 a36
CNOT a36 a35
CNOT a35 b36
Toffoli a34 b35 a35
CNOT a35 a34
CNOT a34 b35
Toffoli a33 b34 a34
CNOT a34 a33
CNOT a33 b34
Toffoli a32 b33 a33
CNOT a33 a32
CNOT a32 b33
Toffoli a31 b32 a32
CNOT a32 a31
CNOT a31 b32
Toffoli a30 b31 a31
CNOT a31 a30
CNOT a30 b31
Toffoli a29 b30 a30
CNOT a30 a29
CNOT a29 b30
Toffoli a28 b29 a29
CNOT a29 a28
CNOT a28 b29
Toffoli a27 b28 a28
CNOT a28 a27
CNOT a27 b28
Toffoli a26 b27 a27
CNOT a27 a26
CNOT a26 b27
Toffoli a25 b26 a26
CNOT a26 a25
CNOT a25 b26
Toffoli a24 b25 a25
CNOT a25 a24
CNOT a24 b25
Toffoli a23 b24 a24
CNOT a24 a23
CNOT a23 b24
Toffoli a22 b23 a23
CNOT a23 a22
CNOT a22 b23
Toffoli a21 b22 a22
CNOT a22 a21
CNOT a21 b22
Toffoli a20 b21 a21
CNOT a21 a20
CNOT a20 b21
Toffoli a19 b20 a20
CNOT a20 a19
CNOT a19 b20
Toffoli a18 b19 a19
CNOT a19 a18
CNOT a18 b19
Toffoli a17 b18 a18
CNOT a18 a17
CNOT a17 b18
Toffoli a16 b17 a17
CNOT a17 a16
CNOT a16 b17
Toffoli a15 b16 a16
CNOT a16 a15
CNOT a15 b16
Toffoli a14 b15 a15
CNOT a15 a14
CNOT a14 b15
Toffoli a13 b14 a14
CNOT a14 a13
CNOT a13 b14
Toffoli a12 b13 a13
CNOT a13 a12
CNOT a12 b13
Toffoli a11 b12 a12
CNOT a12 a11
CNOT a11 b12
Toffoli a10 b11 a11
CNOT a11 a10
CNOT a10 b11
Toffoli a9 b10 a10
CNOT a10 a9
CNOT a9 b10
Toffoli a8 b9 a9
CNOT a9 a8
CNOT a8 b9
Toffoli a7 b8 a8
CNOT a8 a7
CNOT a7 b8
Toffoli a6 b7 a7
CNOT a7 a6
CNOT a6 b7
Toffoli a5 b6 a6
CNOT a6 a5
CNOT a5 b6
Toffoli a4 b5 a5
CNOT a5 a4
CNOT a4 b5
Toffoli a3 b4 a4
CNOT a4 a3
CNOT a3 b4
Toffoli a2 b3 a3
CNOT a3 a2
CNOT a2 b3
Toffoli a1 b2 a2
CNOT a2 a1
CNOT a1 b2
Toffoli a0 b1 a1
CNOT a1 a0
CNOT a0 b1
Toffoli c0 b0 a0
CNOT a0 c0
CNOT c0 b0
.end