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

def step_static(TCLFile):
    integratorInfo_LoadControl = OpenSeesTclRead(TCLFile, 'integrator LoadControl', 3)
    step_static = (1/integratorInfo_LoadControl[:, 2].astype(float)+1)
    return step_static

def out_response(outFile, steps,ndm,type):
    outrespFile=OpenSeesOutputRead(outFile)
    if ndm == 3:
        if type=='all':
            response = outrespFile[(steps) - 1, 1:].reshape(-1, 3)
        elif type=='rotation_moment':
            response = outrespFile[(steps) - 1, 1:].reshape(-1, 3)

    elif ndm == 2:
        if type=='all':
            response_xy = outrespFile[(steps) - 1, 1:].reshape(-1, 2)
            z_res = np.repeat(0, len(response_xy[:, 0]))
            response = np.column_stack([response_xy, z_res])
        elif type=='rotation_moment':
            response_z = outrespFile[(steps) - 1, 1:].reshape(-1, 1)
            x_res = np.repeat(0, len(response_z[:, 0]))
            y_res = np.repeat(0, len(response_z[:, 0]))
            response = np.column_stack([x_res, y_res,response_z])

    return response

#outFile='Node_displacements.out'
#print(out_response(outFile, 2,2))
