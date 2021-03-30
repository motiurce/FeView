# --------------------------------------------------------------------------------------------------------------
#
# M O D E L  D O M A I N  1  (6DOF)
#
# --------------------------------------------------------------------------------------------------------------

model BasicBuilder -ndm 3 -ndf 6

# --------------------------------------------------------------------------------------------------------------
# N O D E S
# --------------------------------------------------------------------------------------------------------------

# node $NodeTag $XCoord $Ycoord $Zcoord

node      1            2            0            0
node      2            1            0            0
node      3            2            0            1
node      4            1            0            1
node      5            0            0            0
node      6            2            0            2
node      7            1            0            2
node      8            0            0            1
node      9            0            0            2
node     10            2            0            3
node     11            2            1            3
node     12            1            0            3
node     13            1            1            3
node     14            0            0            3
node     15            0            1            3

# --------------------------------------------------------------------------------------------------------------
# R E S T R A I N T S
# --------------------------------------------------------------------------------------------------------------

# fix $NodeTag x-transl y-transl z-transl x-rot y-rot z-rot

fix      1   1   1   1   1   1   1
fix      5   1   1   1   1   1   1

# --------------------------------------------------------------------------------------------------------------
# S H E L L M I T C 4   E L E M E N T S
# --------------------------------------------------------------------------------------------------------------


section ElasticMembranePlateSection 138 2.8e+07 0.2 0.25 0

# ShellMITC4 Elements Definition: element ShellMITC4 $eleTag $iNode $jNode $kNode $lNode $secTag

element ShellMITC4      1      2     4     8     5    138
element ShellMITC4      2      1     3     4     2    138
element ShellMITC4      3      4     7     9     8    138
element ShellMITC4      4      3     6     7     4    138
element ShellMITC4      5      7    12    14     9    138
element ShellMITC4      6      6    10    12     7    138
element ShellMITC4      7     12    13    15    14    138
element ShellMITC4      8     10    11    13    12    138

# --------------------------------------------------------------------------------------------------------------
#
# D O M A I N  C O M M O N S
#
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
# R E C O R D E R S
# --------------------------------------------------------------------------------------------------------------

recorder Node -file Node_displacements.out -time -nodeRange 1 15 -dof 1 2 3 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 15 -dof 4 5 6 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 15 -dof 1 2 3 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 15 -dof 4 5 6 reaction
recorder Element -file ShellMITC4_force.out -time -ele 1 2 3 4 5 6 7 8 forces
recorder Element -file ShellMITC4_stress.out -time -ele 1 2 3 4 5 6 7 8 stresses


pattern Plain 100 Linear {
load     11        0        0       10        0        0        0
load     15        0        0       10        0        0        0
}

record

# Analysis options

system BandSPD
numberer RCM
constraints Plain
integrator LoadControl 0.2
algorithm Linear
analysis Static 
analyze 5
