from pyplasm import *

SAND = [0.937, 0.867, 0.435]

P_floor0 = floor0
P_floor1 = T(3)(3)(floor1)
P_floor2 = T(3)(9.5)(floor2)
P_floor3 = T(3)(20.5)(floor3)
P_floor3_torri = T(3)(24)(COLOR([0.2,0,1])(floor3_towers))

two_and_half_model = STRUCT([P_floor0, P_floor1, P_floor2, P_floor3, P_floor3_torri])

floor0_3d = PROD([P_floor0, Q(3)])
floor1_3d = T(3)(3)(PROD([floor1, Q(6.5)]))
floor2_3d = T(3)(9.5)(PROD([floor2, Q(11.5)]))
floor3_3d = T(3)(20.5)(PROD([floor3, Q(0)]))
floor3_torri_3d = T(3)(20.5)(PROD([floor3_towers, Q(3.5)]))


solid_model_3d = STRUCT([COLOR(SAND)(floor0_3d), COLOR(SAND)(floor1_3d), COLOR(SAND)(floor2_3d),
					COLOR(SAND)(floor3_3d), COLOR(SAND)(floor3_torri_3d)])

VIEW(solid_model_3d)
