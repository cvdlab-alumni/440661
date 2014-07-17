from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
#sys.path.insert(0, 'lib/py/')
sys.path.insert(0, 'C:\Users\Andrea\lar-cc\lar-cc\lib\py')

from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import vertexSieve
from myfont import *
from architectural import *
from sysml import *

def MK_TRNSP(hpc):
    return MATERIAL([1,1,1,0.1, 0,0,0.8,0.5, 1,1,1,0.1, 1,1,1,0.1, 100])(hpc)

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#Colors
WINDOW = [0.686, 0.933, 0.933]
DOOR = [0.545, 0.271, 0.075]

master = assemblyDiagramInit([13,11,3])([[.3,2,.3,4,.3,4,.1,3,.1,2,.3,2,.3],[.3,5,.1,2,.1,3,.3,2,.1,3,.3],[.3,1.2,1.5]])
#master = assemblyDiagramInit([5,8,2])([[.3,6,.1,5,.3],[.3,8,.3,4,.3,5,.3,.3],[.3,2.7]])



V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)


def merge(diagram, mergeCells, master) :
	for cell in mergeCells :
		master = diagram2cell(diagram,master,cell)
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
	hpc = S([1,2,3])([300,300,300])(hpc)
	array = [hpc,master]
	return array


"""Hall door"""
doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,2.5],[.3],[2,.7]])

array = merge(doorDiagram, [167,166], master)
hpc = array[0]
master = array[1]
#VIEW(hpc)

"""Hall window"""
toMerge = [71]
windowDiagram = assemblyDiagramInit([1,8,5])([[.3],[.1,.5,.1,.5,.1,.5,.1,.5],[.3,1,.1,1,.5]])

array = merge(windowDiagram, toMerge, master)
hpc = array[0]
master = array[1]
#hpc = S(3)(2)(hpc)
#VIEW(hpc)


"""Hall doorwindow"""
toMerge= [82,81]
doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[.5,1.5,1],[2,.7]])

array = merge(doorDiagram, toMerge, master)
hpc = array[0]
master = array[1]
#VIEW(hpc)

"""Kitchen"""
#door
toMerge = [198,197]
doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[3,1,1],[2,.7]])
array = merge(doorDiagram, toMerge, master)
hpc = array[0]
master = array[1]


#doorwindow
toMerge = [328,327]
doorwindowDiagram_kit = assemblyDiagramInit([1,3,3])([[.3],[3,1,1],[.05,2,.65]])
array = merge(doorwindowDiagram_kit, toMerge, master)
hpc = array[0]
master = array[1]
#VIEW(hpc)

"""Corridor"""
#South door
toMerge = [180,179]
doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,2.5],[.3],[2,.7]])
array = merge(doorDiagram, toMerge, master)
hpc = array[0]
master = array[1]
#VIEW(hpc)

#Bathroom door
toMerge = [184,183]
doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,2.5],[.3],[2,.7]])
array = merge(doorDiagram, toMerge, master)
hpc = array[0]
master = array[1]
#VIEW(hpc)

#West door
toMerge = [152,151]
doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[.5,1,.5],[2,.7]])
array = merge(doorDiagram, toMerge, master)
hpc = array[0]
master = array[1]

#SouthEast door
toMerge = [238,237]
doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,1.5],[.3],[2,.7]])
array = merge(doorDiagram, toMerge, master)
hpc = array[0]
master = array[1]

#East door
toMerge = [272,271]
doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[.5,1,.5],[2,.7]])
array = merge(doorDiagram, toMerge, master)
hpc = array[0]
master = array[1]


#VIEW(hpc)

"""Left room"""
toMerge = [92]
windowDiagram = assemblyDiagramInit([1,5,5])([[.3],[1.1,1,.1,1,1.1],[.3,1,.1,1,.5]])
array = merge(windowDiagram, toMerge, master)
hpc = array[0]
master = array[1]


"""Right room"""
toMerge = [339]
windowDiagram = assemblyDiagramInit([1,5,5])([[.3],[1.1,1,.1,1,1.1],[.3,1,.1,1,.5]])
array = merge(windowDiagram, toMerge, master)
hpc = array[0]
master = array[1]

"""Bottom room"""
toMerge = [321, 320]
doorwindowDiagram_kit = assemblyDiagramInit([1,3,3])([[.3],[.5,1,.5],[.05,2,.65]])
array = merge(doorwindowDiagram_kit, toMerge, master)
hpc = array[0]
master = array[1]
#VIEW(hpc)

# master = diagram2cell(doorDiagram,master,167)
# master = diagram2cell(doorDiagram,master,166)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)




#hpc = S([1,2,3])([300,300,300])(hpc)
#VIEW(hpc)
#VIEW(hpc)



# toRemove = [38,37,35,2,5,8,11,14,41,40,44,43,47,50,49,17,53,20,46, #balconeSX
# 			56,55,62,61,104,103,106,107,110,109,112,113,115,116,122,121,128,127,
# 			124,125,136,137,142,143,148,149,169,170,172,173,175,176,178,179,181,182,
# 			140,139,145,146,187,188,194,193,221,220,254,253,320,319,322,323,325,326,
# 			292,293,259,260,248,247,245,244,242,241,307,308,235,236,268,269,301,302,
# 			390,391,392,393,394,395,426,427,428,423,424,425,387,388,389,420,421,422,384,385,386,
# 			417,418,419,383,416,379,380,413,314,313,310,311,#parte superiore+parte nel mezzo
# 			377,410,407,374,373,371,370,404,368,367,401,398,365,#balconeDX
# 			21,22,23,54,55,24,25,26,27,28,29,30,31,32,63,64,65,60,61,62,57,58,59,376,377#parte in alto a sx
# 			]
#master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]


# toRemove = [38,37,35,2,5,8,11,14,41,40,44,43,47,50,49,17,53,20,46, #balconeSX
# 			56,55,62,61,104,103,106,107,110,109,112,113,115,116,122,121,128,127,
# 			124,125,136,137,142,143,148,149,169,170,172,173,175,176,178,179,181,182,
# 			140,139,145,146,187,188,194,193,221,220,254,253,320,319,322,323,325,326,
# 			292,293,259,260,248,247,245,244,242,241,307,308,235,236,268,269,301,302,
# 			390,391,392,393,394,395,426,427,428,423,424,425,387,388,389,420,421,422,384,385,386,
# 			417,418,419,383,416,379,380,413,314,313,310,311,#parte superiore+parte nel mezzo
# 			377,410,407,374,373,371,370,404,368,367,401,398,365,#balconeDX
# 			21,22,23,54,55,24,25,26,27,28,29,30,31,32,63,64,65,60,61,62,57,58,59,376,377#parte in alto a sx
# 			]
#hpc = S([1,2,3])([3,4,6])(hpc)
#VIEW(hpc)
toRemove = [38,37,35,2,5,41,8,44,11,14,47,43,14,17,20,53,50,49,40,46,56,55,54,21,22,23,57,58,59,24,25,26,27,28,29,30,31,
			32,60,61,62,63,64,65,424,426,434,436,444,446,99,100,132,133,414,415,408,162,161,105,106,108,109,138,139,164,
			165,167,168,170,171,466,467,460,111,112,144,145,173,174,102,103,141,142,135,136,478,479,472,222,221,253,252,
			284,283,486,485,495,496,345,344,342,375,378,347,348,381,384,350,351,354,387,357,356,390,353,
			360,361,362,363,364,365,366,367,368,369,370,371,372,393,394,395,396,397,398,399,400,401,402,403,
			404,405,508,509,502,178,177,514,520,521,182,181,532,533,526,118,117,121,120,123,124,566,568,576,578,206,207,
			237,238,545,544,538,234,233,230,231,228,227,264,265,295,296,259,258,262,261,293,292,289,290,614,613,623,624,
			550,556,557,302,301,304,305,307,308,274,275,243,244,593,591,603,601,
            425,430,435,440,445,429,439,431,441, 
            596, 598, 592, 597, 602,
            567,568,573,572,577,571]

def objExporter((V,FV), filePath):
    out_file = open(filePath,"w")
    out_file.write("# List of Vertices:\n")
    for v in V:
        out_file.write("v")
        for c in v:
            out_file.write(" " + str(c))
        out_file.write("\n")
    out_file.write("# Face Definitions:\n")
    for f in FV:
        out_file.write("f")
        for v in f:
            out_file.write(" " + str(v+1))
        out_file.write("\n")
    out_file.close()


solidCV = [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


exteriorCV =  [cell for k,cell in enumerate(master[1]) if k in toRemove]
exteriorCV += exteriorCells(master)
CV = solidCV + exteriorCV
V = master[0]
FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]

BF = boundaryCells(solidCV,FV)
boundaryFaces = [FV[face] for face in BF]
B_Rep = V,boundaryFaces


verts, triangles = quads2tria(B_Rep)
B_Rep = verts, triangles
objExporter(B_Rep, 'C:\Users\Andrea\\threejs-crumbs\\threejs-crumbs\examples\\assets\models\casa.obj')
#VIEW(STRUCT(MKPOLS((verts, triangles))))


#DRAW(master)
#VIEW(hpc)

# """Hall - the room down on the left"""
# #Hall Door
# # toMerge = 98
# # doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,2.5],[.3],[2,.7]])
# # master = diagram2cell(doorDiagram,master,toMerge)
# # hpc = SKEL_1(STRUCT(MKPOLS(master)))
# # hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# # toMerge = 97
# # doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,2.5],[.3],[2,.5]])
# # master = diagram2cell(doorDiagram,master,toMerge)
# # hpc = SKEL_1(STRUCT(MKPOLS(master)))
# # hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# #VIEW(hpc)


# #toRemove = [271,278,277]
# #master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
# #########################STRUCT hall_door
# hall_door = [271,278,277]
# hall_door = master[0], [cell for k,cell in enumerate(master[1]) if (k in hall_door)]
# hall_door = COLOR(DOOR)((STRUCT(MKPOLS(hall_door))))
# #########################
# toRemove = [271,278,277]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]



# #VIEW(hall_door)

# #VIEW(hpc)
# #DRAW(master)

# #Hall window
# toMerge = 28
# windowDiagram = assemblyDiagramInit([1,8,5])([[.3],[.1,.5,.1,.5,.1,.5,.1,.5],[.3,1,.1,1,.5]])
# master = diagram2cell(windowDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2) 
# #VIEW(hpc)

# #####################################STRUCT hall_window
# hall_window = [315,313,305,303,295,293]
# hall_window = master[0], [cell for k,cell in enumerate(master[1]) if (k in hall_window)]
# hall_window = COLOR(WINDOW)((STRUCT(MKPOLS(hall_window))))
# hall_window = MK_TRNSP(hall_window)
# #####################################
# toRemove = [315,313,305,303,295,293]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

# #VIEW(hpc)

# #Hall doorwindow
# toMerge = 38
# doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[1,1.5,2],[2.4,.5]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# toMerge = 38
# doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[1,1.5,2],[2.4,.5]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# ##########################
# hall_doorw = [317,312,311]
# hall_doorw = master[0], [cell for k,cell in enumerate(master[1]) if (k in hall_doorw)]
# hall_doorw = COLOR(WINDOW)((STRUCT(MKPOLS(hall_doorw))))
# hall_doorw = MK_TRNSP(hall_doorw)
# ##########################

# toRemove = [317,312,311]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

# """Kitchen - aka the room down on the right"""
# #kitchen door
# toMerge = 115
# doorDiagram_kit = assemblyDiagramInit([1,3,2])([[.3],[3,1.5,3],[2.1,.3]])
# master = diagram2cell(doorDiagram_kit,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# toMerge = 114
# doorDiagram_kit = assemblyDiagramInit([1,3,2])([[.3],[3,1.5,3],[2.1,.3]])
# master = diagram2cell(doorDiagram_kit,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# #VIEW(hpc)

# ################################
# kitch_door = [318,324,325]
# kitch_door = master[0], [cell for k,cell in enumerate(master[1]) if (k in kitch_door)]
# kitch_door = COLOR(DOOR)((STRUCT(MKPOLS(kitch_door))))
# ################################
# toRemove = [318,324,325]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

# #kitchen doorwindow
# toMerge = 212
# doorwindowDiagram_kit = assemblyDiagramInit([1,3,3])([[.3],[3,1.5,3],[.5,2,.3]])
# master = diagram2cell(doorwindowDiagram_kit,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# toMerge = 212
# doorwindowDiagram_kit = assemblyDiagramInit([1,3,3])([[.3],[3,1.5,3],[.5,2,.3]])
# master = diagram2cell(doorwindowDiagram_kit,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# ################################
# kitch_doorw = [335,336,327]
# kitch_doorw = master[0], [cell for k,cell in enumerate(master[1]) if (k in kitch_doorw)]
# kitch_doorw = COLOR(WINDOW)((STRUCT(MKPOLS(kitch_doorw))))
# kitch_doorw = MK_TRNSP(kitch_doorw)
# ################################

# toRemove = [335,336,327]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


# """Corridor"""
# #south door - the door on the hall
# toMerge = 100
# doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,1.5],[.3],[2,.7]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# toMerge = 100
# doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,1.5],[.3],[2,.5]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
# #########################################
# s_door = [338,339,344]
# s_door = master[0], [cell for k,cell in enumerate(master[1]) if (k in s_door)]
# s_door = COLOR(DOOR)((STRUCT(MKPOLS(s_door))))
# #########################################
# toRemove = [338,339,344]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


# #north door - the door on the top bathroom
# toMerge = 102
# doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,1.5],[.3],[2,.7]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# toMerge = 102
# doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,1.5],[.3],[2,.7]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# #########################################
# n_door = [351,345,346]
# n_door = master[0], [cell for k,cell in enumerate(master[1]) if (k in n_door)]
# n_door = COLOR(DOOR)((STRUCT(MKPOLS(n_door))))
# #########################################

# toRemove = [351,345,346]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


# #west door - the door on the left room
# toMerge = 82
# doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[.3,1,.3],[2.4,.5]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# toMerge = 82
# doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[.3,1,.3],[2.4,.5]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# #########################################
# w_door = [352,353,358]
# w_door = master[0], [cell for k,cell in enumerate(master[1]) if (k in w_door)]
# w_door = COLOR(DOOR)((STRUCT(MKPOLS(w_door))))
# #########################################

# toRemove = [352,353,358]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


# #south west door - the door on the bottom room
# toMerge = 144
# doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,1.5],[.3],[2,.7]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# toMerge = 144
# doorDiagram = assemblyDiagramInit([3,1,2])([[3,2,1.5],[.3],[2,.5]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# #########################################
# sw_door = [359,360,365]
# sw_door = master[0], [cell for k,cell in enumerate(master[1]) if (k in sw_door)]
# sw_door = COLOR(DOOR)((STRUCT(MKPOLS(sw_door))))
# #########################################


# toRemove = [359,360,365]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


# #east door - the door on the top room
# toMerge = 173
# doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[.3,1,.3],[2.4,.5]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# toMerge = 172
# doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[.3,1,.3],[2.4,.5]])
# master = diagram2cell(doorDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# #########################################
# e_door = [372,373,366]
# e_door = master[0], [cell for k,cell in enumerate(master[1]) if (k in e_door)]
# e_door = COLOR(DOOR)((STRUCT(MKPOLS(e_door))))
# #########################################

# toRemove = [372,373,366]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]



# """Room - the room top on the left"""
# #Room window
# toMerge = 49
# windowDiagram = assemblyDiagramInit([1,5,5])([[.3],[1.1,1,.1,1,1.1],[.3,1,.1,1,.5]])
# master = diagram2cell(windowDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2) 

# #########################################
# room_win = [390,380,379,378,389,388]
# room_win = master[0], [cell for k,cell in enumerate(master[1]) if (k in room_win)]
# room_win = COLOR(WINDOW)((STRUCT(MKPOLS(room_win))))
# room_win = MK_TRNSP(room_win)
# #########################################

# toRemove = [390,380,379,378,389,388]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


# """Room - the room top on the right"""
# #Room window
# toMerge = 224
# windowDiagram = assemblyDiagramInit([1,5,5])([[.3],[1.1,1,.1,1,1.1],[.3,1,.1,1,.5]])
# master = diagram2cell(windowDiagram,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,3) 

# #########################################
# room_winr = [398,408,396,397,407,406]
# room_winr = master[0], [cell for k,cell in enumerate(master[1]) if (k in room_winr)]
# room_winr = COLOR(WINDOW)((STRUCT(MKPOLS(room_winr))))
# room_winr = MK_TRNSP(room_winr)
# #########################################

# toRemove = [398,408,396,397,407,406, 166,165,163,162,160,159]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


# """Room-the bottom room"""
# toMerge = 200
# doorwindowDiagram_kit = assemblyDiagramInit([1,3,3])([[.3],[.5,1,.5],[.5,2,.3]])
# master = diagram2cell(doorwindowDiagram_kit,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# toMerge = 199
# doorwindowDiagram_kit = assemblyDiagramInit([1,3,3])([[.3],[.5,1,.5],[.5,2,.3]])
# master = diagram2cell(doorwindowDiagram_kit,master,toMerge)
# hpc = SKEL_1(STRUCT(MKPOLS(master)))
# hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

# #########################################
# room_win2 = [405,414,404]
# room_win2 = master[0], [cell for k,cell in enumerate(master[1]) if (k in room_win2)]
# room_win2 = COLOR(WINDOW)((STRUCT(MKPOLS(room_win2))))
# room_win2 = MK_TRNSP(room_win2)
# #########################################

# toRemove = [405,414,404]
# master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

#VIEW(hpc)

#################################


#VIEW(master)

#DRAW(master)
