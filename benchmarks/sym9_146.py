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
num_qubits = 12
p = ql.Program('sym9_146', num_qubits, platform)
p.set_sweep_points(sweep_points, num_circuits)
k = ql.Kernel('sym9_146', platform)
k.gate('h',9)
k.gate('t',0)
k.gate('t',1)
k.gate('t',9)
k.gate('cnot',1,0)
k.gate('cnot',9,1)
k.gate('cnot',0,9)
k.gate('tdag',1)
k.gate('cnot',0,1)
k.gate('tdag',0)
k.gate('tdag',1)
k.gate('t',9)
k.gate('cnot',9,1)
k.gate('cnot',0,9)
k.gate('cnot',1,0)
k.gate('h',9)
k.gate('cnot',0,1)
k.gate('h',10)
k.gate('t',2)
k.gate('t',9)
k.gate('t',10)
k.gate('cnot',9,2)
k.gate('cnot',10,9)
k.gate('cnot',2,10)
k.gate('tdag',9)
k.gate('cnot',2,9)
k.gate('tdag',2)
k.gate('tdag',9)
k.gate('t',10)
k.gate('cnot',10,9)
k.gate('cnot',2,10)
k.gate('cnot',9,2)
k.gate('h',10)
k.gate('h',9)
k.gate('t',1)
k.gate('t',2)
k.gate('t',9)
k.gate('cnot',2,1)
k.gate('cnot',9,2)
k.gate('cnot',1,9)
k.gate('tdag',2)
k.gate('cnot',1,2)
k.gate('tdag',1)
k.gate('tdag',2)
k.gate('t',9)
k.gate('cnot',9,2)
k.gate('cnot',1,9)
k.gate('cnot',2,1)
k.gate('h',9)
k.gate('cnot',1,2)
k.gate('h',11)
k.gate('t',3)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,3)
k.gate('cnot',11,10)
k.gate('cnot',3,11)
k.gate('tdag',10)
k.gate('cnot',3,10)
k.gate('tdag',3)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',3,11)
k.gate('cnot',10,3)
k.gate('h',11)
k.gate('h',10)
k.gate('t',3)
k.gate('t',9)
k.gate('t',10)
k.gate('cnot',9,3)
k.gate('cnot',10,9)
k.gate('cnot',3,10)
k.gate('tdag',9)
k.gate('cnot',3,9)
k.gate('tdag',3)
k.gate('tdag',9)
k.gate('t',10)
k.gate('cnot',10,9)
k.gate('cnot',3,10)
k.gate('cnot',9,3)
k.gate('h',10)
k.gate('h',9)
k.gate('t',2)
k.gate('t',3)
k.gate('t',9)
k.gate('cnot',3,2)
k.gate('cnot',9,3)
k.gate('cnot',2,9)
k.gate('tdag',3)
k.gate('cnot',2,3)
k.gate('tdag',2)
k.gate('tdag',3)
k.gate('t',9)
k.gate('cnot',9,3)
k.gate('cnot',2,9)
k.gate('cnot',3,2)
k.gate('h',9)
k.gate('cnot',2,3)
k.gate('h',11)
k.gate('t',4)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,4)
k.gate('cnot',11,10)
k.gate('cnot',4,11)
k.gate('tdag',10)
k.gate('cnot',4,10)
k.gate('tdag',4)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',4,11)
k.gate('cnot',10,4)
k.gate('h',11)
k.gate('h',10)
k.gate('t',4)
k.gate('t',9)
k.gate('t',10)
k.gate('cnot',9,4)
k.gate('cnot',10,9)
k.gate('cnot',4,10)
k.gate('tdag',9)
k.gate('cnot',4,9)
k.gate('tdag',4)
k.gate('tdag',9)
k.gate('t',10)
k.gate('cnot',10,9)
k.gate('cnot',4,10)
k.gate('cnot',9,4)
k.gate('h',10)
k.gate('h',9)
k.gate('t',3)
k.gate('t',4)
k.gate('t',9)
k.gate('cnot',4,3)
k.gate('cnot',9,4)
k.gate('cnot',3,9)
k.gate('tdag',4)
k.gate('cnot',3,4)
k.gate('tdag',3)
k.gate('tdag',4)
k.gate('t',9)
k.gate('cnot',9,4)
k.gate('cnot',3,9)
k.gate('cnot',4,3)
k.gate('h',9)
k.gate('cnot',3,4)
k.gate('h',11)
k.gate('t',5)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,5)
k.gate('cnot',11,10)
k.gate('cnot',5,11)
k.gate('tdag',10)
k.gate('cnot',5,10)
k.gate('tdag',5)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',5,11)
k.gate('cnot',10,5)
k.gate('h',11)
k.gate('h',10)
k.gate('t',5)
k.gate('t',9)
k.gate('t',10)
k.gate('cnot',9,5)
k.gate('cnot',10,9)
k.gate('cnot',5,10)
k.gate('tdag',9)
k.gate('cnot',5,9)
k.gate('tdag',5)
k.gate('tdag',9)
k.gate('t',10)
k.gate('cnot',10,9)
k.gate('cnot',5,10)
k.gate('cnot',9,5)
k.gate('h',10)
k.gate('h',9)
k.gate('t',4)
k.gate('t',5)
k.gate('t',9)
k.gate('cnot',5,4)
k.gate('cnot',9,5)
k.gate('cnot',4,9)
k.gate('tdag',5)
k.gate('cnot',4,5)
k.gate('tdag',4)
k.gate('tdag',5)
k.gate('t',9)
k.gate('cnot',9,5)
k.gate('cnot',4,9)
k.gate('cnot',5,4)
k.gate('h',9)
k.gate('cnot',4,5)
k.gate('h',11)
k.gate('t',6)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,6)
k.gate('cnot',11,10)
k.gate('cnot',6,11)
k.gate('tdag',10)
k.gate('cnot',6,10)
k.gate('tdag',6)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',6,11)
k.gate('cnot',10,6)
k.gate('h',11)
k.gate('h',10)
k.gate('t',6)
k.gate('t',9)
k.gate('t',10)
k.gate('cnot',9,6)
k.gate('cnot',10,9)
k.gate('cnot',6,10)
k.gate('tdag',9)
k.gate('cnot',6,9)
k.gate('tdag',6)
k.gate('tdag',9)
k.gate('t',10)
k.gate('cnot',10,9)
k.gate('cnot',6,10)
k.gate('cnot',9,6)
k.gate('h',10)
k.gate('h',9)
k.gate('t',5)
k.gate('t',6)
k.gate('t',9)
k.gate('cnot',6,5)
k.gate('cnot',9,6)
k.gate('cnot',5,9)
k.gate('tdag',6)
k.gate('cnot',5,6)
k.gate('tdag',5)
k.gate('tdag',6)
k.gate('t',9)
k.gate('cnot',9,6)
k.gate('cnot',5,9)
k.gate('cnot',6,5)
k.gate('h',9)
k.gate('cnot',5,6)
k.gate('h',11)
k.gate('t',7)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,7)
k.gate('cnot',11,10)
k.gate('cnot',7,11)
k.gate('tdag',10)
k.gate('cnot',7,10)
k.gate('tdag',7)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',7,11)
k.gate('cnot',10,7)
k.gate('h',11)
k.gate('h',10)
k.gate('t',7)
k.gate('t',9)
k.gate('t',10)
k.gate('cnot',9,7)
k.gate('cnot',10,9)
k.gate('cnot',7,10)
k.gate('tdag',9)
k.gate('cnot',7,9)
k.gate('tdag',7)
k.gate('tdag',9)
k.gate('t',10)
k.gate('cnot',10,9)
k.gate('cnot',7,10)
k.gate('cnot',9,7)
k.gate('h',10)
k.gate('h',9)
k.gate('t',6)
k.gate('t',7)
k.gate('t',9)
k.gate('cnot',7,6)
k.gate('cnot',9,7)
k.gate('cnot',6,9)
k.gate('tdag',7)
k.gate('cnot',6,7)
k.gate('tdag',6)
k.gate('tdag',7)
k.gate('t',9)
k.gate('cnot',9,7)
k.gate('cnot',6,9)
k.gate('cnot',7,6)
k.gate('h',9)
k.gate('cnot',6,7)
k.gate('h',11)
k.gate('t',8)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,8)
k.gate('cnot',11,10)
k.gate('cnot',8,11)
k.gate('tdag',10)
k.gate('cnot',8,10)
k.gate('tdag',8)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',8,11)
k.gate('cnot',10,8)
k.gate('h',11)
k.gate('h',10)
k.gate('t',8)
k.gate('t',9)
k.gate('t',10)
k.gate('cnot',9,8)
k.gate('cnot',10,9)
k.gate('cnot',8,10)
k.gate('tdag',9)
k.gate('cnot',8,9)
k.gate('tdag',8)
k.gate('tdag',9)
k.gate('t',10)
k.gate('cnot',10,9)
k.gate('cnot',8,10)
k.gate('cnot',9,8)
k.gate('h',10)
k.gate('cnot',10,11)
p.add_kernel(k)
p.compile(optimize=False)
