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
model BasicBuilder -ndm 2 -ndf 3

# N O D E S
# node $NodeTag $XCoord $Ycoord
node      1         1.22        -3.05
node      2         1.22       -1.525
node      3         1.22            0
node      4            0            0
node      5         1.83       0.4575
node      6         2.44        0.915
node      7         3.05       1.3725
node      8         3.66         1.83

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl z-rot
fix      1   1   1   0
fix      8   1   0   0

# E L A S T I C   B E A M - C O L U M N   E L E M E N T S
# Geometric Transformation
geomTransf Linear 1
geomTransf PDelta 2
geomTransf Corotational 3
# Elastic Beam Column Definition
# element elasticBeamColumn $eleTag $iNode $jNode $A $E $Iz $transfTag <-mass $MassPerUnitLength>
element elasticBeamColumn      1      4      3     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      2      1      2     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      3      2      3     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      4      3      5     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      5      5      6     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      6      6      7     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      7      7      8     0.0929 2.48199e+07 0.00071925    1   -mass        0

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 8 -dof 1 2 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 8 -dof 3 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 8 -dof 1 2 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 8 -dof 3 reaction

# Loads - Plain Pattern
pattern Plain 100 Linear {
  load      6   40.032  -53.376        0
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