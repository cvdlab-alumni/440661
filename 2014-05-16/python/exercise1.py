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

DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([5,8,2])([[.3,6,.1,5,.3],[.3,8,.3,4,.3,5,.3,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

toRemove = [19,51,23,55,27,59,21]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)


"""Hall - the room down on the left"""
#Hall Door
toMerge = 17
doorDiagram = assemblyDiagramInit([3,1,2])([[3,1.5,3],[.3],[2.4,.3]])
master = diagram2cell(doorDiagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

toRemove = [74]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#VIEW(hpc)

#Hall window
toMerge = 3
windowDiagram = assemblyDiagramInit([1,8,5])([[.3],[.1,1,.1,1,.1,1,.1,1],[.3,1,.1,1,.5]])
master = diagram2cell(windowDiagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2) 
#VIEW(hpc)

toRemove = [94,104,92,102]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

"""Kitchen - aka the room down on the right"""
#kitchen door
toMerge = 29
doorDiagram_kit = assemblyDiagramInit([1,3,2])([[.3],[3,1,3],[2.4,.3]])
master = diagram2cell(doorDiagram_kit,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

toRemove = [113]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

#kitchen doorwindow
toMerge = 57
doorwindowDiagram_kit = assemblyDiagramInit([1,3,3])([[.3],[3,1,3],[.5,2,.3]])
master = diagram2cell(doorwindowDiagram_kit,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
toRemove = [119]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


"""Room - the room top on the left"""
#Room door
toMerge = 20
doorDiagram = assemblyDiagramInit([3,1,2])([[3,1.5,3],[.3],[2.4,.3]])
master = diagram2cell(doorDiagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


toRemove = [124]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]



#Room window
toMerge = 10
windowDiagram = assemblyDiagramInit([1,8,5])([[.3],[.1,1,.1,1,.1,1,.1,1],[.3,1,.1,1,.5]])
master = diagram2cell(windowDiagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2) 


toRemove = [154,144]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


"""Bathroom"""
#Bathroom door
toMerge = 34
doorDiagram_kit = assemblyDiagramInit([1,3,2])([[.3],[3,2,3],[2.4,.3]])
master = diagram2cell(doorDiagram_kit,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)


toRemove = [165]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

#Bathroom window
toMerge = 61
windowDiagram = assemblyDiagramInit([1,8,5])([[.3],[.1,1,.1,1,.1,1,.1,1],[.3,1,.1,1,.5]])
master = diagram2cell(windowDiagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2) 

toRemove = [195]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


"""Small room"""
#Small room door
toMerge = 30
doorDiagram = assemblyDiagramInit([1,3,2])([[.3],[3,2,3],[2.4,.3]])
master = diagram2cell(doorDiagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)

toRemove = [207]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]


#Small room window
toMerge = 56
windowDiagram = assemblyDiagramInit([1,8,3])([[.3],[.1,1,.1,1,.1,1,.1,1],[.3,1,.5]])
master = diagram2cell(windowDiagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2) 

toRemove = [225, 219]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]




VIEW(hpc)
DRAW(master)