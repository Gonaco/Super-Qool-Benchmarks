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
num_qubits = 515
p = ql.Program('cuccaroAdder_256b', num_qubits, platform)
p.set_sweep_points(sweep_points, num_circuits)
k = ql.Kernel('cuccaroAdder_256b', platform)
k.gate('cnot',1b0)
k.gate('cnot',1c0)
k.gate('toffoli',0b0,a0)
k.gate('cnot',3b1)
k.gate('cnot',3a0)
k.gate('toffoli',1b1,a1)
k.gate('cnot',5b2)
k.gate('cnot',5a1)
k.gate('toffoli',3b2,a2)
k.gate('cnot',7b3)
k.gate('cnot',7a2)
k.gate('toffoli',5b3,a3)
k.gate('cnot',9b4)
k.gate('cnot',9a3)
k.gate('toffoli',7b4,a4)
k.gate('cnot',11b5)
k.gate('cnot',11a4)
k.gate('toffoli',9b5,a5)
k.gate('cnot',13b6)
k.gate('cnot',13a5)
k.gate('toffoli',11b6,a6)
k.gate('cnot',15b7)
k.gate('cnot',15a6)
k.gate('toffoli',13b7,a7)
k.gate('cnot',17b8)
k.gate('cnot',17a7)
k.gate('toffoli',15b8,a8)
k.gate('cnot',19b9)
k.gate('cnot',19a8)
k.gate('toffoli',17b9,a9)
k.gate('cnot',21b10)
k.gate('cnot',21a9)
k.gate('toffoli',19b10,a10)
k.gate('cnot',23b11)
k.gate('cnot',23a10)
k.gate('toffoli',21b11,a11)
k.gate('cnot',25b12)
k.gate('cnot',25a11)
k.gate('toffoli',23b12,a12)
k.gate('cnot',27b13)
k.gate('cnot',27a12)
k.gate('toffoli',25b13,a13)
k.gate('cnot',29b14)
k.gate('cnot',29a13)
k.gate('toffoli',27b14,a14)
k.gate('cnot',31b15)
k.gate('cnot',31a14)
k.gate('toffoli',29b15,a15)
k.gate('cnot',33b16)
k.gate('cnot',33a15)
k.gate('toffoli',31b16,a16)
k.gate('cnot',35b17)
k.gate('cnot',35a16)
k.gate('toffoli',33b17,a17)
k.gate('cnot',37b18)
k.gate('cnot',37a17)
k.gate('toffoli',35b18,a18)
k.gate('cnot',39b19)
k.gate('cnot',39a18)
k.gate('toffoli',37b19,a19)
k.gate('cnot',41b20)
k.gate('cnot',41a19)
k.gate('toffoli',39b20,a20)
k.gate('cnot',43b21)
k.gate('cnot',43a20)
k.gate('toffoli',41b21,a21)
k.gate('cnot',45b22)
k.gate('cnot',45a21)
k.gate('toffoli',43b22,a22)
k.gate('cnot',47b23)
k.gate('cnot',47a22)
k.gate('toffoli',45b23,a23)
k.gate('cnot',49b24)
k.gate('cnot',49a23)
k.gate('toffoli',47b24,a24)
k.gate('cnot',51b25)
k.gate('cnot',51a24)
k.gate('toffoli',49b25,a25)
k.gate('cnot',53b26)
k.gate('cnot',53a25)
k.gate('toffoli',51b26,a26)
k.gate('cnot',55b27)
k.gate('cnot',55a26)
k.gate('toffoli',53b27,a27)
k.gate('cnot',57b28)
k.gate('cnot',57a27)
k.gate('toffoli',55b28,a28)
k.gate('cnot',59b29)
k.gate('cnot',59a28)
k.gate('toffoli',57b29,a29)
k.gate('cnot',61b30)
k.gate('cnot',61a29)
k.gate('toffoli',59b30,a30)
k.gate('cnot',63b31)
k.gate('cnot',63a30)
k.gate('toffoli',61b31,a31)
k.gate('cnot',65b32)
k.gate('cnot',65a31)
k.gate('toffoli',63b32,a32)
k.gate('cnot',67b33)
k.gate('cnot',67a32)
k.gate('toffoli',65b33,a33)
k.gate('cnot',69b34)
k.gate('cnot',69a33)
k.gate('toffoli',67b34,a34)
k.gate('cnot',71b35)
k.gate('cnot',71a34)
k.gate('toffoli',69b35,a35)
k.gate('cnot',73b36)
k.gate('cnot',73a35)
k.gate('toffoli',71b36,a36)
k.gate('cnot',75b37)
k.gate('cnot',75a36)
k.gate('toffoli',73b37,a37)
k.gate('cnot',77b38)
k.gate('cnot',77a37)
k.gate('toffoli',75b38,a38)
k.gate('cnot',79b39)
k.gate('cnot',79a38)
k.gate('toffoli',77b39,a39)
k.gate('cnot',81b40)
k.gate('cnot',81a39)
k.gate('toffoli',79b40,a40)
k.gate('cnot',83b41)
k.gate('cnot',83a40)
k.gate('toffoli',81b41,a41)
k.gate('cnot',85b42)
k.gate('cnot',85a41)
k.gate('toffoli',83b42,a42)
k.gate('cnot',87b43)
k.gate('cnot',87a42)
k.gate('toffoli',85b43,a43)
k.gate('cnot',89b44)
k.gate('cnot',89a43)
k.gate('toffoli',87b44,a44)
k.gate('cnot',91b45)
k.gate('cnot',91a44)
k.gate('toffoli',89b45,a45)
k.gate('cnot',93b46)
k.gate('cnot',93a45)
k.gate('toffoli',91b46,a46)
k.gate('cnot',95b47)
k.gate('cnot',95a46)
k.gate('toffoli',93b47,a47)
k.gate('cnot',97b48)
k.gate('cnot',97a47)
k.gate('toffoli',95b48,a48)
k.gate('cnot',99b49)
k.gate('cnot',99a48)
k.gate('toffoli',97b49,a49)
k.gate('cnot',101b50)
k.gate('cnot',101a49)
k.gate('toffoli',99b50,a50)
k.gate('cnot',103b51)
k.gate('cnot',103a50)
k.gate('toffoli',101b51,a51)
k.gate('cnot',105b52)
k.gate('cnot',105a51)
k.gate('toffoli',103b52,a52)
k.gate('cnot',107b53)
k.gate('cnot',107a52)
k.gate('toffoli',105b53,a53)
k.gate('cnot',109b54)
k.gate('cnot',109a53)
k.gate('toffoli',107b54,a54)
k.gate('cnot',111b55)
k.gate('cnot',111a54)
k.gate('toffoli',109b55,a55)
k.gate('cnot',113b56)
k.gate('cnot',113a55)
k.gate('toffoli',111b56,a56)
k.gate('cnot',115b57)
k.gate('cnot',115a56)
k.gate('toffoli',113b57,a57)
k.gate('cnot',117b58)
k.gate('cnot',117a57)
k.gate('toffoli',115b58,a58)
k.gate('cnot',119b59)
k.gate('cnot',119a58)
k.gate('toffoli',117b59,a59)
k.gate('cnot',121b60)
k.gate('cnot',121a59)
k.gate('toffoli',119b60,a60)
k.gate('cnot',123b61)
k.gate('cnot',123a60)
k.gate('toffoli',121b61,a61)
k.gate('cnot',125b62)
k.gate('cnot',125a61)
k.gate('toffoli',123b62,a62)
k.gate('cnot',127b63)
k.gate('cnot',127a62)
k.gate('toffoli',125b63,a63)
k.gate('cnot',129b64)
k.gate('cnot',129a63)
k.gate('toffoli',127b64,a64)
k.gate('cnot',131b65)
k.gate('cnot',131a64)
k.gate('toffoli',129b65,a65)
k.gate('cnot',133b66)
k.gate('cnot',133a65)
k.gate('toffoli',131b66,a66)
k.gate('cnot',135b67)
k.gate('cnot',135a66)
k.gate('toffoli',133b67,a67)
k.gate('cnot',137b68)
k.gate('cnot',137a67)
k.gate('toffoli',135b68,a68)
k.gate('cnot',139b69)
k.gate('cnot',139a68)
k.gate('toffoli',137b69,a69)
k.gate('cnot',141b70)
k.gate('cnot',141a69)
k.gate('toffoli',139b70,a70)
k.gate('cnot',143b71)
k.gate('cnot',143a70)
k.gate('toffoli',141b71,a71)
k.gate('cnot',145b72)
k.gate('cnot',145a71)
k.gate('toffoli',143b72,a72)
k.gate('cnot',147b73)
k.gate('cnot',147a72)
k.gate('toffoli',145b73,a73)
k.gate('cnot',149b74)
k.gate('cnot',149a73)
k.gate('toffoli',147b74,a74)
k.gate('cnot',151b75)
k.gate('cnot',151a74)
k.gate('toffoli',149b75,a75)
k.gate('cnot',153b76)
k.gate('cnot',153a75)
k.gate('toffoli',151b76,a76)
k.gate('cnot',155b77)
k.gate('cnot',155a76)
k.gate('toffoli',153b77,a77)
k.gate('cnot',157b78)
k.gate('cnot',157a77)
k.gate('toffoli',155b78,a78)
k.gate('cnot',159b79)
k.gate('cnot',159a78)
k.gate('toffoli',157b79,a79)
k.gate('cnot',161b80)
k.gate('cnot',161a79)
k.gate('toffoli',159b80,a80)
k.gate('cnot',163b81)
k.gate('cnot',163a80)
k.gate('toffoli',161b81,a81)
k.gate('cnot',165b82)
k.gate('cnot',165a81)
k.gate('toffoli',163b82,a82)
k.gate('cnot',167b83)
k.gate('cnot',167a82)
k.gate('toffoli',165b83,a83)
k.gate('cnot',169b84)
k.gate('cnot',169a83)
k.gate('toffoli',167b84,a84)
k.gate('cnot',171b85)
k.gate('cnot',171a84)
k.gate('toffoli',169b85,a85)
k.gate('cnot',173b86)
k.gate('cnot',173a85)
k.gate('toffoli',171b86,a86)
k.gate('cnot',175b87)
k.gate('cnot',175a86)
k.gate('toffoli',173b87,a87)
k.gate('cnot',177b88)
k.gate('cnot',177a87)
k.gate('toffoli',175b88,a88)
k.gate('cnot',179b89)
k.gate('cnot',179a88)
k.gate('toffoli',177b89,a89)
k.gate('cnot',181b90)
k.gate('cnot',181a89)
k.gate('toffoli',179b90,a90)
k.gate('cnot',183b91)
k.gate('cnot',183a90)
k.gate('toffoli',181b91,a91)
k.gate('cnot',185b92)
k.gate('cnot',185a91)
k.gate('toffoli',183b92,a92)
k.gate('cnot',187b93)
k.gate('cnot',187a92)
k.gate('toffoli',185b93,a93)
k.gate('cnot',189b94)
k.gate('cnot',189a93)
k.gate('toffoli',187b94,a94)
k.gate('cnot',191b95)
k.gate('cnot',191a94)
k.gate('toffoli',189b95,a95)
k.gate('cnot',193b96)
k.gate('cnot',193a95)
k.gate('toffoli',191b96,a96)
k.gate('cnot',195b97)
k.gate('cnot',195a96)
k.gate('toffoli',193b97,a97)
k.gate('cnot',197b98)
k.gate('cnot',197a97)
k.gate('toffoli',195b98,a98)
k.gate('cnot',199b99)
k.gate('cnot',199a98)
k.gate('toffoli',197b99,a99)
k.gate('cnot',201b100)
k.gate('cnot',201a99)
k.gate('toffoli',199b100,a100)
k.gate('cnot',203b101)
k.gate('cnot',203a100)
k.gate('toffoli',201b101,a101)
k.gate('cnot',205b102)
k.gate('cnot',205a101)
k.gate('toffoli',203b102,a102)
k.gate('cnot',207b103)
k.gate('cnot',207a102)
k.gate('toffoli',205b103,a103)
k.gate('cnot',209b104)
k.gate('cnot',209a103)
k.gate('toffoli',207b104,a104)
k.gate('cnot',211b105)
k.gate('cnot',211a104)
k.gate('toffoli',209b105,a105)
k.gate('cnot',213b106)
k.gate('cnot',213a105)
k.gate('toffoli',211b106,a106)
k.gate('cnot',215b107)
k.gate('cnot',215a106)
k.gate('toffoli',213b107,a107)
k.gate('cnot',217b108)
k.gate('cnot',217a107)
k.gate('toffoli',215b108,a108)
k.gate('cnot',219b109)
k.gate('cnot',219a108)
k.gate('toffoli',217b109,a109)
k.gate('cnot',221b110)
k.gate('cnot',221a109)
k.gate('toffoli',219b110,a110)
k.gate('cnot',223b111)
k.gate('cnot',223a110)
k.gate('toffoli',221b111,a111)
k.gate('cnot',225b112)
k.gate('cnot',225a111)
k.gate('toffoli',223b112,a112)
k.gate('cnot',227b113)
k.gate('cnot',227a112)
k.gate('toffoli',225b113,a113)
k.gate('cnot',229b114)
k.gate('cnot',229a113)
k.gate('toffoli',227b114,a114)
k.gate('cnot',231b115)
k.gate('cnot',231a114)
k.gate('toffoli',229b115,a115)
k.gate('cnot',233b116)
k.gate('cnot',233a115)
k.gate('toffoli',231b116,a116)
k.gate('cnot',235b117)
k.gate('cnot',235a116)
k.gate('toffoli',233b117,a117)
k.gate('cnot',237b118)
k.gate('cnot',237a117)
k.gate('toffoli',235b118,a118)
k.gate('cnot',239b119)
k.gate('cnot',239a118)
k.gate('toffoli',237b119,a119)
k.gate('cnot',241b120)
k.gate('cnot',241a119)
k.gate('toffoli',239b120,a120)
k.gate('cnot',243b121)
k.gate('cnot',243a120)
k.gate('toffoli',241b121,a121)
k.gate('cnot',245b122)
k.gate('cnot',245a121)
k.gate('toffoli',243b122,a122)
k.gate('cnot',247b123)
k.gate('cnot',247a122)
k.gate('toffoli',245b123,a123)
k.gate('cnot',249b124)
k.gate('cnot',249a123)
k.gate('toffoli',247b124,a124)
k.gate('cnot',251b125)
k.gate('cnot',251a124)
k.gate('toffoli',249b125,a125)
k.gate('cnot',253b126)
k.gate('cnot',253a125)
k.gate('toffoli',251b126,a126)
k.gate('cnot',255b127)
k.gate('cnot',255a126)
k.gate('toffoli',253b127,a127)
k.gate('cnot',257b128)
k.gate('cnot',257a127)
k.gate('toffoli',255b128,a128)
k.gate('cnot',259b129)
k.gate('cnot',259a128)
k.gate('toffoli',257b129,a129)
k.gate('cnot',261b130)
k.gate('cnot',261a129)
k.gate('toffoli',259b130,a130)
k.gate('cnot',263b131)
k.gate('cnot',263a130)
k.gate('toffoli',261b131,a131)
k.gate('cnot',265b132)
k.gate('cnot',265a131)
k.gate('toffoli',263b132,a132)
k.gate('cnot',267b133)
k.gate('cnot',267a132)
k.gate('toffoli',265b133,a133)
k.gate('cnot',269b134)
k.gate('cnot',269a133)
k.gate('toffoli',267b134,a134)
k.gate('cnot',271b135)
k.gate('cnot',271a134)
k.gate('toffoli',269b135,a135)
k.gate('cnot',273b136)
k.gate('cnot',273a135)
k.gate('toffoli',271b136,a136)
k.gate('cnot',275b137)
k.gate('cnot',275a136)
k.gate('toffoli',273b137,a137)
k.gate('cnot',277b138)
k.gate('cnot',277a137)
k.gate('toffoli',275b138,a138)
k.gate('cnot',279b139)
k.gate('cnot',279a138)
k.gate('toffoli',277b139,a139)
k.gate('cnot',281b140)
k.gate('cnot',281a139)
k.gate('toffoli',279b140,a140)
k.gate('cnot',283b141)
k.gate('cnot',283a140)
k.gate('toffoli',281b141,a141)
k.gate('cnot',285b142)
k.gate('cnot',285a141)
k.gate('toffoli',283b142,a142)
k.gate('cnot',287b143)
k.gate('cnot',287a142)
k.gate('toffoli',285b143,a143)
k.gate('cnot',289b144)
k.gate('cnot',289a143)
k.gate('toffoli',287b144,a144)
k.gate('cnot',291b145)
k.gate('cnot',291a144)
k.gate('toffoli',289b145,a145)
k.gate('cnot',293b146)
k.gate('cnot',293a145)
k.gate('toffoli',291b146,a146)
k.gate('cnot',295b147)
k.gate('cnot',295a146)
k.gate('toffoli',293b147,a147)
k.gate('cnot',297b148)
k.gate('cnot',297a147)
k.gate('toffoli',295b148,a148)
k.gate('cnot',299b149)
k.gate('cnot',299a148)
k.gate('toffoli',297b149,a149)
k.gate('cnot',301b150)
k.gate('cnot',301a149)
k.gate('toffoli',299b150,a150)
k.gate('cnot',303b151)
k.gate('cnot',303a150)
k.gate('toffoli',301b151,a151)
k.gate('cnot',305b152)
k.gate('cnot',305a151)
k.gate('toffoli',303b152,a152)
k.gate('cnot',307b153)
k.gate('cnot',307a152)
k.gate('toffoli',305b153,a153)
k.gate('cnot',309b154)
k.gate('cnot',309a153)
k.gate('toffoli',307b154,a154)
k.gate('cnot',311b155)
k.gate('cnot',311a154)
k.gate('toffoli',309b155,a155)
k.gate('cnot',313b156)
k.gate('cnot',313a155)
k.gate('toffoli',311b156,a156)
k.gate('cnot',315b157)
k.gate('cnot',315a156)
k.gate('toffoli',313b157,a157)
k.gate('cnot',317b158)
k.gate('cnot',317a157)
k.gate('toffoli',315b158,a158)
k.gate('cnot',319b159)
k.gate('cnot',319a158)
k.gate('toffoli',317b159,a159)
k.gate('cnot',321b160)
k.gate('cnot',321a159)
k.gate('toffoli',319b160,a160)
k.gate('cnot',323b161)
k.gate('cnot',323a160)
k.gate('toffoli',321b161,a161)
k.gate('cnot',325b162)
k.gate('cnot',325a161)
k.gate('toffoli',323b162,a162)
k.gate('cnot',327b163)
k.gate('cnot',327a162)
k.gate('toffoli',325b163,a163)
k.gate('cnot',329b164)
k.gate('cnot',329a163)
k.gate('toffoli',327b164,a164)
k.gate('cnot',331b165)
k.gate('cnot',331a164)
k.gate('toffoli',329b165,a165)
k.gate('cnot',333b166)
k.gate('cnot',333a165)
k.gate('toffoli',331b166,a166)
k.gate('cnot',335b167)
k.gate('cnot',335a166)
k.gate('toffoli',333b167,a167)
k.gate('cnot',337b168)
k.gate('cnot',337a167)
k.gate('toffoli',335b168,a168)
k.gate('cnot',339b169)
k.gate('cnot',339a168)
k.gate('toffoli',337b169,a169)
k.gate('cnot',341b170)
k.gate('cnot',341a169)
k.gate('toffoli',339b170,a170)
k.gate('cnot',343b171)
k.gate('cnot',343a170)
k.gate('toffoli',341b171,a171)
k.gate('cnot',345b172)
k.gate('cnot',345a171)
k.gate('toffoli',343b172,a172)
k.gate('cnot',347b173)
k.gate('cnot',347a172)
k.gate('toffoli',345b173,a173)
k.gate('cnot',349b174)
k.gate('cnot',349a173)
k.gate('toffoli',347b174,a174)
k.gate('cnot',351b175)
k.gate('cnot',351a174)
k.gate('toffoli',349b175,a175)
k.gate('cnot',353b176)
k.gate('cnot',353a175)
k.gate('toffoli',351b176,a176)
k.gate('cnot',355b177)
k.gate('cnot',355a176)
k.gate('toffoli',353b177,a177)
k.gate('cnot',357b178)
k.gate('cnot',357a177)
k.gate('toffoli',355b178,a178)
k.gate('cnot',359b179)
k.gate('cnot',359a178)
k.gate('toffoli',357b179,a179)
k.gate('cnot',361b180)
k.gate('cnot',361a179)
k.gate('toffoli',359b180,a180)
k.gate('cnot',363b181)
k.gate('cnot',363a180)
k.gate('toffoli',361b181,a181)
k.gate('cnot',365b182)
k.gate('cnot',365a181)
k.gate('toffoli',363b182,a182)
k.gate('cnot',367b183)
k.gate('cnot',367a182)
k.gate('toffoli',365b183,a183)
k.gate('cnot',369b184)
k.gate('cnot',369a183)
k.gate('toffoli',367b184,a184)
k.gate('cnot',371b185)
k.gate('cnot',371a184)
k.gate('toffoli',369b185,a185)
k.gate('cnot',373b186)
k.gate('cnot',373a185)
k.gate('toffoli',371b186,a186)
k.gate('cnot',375b187)
k.gate('cnot',375a186)
k.gate('toffoli',373b187,a187)
k.gate('cnot',377b188)
k.gate('cnot',377a187)
k.gate('toffoli',375b188,a188)
k.gate('cnot',379b189)
k.gate('cnot',379a188)
k.gate('toffoli',377b189,a189)
k.gate('cnot',381b190)
k.gate('cnot',381a189)
k.gate('toffoli',379b190,a190)
k.gate('cnot',383b191)
k.gate('cnot',383a190)
k.gate('toffoli',381b191,a191)
k.gate('cnot',385b192)
k.gate('cnot',385a191)
k.gate('toffoli',383b192,a192)
k.gate('cnot',387b193)
k.gate('cnot',387a192)
k.gate('toffoli',385b193,a193)
k.gate('cnot',389b194)
k.gate('cnot',389a193)
k.gate('toffoli',387b194,a194)
k.gate('cnot',391b195)
k.gate('cnot',391a194)
k.gate('toffoli',389b195,a195)
k.gate('cnot',393b196)
k.gate('cnot',393a195)
k.gate('toffoli',391b196,a196)
k.gate('cnot',395b197)
k.gate('cnot',395a196)
k.gate('toffoli',393b197,a197)
k.gate('cnot',397b198)
k.gate('cnot',397a197)
k.gate('toffoli',395b198,a198)
k.gate('cnot',399b199)
k.gate('cnot',399a198)
k.gate('toffoli',397b199,a199)
k.gate('cnot',401b200)
k.gate('cnot',401a199)
k.gate('toffoli',399b200,a200)
k.gate('cnot',403b201)
k.gate('cnot',403a200)
k.gate('toffoli',401b201,a201)
k.gate('cnot',405b202)
k.gate('cnot',405a201)
k.gate('toffoli',403b202,a202)
k.gate('cnot',407b203)
k.gate('cnot',407a202)
k.gate('toffoli',405b203,a203)
k.gate('cnot',409b204)
k.gate('cnot',409a203)
k.gate('toffoli',407b204,a204)
k.gate('cnot',411b205)
k.gate('cnot',411a204)
k.gate('toffoli',409b205,a205)
k.gate('cnot',413b206)
k.gate('cnot',413a205)
k.gate('toffoli',411b206,a206)
k.gate('cnot',415b207)
k.gate('cnot',415a206)
k.gate('toffoli',413b207,a207)
k.gate('cnot',417b208)
k.gate('cnot',417a207)
k.gate('toffoli',415b208,a208)
k.gate('cnot',419b209)
k.gate('cnot',419a208)
k.gate('toffoli',417b209,a209)
k.gate('cnot',421b210)
k.gate('cnot',421a209)
k.gate('toffoli',419b210,a210)
k.gate('cnot',423b211)
k.gate('cnot',423a210)
k.gate('toffoli',421b211,a211)
k.gate('cnot',425b212)
k.gate('cnot',425a211)
k.gate('toffoli',423b212,a212)
k.gate('cnot',427b213)
k.gate('cnot',427a212)
k.gate('toffoli',425b213,a213)
k.gate('cnot',429b214)
k.gate('cnot',429a213)
k.gate('toffoli',427b214,a214)
k.gate('cnot',431b215)
k.gate('cnot',431a214)
k.gate('toffoli',429b215,a215)
k.gate('cnot',433b216)
k.gate('cnot',433a215)
k.gate('toffoli',431b216,a216)
k.gate('cnot',435b217)
k.gate('cnot',435a216)
k.gate('toffoli',433b217,a217)
k.gate('cnot',437b218)
k.gate('cnot',437a217)
k.gate('toffoli',435b218,a218)
k.gate('cnot',439b219)
k.gate('cnot',439a218)
k.gate('toffoli',437b219,a219)
k.gate('cnot',441b220)
k.gate('cnot',441a219)
k.gate('toffoli',439b220,a220)
k.gate('cnot',443b221)
k.gate('cnot',443a220)
k.gate('toffoli',441b221,a221)
k.gate('cnot',445b222)
k.gate('cnot',445a221)
k.gate('toffoli',443b222,a222)
k.gate('cnot',447b223)
k.gate('cnot',447a222)
k.gate('toffoli',445b223,a223)
k.gate('cnot',449b224)
k.gate('cnot',449a223)
k.gate('toffoli',447b224,a224)
k.gate('cnot',451b225)
k.gate('cnot',451a224)
k.gate('toffoli',449b225,a225)
k.gate('cnot',453b226)
k.gate('cnot',453a225)
k.gate('toffoli',451b226,a226)
k.gate('cnot',455b227)
k.gate('cnot',455a226)
k.gate('toffoli',453b227,a227)
k.gate('cnot',457b228)
k.gate('cnot',457a227)
k.gate('toffoli',455b228,a228)
k.gate('cnot',459b229)
k.gate('cnot',459a228)
k.gate('toffoli',457b229,a229)
k.gate('cnot',461b230)
k.gate('cnot',461a229)
k.gate('toffoli',459b230,a230)
k.gate('cnot',463b231)
k.gate('cnot',463a230)
k.gate('toffoli',461b231,a231)
k.gate('cnot',465b232)
k.gate('cnot',465a231)
k.gate('toffoli',463b232,a232)
k.gate('cnot',467b233)
k.gate('cnot',467a232)
k.gate('toffoli',465b233,a233)
k.gate('cnot',469b234)
k.gate('cnot',469a233)
k.gate('toffoli',467b234,a234)
k.gate('cnot',471b235)
k.gate('cnot',471a234)
k.gate('toffoli',469b235,a235)
k.gate('cnot',473b236)
k.gate('cnot',473a235)
k.gate('toffoli',471b236,a236)
k.gate('cnot',475b237)
k.gate('cnot',475a236)
k.gate('toffoli',473b237,a237)
k.gate('cnot',477b238)
k.gate('cnot',477a237)
k.gate('toffoli',475b238,a238)
k.gate('cnot',479b239)
k.gate('cnot',479a238)
k.gate('toffoli',477b239,a239)
k.gate('cnot',481b240)
k.gate('cnot',481a239)
k.gate('toffoli',479b240,a240)
k.gate('cnot',483b241)
k.gate('cnot',483a240)
k.gate('toffoli',481b241,a241)
k.gate('cnot',485b242)
k.gate('cnot',485a241)
k.gate('toffoli',483b242,a242)
k.gate('cnot',487b243)
k.gate('cnot',487a242)
k.gate('toffoli',485b243,a243)
k.gate('cnot',489b244)
k.gate('cnot',489a243)
k.gate('toffoli',487b244,a244)
k.gate('cnot',491b245)
k.gate('cnot',491a244)
k.gate('toffoli',489b245,a245)
k.gate('cnot',493b246)
k.gate('cnot',493a245)
k.gate('toffoli',491b246,a246)
k.gate('cnot',495b247)
k.gate('cnot',495a246)
k.gate('toffoli',493b247,a247)
k.gate('cnot',497b248)
k.gate('cnot',497a247)
k.gate('toffoli',495b248,a248)
k.gate('cnot',499b249)
k.gate('cnot',499a248)
k.gate('toffoli',497b249,a249)
k.gate('cnot',501b250)
k.gate('cnot',501a249)
k.gate('toffoli',499b250,a250)
k.gate('cnot',503b251)
k.gate('cnot',503a250)
k.gate('toffoli',501b251,a251)
k.gate('cnot',505b252)
k.gate('cnot',505a251)
k.gate('toffoli',503b252,a252)
k.gate('cnot',507b253)
k.gate('cnot',507a252)
k.gate('toffoli',505b253,a253)
k.gate('cnot',509b254)
k.gate('cnot',509a253)
k.gate('toffoli',507b254,a254)
k.gate('cnot',511b255)
k.gate('cnot',511a254)
k.gate('toffoli',509b255,a255)
k.gate('cnot',511z)
k.gate('toffoli',509b255,a255)
k.gate('cnot',511a254)
k.gate('cnot',509b255)
k.gate('toffoli',507b254,a254)
k.gate('cnot',509a253)
k.gate('cnot',507b254)
k.gate('toffoli',505b253,a253)
k.gate('cnot',507a252)
k.gate('cnot',505b253)
k.gate('toffoli',503b252,a252)
k.gate('cnot',505a251)
k.gate('cnot',503b252)
k.gate('toffoli',501b251,a251)
k.gate('cnot',503a250)
k.gate('cnot',501b251)
k.gate('toffoli',499b250,a250)
k.gate('cnot',501a249)
k.gate('cnot',499b250)
k.gate('toffoli',497b249,a249)
k.gate('cnot',499a248)
k.gate('cnot',497b249)
k.gate('toffoli',495b248,a248)
k.gate('cnot',497a247)
k.gate('cnot',495b248)
k.gate('toffoli',493b247,a247)
k.gate('cnot',495a246)
k.gate('cnot',493b247)
k.gate('toffoli',491b246,a246)
k.gate('cnot',493a245)
k.gate('cnot',491b246)
k.gate('toffoli',489b245,a245)
k.gate('cnot',491a244)
k.gate('cnot',489b245)
k.gate('toffoli',487b244,a244)
k.gate('cnot',489a243)
k.gate('cnot',487b244)
k.gate('toffoli',485b243,a243)
k.gate('cnot',487a242)
k.gate('cnot',485b243)
k.gate('toffoli',483b242,a242)
k.gate('cnot',485a241)
k.gate('cnot',483b242)
k.gate('toffoli',481b241,a241)
k.gate('cnot',483a240)
k.gate('cnot',481b241)
k.gate('toffoli',479b240,a240)
k.gate('cnot',481a239)
k.gate('cnot',479b240)
k.gate('toffoli',477b239,a239)
k.gate('cnot',479a238)
k.gate('cnot',477b239)
k.gate('toffoli',475b238,a238)
k.gate('cnot',477a237)
k.gate('cnot',475b238)
k.gate('toffoli',473b237,a237)
k.gate('cnot',475a236)
k.gate('cnot',473b237)
k.gate('toffoli',471b236,a236)
k.gate('cnot',473a235)
k.gate('cnot',471b236)
k.gate('toffoli',469b235,a235)
k.gate('cnot',471a234)
k.gate('cnot',469b235)
k.gate('toffoli',467b234,a234)
k.gate('cnot',469a233)
k.gate('cnot',467b234)
k.gate('toffoli',465b233,a233)
k.gate('cnot',467a232)
k.gate('cnot',465b233)
k.gate('toffoli',463b232,a232)
k.gate('cnot',465a231)
k.gate('cnot',463b232)
k.gate('toffoli',461b231,a231)
k.gate('cnot',463a230)
k.gate('cnot',461b231)
k.gate('toffoli',459b230,a230)
k.gate('cnot',461a229)
k.gate('cnot',459b230)
k.gate('toffoli',457b229,a229)
k.gate('cnot',459a228)
k.gate('cnot',457b229)
k.gate('toffoli',455b228,a228)
k.gate('cnot',457a227)
k.gate('cnot',455b228)
k.gate('toffoli',453b227,a227)
k.gate('cnot',455a226)
k.gate('cnot',453b227)
k.gate('toffoli',451b226,a226)
k.gate('cnot',453a225)
k.gate('cnot',451b226)
k.gate('toffoli',449b225,a225)
k.gate('cnot',451a224)
k.gate('cnot',449b225)
k.gate('toffoli',447b224,a224)
k.gate('cnot',449a223)
k.gate('cnot',447b224)
k.gate('toffoli',445b223,a223)
k.gate('cnot',447a222)
k.gate('cnot',445b223)
k.gate('toffoli',443b222,a222)
k.gate('cnot',445a221)
k.gate('cnot',443b222)
k.gate('toffoli',441b221,a221)
k.gate('cnot',443a220)
k.gate('cnot',441b221)
k.gate('toffoli',439b220,a220)
k.gate('cnot',441a219)
k.gate('cnot',439b220)
k.gate('toffoli',437b219,a219)
k.gate('cnot',439a218)
k.gate('cnot',437b219)
k.gate('toffoli',435b218,a218)
k.gate('cnot',437a217)
k.gate('cnot',435b218)
k.gate('toffoli',433b217,a217)
k.gate('cnot',435a216)
k.gate('cnot',433b217)
k.gate('toffoli',431b216,a216)
k.gate('cnot',433a215)
k.gate('cnot',431b216)
k.gate('toffoli',429b215,a215)
k.gate('cnot',431a214)
k.gate('cnot',429b215)
k.gate('toffoli',427b214,a214)
k.gate('cnot',429a213)
k.gate('cnot',427b214)
k.gate('toffoli',425b213,a213)
k.gate('cnot',427a212)
k.gate('cnot',425b213)
k.gate('toffoli',423b212,a212)
k.gate('cnot',425a211)
k.gate('cnot',423b212)
k.gate('toffoli',421b211,a211)
k.gate('cnot',423a210)
k.gate('cnot',421b211)
k.gate('toffoli',419b210,a210)
k.gate('cnot',421a209)
k.gate('cnot',419b210)
k.gate('toffoli',417b209,a209)
k.gate('cnot',419a208)
k.gate('cnot',417b209)
k.gate('toffoli',415b208,a208)
k.gate('cnot',417a207)
k.gate('cnot',415b208)
k.gate('toffoli',413b207,a207)
k.gate('cnot',415a206)
k.gate('cnot',413b207)
k.gate('toffoli',411b206,a206)
k.gate('cnot',413a205)
k.gate('cnot',411b206)
k.gate('toffoli',409b205,a205)
k.gate('cnot',411a204)
k.gate('cnot',409b205)
k.gate('toffoli',407b204,a204)
k.gate('cnot',409a203)
k.gate('cnot',407b204)
k.gate('toffoli',405b203,a203)
k.gate('cnot',407a202)
k.gate('cnot',405b203)
k.gate('toffoli',403b202,a202)
k.gate('cnot',405a201)
k.gate('cnot',403b202)
k.gate('toffoli',401b201,a201)
k.gate('cnot',403a200)
k.gate('cnot',401b201)
k.gate('toffoli',399b200,a200)
k.gate('cnot',401a199)
k.gate('cnot',399b200)
k.gate('toffoli',397b199,a199)
k.gate('cnot',399a198)
k.gate('cnot',397b199)
k.gate('toffoli',395b198,a198)
k.gate('cnot',397a197)
k.gate('cnot',395b198)
k.gate('toffoli',393b197,a197)
k.gate('cnot',395a196)
k.gate('cnot',393b197)
k.gate('toffoli',391b196,a196)
k.gate('cnot',393a195)
k.gate('cnot',391b196)
k.gate('toffoli',389b195,a195)
k.gate('cnot',391a194)
k.gate('cnot',389b195)
k.gate('toffoli',387b194,a194)
k.gate('cnot',389a193)
k.gate('cnot',387b194)
k.gate('toffoli',385b193,a193)
k.gate('cnot',387a192)
k.gate('cnot',385b193)
k.gate('toffoli',383b192,a192)
k.gate('cnot',385a191)
k.gate('cnot',383b192)
k.gate('toffoli',381b191,a191)
k.gate('cnot',383a190)
k.gate('cnot',381b191)
k.gate('toffoli',379b190,a190)
k.gate('cnot',381a189)
k.gate('cnot',379b190)
k.gate('toffoli',377b189,a189)
k.gate('cnot',379a188)
k.gate('cnot',377b189)
k.gate('toffoli',375b188,a188)
k.gate('cnot',377a187)
k.gate('cnot',375b188)
k.gate('toffoli',373b187,a187)
k.gate('cnot',375a186)
k.gate('cnot',373b187)
k.gate('toffoli',371b186,a186)
k.gate('cnot',373a185)
k.gate('cnot',371b186)
k.gate('toffoli',369b185,a185)
k.gate('cnot',371a184)
k.gate('cnot',369b185)
k.gate('toffoli',367b184,a184)
k.gate('cnot',369a183)
k.gate('cnot',367b184)
k.gate('toffoli',365b183,a183)
k.gate('cnot',367a182)
k.gate('cnot',365b183)
k.gate('toffoli',363b182,a182)
k.gate('cnot',365a181)
k.gate('cnot',363b182)
k.gate('toffoli',361b181,a181)
k.gate('cnot',363a180)
k.gate('cnot',361b181)
k.gate('toffoli',359b180,a180)
k.gate('cnot',361a179)
k.gate('cnot',359b180)
k.gate('toffoli',357b179,a179)
k.gate('cnot',359a178)
k.gate('cnot',357b179)
k.gate('toffoli',355b178,a178)
k.gate('cnot',357a177)
k.gate('cnot',355b178)
k.gate('toffoli',353b177,a177)
k.gate('cnot',355a176)
k.gate('cnot',353b177)
k.gate('toffoli',351b176,a176)
k.gate('cnot',353a175)
k.gate('cnot',351b176)
k.gate('toffoli',349b175,a175)
k.gate('cnot',351a174)
k.gate('cnot',349b175)
k.gate('toffoli',347b174,a174)
k.gate('cnot',349a173)
k.gate('cnot',347b174)
k.gate('toffoli',345b173,a173)
k.gate('cnot',347a172)
k.gate('cnot',345b173)
k.gate('toffoli',343b172,a172)
k.gate('cnot',345a171)
k.gate('cnot',343b172)
k.gate('toffoli',341b171,a171)
k.gate('cnot',343a170)
k.gate('cnot',341b171)
k.gate('toffoli',339b170,a170)
k.gate('cnot',341a169)
k.gate('cnot',339b170)
k.gate('toffoli',337b169,a169)
k.gate('cnot',339a168)
k.gate('cnot',337b169)
k.gate('toffoli',335b168,a168)
k.gate('cnot',337a167)
k.gate('cnot',335b168)
k.gate('toffoli',333b167,a167)
k.gate('cnot',335a166)
k.gate('cnot',333b167)
k.gate('toffoli',331b166,a166)
k.gate('cnot',333a165)
k.gate('cnot',331b166)
k.gate('toffoli',329b165,a165)
k.gate('cnot',331a164)
k.gate('cnot',329b165)
k.gate('toffoli',327b164,a164)
k.gate('cnot',329a163)
k.gate('cnot',327b164)
k.gate('toffoli',325b163,a163)
k.gate('cnot',327a162)
k.gate('cnot',325b163)
k.gate('toffoli',323b162,a162)
k.gate('cnot',325a161)
k.gate('cnot',323b162)
k.gate('toffoli',321b161,a161)
k.gate('cnot',323a160)
k.gate('cnot',321b161)
k.gate('toffoli',319b160,a160)
k.gate('cnot',321a159)
k.gate('cnot',319b160)
k.gate('toffoli',317b159,a159)
k.gate('cnot',319a158)
k.gate('cnot',317b159)
k.gate('toffoli',315b158,a158)
k.gate('cnot',317a157)
k.gate('cnot',315b158)
k.gate('toffoli',313b157,a157)
k.gate('cnot',315a156)
k.gate('cnot',313b157)
k.gate('toffoli',311b156,a156)
k.gate('cnot',313a155)
k.gate('cnot',311b156)
k.gate('toffoli',309b155,a155)
k.gate('cnot',311a154)
k.gate('cnot',309b155)
k.gate('toffoli',307b154,a154)
k.gate('cnot',309a153)
k.gate('cnot',307b154)
k.gate('toffoli',305b153,a153)
k.gate('cnot',307a152)
k.gate('cnot',305b153)
k.gate('toffoli',303b152,a152)
k.gate('cnot',305a151)
k.gate('cnot',303b152)
k.gate('toffoli',301b151,a151)
k.gate('cnot',303a150)
k.gate('cnot',301b151)
k.gate('toffoli',299b150,a150)
k.gate('cnot',301a149)
k.gate('cnot',299b150)
k.gate('toffoli',297b149,a149)
k.gate('cnot',299a148)
k.gate('cnot',297b149)
k.gate('toffoli',295b148,a148)
k.gate('cnot',297a147)
k.gate('cnot',295b148)
k.gate('toffoli',293b147,a147)
k.gate('cnot',295a146)
k.gate('cnot',293b147)
k.gate('toffoli',291b146,a146)
k.gate('cnot',293a145)
k.gate('cnot',291b146)
k.gate('toffoli',289b145,a145)
k.gate('cnot',291a144)
k.gate('cnot',289b145)
k.gate('toffoli',287b144,a144)
k.gate('cnot',289a143)
k.gate('cnot',287b144)
k.gate('toffoli',285b143,a143)
k.gate('cnot',287a142)
k.gate('cnot',285b143)
k.gate('toffoli',283b142,a142)
k.gate('cnot',285a141)
k.gate('cnot',283b142)
k.gate('toffoli',281b141,a141)
k.gate('cnot',283a140)
k.gate('cnot',281b141)
k.gate('toffoli',279b140,a140)
k.gate('cnot',281a139)
k.gate('cnot',279b140)
k.gate('toffoli',277b139,a139)
k.gate('cnot',279a138)
k.gate('cnot',277b139)
k.gate('toffoli',275b138,a138)
k.gate('cnot',277a137)
k.gate('cnot',275b138)
k.gate('toffoli',273b137,a137)
k.gate('cnot',275a136)
k.gate('cnot',273b137)
k.gate('toffoli',271b136,a136)
k.gate('cnot',273a135)
k.gate('cnot',271b136)
k.gate('toffoli',269b135,a135)
k.gate('cnot',271a134)
k.gate('cnot',269b135)
k.gate('toffoli',267b134,a134)
k.gate('cnot',269a133)
k.gate('cnot',267b134)
k.gate('toffoli',265b133,a133)
k.gate('cnot',267a132)
k.gate('cnot',265b133)
k.gate('toffoli',263b132,a132)
k.gate('cnot',265a131)
k.gate('cnot',263b132)
k.gate('toffoli',261b131,a131)
k.gate('cnot',263a130)
k.gate('cnot',261b131)
k.gate('toffoli',259b130,a130)
k.gate('cnot',261a129)
k.gate('cnot',259b130)
k.gate('toffoli',257b129,a129)
k.gate('cnot',259a128)
k.gate('cnot',257b129)
k.gate('toffoli',255b128,a128)
k.gate('cnot',257a127)
k.gate('cnot',255b128)
k.gate('toffoli',253b127,a127)
k.gate('cnot',255a126)
k.gate('cnot',253b127)
k.gate('toffoli',251b126,a126)
k.gate('cnot',253a125)
k.gate('cnot',251b126)
k.gate('toffoli',249b125,a125)
k.gate('cnot',251a124)
k.gate('cnot',249b125)
k.gate('toffoli',247b124,a124)
k.gate('cnot',249a123)
k.gate('cnot',247b124)
k.gate('toffoli',245b123,a123)
k.gate('cnot',247a122)
k.gate('cnot',245b123)
k.gate('toffoli',243b122,a122)
k.gate('cnot',245a121)
k.gate('cnot',243b122)
k.gate('toffoli',241b121,a121)
k.gate('cnot',243a120)
k.gate('cnot',241b121)
k.gate('toffoli',239b120,a120)
k.gate('cnot',241a119)
k.gate('cnot',239b120)
k.gate('toffoli',237b119,a119)
k.gate('cnot',239a118)
k.gate('cnot',237b119)
k.gate('toffoli',235b118,a118)
k.gate('cnot',237a117)
k.gate('cnot',235b118)
k.gate('toffoli',233b117,a117)
k.gate('cnot',235a116)
k.gate('cnot',233b117)
k.gate('toffoli',231b116,a116)
k.gate('cnot',233a115)
k.gate('cnot',231b116)
k.gate('toffoli',229b115,a115)
k.gate('cnot',231a114)
k.gate('cnot',229b115)
k.gate('toffoli',227b114,a114)
k.gate('cnot',229a113)
k.gate('cnot',227b114)
k.gate('toffoli',225b113,a113)
k.gate('cnot',227a112)
k.gate('cnot',225b113)
k.gate('toffoli',223b112,a112)
k.gate('cnot',225a111)
k.gate('cnot',223b112)
k.gate('toffoli',221b111,a111)
k.gate('cnot',223a110)
k.gate('cnot',221b111)
k.gate('toffoli',219b110,a110)
k.gate('cnot',221a109)
k.gate('cnot',219b110)
k.gate('toffoli',217b109,a109)
k.gate('cnot',219a108)
k.gate('cnot',217b109)
k.gate('toffoli',215b108,a108)
k.gate('cnot',217a107)
k.gate('cnot',215b108)
k.gate('toffoli',213b107,a107)
k.gate('cnot',215a106)
k.gate('cnot',213b107)
k.gate('toffoli',211b106,a106)
k.gate('cnot',213a105)
k.gate('cnot',211b106)
k.gate('toffoli',209b105,a105)
k.gate('cnot',211a104)
k.gate('cnot',209b105)
k.gate('toffoli',207b104,a104)
k.gate('cnot',209a103)
k.gate('cnot',207b104)
k.gate('toffoli',205b103,a103)
k.gate('cnot',207a102)
k.gate('cnot',205b103)
k.gate('toffoli',203b102,a102)
k.gate('cnot',205a101)
k.gate('cnot',203b102)
k.gate('toffoli',201b101,a101)
k.gate('cnot',203a100)
k.gate('cnot',201b101)
k.gate('toffoli',199b100,a100)
k.gate('cnot',201a99)
k.gate('cnot',199b100)
k.gate('toffoli',197b99,a99)
k.gate('cnot',199a98)
k.gate('cnot',197b99)
k.gate('toffoli',195b98,a98)
k.gate('cnot',197a97)
k.gate('cnot',195b98)
k.gate('toffoli',193b97,a97)
k.gate('cnot',195a96)
k.gate('cnot',193b97)
k.gate('toffoli',191b96,a96)
k.gate('cnot',193a95)
k.gate('cnot',191b96)
k.gate('toffoli',189b95,a95)
k.gate('cnot',191a94)
k.gate('cnot',189b95)
k.gate('toffoli',187b94,a94)
k.gate('cnot',189a93)
k.gate('cnot',187b94)
k.gate('toffoli',185b93,a93)
k.gate('cnot',187a92)
k.gate('cnot',185b93)
k.gate('toffoli',183b92,a92)
k.gate('cnot',185a91)
k.gate('cnot',183b92)
k.gate('toffoli',181b91,a91)
k.gate('cnot',183a90)
k.gate('cnot',181b91)
k.gate('toffoli',179b90,a90)
k.gate('cnot',181a89)
k.gate('cnot',179b90)
k.gate('toffoli',177b89,a89)
k.gate('cnot',179a88)
k.gate('cnot',177b89)
k.gate('toffoli',175b88,a88)
k.gate('cnot',177a87)
k.gate('cnot',175b88)
k.gate('toffoli',173b87,a87)
k.gate('cnot',175a86)
k.gate('cnot',173b87)
k.gate('toffoli',171b86,a86)
k.gate('cnot',173a85)
k.gate('cnot',171b86)
k.gate('toffoli',169b85,a85)
k.gate('cnot',171a84)
k.gate('cnot',169b85)
k.gate('toffoli',167b84,a84)
k.gate('cnot',169a83)
k.gate('cnot',167b84)
k.gate('toffoli',165b83,a83)
k.gate('cnot',167a82)
k.gate('cnot',165b83)
k.gate('toffoli',163b82,a82)
k.gate('cnot',165a81)
k.gate('cnot',163b82)
k.gate('toffoli',161b81,a81)
k.gate('cnot',163a80)
k.gate('cnot',161b81)
k.gate('toffoli',159b80,a80)
k.gate('cnot',161a79)
k.gate('cnot',159b80)
k.gate('toffoli',157b79,a79)
k.gate('cnot',159a78)
k.gate('cnot',157b79)
k.gate('toffoli',155b78,a78)
k.gate('cnot',157a77)
k.gate('cnot',155b78)
k.gate('toffoli',153b77,a77)
k.gate('cnot',155a76)
k.gate('cnot',153b77)
k.gate('toffoli',151b76,a76)
k.gate('cnot',153a75)
k.gate('cnot',151b76)
k.gate('toffoli',149b75,a75)
k.gate('cnot',151a74)
k.gate('cnot',149b75)
k.gate('toffoli',147b74,a74)
k.gate('cnot',149a73)
k.gate('cnot',147b74)
k.gate('toffoli',145b73,a73)
k.gate('cnot',147a72)
k.gate('cnot',145b73)
k.gate('toffoli',143b72,a72)
k.gate('cnot',145a71)
k.gate('cnot',143b72)
k.gate('toffoli',141b71,a71)
k.gate('cnot',143a70)
k.gate('cnot',141b71)
k.gate('toffoli',139b70,a70)
k.gate('cnot',141a69)
k.gate('cnot',139b70)
k.gate('toffoli',137b69,a69)
k.gate('cnot',139a68)
k.gate('cnot',137b69)
k.gate('toffoli',135b68,a68)
k.gate('cnot',137a67)
k.gate('cnot',135b68)
k.gate('toffoli',133b67,a67)
k.gate('cnot',135a66)
k.gate('cnot',133b67)
k.gate('toffoli',131b66,a66)
k.gate('cnot',133a65)
k.gate('cnot',131b66)
k.gate('toffoli',129b65,a65)
k.gate('cnot',131a64)
k.gate('cnot',129b65)
k.gate('toffoli',127b64,a64)
k.gate('cnot',129a63)
k.gate('cnot',127b64)
k.gate('toffoli',125b63,a63)
k.gate('cnot',127a62)
k.gate('cnot',125b63)
k.gate('toffoli',123b62,a62)
k.gate('cnot',125a61)
k.gate('cnot',123b62)
k.gate('toffoli',121b61,a61)
k.gate('cnot',123a60)
k.gate('cnot',121b61)
k.gate('toffoli',119b60,a60)
k.gate('cnot',121a59)
k.gate('cnot',119b60)
k.gate('toffoli',117b59,a59)
k.gate('cnot',119a58)
k.gate('cnot',117b59)
k.gate('toffoli',115b58,a58)
k.gate('cnot',117a57)
k.gate('cnot',115b58)
k.gate('toffoli',113b57,a57)
k.gate('cnot',115a56)
k.gate('cnot',113b57)
k.gate('toffoli',111b56,a56)
k.gate('cnot',113a55)
k.gate('cnot',111b56)
k.gate('toffoli',109b55,a55)
k.gate('cnot',111a54)
k.gate('cnot',109b55)
k.gate('toffoli',107b54,a54)
k.gate('cnot',109a53)
k.gate('cnot',107b54)
k.gate('toffoli',105b53,a53)
k.gate('cnot',107a52)
k.gate('cnot',105b53)
k.gate('toffoli',103b52,a52)
k.gate('cnot',105a51)
k.gate('cnot',103b52)
k.gate('toffoli',101b51,a51)
k.gate('cnot',103a50)
k.gate('cnot',101b51)
k.gate('toffoli',99b50,a50)
k.gate('cnot',101a49)
k.gate('cnot',99b50)
k.gate('toffoli',97b49,a49)
k.gate('cnot',99a48)
k.gate('cnot',97b49)
k.gate('toffoli',95b48,a48)
k.gate('cnot',97a47)
k.gate('cnot',95b48)
k.gate('toffoli',93b47,a47)
k.gate('cnot',95a46)
k.gate('cnot',93b47)
k.gate('toffoli',91b46,a46)
k.gate('cnot',93a45)
k.gate('cnot',91b46)
k.gate('toffoli',89b45,a45)
k.gate('cnot',91a44)
k.gate('cnot',89b45)
k.gate('toffoli',87b44,a44)
k.gate('cnot',89a43)
k.gate('cnot',87b44)
k.gate('toffoli',85b43,a43)
k.gate('cnot',87a42)
k.gate('cnot',85b43)
k.gate('toffoli',83b42,a42)
k.gate('cnot',85a41)
k.gate('cnot',83b42)
k.gate('toffoli',81b41,a41)
k.gate('cnot',83a40)
k.gate('cnot',81b41)
k.gate('toffoli',79b40,a40)
k.gate('cnot',81a39)
k.gate('cnot',79b40)
k.gate('toffoli',77b39,a39)
k.gate('cnot',79a38)
k.gate('cnot',77b39)
k.gate('toffoli',75b38,a38)
k.gate('cnot',77a37)
k.gate('cnot',75b38)
k.gate('toffoli',73b37,a37)
k.gate('cnot',75a36)
k.gate('cnot',73b37)
k.gate('toffoli',71b36,a36)
k.gate('cnot',73a35)
k.gate('cnot',71b36)
k.gate('toffoli',69b35,a35)
k.gate('cnot',71a34)
k.gate('cnot',69b35)
k.gate('toffoli',67b34,a34)
k.gate('cnot',69a33)
k.gate('cnot',67b34)
k.gate('toffoli',65b33,a33)
k.gate('cnot',67a32)
k.gate('cnot',65b33)
k.gate('toffoli',63b32,a32)
k.gate('cnot',65a31)
k.gate('cnot',63b32)
k.gate('toffoli',61b31,a31)
k.gate('cnot',63a30)
k.gate('cnot',61b31)
k.gate('toffoli',59b30,a30)
k.gate('cnot',61a29)
k.gate('cnot',59b30)
k.gate('toffoli',57b29,a29)
k.gate('cnot',59a28)
k.gate('cnot',57b29)
k.gate('toffoli',55b28,a28)
k.gate('cnot',57a27)
k.gate('cnot',55b28)
k.gate('toffoli',53b27,a27)
k.gate('cnot',55a26)
k.gate('cnot',53b27)
k.gate('toffoli',51b26,a26)
k.gate('cnot',53a25)
k.gate('cnot',51b26)
k.gate('toffoli',49b25,a25)
k.gate('cnot',51a24)
k.gate('cnot',49b25)
k.gate('toffoli',47b24,a24)
k.gate('cnot',49a23)
k.gate('cnot',47b24)
k.gate('toffoli',45b23,a23)
k.gate('cnot',47a22)
k.gate('cnot',45b23)
k.gate('toffoli',43b22,a22)
k.gate('cnot',45a21)
k.gate('cnot',43b22)
k.gate('toffoli',41b21,a21)
k.gate('cnot',43a20)
k.gate('cnot',41b21)
k.gate('toffoli',39b20,a20)
k.gate('cnot',41a19)
k.gate('cnot',39b20)
k.gate('toffoli',37b19,a19)
k.gate('cnot',39a18)
k.gate('cnot',37b19)
k.gate('toffoli',35b18,a18)
k.gate('cnot',37a17)
k.gate('cnot',35b18)
k.gate('toffoli',33b17,a17)
k.gate('cnot',35a16)
k.gate('cnot',33b17)
k.gate('toffoli',31b16,a16)
k.gate('cnot',33a15)
k.gate('cnot',31b16)
k.gate('toffoli',29b15,a15)
k.gate('cnot',31a14)
k.gate('cnot',29b15)
k.gate('toffoli',27b14,a14)
k.gate('cnot',29a13)
k.gate('cnot',27b14)
k.gate('toffoli',25b13,a13)
k.gate('cnot',27a12)
k.gate('cnot',25b13)
k.gate('toffoli',23b12,a12)
k.gate('cnot',25a11)
k.gate('cnot',23b12)
k.gate('toffoli',21b11,a11)
k.gate('cnot',23a10)
k.gate('cnot',21b11)
k.gate('toffoli',19b10,a10)
k.gate('cnot',21a9)
k.gate('cnot',19b10)
k.gate('toffoli',17b9,a9)
k.gate('cnot',19a8)
k.gate('cnot',17b9)
k.gate('toffoli',15b8,a8)
k.gate('cnot',17a7)
k.gate('cnot',15b8)
k.gate('toffoli',13b7,a7)
k.gate('cnot',15a6)
k.gate('cnot',13b7)
k.gate('toffoli',11b6,a6)
k.gate('cnot',13a5)
k.gate('cnot',11b6)
k.gate('toffoli',9b5,a5)
k.gate('cnot',11a4)
k.gate('cnot',9b5)
k.gate('toffoli',7b4,a4)
k.gate('cnot',9a3)
k.gate('cnot',7b4)
k.gate('toffoli',5b3,a3)
k.gate('cnot',7a2)
k.gate('cnot',5b3)
k.gate('toffoli',3b2,a2)
k.gate('cnot',5a1)
k.gate('cnot',3b2)
k.gate('toffoli',1b1,a1)
k.gate('cnot',3a0)
k.gate('cnot',1b1)
k.gate('toffoli',0b0,a0)
k.gate('cnot',1c0)
k.gate('cnot',0b0)
p.add_kernel(k)
p.compile(optimize=False)