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

"""Kitchen door"""
toMerge = 30
diagram = assemblyDiagramInit([1,3,2])([[.3],[3,1,3],[2.4,.3]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)

toRemove = [78]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]



DRAW(master)


#toRemove = [26]
#hall = hall[0], [cell for k,cell in enumerate(hall[1]) if not (k in toRemove)]

#VIEW(hpc)
#DRAW(master)