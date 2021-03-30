import numpy as np
from OpenTCLFile import *
from Model_ndm import *
def node(TCLFile):
    ndm = ndm_v(TCLFile)
    if ndm == 3:
        nodeInfo = OpenSeesTclRead(TCLFile, 'node', 5)
    if ndm == 2:
        nodeInfo = OpenSeesTclRead(TCLFile, 'node', 4)

    return nodeInfo


def NodeCoords(TCLFile):
    #global initNodeCoords
    #modelInfo = OpenSeesTclRead(TCLFile, 'model', 6)
    ndm = ndm_v(TCLFile)

    if ndm==3:
        nodeInfo = OpenSeesTclRead(TCLFile, 'node', 5)
        initNodeCoords = nodeInfo[:, 2:5].astype(float)
    elif ndm==2:

        nodeInfo = OpenSeesTclRead(TCLFile, 'node', 4)
        initNodeCoord = nodeInfo[:, 2:4].astype(float)
        initNodeCoords1=[]
        z = np.repeat(0, len(initNodeCoord[:,0]))
        for i in range (len(initNodeCoord[:,0])):

            initNodeCoords1.append((initNodeCoord[i]).tolist())
        initNodeCoords=np.column_stack([initNodeCoords1, z])
    return (initNodeCoords)
