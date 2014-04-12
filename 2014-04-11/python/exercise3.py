import sys
""" import modules from lar-cc/lib """
sys.path.insert(0, 'C:\Users\Andrea\lar-cc\lar-cc\lib\py')
from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from morph import *
from mapper import *


"""exercise3.py"""

"""NEIGHBORHOOD"""
#Colours used
GRASS_GREEN = [0.004,0.651, 0.067]
SAND = [0.937,0.867,0.435]
BROWN = [0.627,0.322,0.176]
ASPHALT = [0.157,0.169,0.165]
PICASSO = [0.008,0.463,0.992]

#House
base = COLOR(WHITE)(CUBOID([5,5,5]))
points_window = [[1,2,2], [2,2,2], [1,3,2], [2,3,2]]
window = T([1,3])([0.5,2])(COLOR(BLUE)(CUBOID([1,1,1])))
door = T([1,3])([2.5])(COLOR(BROWN)(CUBOID([1,2,1])))
points_roof = [[0,0,5], [0,5,5], [5,5,5], [2.5,2.5,7], [5,0,5]]
roof = COLOR(RED)(JOIN(AA(MK)(points_roof)))
house = STRUCT([base,roof,window, door])

#church
base_c = COLOR(WHITE)(CUBOID([5,5,8]))
points_window = [[1,2,2], [2,2,2], [1,3,2], [2,3,2]]
window = T([1,3])([0.5,2])(COLOR(BLUE)(CUBOID([1,1,1])))
door = T([1,3])([2.5])(COLOR(BROWN)(CUBOID([1,2,1])))
points_roof = [[0,0,5], [0,5,5], [5,5,5], [2.5,2.5,7], [5,0,5]]
next_building = T(1)(4)(base)
window_c = T([1,3])([6,2])(COLOR(BLUE)(CUBOID([1,1,1])))
roof_c = T(3)(3)(COLOR(RED)(JOIN(AA(MK)(points_roof))))
church = STRUCT([base_c,roof_c,window, window_c, door, next_building])


#skyscraper
skyscraper = COLOR(WHITE)((CUBOID([10,10,60])))
window_s1 = T([1,3])([4.5,5])(COLOR(BLUE)(CUBOID([2,2,2])))
pair_z = [T([3])([5]), window_s1]
winCol = STRUCT(NN(10)(pair_z))
skyscraper = STRUCT([skyscraper,winCol])


#HouseRow
pair_x = [T([1])([20]), house]
houseRow = STRUCT(NN(3)(pair_x))
houseRow = T([1,2])([-10,60])(houseRow)

neighborhood = STRUCT([houseRow, (T([1,2])([-30,49])(church)), (T([1,2])([70,20])(skyscraper)), (T([1,2])([54,-45])(church)),
  (T([1,2])([-25,-45])(house))])


"""Terrain"""

V_SAND_TERR = [[-10,50], [-10, -30], [64,-30], [64,50]]
P_terr = AA(MK)(V_SAND_TERR)
sand_terr = AA(JOIN)([P_terr])
sand_terr = STRUCT(sand_terr)
sand_terr = STRUCT([COLOR(SAND)(sand_terr)])



V_GREEN_TERR = [[-50,90], [-50, -90], [104,-90], [104,90]]
P_terr = AA(MK)(V_GREEN_TERR)
green_terr = AA(JOIN)([P_terr])
green_terr = STRUCT(green_terr)
green_terr = STRUCT([COLOR(GRASS_GREEN)(green_terr)])

V_ASPH_TERR = [[-50,90], [-50, -90], [104,-90], [104,90]]
P_terr = AA(MK)(V_ASPH_TERR)
asph_terr = AA(JOIN)([P_terr])
asph_terr = STRUCT(asph_terr)
asph_terr = STRUCT([COLOR(ASPHALT)(asph_terr)])

"""Final model"""
final_model = STRUCT([model_3d,green_terr,neighborhood])

VIEW(final_model)




