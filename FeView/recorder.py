from OpenTCLFile import *
def recorder_types(TCLFile):
    recorder_dispInfo = OpenSeesTclRead(TCLFile, 'recorder Node -file Node_displacements.out', 4)
    recorder_rotInfo = OpenSeesTclRead(TCLFile, 'recorder Node -file Node_rotations.out', 4)
    recorder_forceInfo = OpenSeesTclRead(TCLFile, 'recorder Node -file Node_forceReactions.out', 4)
    recorder_momentInfo = OpenSeesTclRead(TCLFile, 'recorder Node -file Node_momentReactions.out', 4)
    recorder_accelInfo = OpenSeesTclRead(TCLFile, 'recorder Node -file Node_accelerations.out', 4)
    recorder_vellInfo = OpenSeesTclRead(TCLFile, 'recorder Node -file Node_velocities.out', 4)

    if (recorder_dispInfo.size>0):
        recorder_disp=1
    else :
        recorder_disp=0
    if (recorder_rotInfo.size>0):
        recorder_rot=1

    else:
        recorder_rot = 0
    if (recorder_forceInfo.size>0):
        recorder_force=1
    else:
        recorder_force = 0
    if (recorder_momentInfo.size>0):
        recorder_moment=1
    else:
        recorder_moment = 0
    if (recorder_accelInfo.size>0):
        recorder_accel=1
    else:
        recorder_accel = 0
    if (recorder_vellInfo.size>0):
        recorder_vel=1
    else:
        recorder_vel = 0
    return recorder_disp, recorder_rot, recorder_force, recorder_moment, recorder_accel, recorder_vel