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
node      1         3.66         1.83
node      2      3.49733        1.708
node      3      3.33467        1.586
node      4        3.172        1.464
node      5      3.00933        1.342
node      6      2.84667         1.22
node      7        2.684        1.098
node      8      2.52133        0.976
node      9      2.35867        0.854
node     10        2.196        0.732
node     11      2.03333         0.61
node     12      1.87067        0.488
node     13        1.708        0.366
node     14      1.54533        0.244
node     15      1.38267        0.122
node     16         1.22            0
node     17         1.22    -0.203333
node     18      1.01667            0
node     19         1.22    -0.406667
node     20     0.813333            0
node     21         1.22        -0.61
node     22         0.61            0
node     23         1.22    -0.813333
node     24     0.406667            0
node     25         1.22     -1.01667
node     26         1.22        -1.22
node     27     0.203333            0
node     28         1.22     -1.42333
node     29            0            0
node     30         1.22     -1.62667
node     31         1.22        -1.83
node     32         1.22     -2.03333
node     33         1.22     -2.23667
node     34         1.22        -2.44
node     35         1.22     -2.64333
node     36         1.22     -2.84667
node     37         1.22        -3.05

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl z-rot
fix      1   1   0   0
fix     37   1   1   0

# E L A S T I C   B E A M - C O L U M N   E L E M E N T S
# Geometric Transformation
geomTransf Linear 1
geomTransf PDelta 2
geomTransf Corotational 3
# Elastic Beam Column Definition
# element elasticBeamColumn $eleTag $iNode $jNode $A $E $Iz $transfTag <-mass $MassPerUnitLength>
element elasticBeamColumn      1     29     27     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      2     27     24     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      3     24     22     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      4     22     20     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      5     20     18     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      6     18     16     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      7     16     15     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      8     15     14     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      9     14     13     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     10     13     12     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     11     12     11     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     12     11     10     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     13     10      9     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     14      9      8     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     15      8      7     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     16      7      6     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     17      6      5     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     18      5      4     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     19      4      3     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     20      3      2     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     21      2      1     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     22     37     36     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     23     36     35     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     24     35     34     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     25     34     33     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     26     33     32     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     27     32     31     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     28     31     30     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     29     30     28     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     30     28     26     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     31     26     25     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     32     25     23     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     33     23     21     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     34     21     19     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     35     19     17     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     36     17     16     0.0929 2.48199e+07 0.00071925    1   -mass        0

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 37 -dof 1 2 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 37 -dof 3 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 37 -dof 1 2 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 37 -dof 3 reaction
recorder Element -file ElasticBeamColumn_localForce.out -time -ele 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 localForce

# Loads - Plain Pattern
pattern Plain 100 Linear {
load     29        0   -44.48        0
eleLoad -ele      1 -type -beamUniform   -26.27        0
eleLoad -ele      2 -type -beamUniform   -26.27        0
eleLoad -ele      3 -type -beamUniform   -26.27        0
eleLoad -ele      4 -type -beamUniform   -26.27        0
eleLoad -ele      5 -type -beamUniform   -26.27        0
eleLoad -ele      6 -type -beamUniform   -26.27        0
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