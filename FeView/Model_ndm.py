import numpy as np
from OpenTCLFile import *
def ndm_v(TCLFile):
    modelInfo = OpenSeesTclRead(TCLFile, 'model', 6)
    ndm = modelInfo[:, 3].astype(int)
    return np.unique(ndm)