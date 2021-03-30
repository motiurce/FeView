import numpy as np

def brick_cell(elemList, nodeList):
    nodeiRow = []
    for i in range(len(elemList[:, 0])):
        nodeiRow.append(
            (8, int(np.argwhere(nodeList[:, 1] == elemList[i, 3])), int(np.argwhere(nodeList[:, 1] == elemList[i, 4])),
             int(np.argwhere(nodeList[:, 1] == elemList[i, 5])), int(np.argwhere(nodeList[:, 1] == elemList[i, 6])),
             int(np.argwhere(nodeList[:, 1] == elemList[i, 7])), int(np.argwhere(nodeList[:, 1] == elemList[i, 8])),
             int(np.argwhere(nodeList[:, 1] == elemList[i, 9])), int(np.argwhere(nodeList[:, 1] == elemList[i, 10]))))
    return np.array(nodeiRow)

def cell_type_brick(elemList):
    x = np.repeat(12, (len(elemList[:, 0])))
    return x