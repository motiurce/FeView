import numpy as np

def frame_cell(elemList, nodeList):
    nodeiRow = []
    for i in range(len(elemList[:, 0])):
        nodeiRow.append((2, int(np.argwhere(nodeList[:, 1] == elemList[i, 3])),
                         int(np.argwhere(nodeList[:, 1] == elemList[i, 4]))))
    return np.array(nodeiRow)

def cell_type_frame(elemList):
    x = np.repeat(4, (len(elemList[:, 0])))
    return x