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
num_qubits = 7
p = ql.Program('4mod5-bdd_287', num_qubits, platform)
p.set_sweep_points(sweep_points, num_circuits)
k = ql.Kernel('4mod5-bdd_287', platform)
k.gate('x',4)
k.gate('x',6)
k.gate('cnot',3,4)
k.gate('cnot',1,4)
k.gate('h',5)
k.gate('t',0)
k.gate('t',4)
k.gate('t',5)
k.gate('cnot',4,0)
k.gate('cnot',5,4)
k.gate('cnot',0,5)
k.gate('tdag',4)
k.gate('cnot',0,4)
k.gate('tdag',0)
k.gate('tdag',4)
k.gate('t',5)
k.gate('cnot',5,4)
k.gate('cnot',0,5)
k.gate('cnot',4,0)
k.gate('h',5)
k.gate('h',6)
k.gate('t',0)
k.gate('t',4)
k.gate('t',6)
k.gate('cnot',4,0)
k.gate('cnot',6,4)
k.gate('cnot',0,6)
k.gate('tdag',4)
k.gate('cnot',0,4)
k.gate('tdag',0)
k.gate('tdag',4)
k.gate('t',6)
k.gate('cnot',6,4)
k.gate('cnot',0,6)
k.gate('cnot',4,0)
k.gate('h',6)
k.gate('cnot',4,6)
k.gate('x',6)
k.gate('h',5)
k.gate('t',2)
k.gate('t',6)
k.gate('t',5)
k.gate('cnot',6,2)
k.gate('cnot',5,6)
k.gate('cnot',2,5)
k.gate('tdag',6)
k.gate('cnot',2,6)
k.gate('tdag',2)
k.gate('tdag',6)
k.gate('t',5)
k.gate('cnot',5,6)
k.gate('cnot',2,5)
k.gate('cnot',6,2)
k.gate('h',5)
k.gate('h',6)
k.gate('t',2)
k.gate('t',5)
k.gate('t',6)
k.gate('cnot',5,2)
k.gate('cnot',6,5)
k.gate('cnot',2,6)
k.gate('tdag',5)
k.gate('cnot',2,5)
k.gate('tdag',2)
k.gate('tdag',5)
k.gate('t',6)
k.gate('cnot',6,5)
k.gate('cnot',2,6)
k.gate('cnot',5,2)
k.gate('h',6)
p.add_kernel(k)
p.compile(optimize=False)
