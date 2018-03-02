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
p = ql.Program('cm152a_212', num_qubits, platform)
p.set_sweep_points(sweep_points, num_circuits)
k = ql.Kernel('cm152a_212', platform)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',4)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,4)
k.gate('cnot',10,3)
k.gate('cnot',4,10)
k.gate('tdag',3)
k.gate('cnot',4,3)
k.gate('tdag',4)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',4,10)
k.gate('cnot',3,4)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',4)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,4)
k.gate('cnot',10,3)
k.gate('cnot',4,10)
k.gate('tdag',3)
k.gate('cnot',4,3)
k.gate('tdag',4)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',4,10)
k.gate('cnot',3,4)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',8)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,8)
k.gate('cnot',10,3)
k.gate('cnot',8,10)
k.gate('tdag',3)
k.gate('cnot',8,3)
k.gate('tdag',8)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',8,10)
k.gate('cnot',3,8)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',8)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,8)
k.gate('cnot',10,3)
k.gate('cnot',8,10)
k.gate('tdag',3)
k.gate('cnot',8,3)
k.gate('tdag',8)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',8,10)
k.gate('cnot',3,8)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',2)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,2)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('tdag',11)
k.gate('cnot',2,11)
k.gate('tdag',2)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('cnot',11,2)
k.gate('h',0)
k.gate('h',11)
k.gate('t',8)
k.gate('t',3)
k.gate('t',11)
k.gate('cnot',3,8)
k.gate('cnot',11,3)
k.gate('cnot',8,11)
k.gate('tdag',3)
k.gate('cnot',8,3)
k.gate('tdag',8)
k.gate('tdag',3)
k.gate('t',11)
k.gate('cnot',11,3)
k.gate('cnot',8,11)
k.gate('cnot',3,8)
k.gate('h',11)
k.gate('h',0)
k.gate('t',2)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,2)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('tdag',11)
k.gate('cnot',2,11)
k.gate('tdag',2)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('cnot',11,2)
k.gate('h',0)
k.gate('h',11)
k.gate('t',8)
k.gate('t',3)
k.gate('t',11)
k.gate('cnot',3,8)
k.gate('cnot',11,3)
k.gate('cnot',8,11)
k.gate('tdag',3)
k.gate('cnot',8,3)
k.gate('tdag',8)
k.gate('tdag',3)
k.gate('t',11)
k.gate('cnot',11,3)
k.gate('cnot',8,11)
k.gate('cnot',3,8)
k.gate('h',11)
k.gate('x',2)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',6)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,6)
k.gate('cnot',10,3)
k.gate('cnot',6,10)
k.gate('tdag',3)
k.gate('cnot',6,3)
k.gate('tdag',6)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',6,10)
k.gate('cnot',3,6)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',6)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,6)
k.gate('cnot',10,3)
k.gate('cnot',6,10)
k.gate('tdag',3)
k.gate('cnot',6,3)
k.gate('tdag',6)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',6,10)
k.gate('cnot',3,6)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',9)
k.gate('t',11)
k.gate('cnot',9,2)
k.gate('cnot',11,9)
k.gate('cnot',2,11)
k.gate('tdag',9)
k.gate('cnot',2,9)
k.gate('tdag',2)
k.gate('tdag',9)
k.gate('t',11)
k.gate('cnot',11,9)
k.gate('cnot',2,11)
k.gate('cnot',9,2)
k.gate('h',11)
k.gate('h',9)
k.gate('t',10)
k.gate('t',3)
k.gate('t',9)
k.gate('cnot',3,10)
k.gate('cnot',9,3)
k.gate('cnot',10,9)
k.gate('tdag',3)
k.gate('cnot',10,3)
k.gate('tdag',10)
k.gate('tdag',3)
k.gate('t',9)
k.gate('cnot',9,3)
k.gate('cnot',10,9)
k.gate('cnot',3,10)
k.gate('h',9)
k.gate('h',11)
k.gate('t',2)
k.gate('t',9)
k.gate('t',11)
k.gate('cnot',9,2)
k.gate('cnot',11,9)
k.gate('cnot',2,11)
k.gate('tdag',9)
k.gate('cnot',2,9)
k.gate('tdag',2)
k.gate('tdag',9)
k.gate('t',11)
k.gate('cnot',11,9)
k.gate('cnot',2,11)
k.gate('cnot',9,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',9)
k.gate('t',11)
k.gate('cnot',9,2)
k.gate('cnot',11,9)
k.gate('cnot',2,11)
k.gate('tdag',9)
k.gate('cnot',2,9)
k.gate('tdag',2)
k.gate('tdag',9)
k.gate('t',11)
k.gate('cnot',11,9)
k.gate('cnot',2,11)
k.gate('cnot',9,2)
k.gate('h',11)
k.gate('h',9)
k.gate('t',10)
k.gate('t',3)
k.gate('t',9)
k.gate('cnot',3,10)
k.gate('cnot',9,3)
k.gate('cnot',10,9)
k.gate('tdag',3)
k.gate('cnot',10,3)
k.gate('tdag',10)
k.gate('tdag',3)
k.gate('t',9)
k.gate('cnot',9,3)
k.gate('cnot',10,9)
k.gate('cnot',3,10)
k.gate('h',9)
k.gate('h',11)
k.gate('t',2)
k.gate('t',9)
k.gate('t',11)
k.gate('cnot',9,2)
k.gate('cnot',11,9)
k.gate('cnot',2,11)
k.gate('tdag',9)
k.gate('cnot',2,9)
k.gate('tdag',2)
k.gate('tdag',9)
k.gate('t',11)
k.gate('cnot',11,9)
k.gate('cnot',2,11)
k.gate('cnot',9,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',2)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,2)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('tdag',11)
k.gate('cnot',2,11)
k.gate('tdag',2)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('cnot',11,2)
k.gate('h',0)
k.gate('h',11)
k.gate('t',10)
k.gate('t',3)
k.gate('t',11)
k.gate('cnot',3,10)
k.gate('cnot',11,3)
k.gate('cnot',10,11)
k.gate('tdag',3)
k.gate('cnot',10,3)
k.gate('tdag',10)
k.gate('tdag',3)
k.gate('t',11)
k.gate('cnot',11,3)
k.gate('cnot',10,11)
k.gate('cnot',3,10)
k.gate('h',11)
k.gate('h',0)
k.gate('t',2)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,2)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('tdag',11)
k.gate('cnot',2,11)
k.gate('tdag',2)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('cnot',11,2)
k.gate('h',0)
k.gate('h',11)
k.gate('t',10)
k.gate('t',3)
k.gate('t',11)
k.gate('cnot',3,10)
k.gate('cnot',11,3)
k.gate('cnot',10,11)
k.gate('tdag',3)
k.gate('cnot',10,3)
k.gate('tdag',10)
k.gate('tdag',3)
k.gate('t',11)
k.gate('cnot',11,3)
k.gate('cnot',10,11)
k.gate('cnot',3,10)
k.gate('h',11)
k.gate('x',2)
k.gate('x',3)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',5)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,5)
k.gate('cnot',10,3)
k.gate('cnot',5,10)
k.gate('tdag',3)
k.gate('cnot',5,3)
k.gate('tdag',5)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',5,10)
k.gate('cnot',3,5)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',5)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,5)
k.gate('cnot',10,3)
k.gate('cnot',5,10)
k.gate('tdag',3)
k.gate('cnot',5,3)
k.gate('tdag',5)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',5,10)
k.gate('cnot',3,5)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',9)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,9)
k.gate('cnot',10,3)
k.gate('cnot',9,10)
k.gate('tdag',3)
k.gate('cnot',9,3)
k.gate('tdag',9)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',9,10)
k.gate('cnot',3,9)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',9)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,9)
k.gate('cnot',10,3)
k.gate('cnot',9,10)
k.gate('tdag',3)
k.gate('cnot',9,3)
k.gate('tdag',9)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',9,10)
k.gate('cnot',3,9)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',2)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,2)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('tdag',11)
k.gate('cnot',2,11)
k.gate('tdag',2)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('cnot',11,2)
k.gate('h',0)
k.gate('h',11)
k.gate('t',9)
k.gate('t',3)
k.gate('t',11)
k.gate('cnot',3,9)
k.gate('cnot',11,3)
k.gate('cnot',9,11)
k.gate('tdag',3)
k.gate('cnot',9,3)
k.gate('tdag',9)
k.gate('tdag',3)
k.gate('t',11)
k.gate('cnot',11,3)
k.gate('cnot',9,11)
k.gate('cnot',3,9)
k.gate('h',11)
k.gate('h',0)
k.gate('t',2)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,2)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('tdag',11)
k.gate('cnot',2,11)
k.gate('tdag',2)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',2,0)
k.gate('cnot',11,2)
k.gate('h',0)
k.gate('h',11)
k.gate('t',9)
k.gate('t',3)
k.gate('t',11)
k.gate('cnot',3,9)
k.gate('cnot',11,3)
k.gate('cnot',9,11)
k.gate('tdag',3)
k.gate('cnot',9,3)
k.gate('tdag',9)
k.gate('tdag',3)
k.gate('t',11)
k.gate('cnot',11,3)
k.gate('cnot',9,11)
k.gate('cnot',3,9)
k.gate('h',11)
k.gate('x',2)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',7)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,7)
k.gate('cnot',10,3)
k.gate('cnot',7,10)
k.gate('tdag',3)
k.gate('cnot',7,3)
k.gate('tdag',7)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',7,10)
k.gate('cnot',3,7)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',0)
k.gate('t',1)
k.gate('t',11)
k.gate('t',0)
k.gate('cnot',11,1)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('tdag',11)
k.gate('cnot',1,11)
k.gate('tdag',1)
k.gate('tdag',11)
k.gate('t',0)
k.gate('cnot',0,11)
k.gate('cnot',1,0)
k.gate('cnot',11,1)
k.gate('h',0)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('h',10)
k.gate('t',7)
k.gate('t',3)
k.gate('t',10)
k.gate('cnot',3,7)
k.gate('cnot',10,3)
k.gate('cnot',7,10)
k.gate('tdag',3)
k.gate('cnot',7,3)
k.gate('tdag',7)
k.gate('tdag',3)
k.gate('t',10)
k.gate('cnot',10,3)
k.gate('cnot',7,10)
k.gate('cnot',3,7)
k.gate('h',10)
k.gate('h',11)
k.gate('t',2)
k.gate('t',10)
k.gate('t',11)
k.gate('cnot',10,2)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('tdag',10)
k.gate('cnot',2,10)
k.gate('tdag',2)
k.gate('tdag',10)
k.gate('t',11)
k.gate('cnot',11,10)
k.gate('cnot',2,11)
k.gate('cnot',10,2)
k.gate('h',11)
k.gate('x',1)
k.gate('h',0)
k.gate('t',1)
k.gate('t',10)
k.gate('t',0)
k.gate('cnot',10,1)
k.gate('cnot',0,10)
k.gate('cnot',1,0)
k.gate('tdag',10)
k.gate('cnot',1,10)
k.gate('tdag',1)
k.gate('tdag',10)
k.gate('t',0)
k.gate('cnot',0,10)
k.gate('cnot',1,0)
k.gate('cnot',10,1)
k.gate('h',0)
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
k.gate('t',11)
k.gate('t',3)
k.gate('t',9)
k.gate('cnot',3,11)
k.gate('cnot',9,3)
k.gate('cnot',11,9)
k.gate('tdag',3)
k.gate('cnot',11,3)
k.gate('tdag',11)
k.gate('tdag',3)
k.gate('t',9)
k.gate('cnot',9,3)
k.gate('cnot',11,9)
k.gate('cnot',3,11)
k.gate('h',9)
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
k.gate('h',0)
k.gate('t',1)
k.gate('t',10)
k.gate('t',0)
k.gate('cnot',10,1)
k.gate('cnot',0,10)
k.gate('cnot',1,0)
k.gate('tdag',10)
k.gate('cnot',1,10)
k.gate('tdag',1)
k.gate('tdag',10)
k.gate('t',0)
k.gate('cnot',0,10)
k.gate('cnot',1,0)
k.gate('cnot',10,1)
k.gate('h',0)
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
k.gate('t',11)
k.gate('t',3)
k.gate('t',9)
k.gate('cnot',3,11)
k.gate('cnot',9,3)
k.gate('cnot',11,9)
k.gate('tdag',3)
k.gate('cnot',11,3)
k.gate('tdag',11)
k.gate('tdag',3)
k.gate('t',9)
k.gate('cnot',9,3)
k.gate('cnot',11,9)
k.gate('cnot',3,11)
k.gate('h',9)
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
p.add_kernel(k)
p.compile(optimize=False)
