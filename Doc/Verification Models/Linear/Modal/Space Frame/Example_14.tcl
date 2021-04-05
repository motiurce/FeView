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

# M O D E L  D O M A I N  1  (6DOF)

model BasicBuilder -ndm 3 -ndf 6

# N O D E S
# node $NodeTag $XCoord $Ycoord $Zcoord
node      1            0            0            0
node      2            0            0        3.962
node      3            0         7.62            0
node      4            0            0        7.924
node      5            0         7.62        3.962
node      6       10.668            0            0
node      7            0         7.62        7.924
node      8       10.668            0        3.962
node      9       10.668         7.62            0
node     10       10.668            0        7.924
node     11       10.668         7.62        3.962
node     12        11.58         8.23        3.962
node     13            0        15.24            0
node     14       10.668         7.62        7.924
node     15            0        15.24        3.962
node     16        11.58         8.23        7.924
node     17            0        15.24        7.924
node     18       10.668        15.24            0
node     19       10.668        15.24        3.962
node     20       10.668        15.24        7.924
node     21       21.336            0            0
node     22       21.336            0        3.962
node     23       21.336         7.62            0
node     24       21.336            0        7.924
node     25       21.336         7.62        3.962
node     26       21.336         7.62        7.924
node     27       21.336        15.24            0
node     28       21.336        15.24        3.962
node     29       21.336        15.24        7.924

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl z-transl x-rot y-rot z-rot
fix      1   1   1   1   1   1   1
fix      3   1   1   1   1   1   1
fix      6   1   1   1   1   1   1
fix      9   1   1   1   1   1   1
fix     13   1   1   1   1   1   1
fix     18   1   1   1   1   1   1
fix     21   1   1   1   1   1   1
fix     23   1   1   1   1   1   1
fix     27   1   1   1   1   1   1

# --------------------------------------------------------------------------------------------------------------
# R I G I D    D I A P H R A G M S
# --------------------------------------------------------------------------------------------------------------
# Rigid Diaphragm Definition : rigidDiaphragm $perpendicularAxis $MasterNode $SlaveNode1 $SlaveNode2 . . . .
fix                12     0 0 1 1 1 0
rigidDiaphragm      3     12 2 5 8 11 15 19 22 25 28 ; # ID : 1
fix                16     0 0 1 1 1 0
rigidDiaphragm      3     16 4 7 10 14 17 20 24 26 29 ; # ID : 2

# M A S S E S
# Mass Definition : mass $NodeTag $(ndf nodal mass values corresponding to each DOF)
mass     12  90.6457  90.6457        0        0        0        0
mass     16  90.6457  90.6457        0        0        0        0

# E L A S T I C   B E A M - C O L U M N   E L E M E N T S
# Geometric Transformation
geomTransf Linear 1 -1 0 0
geomTransf PDelta 3 -1 0 0
geomTransf Corotational 5 -1 0 0
geomTransf Linear 2  0 0 1
geomTransf PDelta 4  0 0 1
geomTransf Corotational 6 0 0 1
# Elastic Beam Column Definition
# element elasticBeamColumn $eleTag $iNode $jNode $A $E $G $J $Iy $Iz $transfTag <-mass $MassPerUnitLength>
element elasticBeamColumn      1      1      2     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn      2      2      4     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn      3      4     10     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn      4     10     24     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn      5      6      8     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn      6      8     10     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn      7     21     22     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn      8     22     24     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn      9      2      8     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     10      8     22     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     11      3      5     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     12      5      7     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     13      7     14     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     14     14     26     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     15      9     11     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     16     11     14     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     17     23     25     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     18     25     26     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     19      5     11     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     20     11     25     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     21      2      5     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     22      4      7     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     23     10     14     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     24     24     26     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     25     22     25     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     26      8     11     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     27     13     15     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     28     15     17     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     29     17     20     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     30     20     29     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     31     18     19     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     32     19     20     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     33     27     28     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     34     28     29     0.3716 1.67573e+07 6.98219e+06            1     0.010789     0.010789    1   -mass        0
element elasticBeamColumn     35     15     19     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     36     19     28     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     37      5     15     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     38      7     17     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     39     14     20     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     40     26     29     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     41     25     28     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0
element elasticBeamColumn     42     11     19     0.4645 2.39389e+07 9.97456e+06            1      0.01381      0.02253    2   -mass        0

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 29 -dof 1 2 3 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 29 -dof 4 5 6 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 29 -dof 1 2 3 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 29 -dof 4 5 6 reaction

# recording the initial status
record

# Perform eigenvalue analysis
puts "Running eigenvalue analysis\n"

set numModes 4

# Record eigenvectors
for { set k 1 } { $k <= $numModes } { incr k } {
    recorder Node -file [format "Mode_%i.out" $k] -nodeRange 1 29 -dof 1 2 3 "eigen $k"
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