puts " ||||||| ||||||| ||      || ||                 v1.0"
puts " ||      ||      ||      ||                        "
puts " ||      ||      ||      || ||  |||||  ||        ||"
puts " ||||||  ||||||   ||    ||  || ||   || ||        ||"
puts " ||      ||        ||  ||   || ||||||  ||   ||   ||"	
puts " ||      ||         ||||    || ||       || |||| || "
puts " ||      |||||||     ||     ||  ||||||   ||   ||   "

# U N I T S
# Length : m
# Force  : kN
# Moment : kNm
# Stress : kPa
# Mass   : ton

# M O D E L  D O M A I N  
model BasicBuilder -ndm 3 -ndf 6

# N O D E S
# node $NodeTag $XCoord $Ycoord $Zcoord
node      1            0            5            4
node      2            0            5            0
node      3            0            0            4
node      4            5            5            4
node      5            5            5            0
node      6            0            0            0
node      7            5            0            4
node      8            5            0            0

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl z-transl x-rot y-rot z-rot
fix      2   1   1   1   1   1   1
fix      5   1   1   1   1   1   1
fix      6   1   1   1   1   1   1
fix      8   1   1   1   1   1   1

# E L A S T I C   B E A M - C O L U M N   E L E M E N T S
# Geometric Transformation
geomTransf Linear 1 -1 0 0
geomTransf PDelta 3 -1 0 0
geomTransf Corotational 5 -1 0 0
geomTransf Linear 2  0 0 1
geomTransf PDelta 4  0 0 1
geomTransf Corotational 6 0 0 1
# Elastic Beam Column Definition
# element elasticBeamColumn $eleTag $iNode $jNode $A $E $G $J $Iy $Iz $transfTag <-mass $MassPerUnitLength>
element elasticBeamColumn      1      3      7       0.04      3e+07   1.25e+07  0.000225333  0.000133333  0.000133333    2   -mass        0
element elasticBeamColumn      2      7      4       0.04      3e+07   1.25e+07  0.000225333  0.000133333  0.000133333    2   -mass        0
element elasticBeamColumn      3      4      1       0.04      3e+07   1.25e+07  0.000225333  0.000133333  0.000133333    2   -mass        0
element elasticBeamColumn      4      1      3       0.04      3e+07   1.25e+07  0.000225333  0.000133333  0.000133333    2   -mass        0
element elasticBeamColumn      5      6      3       0.04      3e+07   1.25e+07  0.000225333  0.000133333  0.000133333    1   -mass        0
element elasticBeamColumn      6      8      7       0.04      3e+07   1.25e+07  0.000225333  0.000133333  0.000133333    1   -mass        0
element elasticBeamColumn      7      5      4       0.04      3e+07   1.25e+07  0.000225333  0.000133333  0.000133333    1   -mass        0
element elasticBeamColumn      8      2      1       0.04      3e+07   1.25e+07  0.000225333  0.000133333  0.000133333    1   -mass        0

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 8 -dof 1 2 3 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 8 -dof 4 5 6 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 8 -dof 1 2 3 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 8 -dof 4 5 6 reaction

# Loads - Plain Pattern
pattern Plain 100 Linear {
load      1       10       10        0        0        0        0
load      3       10       10        0        0        0        0
}

# recording the initial status
record

# Analysis options
system BandGeneral
numberer RCM
constraints Transformation
integrator LoadControl 1
algorithm Linear
analysis Static
analyze 1