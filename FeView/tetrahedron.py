import numpy as np
def tetra4_cell(elemList, nodeList):
    nodeiRow = []
    for i in range(len(elemList[:, 0])):
        nodeiRow.append((4, int(np.argwhere(nodeList[:, 1] == elemList[i, 3])),
                         int(np.argwhere(nodeList[:, 1] == elemList[i, 4])),
                         int(np.argwhere(nodeList[:, 1] == elemList[i, 5])),
                        int(np.argwhere(nodeList[:, 1] == elemList[i, 6]))))

    return np.array(nodeiRow)


def cell_type_tetra4(elemList):
    x = np.repeat(10, (len(elemList[:, 0])))
    return x


