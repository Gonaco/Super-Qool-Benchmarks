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
num_qubits = 4
p = ql.Program('decod24-v2_43', num_qubits, platform)
p.set_sweep_points(sweep_points, num_circuits)
k = ql.Kernel('decod24-v2_43', platform)
k.gate('x',0)
k.gate('h',0)
k.gate('t',3)
k.gate('t',2)
k.gate('t',0)
k.gate('cnot',2,3)
k.gate('cnot',0,2)
k.gate('cnot',3,0)
k.gate('tdag',2)
k.gate('cnot',3,2)
k.gate('tdag',3)
k.gate('tdag',2)
k.gate('t',0)
k.gate('cnot',0,2)
k.gate('cnot',3,0)
k.gate('cnot',2,3)
k.gate('h',0)
k.gate('h',3)
k.gate('t',2)
k.gate('t',0)
k.gate('t',3)
k.gate('cnot',0,2)
k.gate('cnot',3,0)
k.gate('cnot',2,3)
k.gate('tdag',0)
k.gate('cnot',2,0)
k.gate('tdag',2)
k.gate('tdag',0)
k.gate('t',3)
k.gate('cnot',3,0)
k.gate('cnot',2,3)
k.gate('cnot',0,2)
k.gate('h',3)
k.gate('h',1)
k.gate('t',0)
k.gate('t',2)
k.gate('t',1)
k.gate('cnot',2,0)
k.gate('cnot',1,2)
k.gate('cnot',0,1)
k.gate('tdag',2)
k.gate('cnot',0,2)
k.gate('tdag',0)
k.gate('tdag',2)
k.gate('t',1)
k.gate('cnot',1,2)
k.gate('cnot',0,1)
k.gate('cnot',2,0)
k.gate('h',1)
k.gate('cnot',3,2)
k.gate('x',0)
k.gate('x',3)
p.add_kernel(k)
p.compile(optimize=False)
