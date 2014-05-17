def NUMBERING(assembledDiagram):
	V,CV = assembledDiagram
	hpc = SKEL_1(STRUCT(MKPOLS(assembledDiagram)))
	hpc = cellNumbering (assembledDiagram,hpc)(range(len(CV)),CYAN,2)
	return hpc

def MERGE(master, assembledDiagram, cellToMerge):
	V, CV = master
	master = diagram2cell(assembledDiagram,master,cellToMerge)
	VIEW(NUMBERING(master))
	return master

def REMOVE(master, cellsToRemove):
	return master[0], [cell for k,cell in enumerate(master[1]) if not (k in cellsToRemove)]

def MERGING_NUMBERING_ELIMINATION(master, assembledDiagram, cellToMerge, cellsToRemove):
	NUMBERING(master)
	V,CV = master
	if cellToMerge in CV: 
		master = MERGE(master, assembledDiagram, cellToMerge)
		for i in range(len(cellsToRemove)):
			cellsToRemove[i] = cellsToRemove[i]+1
	master = REMOVE(master, cellsToRemove)
	return master


