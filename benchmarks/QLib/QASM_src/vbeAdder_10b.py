from openql import openql as ql
import os
import numpy as np
curdir = os.path.dirname(__file__)
output_dir = os.path.join(curdir, 'test_output')
ql.set_output_dir(output_dir)
config_fn = os.path.join(curdir, '/home/daniel/Master/Quantum_Computing_and_Quantum_Information/OpenQL/tests/hardware_config_cc_light.json')
platform  = ql.Platform('platform_none', config_fn)
sweep_points = [1,2]
num_circuits = 1
num_qubits = 32
p = ql.Program('vbeAdder_10b', num_qubits, platform)
p.set_sweep_points(sweep_points, num_circuits)
k = ql.Kernel('vbeAdder_10b', platform)
k.gate('toffoli',1b1,c1)
k.gate('cnot',1b1)
k.gate('toffoli',0b1,c1)
k.gate('toffoli',4b2,c2)
k.gate('cnot',4b2)
k.gate('toffoli',3b2,c2)
k.gate('toffoli',7b3,c3)
k.gate('cnot',7b3)
k.gate('toffoli',6b3,c3)
k.gate('toffoli',10b4,c4)
k.gate('cnot',10b4)
k.gate('toffoli',9b4,c4)
k.gate('toffoli',13b5,c5)
k.gate('cnot',13b5)
k.gate('toffoli',12b5,c5)
k.gate('toffoli',16b6,c6)
k.gate('cnot',16b6)
k.gate('toffoli',15b6,c6)
k.gate('toffoli',19b7,c7)
k.gate('cnot',19b7)
k.gate('toffoli',18b7,c7)
k.gate('toffoli',22b8,c8)
k.gate('cnot',22b8)
k.gate('toffoli',21b8,c8)
k.gate('toffoli',25b9,c9)
k.gate('cnot',25b9)
k.gate('toffoli',24b9,c9)
k.gate('toffoli',28b10,c10)
k.gate('cnot',28b10)
k.gate('toffoli',27b10,c10)
k.gate('cnot',28b10)
k.gate('toffoli',24b9,c9)
k.gate('cnot',25b9)
k.gate('toffoli',25b9,c9)
k.gate('cnot',25b9)
k.gate('cnot',24b9)
k.gate('toffoli',21b8,c8)
k.gate('cnot',22b8)
k.gate('toffoli',22b8,c8)
k.gate('cnot',22b8)
k.gate('cnot',21b8)
k.gate('toffoli',18b7,c7)
k.gate('cnot',19b7)
k.gate('toffoli',19b7,c7)
k.gate('cnot',19b7)
k.gate('cnot',18b7)
k.gate('toffoli',15b6,c6)
k.gate('cnot',16b6)
k.gate('toffoli',16b6,c6)
k.gate('cnot',16b6)
k.gate('cnot',15b6)
k.gate('toffoli',12b5,c5)
k.gate('cnot',13b5)
k.gate('toffoli',13b5,c5)
k.gate('cnot',13b5)
k.gate('cnot',12b5)
k.gate('toffoli',9b4,c4)
k.gate('cnot',10b4)
k.gate('toffoli',10b4,c4)
k.gate('cnot',10b4)
k.gate('cnot',9b4)
k.gate('toffoli',6b3,c3)
k.gate('cnot',7b3)
k.gate('toffoli',7b3,c3)
k.gate('cnot',7b3)
k.gate('cnot',6b3)
k.gate('toffoli',3b2,c2)
k.gate('cnot',4b2)
k.gate('toffoli',4b2,c2)
k.gate('cnot',4b2)
k.gate('cnot',3b2)
k.gate('toffoli',0b1,c1)
k.gate('cnot',1b1)
k.gate('toffoli',1b1,c1)
k.gate('cnot',1b1)
k.gate('cnot',0b1)
p.add_kernel(k)
p.compile(optimize=False)
