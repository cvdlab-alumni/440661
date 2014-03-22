from pyplasm import *


##############################FUNZIONI UTILI############################
#Funzione circle parametrica per raggio 
def circle(r):
	def circle0(p):
		alpha = p[0]
		return [r*COS(alpha), r*SIN(alpha)]
	return circle0


########################################################################
#####################FLOOR 0############################################
"""Base del castello; alza di 3 metri l'intero edificio"""
cinta_esterna0 = MAP(circle(28))(INTERVALS(2*PI)(8))
cinta_interna0 = MAP(circle(11.3))(INTERVALS(2*PI)(8))
#cortina_esterna0 = MAP(circle(25.6))(INTERVALS(2*PI)(8))
#cortina_interna0 = MAP(circle(8.9))(INTERVALS(2*PI)(8))

torre1_0 = T(1)(29.3)(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
torre2_0 = T([2])([29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
torre3_0 = T([2])([-29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
torre4_0 = T([1])([-29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
torre5_0 = T([1,2])([20.718,20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
torre6_0 = T([1,2])([-20.718,20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
torre7_0 = T([1,2])([-20.718,-20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
torre8_0 = T([1,2])([20.718,-20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))

floor0 = STRUCT([cinta_esterna0, cinta_interna0,
				 torre1_0, torre2_0, torre3_0, torre4_0, torre5_0, torre6_0, torre7_0, torre8_0])
#VIEW(floor0)

########################################################################
#####################FLOOR 1############################################
"""Primo piano: tutte le torri tranne la 3, 5 e 7 non presentano scale a chiocciola"""
cinta_esterna1 = MAP(circle(28))(INTERVALS(2*PI)(8))
cinta_interna1 = MAP(circle(11.3))(INTERVALS(2*PI)(8))
cortina_esterna1 = MAP(circle(25.6))(INTERVALS(2*PI)(8))
cortina_interna1 = MAP(circle(8.9))(INTERVALS(2*PI)(8))

torre1_1 = T([1,2])([20.718,20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna1_1 = T([1,2])([20.718,20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala1_1 = T([1,2])([20.718,20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre2_1 = T([2])([29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna2_1 = T([2])([29.3])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala2_1 = T([2])([29.3])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre3_1 = T([1,2])([-20.718,20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna3_1 = T([1,2])([-20.718,20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
scala3_1 = T([1,2])([-20.718,20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(32)))


torre4_1 = T([1])([-29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna4_1 = T([1])([-29.3])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala4_1 = T([1])([-29.3])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre5_1 = T([1,2])([-20.718,-20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna5_1 = T([1,2])([-20.718,-20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
scala5_1 = T([1,2])([-20.718,-20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(32)))

torre6_1 = T([2])([-29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna6_1 = T([2])([-29.3])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala6_1 = T([2])([-29.3])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre7_1 = T([1,2])([20.718,-20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna7_1 = T([1,2])([20.718,-20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
scala7_1 = T([1,2])([20.718,-20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(32)))

torre8_1 = T(1)(29.3)(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna8_1 = T(1)(29.3)(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala8_1 = T(1)(29.3)(MAP(circle(1.3))(INTERVALS(2*PI)(8)))



floor1 = STRUCT([cinta_esterna1, cinta_interna1, cortina_interna1, cortina_esterna1,
				torre1_1, colonna1_1, finta_scala1_1,
				torre2_1, colonna2_1, finta_scala2_1,
				torre3_1, colonna3_1, scala3_1,
				torre4_1, colonna4_1, finta_scala4_1,
				torre5_1, colonna5_1, scala5_1,
				torre6_1, colonna6_1, finta_scala6_1,
				torre7_1, colonna7_1, scala7_1,
				 torre8_1, colonna8_1, finta_scala8_1])


########################################################################
#####################FLOOR 2############################################
"""Secondo piano: tutte le torri tranne la 3, 5 e 7 non presentano scale a chiocciola"""
cinta_esterna2 = MAP(circle(28))(INTERVALS(2*PI)(8))
cinta_interna2 = MAP(circle(11.3))(INTERVALS(2*PI)(8))
cortina_esterna2 = MAP(circle(25.6))(INTERVALS(2*PI)(8))
cortina_interna2 = MAP(circle(8.9))(INTERVALS(2*PI)(8))

torre1_2 = T([1,2])([20.718,20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna1_2 = T([1,2])([20.718,20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala1_2 = T([1,2])([20.718,20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre2_2 = T([2])([29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna2_2 = T([2])([29.3])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala2_2 = T([2])([29.3])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre3_2 = T([1,2])([-20.718,20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna3_2 = T([1,2])([-20.718,20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
scala3_2 = T([1,2])([-20.718,20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(32)))


torre4_2 = T([1])([-29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna4_2 = T([1])([-29.3])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala4_2 = T([1])([-29.3])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre5_2 = T([1,2])([-20.718,-20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna5_2 = T([1,2])([-20.718,-20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
scala5_2 = T([1,2])([-20.718,-20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(32)))

torre6_2 = T([2])([-29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna6_2 = T([2])([-29.3])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala6_2 = T([2])([-29.3])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre7_2 = T([1,2])([20.718,-20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna7_2 = T([1,2])([20.718,-20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
scala7_2 = T([1,2])([20.718,-20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(32)))

torre8_2 = T(1)(29.3)(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna8_2 = T(1)(29.3)(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala8_2 = T(1)(29.3)(MAP(circle(1.3))(INTERVALS(2*PI)(8)))



floor2 = STRUCT([cinta_esterna2, cinta_interna2, cortina_interna2, cortina_esterna2,
				torre1_2, colonna1_2, finta_scala1_2,
				torre2_2, colonna2_2, finta_scala2_2,
				torre3_2, colonna3_2, scala3_2,
				torre4_2, colonna4_2, finta_scala4_2,
				torre5_2, colonna5_2, scala5_2,
				torre6_2, colonna6_2, finta_scala6_2,
				torre7_2, colonna7_2, scala7_2,
				torre8_2, colonna8_2, finta_scala8_2])


########################################################################
#####################FLOOR 3############################################
"""Tetto"""
cinta_esterna3 = MAP(circle(28))(INTERVALS(2*PI)(8))
cinta_interna3 = MAP(circle(11.3))(INTERVALS(2*PI)(8))
cortina_esterna3 = MAP(circle(25.6))(INTERVALS(2*PI)(8))
cortina_interna3 = MAP(circle(8.9))(INTERVALS(2*PI)(8))

torre1_3 = T([1,2])([20.718,20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna1_3 = T([1,2])([20.718,20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala1_3 = T([1,2])([20.718,20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre2_3 = T([2])([29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna2_3 = T([2])([29.3])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala2_3 = T([2])([29.3])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre3_3 = T([1,2])([-20.718,20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna3_3 = T([1,2])([-20.718,20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
scala3_3 = T([1,2])([-20.718,20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(32)))


torre4_3 = T([1])([-29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna4_3 = T([1])([-29.3])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala4_3 = T([1])([-29.3])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre5_3 = T([1,2])([-20.718,-20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna5_3 = T([1,2])([-20.718,-20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
scala5_3 = T([1,2])([-20.718,-20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(32)))

torre6_3 = T([2])([-29.3])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna6_3 = T([2])([-29.3])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala6_3 = T([2])([-29.3])(MAP(circle(1.3))(INTERVALS(2*PI)(8)))

torre7_3 = T([1,2])([20.718,-20.718])(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna7_3 = T([1,2])([20.718,-20.718])(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
scala7_3 = T([1,2])([20.718,-20.718])(MAP(circle(1.3))(INTERVALS(2*PI)(32)))

torre8_3 = T(1)(29.3)(MAP(circle(3.9))(INTERVALS(2*PI)(8)))
colonna8_3 = T(1)(29.3)(MAP(circle(0.11))(INTERVALS(2*PI)(32)))
finta_scala8_3 = T(1)(29.3)(MAP(circle(1.3))(INTERVALS(2*PI)(8)))



floor3 = STRUCT([cinta_esterna3, cinta_interna3, cortina_interna3, cortina_esterna3,
				torre1_3, colonna1_3, finta_scala1_3,
				torre2_3, colonna2_3, finta_scala2_3,
				torre3_3, colonna3_3, scala3_3,
				torre4_3, colonna4_3, finta_scala4_3,
				torre5_3, colonna5_3, scala5_3,
				torre6_3, colonna6_3, finta_scala6_3,
				torre7_3, colonna7_3, scala7_3,
				torre8_3, colonna8_3, finta_scala8_3])

VIEW(floor3)