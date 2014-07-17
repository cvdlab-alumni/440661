import sys
from exercise3 import *
""" import modules from lar-cc/lib """
sys.path.insert(0, 'C:\Users\Andrea\lar-cc\lar-cc\lib\py')
from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from morph import *
from mapper import *

"""exercise4.py"""

#Colours
CROWN = [0,0.992,0]
TRUNK = [0.361,0.2,0.09]
LAMP = [1,1,0,0.5]
STONE = [0.545,0.553,0.478]
PINK = [1,0.411,0.706]


"""Tree"""
trunk = (CIRCLE(0.25)([8,8]))
trunk = PROD([trunk, Q(4)])
crown = T(3)(4)(COLOR(CROWN)(SPHERE(1)([8,8])))
tree = STRUCT([(COLOR(TRUNK)(trunk)),crown])
pair_y = [T([2])([4]), tree]
treeRow1 = STRUCT(NN(10)(pair_y))
treeRow1 = T([1,2])([16,-70])(treeRow1)
treeRow2 = T([1])([22])(treeRow1)

"""Street lamp"""
trunk_l = (CIRCLE(0.1)([8,8]))
trunk_l = PROD([trunk_l, Q(4)])
lamp = T(3)(4)(COLOR(LAMP)(SPHERE(0.4)([8,8])))
lamp = STRUCT([(COLOR(ASPHALT)(trunk_l)),lamp])

pair_y = [T([2])([4]), lamp]
lampRow1 = STRUCT(NN(10)(pair_y))
lampRow1 = T([1,2])([19,-70])(lampRow1)
lampRow2 = T([1])([16])(lampRow1)

"""Street"""
points_street = [[19,-90],[19,-15],[35,-15],[35,-90]]
street = AA(MK)(points_street)
street = AA(JOIN)([street])
street = COLOR(STONE)(STRUCT(street))

"""Flowers"""
stem = (CIRCLE(0.05)([16,16]))
stem = COLOR(GREEN)(PROD([stem, Q(0.5)]))
crown = T(3)(0.5)(SPHERE(0.1)([8,8]))
flower_y = STRUCT([stem,(COLOR(YELLOW)(crown))])

flower_p = STRUCT([stem,(COLOR(PINK)(crown))])


"""Flower containers"""
cont_ext = CUBOID([2,2,1])
cont_int = COLOR(TRUNK)(T([1,2])([0.5,0.5])(CUBOID([1,1,1])))
contain_flow1 = T([1,2,3])([1,1,1])(flower_y)
contain_flow2 = T([1,2,3])([1,1.2,1])(flower_p)
container = (STRUCT([cont_ext,cont_int, contain_flow1, contain_flow2]))

container_y = [T([2])([3]), container]
contRow1 = STRUCT(NN(6)(container_y))
contRow1 = T([1,2])([19,-90])(contRow1)
contRow2 = T([1])([14])(contRow1)

final_model = STRUCT([model_3d,green_terr,neighborhood, lampRow1, lampRow2, street, treeRow1, treeRow2, contRow1, contRow2])


VIEW(final_model)




