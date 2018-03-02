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
num_qubits = 14
p = ql.Program('cm42a_207', num_qubits, platform)
p.set_sweep_points(sweep_points, num_circuits)
k = ql.Kernel('cm42a_207', platform)
k.gate('x',9)
k.gate('x',8)
k.gate('x',7)
k.gate('x',6)
k.gate('x',5)
k.gate('x',4)
k.gate('x',3)
k.gate('x',1)
k.gate('x',0)
k.gate('cnot',10,2)
k.gate('x',10)
k.gate('x',13)
k.gate('h',7)
k.gate('t',10)
k.gate('t',9)
k.gate('t',7)
k.gate('cnot',9,10)
k.gate('cnot',7,9)
k.gate('cnot',10,7)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',7)
k.gate('cnot',7,9)
k.gate('cnot',10,7)
k.gate('cnot',9,10)
k.gate('h',7)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',7)
k.gate('t',10)
k.gate('t',9)
k.gate('t',7)
k.gate('cnot',9,10)
k.gate('cnot',7,9)
k.gate('cnot',10,7)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',7)
k.gate('cnot',7,9)
k.gate('cnot',10,7)
k.gate('cnot',9,10)
k.gate('h',7)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',6)
k.gate('t',10)
k.gate('t',9)
k.gate('t',6)
k.gate('cnot',9,10)
k.gate('cnot',6,9)
k.gate('cnot',10,6)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',6)
k.gate('cnot',6,9)
k.gate('cnot',10,6)
k.gate('cnot',9,10)
k.gate('h',6)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',6)
k.gate('t',10)
k.gate('t',9)
k.gate('t',6)
k.gate('cnot',9,10)
k.gate('cnot',6,9)
k.gate('cnot',10,6)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',6)
k.gate('cnot',6,9)
k.gate('cnot',10,6)
k.gate('cnot',9,10)
k.gate('h',6)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',3)
k.gate('t',10)
k.gate('t',9)
k.gate('t',3)
k.gate('cnot',9,10)
k.gate('cnot',3,9)
k.gate('cnot',10,3)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',3)
k.gate('cnot',3,9)
k.gate('cnot',10,3)
k.gate('cnot',9,10)
k.gate('h',3)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',3)
k.gate('t',10)
k.gate('t',9)
k.gate('t',3)
k.gate('cnot',9,10)
k.gate('cnot',3,9)
k.gate('cnot',10,3)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',3)
k.gate('cnot',3,9)
k.gate('cnot',10,3)
k.gate('cnot',9,10)
k.gate('h',3)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',2)
k.gate('t',10)
k.gate('t',9)
k.gate('t',2)
k.gate('cnot',9,10)
k.gate('cnot',2,9)
k.gate('cnot',10,2)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',2)
k.gate('cnot',2,9)
k.gate('cnot',10,2)
k.gate('cnot',9,10)
k.gate('h',2)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',2)
k.gate('t',10)
k.gate('t',9)
k.gate('t',2)
k.gate('cnot',9,10)
k.gate('cnot',2,9)
k.gate('cnot',10,2)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',2)
k.gate('cnot',2,9)
k.gate('cnot',10,2)
k.gate('cnot',9,10)
k.gate('h',2)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',7)
k.gate('t',10)
k.gate('t',11)
k.gate('t',7)
k.gate('cnot',11,10)
k.gate('cnot',7,11)
k.gate('cnot',10,7)
k.gate('tdag',11)
k.gate('cnot',10,11)
k.gate('tdag',10)
k.gate('tdag',11)
k.gate('t',7)
k.gate('cnot',7,11)
k.gate('cnot',10,7)
k.gate('cnot',11,10)
k.gate('h',7)
k.gate('h',11)
k.gate('t',13)
k.gate('t',12)
k.gate('t',11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',11)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('h',11)
k.gate('h',7)
k.gate('t',10)
k.gate('t',11)
k.gate('t',7)
k.gate('cnot',11,10)
k.gate('cnot',7,11)
k.gate('cnot',10,7)
k.gate('tdag',11)
k.gate('cnot',10,11)
k.gate('tdag',10)
k.gate('tdag',11)
k.gate('t',7)
k.gate('cnot',7,11)
k.gate('cnot',10,7)
k.gate('cnot',11,10)
k.gate('h',7)
k.gate('h',11)
k.gate('t',13)
k.gate('t',12)
k.gate('t',11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',11)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('h',11)
k.gate('h',6)
k.gate('t',10)
k.gate('t',11)
k.gate('t',6)
k.gate('cnot',11,10)
k.gate('cnot',6,11)
k.gate('cnot',10,6)
k.gate('tdag',11)
k.gate('cnot',10,11)
k.gate('tdag',10)
k.gate('tdag',11)
k.gate('t',6)
k.gate('cnot',6,11)
k.gate('cnot',10,6)
k.gate('cnot',11,10)
k.gate('h',6)
k.gate('h',11)
k.gate('t',13)
k.gate('t',12)
k.gate('t',11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',11)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('h',11)
k.gate('h',6)
k.gate('t',10)
k.gate('t',11)
k.gate('t',6)
k.gate('cnot',11,10)
k.gate('cnot',6,11)
k.gate('cnot',10,6)
k.gate('tdag',11)
k.gate('cnot',10,11)
k.gate('tdag',10)
k.gate('tdag',11)
k.gate('t',6)
k.gate('cnot',6,11)
k.gate('cnot',10,6)
k.gate('cnot',11,10)
k.gate('h',6)
k.gate('h',11)
k.gate('t',13)
k.gate('t',12)
k.gate('t',11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',11)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('h',11)
k.gate('x',12)
k.gate('h',5)
k.gate('t',10)
k.gate('t',9)
k.gate('t',5)
k.gate('cnot',9,10)
k.gate('cnot',5,9)
k.gate('cnot',10,5)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',5)
k.gate('cnot',5,9)
k.gate('cnot',10,5)
k.gate('cnot',9,10)
k.gate('h',5)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',5)
k.gate('t',10)
k.gate('t',9)
k.gate('t',5)
k.gate('cnot',9,10)
k.gate('cnot',5,9)
k.gate('cnot',10,5)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',5)
k.gate('cnot',5,9)
k.gate('cnot',10,5)
k.gate('cnot',9,10)
k.gate('h',5)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',4)
k.gate('t',10)
k.gate('t',9)
k.gate('t',4)
k.gate('cnot',9,10)
k.gate('cnot',4,9)
k.gate('cnot',10,4)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',4)
k.gate('cnot',4,9)
k.gate('cnot',10,4)
k.gate('cnot',9,10)
k.gate('h',4)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',4)
k.gate('t',10)
k.gate('t',9)
k.gate('t',4)
k.gate('cnot',9,10)
k.gate('cnot',4,9)
k.gate('cnot',10,4)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',4)
k.gate('cnot',4,9)
k.gate('cnot',10,4)
k.gate('cnot',9,10)
k.gate('h',4)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',4)
k.gate('t',10)
k.gate('t',13)
k.gate('t',4)
k.gate('cnot',13,10)
k.gate('cnot',4,13)
k.gate('cnot',10,4)
k.gate('tdag',13)
k.gate('cnot',10,13)
k.gate('tdag',10)
k.gate('tdag',13)
k.gate('t',4)
k.gate('cnot',4,13)
k.gate('cnot',10,4)
k.gate('cnot',13,10)
k.gate('h',4)
k.gate('h',13)
k.gate('t',12)
k.gate('t',11)
k.gate('t',13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('tdag',11)
k.gate('cnot',12,11)
k.gate('tdag',12)
k.gate('tdag',11)
k.gate('t',13)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('h',13)
k.gate('h',4)
k.gate('t',10)
k.gate('t',13)
k.gate('t',4)
k.gate('cnot',13,10)
k.gate('cnot',4,13)
k.gate('cnot',10,4)
k.gate('tdag',13)
k.gate('cnot',10,13)
k.gate('tdag',10)
k.gate('tdag',13)
k.gate('t',4)
k.gate('cnot',4,13)
k.gate('cnot',10,4)
k.gate('cnot',13,10)
k.gate('h',4)
k.gate('h',13)
k.gate('t',12)
k.gate('t',11)
k.gate('t',13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('tdag',11)
k.gate('cnot',12,11)
k.gate('tdag',12)
k.gate('tdag',11)
k.gate('t',13)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('h',13)
k.gate('h',2)
k.gate('t',10)
k.gate('t',13)
k.gate('t',2)
k.gate('cnot',13,10)
k.gate('cnot',2,13)
k.gate('cnot',10,2)
k.gate('tdag',13)
k.gate('cnot',10,13)
k.gate('tdag',10)
k.gate('tdag',13)
k.gate('t',2)
k.gate('cnot',2,13)
k.gate('cnot',10,2)
k.gate('cnot',13,10)
k.gate('h',2)
k.gate('h',13)
k.gate('t',12)
k.gate('t',11)
k.gate('t',13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('tdag',11)
k.gate('cnot',12,11)
k.gate('tdag',12)
k.gate('tdag',11)
k.gate('t',13)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('h',13)
k.gate('h',2)
k.gate('t',10)
k.gate('t',13)
k.gate('t',2)
k.gate('cnot',13,10)
k.gate('cnot',2,13)
k.gate('cnot',10,2)
k.gate('tdag',13)
k.gate('cnot',10,13)
k.gate('tdag',10)
k.gate('tdag',13)
k.gate('t',2)
k.gate('cnot',2,13)
k.gate('cnot',10,2)
k.gate('cnot',13,10)
k.gate('h',2)
k.gate('h',13)
k.gate('t',12)
k.gate('t',11)
k.gate('t',13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('tdag',11)
k.gate('cnot',12,11)
k.gate('tdag',12)
k.gate('tdag',11)
k.gate('t',13)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('h',13)
k.gate('x',11)
k.gate('h',9)
k.gate('t',10)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,10)
k.gate('cnot',9,8)
k.gate('cnot',10,9)
k.gate('tdag',8)
k.gate('cnot',10,8)
k.gate('tdag',10)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',10,9)
k.gate('cnot',8,10)
k.gate('h',9)
k.gate('h',8)
k.gate('t',11)
k.gate('t',7)
k.gate('t',8)
k.gate('cnot',7,11)
k.gate('cnot',8,7)
k.gate('cnot',11,8)
k.gate('tdag',7)
k.gate('cnot',11,7)
k.gate('tdag',11)
k.gate('tdag',7)
k.gate('t',8)
k.gate('cnot',8,7)
k.gate('cnot',11,8)
k.gate('cnot',7,11)
k.gate('h',8)
k.gate('h',7)
k.gate('t',13)
k.gate('t',12)
k.gate('t',7)
k.gate('cnot',12,13)
k.gate('cnot',7,12)
k.gate('cnot',13,7)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',7)
k.gate('cnot',7,12)
k.gate('cnot',13,7)
k.gate('cnot',12,13)
k.gate('h',7)
k.gate('h',8)
k.gate('t',11)
k.gate('t',7)
k.gate('t',8)
k.gate('cnot',7,11)
k.gate('cnot',8,7)
k.gate('cnot',11,8)
k.gate('tdag',7)
k.gate('cnot',11,7)
k.gate('tdag',11)
k.gate('tdag',7)
k.gate('t',8)
k.gate('cnot',8,7)
k.gate('cnot',11,8)
k.gate('cnot',7,11)
k.gate('h',8)
k.gate('h',9)
k.gate('t',10)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,10)
k.gate('cnot',9,8)
k.gate('cnot',10,9)
k.gate('tdag',8)
k.gate('cnot',10,8)
k.gate('tdag',10)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',10,9)
k.gate('cnot',8,10)
k.gate('h',9)
k.gate('h',8)
k.gate('t',11)
k.gate('t',7)
k.gate('t',8)
k.gate('cnot',7,11)
k.gate('cnot',8,7)
k.gate('cnot',11,8)
k.gate('tdag',7)
k.gate('cnot',11,7)
k.gate('tdag',11)
k.gate('tdag',7)
k.gate('t',8)
k.gate('cnot',8,7)
k.gate('cnot',11,8)
k.gate('cnot',7,11)
k.gate('h',8)
k.gate('h',7)
k.gate('t',13)
k.gate('t',12)
k.gate('t',7)
k.gate('cnot',12,13)
k.gate('cnot',7,12)
k.gate('cnot',13,7)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',7)
k.gate('cnot',7,12)
k.gate('cnot',13,7)
k.gate('cnot',12,13)
k.gate('h',7)
k.gate('h',8)
k.gate('t',11)
k.gate('t',7)
k.gate('t',8)
k.gate('cnot',7,11)
k.gate('cnot',8,7)
k.gate('cnot',11,8)
k.gate('tdag',7)
k.gate('cnot',11,7)
k.gate('tdag',11)
k.gate('tdag',7)
k.gate('t',8)
k.gate('cnot',8,7)
k.gate('cnot',11,8)
k.gate('cnot',7,11)
k.gate('h',8)
k.gate('h',8)
k.gate('t',10)
k.gate('t',9)
k.gate('t',8)
k.gate('cnot',9,10)
k.gate('cnot',8,9)
k.gate('cnot',10,8)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',8)
k.gate('cnot',8,9)
k.gate('cnot',10,8)
k.gate('cnot',9,10)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',7)
k.gate('t',9)
k.gate('cnot',7,11)
k.gate('cnot',9,7)
k.gate('cnot',11,9)
k.gate('tdag',7)
k.gate('cnot',11,7)
k.gate('tdag',11)
k.gate('tdag',7)
k.gate('t',9)
k.gate('cnot',9,7)
k.gate('cnot',11,9)
k.gate('cnot',7,11)
k.gate('h',9)
k.gate('h',7)
k.gate('t',13)
k.gate('t',12)
k.gate('t',7)
k.gate('cnot',12,13)
k.gate('cnot',7,12)
k.gate('cnot',13,7)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',7)
k.gate('cnot',7,12)
k.gate('cnot',13,7)
k.gate('cnot',12,13)
k.gate('h',7)
k.gate('h',9)
k.gate('t',11)
k.gate('t',7)
k.gate('t',9)
k.gate('cnot',7,11)
k.gate('cnot',9,7)
k.gate('cnot',11,9)
k.gate('tdag',7)
k.gate('cnot',11,7)
k.gate('tdag',11)
k.gate('tdag',7)
k.gate('t',9)
k.gate('cnot',9,7)
k.gate('cnot',11,9)
k.gate('cnot',7,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',10)
k.gate('t',9)
k.gate('t',8)
k.gate('cnot',9,10)
k.gate('cnot',8,9)
k.gate('cnot',10,8)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',8)
k.gate('cnot',8,9)
k.gate('cnot',10,8)
k.gate('cnot',9,10)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',7)
k.gate('t',9)
k.gate('cnot',7,11)
k.gate('cnot',9,7)
k.gate('cnot',11,9)
k.gate('tdag',7)
k.gate('cnot',11,7)
k.gate('tdag',11)
k.gate('tdag',7)
k.gate('t',9)
k.gate('cnot',9,7)
k.gate('cnot',11,9)
k.gate('cnot',7,11)
k.gate('h',9)
k.gate('h',7)
k.gate('t',13)
k.gate('t',12)
k.gate('t',7)
k.gate('cnot',12,13)
k.gate('cnot',7,12)
k.gate('cnot',13,7)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',7)
k.gate('cnot',7,12)
k.gate('cnot',13,7)
k.gate('cnot',12,13)
k.gate('h',7)
k.gate('h',9)
k.gate('t',11)
k.gate('t',7)
k.gate('t',9)
k.gate('cnot',7,11)
k.gate('cnot',9,7)
k.gate('cnot',11,9)
k.gate('tdag',7)
k.gate('cnot',11,7)
k.gate('tdag',11)
k.gate('tdag',7)
k.gate('t',9)
k.gate('cnot',9,7)
k.gate('cnot',11,9)
k.gate('cnot',7,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',10)
k.gate('t',13)
k.gate('t',8)
k.gate('cnot',13,10)
k.gate('cnot',8,13)
k.gate('cnot',10,8)
k.gate('tdag',13)
k.gate('cnot',10,13)
k.gate('tdag',10)
k.gate('tdag',13)
k.gate('t',8)
k.gate('cnot',8,13)
k.gate('cnot',10,8)
k.gate('cnot',13,10)
k.gate('h',8)
k.gate('h',13)
k.gate('t',12)
k.gate('t',11)
k.gate('t',13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('tdag',11)
k.gate('cnot',12,11)
k.gate('tdag',12)
k.gate('tdag',11)
k.gate('t',13)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('h',13)
k.gate('h',8)
k.gate('t',10)
k.gate('t',13)
k.gate('t',8)
k.gate('cnot',13,10)
k.gate('cnot',8,13)
k.gate('cnot',10,8)
k.gate('tdag',13)
k.gate('cnot',10,13)
k.gate('tdag',10)
k.gate('tdag',13)
k.gate('t',8)
k.gate('cnot',8,13)
k.gate('cnot',10,8)
k.gate('cnot',13,10)
k.gate('h',8)
k.gate('h',13)
k.gate('t',12)
k.gate('t',11)
k.gate('t',13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('tdag',11)
k.gate('cnot',12,11)
k.gate('tdag',12)
k.gate('tdag',11)
k.gate('t',13)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('h',13)
k.gate('h',6)
k.gate('t',10)
k.gate('t',13)
k.gate('t',6)
k.gate('cnot',13,10)
k.gate('cnot',6,13)
k.gate('cnot',10,6)
k.gate('tdag',13)
k.gate('cnot',10,13)
k.gate('tdag',10)
k.gate('tdag',13)
k.gate('t',6)
k.gate('cnot',6,13)
k.gate('cnot',10,6)
k.gate('cnot',13,10)
k.gate('h',6)
k.gate('h',13)
k.gate('t',12)
k.gate('t',11)
k.gate('t',13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('tdag',11)
k.gate('cnot',12,11)
k.gate('tdag',12)
k.gate('tdag',11)
k.gate('t',13)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('h',13)
k.gate('h',6)
k.gate('t',10)
k.gate('t',13)
k.gate('t',6)
k.gate('cnot',13,10)
k.gate('cnot',6,13)
k.gate('cnot',10,6)
k.gate('tdag',13)
k.gate('cnot',10,13)
k.gate('tdag',10)
k.gate('tdag',13)
k.gate('t',6)
k.gate('cnot',6,13)
k.gate('cnot',10,6)
k.gate('cnot',13,10)
k.gate('h',6)
k.gate('h',13)
k.gate('t',12)
k.gate('t',11)
k.gate('t',13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('tdag',11)
k.gate('cnot',12,11)
k.gate('tdag',12)
k.gate('tdag',11)
k.gate('t',13)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('h',13)
k.gate('x',10)
k.gate('h',0)
k.gate('t',10)
k.gate('t',9)
k.gate('t',0)
k.gate('cnot',9,10)
k.gate('cnot',0,9)
k.gate('cnot',10,0)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',0)
k.gate('cnot',0,9)
k.gate('cnot',10,0)
k.gate('cnot',9,10)
k.gate('h',0)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',0)
k.gate('t',10)
k.gate('t',9)
k.gate('t',0)
k.gate('cnot',9,10)
k.gate('cnot',0,9)
k.gate('cnot',10,0)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',0)
k.gate('cnot',0,9)
k.gate('cnot',10,0)
k.gate('cnot',9,10)
k.gate('h',0)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',1)
k.gate('t',10)
k.gate('t',9)
k.gate('t',1)
k.gate('cnot',9,10)
k.gate('cnot',1,9)
k.gate('cnot',10,1)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',1)
k.gate('cnot',1,9)
k.gate('cnot',10,1)
k.gate('cnot',9,10)
k.gate('h',1)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',1)
k.gate('t',10)
k.gate('t',9)
k.gate('t',1)
k.gate('cnot',9,10)
k.gate('cnot',1,9)
k.gate('cnot',10,1)
k.gate('tdag',9)
k.gate('cnot',10,9)
k.gate('tdag',10)
k.gate('tdag',9)
k.gate('t',1)
k.gate('cnot',1,9)
k.gate('cnot',10,1)
k.gate('cnot',9,10)
k.gate('h',1)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',8)
k.gate('t',13)
k.gate('t',12)
k.gate('t',8)
k.gate('cnot',12,13)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('tdag',12)
k.gate('cnot',13,12)
k.gate('tdag',13)
k.gate('tdag',12)
k.gate('t',8)
k.gate('cnot',8,12)
k.gate('cnot',13,8)
k.gate('cnot',12,13)
k.gate('h',8)
k.gate('h',9)
k.gate('t',11)
k.gate('t',8)
k.gate('t',9)
k.gate('cnot',8,11)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('tdag',8)
k.gate('cnot',11,8)
k.gate('tdag',11)
k.gate('tdag',8)
k.gate('t',9)
k.gate('cnot',9,8)
k.gate('cnot',11,9)
k.gate('cnot',8,11)
k.gate('h',9)
k.gate('h',0)
k.gate('t',10)
k.gate('t',13)
k.gate('t',0)
k.gate('cnot',13,10)
k.gate('cnot',0,13)
k.gate('cnot',10,0)
k.gate('tdag',13)
k.gate('cnot',10,13)
k.gate('tdag',10)
k.gate('tdag',13)
k.gate('t',0)
k.gate('cnot',0,13)
k.gate('cnot',10,0)
k.gate('cnot',13,10)
k.gate('h',0)
k.gate('h',13)
k.gate('t',12)
k.gate('t',11)
k.gate('t',13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('tdag',11)
k.gate('cnot',12,11)
k.gate('tdag',12)
k.gate('tdag',11)
k.gate('t',13)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('h',13)
k.gate('h',0)
k.gate('t',10)
k.gate('t',13)
k.gate('t',0)
k.gate('cnot',13,10)
k.gate('cnot',0,13)
k.gate('cnot',10,0)
k.gate('tdag',13)
k.gate('cnot',10,13)
k.gate('tdag',10)
k.gate('tdag',13)
k.gate('t',0)
k.gate('cnot',0,13)
k.gate('cnot',10,0)
k.gate('cnot',13,10)
k.gate('h',0)
k.gate('h',13)
k.gate('t',12)
k.gate('t',11)
k.gate('t',13)
k.gate('cnot',11,12)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('tdag',11)
k.gate('cnot',12,11)
k.gate('tdag',12)
k.gate('tdag',11)
k.gate('t',13)
k.gate('cnot',13,11)
k.gate('cnot',12,13)
k.gate('cnot',11,12)
k.gate('h',13)
k.gate('x',10)
k.gate('h',6)
k.gate('t',11)
k.gate('t',10)
k.gate('t',6)
k.gate('cnot',10,11)
k.gate('cnot',6,10)
k.gate('cnot',11,6)
k.gate('tdag',10)
k.gate('cnot',11,10)
k.gate('tdag',11)
k.gate('tdag',10)
k.gate('t',6)
k.gate('cnot',6,10)
k.gate('cnot',11,6)
k.gate('cnot',10,11)
k.gate('h',6)
k.gate('h',2)
k.gate('t',11)
k.gate('t',10)
k.gate('t',2)
k.gate('cnot',10,11)
k.gate('cnot',2,10)
k.gate('cnot',11,2)
k.gate('tdag',10)
k.gate('cnot',11,10)
k.gate('tdag',11)
k.gate('tdag',10)
k.gate('t',2)
k.gate('cnot',2,10)
k.gate('cnot',11,2)
k.gate('cnot',10,11)
k.gate('h',2)
p.add_kernel(k)
p.compile(optimize=False)
