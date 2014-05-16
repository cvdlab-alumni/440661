from exercise1 import *
pink9 = [1,0.855,0.725]

top = assemblyDiagramInit([5,8,2])([[.3,6,.1,5,.3],[.3,8,.3,4,.3,5,.3,.3],[.3,2.7]])
V,CV = top
hpc = SKEL_1(STRUCT(MKPOLS(top)))
hpc = cellNumbering (top,hpc)(range(len(CV)),CYAN,2)

master = COLOR(pink9)(STRUCT(MKPOLS(master)))
top = STRUCT(MKPOLS(top))

palazzo = STRUCT([master, T(3)(3)(master), T(3)(6)(master), T(3)(9)(master), T(3)(12)(master), T(3)(15)(top)  ])

VIEW(palazzo)
