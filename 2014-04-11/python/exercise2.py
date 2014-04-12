import sys
""" import modules from lar-cc/lib """
sys.path.insert(0, 'C:\Users\Andrea\lar-cc\lar-cc\lib\py')
from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from morph import *
from mapper import *


V_EXT = [[0,0],[0,-3],[2,-5],[5,-5],[7,-3],[14,-10],[12,-12],[12,-15],[14,-17],[17,-17],[19,-15],[19,-12],
#bordello

[25,-12],[25,-10],[17,-10],[19,-3],[25,-3],[25,0],[19,0],[17,2],[17,18],[19,20],[35,20],[37,18],[37,2],[35,0],[29,0],
[29,-3],[35,-3],[37,-10],[29,-10],[29,-12],
#bordello
[35,-12],[35,-15],[37,-17],
[40,-17],[42,-15],[42,-12],[40,-10],[47,-3],[49,-5],[52,-5],[54,-3],[54,0],[52,2],[49,2],[49,18],[52,18],[54,20],[54,23],[52,25],
[49,25],[47,23],[40,30],[42,32],[42,35],[40,37],[37,37],[35,35],[35,32],[19,32],[19,35],[17,37],[14,37],[12,35],[12,32],[14,30],
[7,23],[5,25],[2,25],[0,23],[0,20],[2,18],[5,18],[5,2],[2,2],[0,0]]

V_INT = [[19,-3],
#bordello2
[25,-3],[25,0],[19,0],[17,2],[17,18],[19,20],[35,20],[37,18],[37,2],[35,0],[29,0],
[29,-3],
#bordello2
[35,-3],[40,2],[40,18], [35,23],[19,23],[14,18],[14,2],[19,-3]]
V_INT2 = [[19,-3], [35,-3],[40,2],[40,18], [35,23],[19,23],[14,18],[14,2],[19,-3]]
#EAST_ROOM = [[17,-10], [37,-10],[35,-3],[19,-3],[17,-10]] 
NEAST_ROOM = [[37,-10], [47,0],[40,2],[35,-3],[37,-10]]
NORTH_ROOM = [[47,0], [47,20],[40,18],[40,2],[47,0]]
NWEST_ROOM = [[40,18], [47,20],[37,30],[35,23],[40,18]]
WEST_ROOM = [[37,30], [17,30],[19,23],[35,23],[37,30]]
SWEST_ROOM = [[19,23], [17,30],[5,20],[14,18],[19,23]]
SWEST_ROOM = [[19,23], [17,30],[7,20],[14,18],[19,23]]
SOUTH_ROOM = [[7,0], [14,2],[14,18],[7,20],[7,0]]
SEAST_ROOM = [[7,0], [14,2],[19,-3],[17,-10],[7,0]]
#COURT = [[19,0], [35,0],[37,2],[37,18],[35,20],[19,20],[17,18],[17,2],[19,0]]




fondamenta_ext = POLYLINE(V_EXT)
fondamenta_int = POLYLINE(V_INT)
#east_room = POLYLINE(EAST_ROOM)
neast_room = POLYLINE(NEAST_ROOM)
north_room = POLYLINE(NORTH_ROOM)
nwest_room = POLYLINE(NWEST_ROOM)
west_room = POLYLINE(WEST_ROOM)
swest_room = POLYLINE(SWEST_ROOM)
south_room = POLYLINE(SOUTH_ROOM)
seast_room = POLYLINE(SEAST_ROOM)
#court = POLYLINE(COURT)

"""FLOOR0"""
P_floor = AA(MK)(V_EXT)
floor = AA(JOIN)([P_floor])

floor = STRUCT(floor)
floor0 = PROD([floor,Q(3)])

#Columns of the rooms
column_e = (CIRCLE(0.5)([32,32]))
column_e = T([1,2])([27,-6.5])(column_e)
#column_e = PROD([column_e, Q(15)])

column_w = (CIRCLE(0.5)([32,32]))
column_w = T([1,2])([27,26.5])(column_w)
#column_w = PROD([column_w, Q(15)])

column_s = (CIRCLE(0.5)([32,32]))
column_s = T([1,2])([9.5,10])(column_s)
#column_s = PROD([column_s, Q(15)])

column_n = (CIRCLE(0.5)([32,32]))
column_n = T([1,2])([43.5,10])(column_n)
#column_n = PROD([column_n, Q(15)])

column_ne = (CIRCLE(0.5)([32,32]))
column_ne = T([1,2])([40,-3])(column_ne)
#column_ne = PROD([column_ne, Q(15)])

column_nw = (CIRCLE(0.5)([32,32]))
column_nw = T([1,2])([40,23])(column_nw)
#column_nw = PROD([column_nw, Q(15)])

column_sw = (CIRCLE(0.5)([32,32]))
column_sw = T([1,2])([14,23])(column_sw)
#column_sw = PROD([column_sw, Q(15)])

column_se = (CIRCLE(0.5)([32,32]))
column_se = T([1,2])([14,-3])(column_se)
#column_se = PROD([column_se, Q(15)])

#Columns of the towers
columnI = (CIRCLE(0.25)([32,32]))
columnI = T([1,2])([38.5,-13.5])(columnI)
#columnI = PROD([columnI, Q(15)])

columnII = (CIRCLE(0.25)([32,32]))
columnII = T([1,2])([50.5,-1.5])(columnII)
#columnII = PROD([columnII, Q(15)])

columnIII = (CIRCLE(0.25)([32,32]))
columnIII = T([1,2])([50.5,21.5])(columnIII)
#columnIII = PROD([columnIII, Q(15)])

columnIV = (CIRCLE(0.25)([32,32]))
columnIV = T([1,2])([38.5,33.5])(columnIV)
#columnIV = PROD([columnIV, Q(15)])

columnV = (CIRCLE(0.25)([32,32]))
columnV = T([1,2])([15.5,33.5])(columnV)
#columnV = PROD([columnV, Q(15)])

columnVI = (CIRCLE(0.25)([32,32]))
columnVI = T([1,2])([3.5,21.5])(columnVI)
#columnVI = PROD([columnVI, Q(15)])

columnVII = (CIRCLE(0.25)([32,32]))
columnVII = T([1,2])([3.5,-1.5])(columnVII)
#columnVII = PROD([columnVII, Q(15)])


columnVIII = (CIRCLE(0.25)([32,32]))
columnVIII = T([1,2])([15.5,-13.5])(columnVIII)
#columnVIII = PROD([columnVIII, Q(15)])

columns = STRUCT([column_e, column_w, column_s, column_n, column_ne,
	column_nw, column_sw, column_se, columnI, columnII, columnIII, columnIV, columnV,
	columnVI, columnVII, columnVIII])
columns = PROD([columns,Q(26)])

model = STRUCT([fondamenta_int,fondamenta_ext, neast_room, north_room
	,nwest_room,west_room, swest_room, south_room, seast_room])
model = (PROD([model,Q(13)]))

#VIEW(model)


"""SECOND FLOOR"""
#V_FLOOR1 = [[17,-10],[37,-10],[47,0],[47,20],[37,30],[17,30],[7,20],
#		[7,0],[17,-10]]
V_FLOOR1 = [[19,-12],[35,-12],[40,-10],[47,-3],[49,2],[49,18],[47,23],[40,30],
[35,32],[19,32],[14,30],[7,23],[5,18],[5,2],[7,-3],[14,-10]]
P_int = AA(MK)(V_INT)
int1 = AA(JOIN)([P_int])
int1 = STRUCT(int1)

P_floor1 = AA(MK)(V_FLOOR1)
floor1 = AA(JOIN)([P_floor1])
floor1 = STRUCT(floor1)

floor1 = DIFFERENCE([floor1,int1])
floor1 = T([3])(11)(PROD([floor1,Q(2)]))


V_EXT2 = [[0,0],[0,-3],[2,-5],[5,-5],[7,-3],[14,-10],[12,-12],[12,-15],[14,-17],[17,-17],[19,-15],[19,-12],
[35,-12],[35,-15],[37,-17],
[40,-17],[42,-15],[42,-12],[40,-10],[47,-3],[49,-5],[52,-5],[54,-3],[54,0],[52,2],[49,2],[49,18],[52,18],[54,20],[54,23],[52,25],
[49,25],[47,23],[40,30],[42,32],[42,35],[40,37],[37,37],[35,35],[35,32],[19,32],[19,35],[17,37],[14,37],[12,35],[12,32],[14,30],
[7,23],[5,25],[2,25],[0,23],[0,20],[2,18],[5,18],[5,2],[2,2],[0,0]]
fondamenta_ext2 = POLYLINE(V_EXT2)


model_floor1 = STRUCT([fondamenta_int,fondamenta_ext2, neast_room, north_room
	,nwest_room,west_room, swest_room, south_room, seast_room])
model_floor1 = (PROD([model_floor1,Q(13)]))


floor1_main =  T([3])(13)(model_floor1)
#VIEW((floor1))

"""ROOF"""
roof = T([3])(13)(floor1)

"""FINAL MODEL"""
model_3d = STRUCT([model, floor0, columns, floor1, floor1_main, roof])

"""WINDOWS"""

P_win1 = [[26.5,-12,13],[27.5,-12,13],[26.5,-12,14],[27.5,-12,14]]
P_win1 = AA(MK)(P_win1)
win1 = AA(JOIN)([P_win1])
win1 = STRUCT(win1)



model_3d = DIFFERENCE([model_3d,win1])

#VIEW(model_3d)




