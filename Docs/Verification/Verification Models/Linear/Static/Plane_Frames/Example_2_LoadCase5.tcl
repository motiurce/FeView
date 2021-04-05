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

# M O D E L  D O M A I N  1  (3DOF)
model BasicBuilder -ndm 2 -ndf 3

# N O D E S
# node $NodeTag $XCoord $Ycoord
node      1         3.66         1.83
node      2        3.172        1.464
node      3        2.684        1.098
node      4        2.196        0.732
node      5        1.708        0.366
node      6         1.22            0
node      7      1.01667            0
node      8     0.813333            0
node      9         1.22        -0.61
node     10         0.61            0
node     11     0.406667            0
node     12         1.22        -1.22
node     13     0.203333            0
node     14            0            0
node     15         1.22        -1.83
node     16         1.22        -2.44
node     17         1.22        -3.05

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl z-rot
fix      1   1   0   0
fix     17   1   1   0

# E L A S T I C   B E A M - C O L U M N   E L E M E N T S
# Geometric Transformation
geomTransf Linear 1
geomTransf PDelta 2
geomTransf Corotational 3
# Elastic Beam Column Definition
# element elasticBeamColumn $eleTag $iNode $jNode $A $E $Iz $transfTag <-mass $MassPerUnitLength>
element elasticBeamColumn      1     14     13     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      2     13     11     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      3     11     10     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      4     10      8     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      5      8      7     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      6      7      6     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      7      6      5     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      8      5      4     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn      9      4      3     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     10      3      2     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     11      2      1     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     12     17     16     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     13     16     15     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     14     15     12     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     15     12      9     0.0929 2.48199e+07 0.00071925    1   -mass        0
element elasticBeamColumn     16      9      6     0.0929 2.48199e+07 0.00071925    1   -mass        0

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 17 -dof 1 2 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 17 -dof 3 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 17 -dof 1 2 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 17 -dof 3 reaction

# Loads - Plain Pattern
pattern Plain 100 Linear {
  eleLoad -ele      7 -type -beamUniform  -29.186        0
  eleLoad -ele      8 -type -beamUniform  -29.186        0
  eleLoad -ele      9 -type -beamUniform  -29.186        0
  eleLoad -ele     10 -type -beamUniform  -29.186        0
  eleLoad -ele     11 -type -beamUniform  -29.186        0
  eleLoad -ele     12 -type -beamUniform  -29.186        0
  eleLoad -ele     13 -type -beamUniform  -29.186        0
  eleLoad -ele     14 -type -beamUniform  -29.186        0
  eleLoad -ele     15 -type -beamUniform  -29.186        0
  eleLoad -ele     16 -type -beamUniform  -29.186        0
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