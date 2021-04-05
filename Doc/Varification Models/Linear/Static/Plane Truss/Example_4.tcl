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
node      1            8            0
node      2            7            0
node      3            7          0.5
node      4            6            0
node      5            6            1
node      6            5            0
node      7            5          1.5
node      8            4            0
node      9            4            2
node     10            3            0
node     11            3          1.5
node     12            2            0
node     13            2            1
node     14            1            0
node     15            1          0.5
node     16            0            0

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl
fix      1   1   1
fix     16   1   1

# T R U S S   E L E M E N T S
# Uniaxial Materials definition used by Truss Elements
uniaxialMaterial Elastic 154 2e+08
# Truss Definition : element truss $eleTag $inode $jnode $A $matTag -rho $rho -cMass $cFlag -doRayleigh $rFlag
element truss      1     16    14        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss      2     14    12        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss      3     12    10        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss      4     10     8        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss      5      8     6        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss      6      6     4        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss      7      4     2        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss      8      2     1        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss      9      1     3        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     10      3     5        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     11      5     7        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     12      7     9        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     13      9    11        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     14     11    13        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     15     13    15        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     16     15    16        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     17     15    14        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     18     13    12        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     19     11    10        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     20      9     8        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     21      6     7        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     22      4     5        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     23      2     3        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     24      3     4        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     25      4     7        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     26      7     8        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     27      8    11        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     28     11    12        0.002 154   -rho        0 -cMass 0 -doRayleigh 0
element truss     29     12    15        0.002 154   -rho        0 -cMass 0 -doRayleigh 0

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 16 -dof 1 2 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 16 -dof 3 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 16 -dof 1 2 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 16 -dof 3 reaction

# Loads - Plain Pattern
pattern Plain 100 Linear {
load      2        0      -10
load      4        0      -10
load      6        0      -10
load      8        0      -10
load     10        0      -10
load     12        0      -10
load     14        0      -10
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
