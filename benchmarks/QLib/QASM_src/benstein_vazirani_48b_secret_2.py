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
num_qubits = 50
p = ql.Program('benstein_vazirani_48b_secret_2', num_qubits, platform)
p.set_sweep_points(sweep_points, num_circuits)
k = ql.Kernel('benstein_vazirani_48b_secret_2', platform)
k.gate('prepx',48)
k.gate('x',48)
k.gate('h',0)
k.gate('h',1)
k.gate('h',2)
k.gate('h',3)
k.gate('h',4)
k.gate('h',5)
k.gate('h',6)
k.gate('h',7)
k.gate('h',8)
k.gate('h',9)
k.gate('h',10)
k.gate('h',11)
k.gate('h',12)
k.gate('h',13)
k.gate('h',14)
k.gate('h',15)
k.gate('h',16)
k.gate('h',17)
k.gate('h',18)
k.gate('h',19)
k.gate('h',20)
k.gate('h',21)
k.gate('h',22)
k.gate('h',23)
k.gate('h',24)
k.gate('h',25)
k.gate('h',26)
k.gate('h',27)
k.gate('h',28)
k.gate('h',29)
k.gate('h',30)
k.gate('h',31)
k.gate('h',32)
k.gate('h',33)
k.gate('h',34)
k.gate('h',35)
k.gate('h',36)
k.gate('h',37)
k.gate('h',38)
k.gate('h',39)
k.gate('h',40)
k.gate('h',41)
k.gate('h',42)
k.gate('h',43)
k.gate('h',44)
k.gate('h',45)
k.gate('h',46)
k.gate('h',47)
k.gate('h',48)
k.gate('cnot',1y)
k.gate('h',0)
k.gate('h',1)
k.gate('h',2)
k.gate('h',3)
k.gate('h',4)
k.gate('h',5)
k.gate('h',6)
k.gate('h',7)
k.gate('h',8)
k.gate('h',9)
k.gate('h',10)
k.gate('h',11)
k.gate('h',12)
k.gate('h',13)
k.gate('h',14)
k.gate('h',15)
k.gate('h',16)
k.gate('h',17)
k.gate('h',18)
k.gate('h',19)
k.gate('h',20)
k.gate('h',21)
k.gate('h',22)
k.gate('h',23)
k.gate('h',24)
k.gate('h',25)
k.gate('h',26)
k.gate('h',27)
k.gate('h',28)
k.gate('h',29)
k.gate('h',30)
k.gate('h',31)
k.gate('h',32)
k.gate('h',33)
k.gate('h',34)
k.gate('h',35)
k.gate('h',36)
k.gate('h',37)
k.gate('h',38)
k.gate('h',39)
k.gate('h',40)
k.gate('h',41)
k.gate('h',42)
k.gate('h',43)
k.gate('h',44)
k.gate('h',45)
k.gate('h',46)
k.gate('h',47)
k.gate('h',48)
p.add_kernel(k)
p.compile(optimize=False)
