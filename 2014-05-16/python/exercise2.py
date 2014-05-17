from exercise1 import *
from splines import *
pink9 = [1,0.855,0.725]

"""Top of the dwelling"""
top = assemblyDiagramInit([5,8,2])([[.3,6,.1,5,.3],[.3,8,.3,4,.3,5,.3,.3],[.3,2.7]])
V,CV = top
hpc = SKEL_1(STRUCT(MKPOLS(top)))
hpc = cellNumbering (top,hpc)(range(len(CV)),CYAN,2)

"""Corridor"""
corridor = assemblyDiagramInit([3,3,2])([[.3,11,.3],[.3,17.9,.3],[.3,2.7]])
V,CV = corridor
hpc_corridor = SKEL_1(STRUCT(MKPOLS(corridor)))
hpc_corridor = cellNumbering (corridor,hpc_corridor)(range(len(CV)),CYAN,2)
#VIEW(hpc_corridor)

toRemove = [9]
corridor = corridor[0], [cell for k,cell in enumerate(corridor[1]) if not (k in toRemove)]
#VIEW(hpc_corridor)


#Door1
toMerge = 7
doorDiagram = assemblyDiagramInit([3,1,2])([[8,1,2.7],[.3],[2.4,.3]])
corridor = diagram2cell(doorDiagram,corridor,toMerge)
hpc_corridor = SKEL_1(STRUCT(MKPOLS(corridor)))
hpc_corridor = cellNumbering (corridor,hpc_corridor)(range(len(corridor[1])),CYAN,2)
#VIEW(hpc_corridor)

toRemove = [18]
corridor = corridor[0], [cell for k,cell in enumerate(corridor[1]) if not (k in toRemove)]

#Door2
toMerge = 9
doorDiagram = assemblyDiagramInit([3,1,2])([[1.6,1,4.7],[.3],[2.4,.3]])
corridor = diagram2cell(doorDiagram,corridor,toMerge)
hpc_corridor = SKEL_1(STRUCT(MKPOLS(corridor)))
hpc_corridor = cellNumbering (corridor,hpc_corridor)(range(len(corridor[1])),CYAN,2)
#VIEW(hpc_corridor)

toRemove = [22]
corridor = corridor[0], [cell for k,cell in enumerate(corridor[1]) if not (k in toRemove)]

#VIEW(hpc_corridor)

#Entrance
toMerge = 12
doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[3,1,3],[2.4,.3]])
corridor = diagram2cell(doorDiagram,corridor,toMerge)
hpc_corridor = SKEL_1(STRUCT(MKPOLS(corridor)))
hpc_corridor = cellNumbering (corridor,hpc_corridor)(range(len(corridor[1])),CYAN,2)
#VIEW(hpc_corridor)

toRemove = [26]
corridor = corridor[0], [cell for k,cell in enumerate(corridor[1]) if not (k in toRemove)]

#DRAW(corridor)

"""Stairs"""
stair = spiralStair(width=0.2,R=3,r=0.25,riser=0.1,pitch=4.4,nturns=1.5,steps=24)
stair = larApply(r(0,0,3*PI/4))(stair)
stair = larApply(t(0,-3,0))(stair)
stairColumn = larApply(t(0,-3,0))(larRod(0.25,4.2)())
stairs3D = evalStruct(Struct([stairColumn,stair,t(0,0,4)]*4))
stairs = (STRUCT(CAT(AA(MKPOLS)(stairs3D))))

"""Assembling"""

master = COLOR(pink9)(STRUCT(MKPOLS(master)))
top = STRUCT(MKPOLS(top))
corridor = (STRUCT(MKPOLS(corridor)))
master_rotate = R([1,2])(160.222)(master)


floor = STRUCT([master, T([2])([-18.5])(corridor), (T([1,2])([11.65,-18.5])(master_rotate))])
roof = STRUCT([top, T([2])([-18.5])(top), (T([2])([-37])(top))])
dwelling = STRUCT([floor, T(3)(3)(floor), T(3)(6)(floor), T(3)(9)(floor), T(3)(12)(floor), T(3)(15)(roof), T([1,2])([8,-5])(stairs)])


VIEW(dwelling)
