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
node      1            0            0
node      2            0      0.00508
node      3       0.0254            0
node      4       0.0254      0.00508
node      5       0.0508            0
node      6       0.0508      0.00508
node      7       0.0762            0
node      8       0.0762      0.00508
node      9       0.1016            0
node     10       0.1016      0.00508
node     11        0.127            0
node     12        0.127      0.00508
node     13       0.1524            0
node     14       0.1524      0.00508

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl
fix      1   1   1
fix      2   1   0

# Q U A D   E L E M E N T S
# nDMaterial Definition used by Quad Elements
# (ïnly if they have not already been defined on this model domain)
nDMaterial ElasticIsotropic 127 6.895e+07 0.3            0
# Quad elements Definition : element quad $EleTag $Nodei $Nodej Nodek $Nodel $thick $type $MatTag
element quad      1      3     4     2     1  0.00254  PlaneStress 127        0        0        0        0
element quad      2     12    11    13    14  0.00254  PlaneStress 127        0        0        0        0
element quad      3      5     6     4     3  0.00254  PlaneStress 127        0        0        0        0
element quad      4      7     8     6     5  0.00254  PlaneStress 127        0        0        0        0
element quad      5      9    10     8     7  0.00254  PlaneStress 127        0        0        0        0
element quad      6     11    12    10     9  0.00254  PlaneStress 127        0        0        0        0

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 14 -dof 1 2 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 14 -dof 3 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 14 -dof 1 2 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 14 -dof 3 reaction

# Loads - Plain Pattern
pattern Plain 100 Linear {
load     13   0.0022        0
load     14   0.0022        0
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