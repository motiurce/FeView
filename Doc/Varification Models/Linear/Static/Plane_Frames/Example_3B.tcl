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
node      1            0            0
node      2            0       0.3658
node      3            0       0.7316
node      4            0       1.0974
node      5            0       1.4632
node      6            0        1.829
node      7            0       2.1948
node      8            0       2.5606
node      9            0       2.9264
node     10            0       3.2922
node     11            0        3.658
node     12        3.658            0
node     13       0.3658        3.658
node     14        3.658       0.3658
node     15        3.658       0.7316
node     16       0.7316        3.658
node     17       1.0974        3.658
node     18        3.658       1.0974
node     19        3.658       1.4632
node     20       1.4632        3.658
node     21        1.829        3.658
node     22        3.658        1.829
node     23       2.1948        3.658
node     24        3.658       2.1948
node     25       2.5606        3.658
node     26        3.658       2.5606
node     27       2.9264        3.658
node     28        3.658       2.9264
node     29        3.658       3.2922
node     30       3.2922        3.658
node     31        3.658        3.658

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl z-rot
fix      1   1   1   1
fix     12   0   1   0

# E L A S T I C   B E A M - C O L U M N   E L E M E N T S
# Geometric Transformation
geomTransf Linear 1
geomTransf PDelta 2
geomTransf Corotational 3
# Elastic Beam Column Definition
# element elasticBeamColumn $eleTag $iNode $jNode $A $E $Iz $transfTag <-mass $MassPerUnitLength>
element elasticBeamColumn      1      1      2     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn      2      2      3     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn      3      3      4     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn      4      4      5     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn      5      5      6     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn      6      6      7     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn      7      7      8     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn      8      8      9     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn      9      9     10     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     10     10     11     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     11     11     13     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     12     13     16     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     13     16     17     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     14     17     20     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     15     20     21     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     16     21     23     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     17     23     25     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     18     25     27     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     19     27     30     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     20     30     31     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     21     12     14     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     22     14     15     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     23     15     18     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     24     18     19     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     25     19     22     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     26     22     24     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     27     24     26     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     28     26     28     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     29     28     29     0.0929 1.99938e+08 0.000719248    1   -mass        0
element elasticBeamColumn     30     29     31     0.0929 1.99938e+08 0.000719248    1   -mass        0

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 31 -dof 1 2 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 31 -dof 3 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 31 -dof 1 2 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 31 -dof 3 reaction


# Loads - Plain Pattern
pattern Plain 100 Linear {
  sp      1 3    -0.01
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