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
node      1            5            0
node      2         4.75            0
node      3          4.5            0
node      4         4.25            0
node      5            4            0
node      6         3.75            0
node      7          3.5            0
node      8         3.25            0
node      9            3            0
node     10         2.75            0
node     11          2.5            0
node     12         2.25            0
node     13            2            0
node     14         1.75            0
node     15          1.5            0
node     16         1.25            0
node     17            1            0
node     18         0.75            0
node     19          0.5            0
node     20         0.25            0
node     21            0            0

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl z-rot
fix     21   1   1   1

# E L A S T I C   B E A M - C O L U M N   E L E M E N T S
# Geometric Transformation
geomTransf Linear 1
geomTransf PDelta 2
geomTransf Corotational 3
# Elastic Beam Column Definition
# element elasticBeamColumn $eleTag $iNode $jNode $A $E $Iz $transfTag <-mass $MassPerUnitLength>
element elasticBeamColumn      1     21     20       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn      2     20     19       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn      3     19     18       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn      4     18     17       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn      5     17     16       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn      6     16     15       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn      7     15     14       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn      8     14     13       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn      9     13     12       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn     10     12     11       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn     11     11     10       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn     12     10      9       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn     13      9      8       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn     14      8      7       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn     15      7      6       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn     16      6      5       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn     17      5      4       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn     18      4      3       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn     19      3      2       0.06      3e+07    0.00045    1   -mass    0.144
element elasticBeamColumn     20      2      1       0.06      3e+07    0.00045    1   -mass    0.144

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 21 -dof 1 2 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 21 -dof 3 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 21 -dof 1 2 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 21 -dof 3 reaction

# Loads - Plain Pattern
pattern Plain 100 Linear {
load      1        0      -10        0
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
set committedSteps 1
analyze 1