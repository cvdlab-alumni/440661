from pyplasm import *



########################################################################
#####################FLOOR 0############################################
"""Base del castello; alza di 3 metri l'intero edificio"""
cinta_esterna0 = CIRCLE(28)([8,32])
cinta_interna0 = CIRCLE(11.3)([8,32])
torre1_0 = T(1)(29.3)(CIRCLE(3.9)([8,32]))
torre2_0 = T([2])([29.3])(CIRCLE(3.9)([8,32]))
torre3_0 = T([2])([-29.3])(CIRCLE(3.9)([8,32]))
torre4_0 = T([1])([-29.3])(CIRCLE(3.9)([8,32]))
torre5_0 = T([1,2])([20.718,20.718])(CIRCLE(3.9)([8,32]))
torre6_0 = T([1,2])([-20.718,20.718])(CIRCLE(3.9)([8,32]))
torre7_0 = T([1,2])([-20.718,-20.718])(CIRCLE(3.9)([8,32]))
torre8_0 = T([1,2])([20.718,-20.718])(CIRCLE(3.9)([8,32]))

floor0_court = DIFFERENCE([cinta_esterna0, cinta_interna0])

floor0_tower =	STRUCT([torre1_0, torre2_0, torre3_0, torre4_0, torre5_0, torre6_0, torre7_0, torre8_0])
floor0 = STRUCT([COLOR([1,0.27,0])(floor0_court), COLOR([1,0.55,0])(floor0_tower)])

#VIEW(floor0)

########################################################################
#####################FLOOR 1############################################
"""Primo piano: tutte le torri tranne la 3, 5 e 7 non presentano scale a chiocciola"""

cinta_esterna1 = CIRCLE(28)([8,32])
cinta_interna1 = CIRCLE(11.3)([8,32])
#cortina_esterna1 = CIRCLE(25.6)([8,32])
#cortina_interna1 = CIRCLE(8.9)([8,32])

torre1_1 = T(1)(29.3)(CIRCLE(3.9)([8,32]))
colonna1_1 = T([1,2])([20.718,20.718])(CIRCLE(0.11)([8,32]))
finta_scala1_1 = T([1,2])([20.718,20.718])(CIRCLE(1.3)([8,32]))


torre2_1 = T([2])([29.3])(CIRCLE(3.9)([8,32]))
colonna2_1 = T([2])([29.3])(CIRCLE(0.11)([8,32]))
finta_scala2_1 = T([2])([29.3])(CIRCLE(1.3)([8,32]))


torre3_1 = T([2])([-29.3])(CIRCLE(3.9)([8,32]))
colonna3_1 = T([1,2])([-20.718,20.718])(CIRCLE(0.11)([8,32]))
scala3_1 = T([1,2])([-20.718,20.718])(CIRCLE(1.3)([8,32]))


torre4_1 = T([1])([-29.3])(CIRCLE(3.9)([8,32]))
colonna4_1 = T([1])([-29.3])(CIRCLE(0.11)([8,32]))
finta_scala4_1 = T([1])([-29.3])(CIRCLE(1.3)([8,32]))


torre5_1 = T([1,2])([20.718,20.718])(CIRCLE(3.9)([8,32]))
colonna5_1 = T([1,2])([-20.718,-20.718])(CIRCLE(0.11)([8,32]))
scala5_1 = T([1,2])([-20.718,-20.718])(CIRCLE(1.3)([8,32]))


torre6_1 = T([1,2])([-20.718,20.718])(CIRCLE(3.9)([8,32]))
colonna6_1 = T([2])([-29.3])(CIRCLE(0.11)([8,32]))
finta_scala6_1 = T([2])([-29.3])(CIRCLE(1.3)([8,32]))

torre7_1 = T([1,2])([-20.718,-20.718])(CIRCLE(3.9)([8,32]))
colonna7_1 = T([1,2])([20.718,-20.718])(CIRCLE(0.11)([8,32]))
scala7_1 = T([1,2])([20.718,-20.718])(CIRCLE(1.3)([8,32]))


torre8_1 = T([1,2])([20.718,-20.718])(CIRCLE(3.9)([8,32]))
colonna8_1 = T(1)(29.3)(CIRCLE(0.11)([8,32]))
finta_scala8_1 = T(1)(29.3)(CIRCLE(1.3)([8,32]))


colonnina1_1 = T([1,2])([14, 6])(CIRCLE(0.5)([8,32]))
colonnina4_1 = T([1,2])([-14, 6])(CIRCLE(0.5)([8,32]))
colonnina5_1 = T([1,2])([-14, -6])(CIRCLE(0.5)([8,32]))
colonnina8_1 = T([1,2])([14, -6])(CIRCLE(0.5)([8,32]))

colonnina2_1 = T([1,2])([6, 14])(CIRCLE(0.5)([8,32]))
colonnina7_1 = T([1,2])([6, -14])(CIRCLE(0.5)([8,32]))
colonnina3_1 = T([1,2])([-6, 14])(CIRCLE(0.5)([8,32]))
colonnina6_1 = T([1,2])([-6, -14])(CIRCLE(0.5)([8,32]))

floor1_court = DIFFERENCE([cinta_esterna1, cinta_interna1])

floor1_colonnine = STRUCT([colonnina1_1, colonnina2_1, colonnina3_1, colonnina4_1, 
							colonnina5_1, colonnina6_1, colonnina7_1, colonnina8_1])
floor1_towers = STRUCT([torre1_1, torre2_1, torre3_1, torre4_1,
						torre5_1, torre6_1, torre7_1, torre8_1])
floor1_scale = STRUCT([scala3_1, scala5_1, scala7_1])
floor1_finteScale = STRUCT([finta_scala1_1,finta_scala2_1,finta_scala4_1,
					finta_scala6_1, finta_scala8_1,])
floor1_colonne = STRUCT([colonna1_1, colonna2_1, colonna3_1,colonna4_1,
						colonna5_1,colonna6_1,colonna7_1,colonna8_1])
floor1 = STRUCT([COLOR([1,0.65,0])(floor1_court), COLOR([1,0.843,0])(floor1_towers),COLOR([0.72,0.52,0.04])(floor1_scale),
				 COLOR([0.85,0.65,0.125])(floor1_finteScale), COLOR([0.85,0.65,0.125])(floor1_colonne), COLOR(YELLOW)(floor1_colonnine)])

#VIEW(floor1)

########################################################################
#####################FLOOR 2############################################
"""Secondo piano: tutte le torri tranne la 3, 5 e 7 non presentano scale a chiocciola"""
cinta_esterna2 = CIRCLE(28)([8,32])
cinta_interna2 = CIRCLE(11.3)([8,32])
#cortina_esterna1 = CIRCLE(25.6)([8,32])
#cortina_interna1 = CIRCLE(8.9)([8,32])

torre1_2 = T(1)(29.3)(CIRCLE(3.9)([8,32]))
colonna1_2 = T([1,2])([20.718,20.718])(CIRCLE(0.11)([8,32]))
finta_scala1_2 = T([1,2])([20.718,20.718])(CIRCLE(1.3)([8,32]))


torre2_2 = T([2])([29.3])(CIRCLE(3.9)([8,32]))
colonna2_2 = T([2])([29.3])(CIRCLE(0.11)([8,32]))
finta_scala2_2 = T([2])([29.3])(CIRCLE(1.3)([8,32]))


torre3_2 = T([2])([-29.3])(CIRCLE(3.9)([8,32]))
colonna3_2 = T([1,2])([-20.718,20.718])(CIRCLE(0.11)([8,32]))
scala3_2 = T([1,2])([-20.718,20.718])(CIRCLE(1.3)([8,32]))


torre4_2 = T([1])([-29.3])(CIRCLE(3.9)([8,32]))
colonna4_2 = T([1])([-29.3])(CIRCLE(0.11)([8,32]))
finta_scala4_2 = T([1])([-29.3])(CIRCLE(1.3)([8,32]))


torre5_2 = T([1,2])([20.718,20.718])(CIRCLE(3.9)([8,32]))
colonna5_2 = T([1,2])([-20.718,-20.718])(CIRCLE(0.11)([8,32]))
scala5_2 = T([1,2])([-20.718,-20.718])(CIRCLE(1.3)([8,32]))


torre6_2 = T([1,2])([-20.718,20.718])(CIRCLE(3.9)([8,32]))
colonna6_2 = T([2])([-29.3])(CIRCLE(0.11)([8,32]))
finta_scala6_2 = T([2])([-29.3])(CIRCLE(1.3)([8,32]))

torre7_2 = T([1,2])([-20.718,-20.718])(CIRCLE(3.9)([8,32]))
colonna7_2 = T([1,2])([20.718,-20.718])(CIRCLE(0.11)([8,32]))
scala7_2 = T([1,2])([20.718,-20.718])(CIRCLE(1.3)([8,32]))


torre8_2 = T([1,2])([20.718,-20.718])(CIRCLE(3.9)([8,32]))
colonna8_2 = T(1)(29.3)(CIRCLE(0.11)([8,32]))
finta_scala8_2 = T(1)(29.3)(CIRCLE(1.3)([8,32]))


colonnina1_2 = T([1,2])([14, 6])(CIRCLE(0.5)([8,32]))
colonnina4_2 = T([1,2])([-14, 6])(CIRCLE(0.5)([8,32]))
colonnina5_2 = T([1,2])([-14, -6])(CIRCLE(0.5)([8,32]))
colonnina8_2 = T([1,2])([14, -6])(CIRCLE(0.5)([8,32]))
colonnina2_2 = T([1,2])([6, 14])(CIRCLE(0.5)([8,32]))
colonnina7_2 = T([1,2])([6, -14])(CIRCLE(0.5)([8,32]))
colonnina3_2 = T([1,2])([-6, 14])(CIRCLE(0.5)([8,32]))
colonnina6_2 = T([1,2])([-6, -14])(CIRCLE(0.5)([8,32]))

floor2_court = DIFFERENCE([cinta_esterna2, cinta_interna2])

floor2_colonnine = STRUCT([colonnina1_2, colonnina2_2, colonnina3_2, colonnina4_2, 
							colonnina5_2, colonnina6_2, colonnina7_2, colonnina8_2])
floor2_towers = STRUCT([torre1_2, torre2_2, torre3_2, torre4_2,
						torre5_2, torre6_2, torre7_2, torre8_2])
floor2_scale = STRUCT([scala3_2, scala5_2, scala7_2])
floor2_finteScale = STRUCT([finta_scala1_2,finta_scala2_2,finta_scala4_2,
					finta_scala6_2, finta_scala8_2,])
floor2_colonne = STRUCT([colonna1_2, colonna2_2, colonna3_2,colonna4_2,
						colonna5_2,colonna6_2,colonna7_2,colonna8_2])
floor2 = STRUCT([COLOR([0,1,0])(floor2_court), COLOR([0.2,1,0])(floor2_towers),COLOR([0.4,1,0])(floor2_scale),
				 COLOR([0.6,1,0])(floor2_finteScale), COLOR([0.8,1,0])(floor2_colonne), COLOR([0.8,1,0.2])(floor2_colonnine)])

#VIEW(floor2)

########################################################################
#####################FLOOR 3############################################
"""Tetto - Le torri sono piu' alte rispetto all'edificio"""
cinta_esterna3 = CIRCLE(28)([8,32])
cinta_interna3 = CIRCLE(11.3)([8,32])
#cortina_esterna1 = CIRCLE(25.6)([8,32])
#cortina_interna1 = CIRCLE(8.9)([8,32])

torre1_3 = T(1)(29.3)(CIRCLE(3.9)([8,32]))
colonna1_3 = T([1,2])([20.718,20.718])(CIRCLE(0.11)([8,32]))
finta_scala1_3 = T([1,2])([20.718,20.718])(CIRCLE(1.3)([8,32]))


torre2_3 = T([2])([29.3])(CIRCLE(3.9)([8,32]))
colonna2_3 = T([2])([29.3])(CIRCLE(0.11)([8,32]))
finta_scala2_3 = T([2])([29.3])(CIRCLE(1.3)([8,32]))


torre3_3 = T([2])([-29.3])(CIRCLE(3.9)([8,32]))
colonna3_3 = T([1,2])([-20.718,20.718])(CIRCLE(0.11)([8,32]))
scala3_3 = T([1,2])([-20.718,20.718])(CIRCLE(1.3)([8,32]))


torre4_3 = T([1])([-29.3])(CIRCLE(3.9)([8,32]))
colonna4_3 = T([1])([-29.3])(CIRCLE(0.11)([8,32]))
finta_scala4_3 = T([1])([-29.3])(CIRCLE(1.3)([8,32]))


torre5_3 = T([1,2])([20.718,20.718])(CIRCLE(3.9)([8,32]))
colonna5_3 = T([1,2])([-20.718,-20.718])(CIRCLE(0.11)([8,32]))
scala5_3 = T([1,2])([-20.718,-20.718])(CIRCLE(1.3)([8,32]))


torre6_3 = T([1,2])([-20.718,20.718])(CIRCLE(3.9)([8,32]))
colonna6_3 = T([2])([-29.3])(CIRCLE(0.11)([8,32]))
finta_scala6_3 = T([2])([-29.3])(CIRCLE(1.3)([8,32]))

torre7_3 = T([1,2])([-20.718,-20.718])(CIRCLE(3.9)([8,32]))
colonna7_3 = T([1,2])([20.718,-20.718])(CIRCLE(0.11)([8,32]))
scala7_3 = T([1,2])([20.718,-20.718])(CIRCLE(1.3)([8,32]))


torre8_3 = T([1,2])([20.718,-20.718])(CIRCLE(3.9)([8,32]))
colonna8_3 = T(1)(29.3)(CIRCLE(0.11)([8,32]))
finta_scala8_3 = T(1)(29.3)(CIRCLE(1.3)([8,32]))


colonnina1_3 = T([1,2])([14, 6])(CIRCLE(0.5)([8,32]))
colonnina4_3 = T([1,2])([-14, 6])(CIRCLE(0.5)([8,32]))
colonnina5_3 = T([1,2])([-14, -6])(CIRCLE(0.5)([8,32]))
colonnina8_3 = T([1,2])([14, -6])(CIRCLE(0.5)([8,32]))
colonnina2_3 = T([1,2])([6, 14])(CIRCLE(0.5)([8,32]))
colonnina7_3 = T([1,2])([6, -14])(CIRCLE(0.5)([8,32]))
colonnina3_3 = T([1,2])([-6, 14])(CIRCLE(0.5)([8,32]))
colonnina6_3 = T([1,2])([-6, -14])(CIRCLE(0.5)([8,32]))

floor3_court = DIFFERENCE([cinta_esterna3, cinta_interna3])

floor3_colonnine = STRUCT([colonnina1_3, colonnina2_3, colonnina3_3, colonnina4_3, 
							colonnina5_3, colonnina6_3, colonnina7_3, colonnina8_3])

floor3_scale = STRUCT([scala3_3, scala5_3, scala7_3])

floor3_finteScale = STRUCT([finta_scala1_3,finta_scala2_3,finta_scala4_3,
					finta_scala6_3, finta_scala8_3])
floor3_towers = STRUCT([torre1_3, torre2_3, torre3_3, torre4_3,
						torre5_3, torre6_3, torre7_3, torre8_3, floor3_scale, floor3_finteScale])
floor3_colonne = STRUCT([colonna1_3, colonna2_3, colonna3_3,colonna4_3,
						colonna5_3,colonna6_3,colonna7_3,colonna8_3])
floor3 = STRUCT([COLOR([0,0,1])(floor3_court),COLOR([0.4,0,1])(floor3_scale),
				 COLOR([0.6,0,1])(floor3_finteScale), COLOR([0.8,0,1])(floor3_colonne), COLOR([0.8,0.2,1])(floor3_colonnine)])

#VIEW(floor3)

###################################################################################
P_floor0 = floor0
P_floor1 = T(3)(3)(floor1)
P_floor2 = T(3)(9.5)(floor2)
P_floor3 = T(3)(20.5)(floor3)
P_floor3_torri = T(3)(24)(COLOR([0.2,0,1])(floor3_towers))

two_and_half_model = STRUCT([P_floor0, P_floor1, P_floor2, P_floor3, P_floor3_torri])

#VIEW(two_and_half_model)

