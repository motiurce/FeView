import numpy as np

def tri_cell(elemList, nodeList):
    nodeiRow = []
    for i in range(len(elemList[:, 0])):
        nodeiRow.append((3, int(np.argwhere(nodeList[:, 1] == elemList[i, 3])),
                         int(np.argwhere(nodeList[:, 1] == elemList[i, 4])),
                         int(np.argwhere(nodeList[:, 1] == elemList[i, 5]))))

    return np.array(nodeiRow)



def cell_type_tri(elemList):
    x = np.repeat(5, (len(elemList[:, 0])))
    return x