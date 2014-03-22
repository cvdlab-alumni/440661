from pyplasm import *


"""North"""

x_torriN = QUOTE([7.8,-10.3] * 2)
y_torriN = QUOTE([24,0])
x_facciataN = QUOTE([-7.8,10.3]) 
y_facciataN = QUOTE([20.5])
torri_north = INSR(PROD)([x_torriN, y_torriN, Q(0)])
punti_facciataN = [[7.8,0],[11.45,0],[14.45,0],[18.1,0],[7.8,20.5],[11.45,20.5],[14.45,20.5],[18.1,20.5]]
punti_porta = [[11.45,0],[14.45,0],[11.45,3],[14.45,3]]
porta = JOIN(AA(MK)(punti_porta)) 
f_north = JOIN(AA(MK)(punti_facciataN))
f_north = DIFFERENCE([f_north, porta]) 
north = STRUCT([torri_north,f_north])

"""South"""

x_torriS = QUOTE([7.8,-10.3] * 2)
y_torriS = QUOTE([24,0])
x_facciataS = QUOTE([-7.8,10.3]) 
y_facciataS = QUOTE([20.5])
torri_south = INSR(PROD)([x_torriN, y_torriN, Q(0)])
punti_facciataS = [[7.8,0],[11.45,0],[14.45,0],[18.1,0],[7.8,20.5],[11.45,20.5],[14.45,20.5],[18.1,20.5]]
f_south = JOIN(AA(MK)(punti_facciataS))
south = STRUCT([torri_south,f_south])

"""East"""
east = MAP([S3,S2,S1])(south)
final = STRUCT([north, east])

"""WEST"""
west = MAP([S3,S2,S1])(T(1)(25.9)(east))
south = MAP([S3,S2,S1])(west)

final = STRUCT([north, east, west, south])
VIEW(final)
