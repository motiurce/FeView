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
model BasicBuilder -ndm 2 -ndf 2

# N O D E S
# node $NodeTag $XCoord $Ycoord
node      1       0.0061      0.00305
node      2      0.00406      0.00203
node      3      0.00457      0.00076
node      4       0.0061            0
node      5      0.00203      0.00203
node      6      0.00102      0.00051
node      7            0      0.00305
node      8            0            0

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl
fix      1   1   1
fix      4   1   1
fix      7   1   1
fix      8   1   1

# Q U A D   E L E M E N T S
# nDMaterial Definition used by Quad Elements
nDMaterial ElasticIsotropic 127 6.895e+06 0.25            0
# Quad elements Definition : element quad $EleTag $Nodei $Nodej Nodek $Nodel $thick $type $MatTag
element quad      1      6     5     7     8 2.54e-05  PlaneStress 127        0        0        0        0
element quad      2      5     2     1     7 2.54e-05  PlaneStress 127        0        0        0        0
element quad      3      2     3     4     1 2.54e-05  PlaneStress 127        0        0        0        0
element quad      4      3     6     8     4 2.54e-05  PlaneStress 127        0        0        0        0
element quad      5      3     2     5     6 2.54e-05  PlaneStress 127        0        0        0        0

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 8 -dof 1 2 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 8 -dof 3 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 8 -dof 1 2 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 8 -dof 3 reaction

# Loads - Plain Pattern
pattern Plain 100 Linear {
  sp      1 1 7.62e-06
  sp      1 2 6.096e-06
  sp      4 1 6.096e-06
  sp      4 2 3.048e-06
  sp      7 1 1.524e-06
  sp      7 2 3.048e-06
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