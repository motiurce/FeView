import pandas as pd
import numpy as np
from OpenTCLFile import*

def OpenSeesOutputRead(outFile):
    if outFile[-4:] == '.xml':
        skip = 4
    else:
        skip = 0
    outData = pd.read_csv(outFile, delim_whitespace=True, header=None,
                          comment='<', skiprows=skip)

    return np.array(outData)


def integratorInfo(TCLFile):
    integratorInfo_LoadControl = (OpenSeesTclRead(TCLFile, 'integrator LoadControl', 3))
    integratorInfo_LoadControls = integratorInfo_LoadControl[:, 2].astype(float)
    #print(integratorInfo_LoadControls)
    return np.unique(integratorInfo_LoadControls)

def step_static(TCLFile):
    #integratorInfo_LoadControl = (OpenSeesTclRead(TCLFile, 'integrator LoadControl', 3))


    #step_static = (1/integratorInfo_LoadControl[:, 2].astype(float)+1)
    step_static=1/integratorInfo(TCLFile)+1
    return (step_static)