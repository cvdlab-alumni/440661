from exercise1 import *
from splines import *
pink9 = [1,0.855,0.725]

"""Corridor"""
###################################
#Corridor_base
Corridor_base = assemblyDiagramInit([5,3,2])([[.3,4.9,.1,8.8,.3],[.3,5,.3],[.3,3.7]]) #x=13.8, y=15.6
V,CV = Corridor_base
hpc_corridor_base = SKEL_1(STRUCT(MKPOLS(Corridor_base)))
hpc_corridor_base = cellNumbering (Corridor_base,hpc_corridor_base)(range(len(CV)),CYAN,2)

toRemove = [9,15,21]
Corridor_base = Corridor_base[0], [cell for k,cell in enumerate(Corridor_base[1]) if not (k in toRemove)]

#Door1
toMerge = 20
doorDiagram = assemblyDiagramInit([3,1,2])([[1.3,1,6.5],[.3],[2.4,.3]])
Corridor_base = diagram2cell(doorDiagram,Corridor_base,toMerge)
hpc_corridor_base = SKEL_1(STRUCT(MKPOLS(Corridor_base)))
hpc_corridor_base = cellNumbering (Corridor_base,hpc_corridor_base)(range(len(Corridor_base[1])),CYAN,2)

toRemove = [28]
Corridor_base = Corridor_base[0], [cell for k,cell in enumerate(Corridor_base[1]) if not (k in toRemove)]

###################################
#Corridor
corridor = assemblyDiagramInit([5,3,2])([[.3,4.9,.1,8.8,.3],[.3,5,.3],[.3,2.7]]) #x=13.8, y=15.6
V,CV = corridor
hpc_corridor = SKEL_1(STRUCT(MKPOLS(corridor)))
hpc_corridor = cellNumbering (corridor,hpc_corridor)(range(len(CV)),CYAN,2)

toRemove = [9,8,15,21]
corridor = corridor[0], [cell for k,cell in enumerate(corridor[1]) if not (k in toRemove)]

#Door1
toMerge = 19
doorDiagram = assemblyDiagramInit([3,1,2])([[1.3,1,6.5],[.3],[2.4,.3]])
corridor = diagram2cell(doorDiagram,corridor,toMerge)
hpc_corridor = SKEL_1(STRUCT(MKPOLS(corridor)))
hpc_corridor = cellNumbering (corridor,hpc_corridor)(range(len(corridor[1])),CYAN,2)


toRemove = [27]
corridor = corridor[0], [cell for k,cell in enumerate(corridor[1]) if not (k in toRemove)]

#Door2
toMerge = 16
doorDiagram = assemblyDiagramInit([3,1,2])([[1.4,1,6.5],[.3],[2.4,.3]])
corridor = diagram2cell(doorDiagram,corridor,toMerge)
hpc_corridor = SKEL_1(STRUCT(MKPOLS(corridor)))
hpc_corridor = cellNumbering (corridor,hpc_corridor)(range(len(corridor[1])),CYAN,2)

toRemove = [31]
corridor = corridor[0], [cell for k,cell in enumerate(corridor[1]) if not (k in toRemove)]

#Window
toMerge = 3
doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[3,1,3],[2.4,.3]])
corridor = diagram2cell(doorDiagram,corridor,toMerge)
hpc_corridor = SKEL_1(STRUCT(MKPOLS(corridor)))
hpc_corridor = cellNumbering (corridor,hpc_corridor)(range(len(corridor[1])),CYAN,2)

#########################
cor_w = [35]
cor_w = corridor[0], [cell for k,cell in enumerate(corridor[1]) if (k in cor_w)]
cor_w = COLOR(WINDOW)((STRUCT(MKPOLS(cor_w))))
cor_w = MK_TRNSP(cor_w)
#########################

toRemove = [35]
corridor = corridor[0], [cell for k,cell in enumerate(corridor[1]) if not (k in toRemove)]

"""Stairs"""
step1 = CUBOID([1,0.5,0.2])

step2 = T([2,3])([0.4,0.2])(step1)
step3 = T([2,3])([0.8,0.4])(step1)
step4 = T([2,3])([1.2,0.6])(step1)
step5 = T([2,3])([1.6,0.8])(step1)
step6 = T([2,3])([2.0,1.0])(CUBOID([1,1,0.2]))
stair1 = STRUCT([step1, step2, step3, step4, step5, step6])

stair_floor = STRUCT([stair1, T([1,2,3])([0,2,1.3])(R([1,2])(PI/2)(stair1))
					,T([1,2,3])([-2,2,2.6])(R([1,2])(PI)(stair1)),
   					T([1,2,3])([-2,0,3.5])(R([1,2])(3*PI/2)(stair1))
   					])


"""Hill"""
c10 = larBezier(S1)([[0,0,0],[10,0,0]])
c11 = larBezier(S1)([[0,10,0],[2.5,10,3],[5,10,-3],[7.5,10,3],[10,10,0]])
c20 = larBezier(S2)([[0,0,0],[0,0,3],[0,10,3],[0,10,0]])
c21 = larBezier(S2)([[10,0,0],[10,5,3],[10,10,0]])
dom = larDomain([10])
dom2D = larModelProduct([dom, dom])
out = larMap(larCoonsPatch([c10,c11,c20,c21]))(dom2D)

"""Struct balcone"""
balcone = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
balcone = master[0], [cell for k,cell in enumerate(master[1]) if (k in balcone)]
balcone = (STRUCT(MKPOLS(balcone)))

balcone2 = [219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,
			238,239,240,241]
balcone2 = master[0], [cell for k,cell in enumerate(master[1]) if (k in balcone2)]
balcone2 = (STRUCT(MKPOLS(balcone2)))


toRemove = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

"""Assembling"""
column = CUBOID([1,3,4])
column_couple = STRUCT([T([1,2,3])([6,0,-4])(column), T([1,2,3])([12,0,-4])(column)])
master = COLOR(pink9)(STRUCT(MKPOLS(master)))
master = STRUCT([balcone, master, balcone2, hall_door, hall_window, hall_doorw,kitch_door,kitch_doorw,
				s_door, n_door, w_door, sw_door, e_door, room_win, room_winr, room_win2])

corridor = COLOR(pink9)(STRUCT(MKPOLS(corridor)))
corridor = STRUCT([corridor, T([1,2,3])([4.5,2,-4])(stair_floor)])
Corridor_base = (STRUCT(MKPOLS(Corridor_base)))
master_rotate = R([1,2])(160.222)(master)
hill = R([1,2])(79.999)(COLOR(GREEN)(STRUCT(MKPOLS(out))))

floor = STRUCT([T(2)(-10.6)(master), T([1,2])([2,-16.2])(corridor), T([1,2])([2,-16.2])(cor_w), (T([1,2])([18.3,-16.2])(master_rotate)), 
				])
roof = T([3])([21])(CUBOID([17, 40, 3])) #top of the dwelling
dwelling = STRUCT([T([1,2,3])([2,-16,-4])(Corridor_base), column_couple, T(2)(-30)(column_couple),
				floor, T(3)(3)(floor), T(3)(6)(floor), T(3)(9)(floor), T(3)(12)(floor),
				T(3)(15)(floor),T(3)(18)(floor), T([1,2,3])([1.2,-33.5,0])(roof)])

#VIEW(dwelling)

ground = STRUCT([T(2)(-10)(hill), T(2)(17)(hill)])


model = STRUCT([T([1,2,3])([5,-3.5,7])(dwelling), ground])

VIEW(model)
