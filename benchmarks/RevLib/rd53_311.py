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
num_qubits = 13
p = ql.Program('rd53_311', num_qubits, platform)
p.set_sweep_points(sweep_points, num_circuits)
k = ql.Kernel('rd53_311', platform)
k.gate('x',11)
k.gate('cnot',3,5)
k.gate('h',5)
k.gate('t',3)
k.gate('t',4)
k.gate('t',5)
k.gate('cnot',4,3)
k.gate('cnot',5,4)
k.gate('cnot',3,5)
k.gate('tdag',4)
k.gate('cnot',3,4)
k.gate('tdag',3)
k.gate('tdag',4)
k.gate('t',5)
k.gate('cnot',5,4)
k.gate('cnot',3,5)
k.gate('cnot',4,3)
k.gate('h',5)
k.gate('cnot',4,5)
k.gate('h',6)
k.gate('t',3)
k.gate('t',4)
k.gate('t',6)
k.gate('cnot',4,3)
k.gate('cnot',6,4)
k.gate('cnot',3,6)
k.gate('tdag',4)
k.gate('cnot',3,4)
k.gate('tdag',3)
k.gate('tdag',4)
k.gate('t',6)
k.gate('cnot',6,4)
k.gate('cnot',3,6)
k.gate('cnot',4,3)
k.gate('h',6)
k.gate('cnot',6,7)
k.gate('h',7)
k.gate('t',0)
k.gate('t',5)
k.gate('t',7)
k.gate('cnot',5,0)
k.gate('cnot',7,5)
k.gate('cnot',0,7)
k.gate('tdag',5)
k.gate('cnot',0,5)
k.gate('tdag',0)
k.gate('tdag',5)
k.gate('t',7)
k.gate('cnot',7,5)
k.gate('cnot',0,7)
k.gate('cnot',5,0)
k.gate('h',7)
k.gate('h',7)
k.gate('t',0)
k.gate('t',6)
k.gate('t',7)
k.gate('cnot',6,0)
k.gate('cnot',7,6)
k.gate('cnot',0,7)
k.gate('tdag',6)
k.gate('cnot',0,6)
k.gate('tdag',0)
k.gate('tdag',6)
k.gate('t',7)
k.gate('cnot',7,6)
k.gate('cnot',0,7)
k.gate('cnot',6,0)
k.gate('h',7)
k.gate('h',8)
k.gate('t',0)
k.gate('t',6)
k.gate('t',8)
k.gate('cnot',6,0)
k.gate('cnot',8,6)
k.gate('cnot',0,8)
k.gate('tdag',6)
k.gate('cnot',0,6)
k.gate('tdag',0)
k.gate('tdag',6)
k.gate('t',8)
k.gate('cnot',8,6)
k.gate('cnot',0,8)
k.gate('cnot',6,0)
k.gate('h',8)
k.gate('cnot',8,9)
k.gate('h',9)
k.gate('t',2)
k.gate('t',7)
k.gate('t',9)
k.gate('cnot',7,2)
k.gate('cnot',9,7)
k.gate('cnot',2,9)
k.gate('tdag',7)
k.gate('cnot',2,7)
k.gate('tdag',2)
k.gate('tdag',7)
k.gate('t',9)
k.gate('cnot',9,7)
k.gate('cnot',2,9)
k.gate('cnot',7,2)
k.gate('h',9)
k.gate('h',9)
k.gate('t',2)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,2)
k.gate('cnot',9,8)
k.gate('cnot',2,9)
k.gate('tdag',8)
k.gate('cnot',2,8)
k.gate('tdag',2)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',2,9)
k.gate('cnot',8,2)
k.gate('h',9)
k.gate('h',10)
k.gate('t',2)
k.gate('t',8)
k.gate('t',10)
k.gate('cnot',8,2)
k.gate('cnot',10,8)
k.gate('cnot',2,10)
k.gate('tdag',8)
k.gate('cnot',2,8)
k.gate('tdag',2)
k.gate('tdag',8)
k.gate('t',10)
k.gate('cnot',10,8)
k.gate('cnot',2,10)
k.gate('cnot',8,2)
k.gate('h',10)
k.gate('cnot',10,9)
k.gate('h',10)
k.gate('t',1)
k.gate('t',9)
k.gate('t',10)
k.gate('cnot',9,1)
k.gate('cnot',10,9)
k.gate('cnot',1,10)
k.gate('tdag',9)
k.gate('cnot',1,9)
k.gate('tdag',1)
k.gate('tdag',9)
k.gate('t',10)
k.gate('cnot',10,9)
k.gate('cnot',1,10)
k.gate('cnot',9,1)
k.gate('h',10)
k.gate('cnot',3,11)
k.gate('cnot',4,11)
k.gate('cnot',0,11)
k.gate('x',11)
k.gate('cnot',2,11)
k.gate('x',11)
k.gate('cnot',1,11)
k.gate('x',11)
k.gate('x',5)
k.gate('h',6)
k.gate('t',0)
k.gate('t',5)
k.gate('t',6)
k.gate('cnot',5,0)
k.gate('cnot',6,5)
k.gate('cnot',0,6)
k.gate('tdag',5)
k.gate('cnot',0,5)
k.gate('tdag',0)
k.gate('tdag',5)
k.gate('t',6)
k.gate('cnot',6,5)
k.gate('cnot',0,6)
k.gate('cnot',5,0)
k.gate('h',6)
k.gate('h',5)
k.gate('t',0)
k.gate('t',6)
k.gate('t',5)
k.gate('cnot',6,0)
k.gate('cnot',5,6)
k.gate('cnot',0,5)
k.gate('tdag',6)
k.gate('cnot',0,6)
k.gate('tdag',0)
k.gate('tdag',6)
k.gate('t',5)
k.gate('cnot',5,6)
k.gate('cnot',0,5)
k.gate('cnot',6,0)
k.gate('h',5)
k.gate('cnot',5,12)
k.gate('h',12)
k.gate('t',2)
k.gate('t',7)
k.gate('t',12)
k.gate('cnot',7,2)
k.gate('cnot',12,7)
k.gate('cnot',2,12)
k.gate('tdag',7)
k.gate('cnot',2,7)
k.gate('tdag',2)
k.gate('tdag',7)
k.gate('t',12)
k.gate('cnot',12,7)
k.gate('cnot',2,12)
k.gate('cnot',7,2)
k.gate('h',12)
k.gate('h',12)
k.gate('t',2)
k.gate('t',5)
k.gate('t',12)
k.gate('cnot',5,2)
k.gate('cnot',12,5)
k.gate('cnot',2,12)
k.gate('tdag',5)
k.gate('cnot',2,5)
k.gate('tdag',2)
k.gate('tdag',5)
k.gate('t',12)
k.gate('cnot',12,5)
k.gate('cnot',2,12)
k.gate('cnot',5,2)
k.gate('h',12)
k.gate('x',7)
k.gate('h',5)
k.gate('t',2)
k.gate('t',7)
k.gate('t',5)
k.gate('cnot',7,2)
k.gate('cnot',5,7)
k.gate('cnot',2,5)
k.gate('tdag',7)
k.gate('cnot',2,7)
k.gate('tdag',2)
k.gate('tdag',7)
k.gate('t',5)
k.gate('cnot',5,7)
k.gate('cnot',2,5)
k.gate('cnot',7,2)
k.gate('h',5)
k.gate('h',7)
k.gate('t',2)
k.gate('t',5)
k.gate('t',7)
k.gate('cnot',5,2)
k.gate('cnot',7,5)
k.gate('cnot',2,7)
k.gate('tdag',5)
k.gate('cnot',2,5)
k.gate('tdag',2)
k.gate('tdag',5)
k.gate('t',7)
k.gate('cnot',7,5)
k.gate('cnot',2,7)
k.gate('cnot',5,2)
k.gate('h',7)
k.gate('cnot',7,12)
k.gate('h',7)
k.gate('t',1)
k.gate('t',12)
k.gate('t',7)
k.gate('cnot',12,1)
k.gate('cnot',7,12)
k.gate('cnot',1,7)
k.gate('tdag',12)
k.gate('cnot',1,12)
k.gate('tdag',1)
k.gate('tdag',12)
k.gate('t',7)
k.gate('cnot',7,12)
k.gate('cnot',1,7)
k.gate('cnot',12,1)
k.gate('h',7)
k.gate('x',7)
p.add_kernel(k)
p.compile(optimize=False)
