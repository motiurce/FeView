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
model BasicBuilder -ndm 3 -ndf 3

# N O D E S
# node $NodeTag $XCoord $Ycoord $Zcoord
node      1         1.25            0            3
node      2          2.5            0            0
node      3            0            0            0
node      4            0            2            0
node      5          2.5            2            0

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl z-transl
fix      2   1   1   1
fix      3   1   1   1
fix      4   1   1   1
fix      5   1   1   1

# T R U S S   E L E M E N T S
# Uniaxial Materials definition used by Truss Elements
# (ïnly if they have not been already defined on this model domain)
uniaxialMaterial Elastic 158 2e+08
# Truss Definition : element truss $eleTag $inode $jnode $A $matTag -rho $rho -cMass $cFlag -doRayleigh $rFlag
element truss      1      3     4        0.001 158   -rho  0.00785 -cMass 0 -doRayleigh 0
element truss      2      4     5        0.001 158   -rho  0.00785 -cMass 0 -doRayleigh 0
element truss      3      5     2        0.001 158   -rho  0.00785 -cMass 0 -doRayleigh 0
element truss      4      2     3        0.001 158   -rho  0.00785 -cMass 0 -doRayleigh 0
element truss      5      3     1        0.001 158   -rho  0.00785 -cMass 0 -doRayleigh 0
element truss      6      1     2        0.001 158   -rho  0.00785 -cMass 0 -doRayleigh 0
element truss      7      5     1        0.001 158   -rho  0.00785 -cMass 0 -doRayleigh 0
element truss      8      1     4        0.001 158   -rho  0.00785 -cMass 0 -doRayleigh 0
element truss      9      2     4        0.001 158   -rho  0.00785 -cMass 0 -doRayleigh 0

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 5 -dof 1 2 3 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 5 -dof 4 5 6 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 5 -dof 1 2 3 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 5 -dof 4 5 6 reaction

# recording the initial status
record

# Perform eigenvalue analysis

set numModes 3

# Record eigenvectors
for { set k 1 } { $k <= $numModes } { incr k } {
    recorder Node -file [format "Mode_%i.out" $k] -nodeRange 1 5 -dof 1 2 3 "eigen $k"
}

set lambda [eigen -fullGenLapack $numModes]

# Calculate periods
set T {}
foreach lam $lambda {
    lappend T [expr 6.283185/sqrt($lam)]
}

# Write periods file
set period "Periods.out"
set Periods [open $period "w"]
foreach t $T {
    puts $Periods "$t"
}
close $Periods

# Analysis options
system BandGeneral
numberer RCM
constraints Transformation
integrator LoadControl 1
algorithm Linear
analysis Static
analyze 1