import numpy as np

def OpenSeesTclRead(tclFile, startswith, n_cols):
    fileInfo = []
    tclfile = open(tclFile, 'r')
    for line in tclfile:
        if line[:len(startswith)] == startswith:
            args = line.split()
            for i in range(0, n_cols):
                fileInfo.append(args[i])

    tclfile.close()
    return np.array(fileInfo).reshape((-1, n_cols))

def OpenSeesTcl_2nodes(tclFile, startswith):
    fileInfo = []
    nodel=[]
    tclfile = open(tclFile, 'r')
    with tclfile as f:
        f.readline()
        for line in f:
             if line[:len(startswith)] == startswith:
                 a = np.array(line.split())
                 #print(args)
                 #a=args[2:len(args)].astype(int)
                 #args = args[:, 2:5].astype(int)
                 for i in range(3, len(a)):
                    #fileInfo.append(a[i])
                    nodel.append(('info', a[0],a[1],a[2],a[i]))
    tclfile.close()
    return np.array(nodel).reshape((-1, 5))

