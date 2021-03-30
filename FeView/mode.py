from OpenTCLFile import *
def modeNumber(TCLFile):
    global numModes
    modeNumbers = OpenSeesTclRead(TCLFile, 'set numModes', 3)
    if str(modeNumbers):
        numModes = modeNumbers[:, 2]#.astype(int)
    return numModes