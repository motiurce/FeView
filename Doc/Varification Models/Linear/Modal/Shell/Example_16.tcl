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
model BasicBuilder -ndm 3 -ndf 6

# N O D E S
# node $NodeTag $XCoord $Ycoord $Zcoord
node      1            0            0            0
node      2            0         0.02            0
node      3         0.02            0            0
node      4         0.02         0.02            0
node      5         0.04            0            0
node      6            0         0.04            0
node      7         0.02         0.04            0
node      8         0.04         0.02            0
node      9         0.04         0.04            0
node     10            0         0.06            0
node     11         0.06            0            0
node     12         0.06         0.02            0
node     13         0.02         0.06            0
node     14         0.06         0.04            0
node     15         0.04         0.06            0
node     16            0         0.08            0
node     17         0.08            0            0
node     18         0.08         0.02            0
node     19         0.02         0.08            0
node     20         0.06         0.06            0
node     21         0.08         0.04            0
node     22         0.04         0.08            0
node     23         0.06         0.08            0
node     24          0.1            0            0
node     25            0          0.1            0
node     26         0.08         0.06            0
node     27          0.1         0.02            0
node     28         0.02          0.1            0
node     29         0.04          0.1            0
node     30          0.1         0.04            0
node     31         0.08         0.08            0
node     32          0.1         0.06            0
node     33         0.06          0.1            0
node     34         0.12            0            0
node     35         0.12         0.02            0
node     36         0.12         0.04            0
node     37          0.1         0.08            0
node     38         0.08          0.1            0
node     39         0.12         0.06            0
node     40         0.14            0            0
node     41          0.1          0.1            0
node     42         0.14         0.02            0
node     43         0.12         0.08            0
node     44         0.14         0.04            0
node     45         0.14         0.06            0
node     46         0.12          0.1            0
node     47         0.16            0            0
node     48         0.16         0.02            0
node     49         0.14         0.08            0
node     50         0.16         0.04            0
node     51         0.16         0.06            0
node     52         0.14          0.1            0
node     53         0.16         0.08            0
node     54         0.18            0            0
node     55         0.18         0.02            0
node     56         0.18         0.04            0
node     57         0.16          0.1            0
node     58         0.18         0.06            0
node     59         0.18         0.08            0
node     60          0.2            0            0
node     61          0.2         0.02            0
node     62          0.2            0         0.02
node     63          0.2         0.02         0.02
node     64          0.2         0.04            0
node     65          0.2            0         0.04
node     66          0.2         0.02         0.04
node     67          0.2         0.04         0.02
node     68         0.18          0.1            0
node     69          0.2         0.04         0.04
node     70          0.2            0         0.06
node     71          0.2         0.06            0
node     72          0.2         0.02         0.06
node     73          0.2         0.06         0.02
node     74          0.2         0.06         0.04
node     75          0.2         0.04         0.06
node     76          0.2            0         0.08
node     77          0.2         0.08            0
node     78          0.2         0.02         0.08
node     79          0.2         0.08         0.02
node     80          0.2         0.06         0.06
node     81          0.2         0.08         0.04
node     82          0.2         0.04         0.08
node     83          0.2            0          0.1
node     84          0.2         0.08         0.06
node     85          0.2         0.06         0.08
node     86          0.2          0.1            0
node     87          0.2          0.1         0.02
node     88          0.2         0.02          0.1
node     89          0.2          0.1         0.04
node     90          0.2         0.04          0.1
node     91          0.2         0.08         0.08
node     92          0.2         0.06          0.1
node     93          0.2          0.1         0.06
node     94          0.2         0.08          0.1
node     95          0.2          0.1         0.08
node     96          0.2          0.1          0.1

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl z-transl x-rot y-rot z-rot
fix      1   1   1   1   1   1   1
fix      2   1   1   1   1   1   1
fix      6   1   1   1   1   1   1
fix     10   1   1   1   1   1   1
fix     16   1   1   1   1   1   1
fix     25   1   1   1   1   1   1

# S H E L L M I T C 4   E L E M E N T S
# Materials/Sections Definition used by shell elements
# (if the have not already been defined on this model domain)
nDMaterial ElasticIsotropic 127 2e+08 0.3         7.85
section PlateFiber 137 127 0.02
# ShellMITC4 Elements Definition: element ShellMITC4 $eleTag $iNode $jNode $kNode $lNode $secTag
element ShellMITC4      1     61    63    62    60    137
element ShellMITC4      2     64    67    63    61    137
element ShellMITC4      3     71    73    67    64    137
element ShellMITC4      4     77    79    73    71    137
element ShellMITC4      5     86    87    79    77    137
element ShellMITC4      6     63    66    65    62    137
element ShellMITC4      7     67    69    66    63    137
element ShellMITC4      8     73    74    69    67    137
element ShellMITC4      9     79    81    74    73    137
element ShellMITC4     10     87    89    81    79    137
element ShellMITC4     11     66    72    70    65    137
element ShellMITC4     12     69    75    72    66    137
element ShellMITC4     13     74    80    75    69    137
element ShellMITC4     14     81    84    80    74    137
element ShellMITC4     15     89    93    84    81    137
element ShellMITC4     16     72    78    76    70    137
element ShellMITC4     17     75    82    78    72    137
element ShellMITC4     18     80    85    82    75    137
element ShellMITC4     19     84    91    85    80    137
element ShellMITC4     20     93    95    91    84    137
element ShellMITC4     21     78    88    83    76    137
element ShellMITC4     22     82    90    88    78    137
element ShellMITC4     23     85    92    90    82    137
element ShellMITC4     24     91    94    92    85    137
element ShellMITC4     25     95    96    94    91    137
element ShellMITC4     26      3     4     2     1    137
element ShellMITC4     27      5     8     4     3    137
element ShellMITC4     28     11    12     8     5    137
element ShellMITC4     29     17    18    12    11    137
element ShellMITC4     30     24    27    18    17    137
element ShellMITC4     31     34    35    27    24    137
element ShellMITC4     32     40    42    35    34    137
element ShellMITC4     33     47    48    42    40    137
element ShellMITC4     34     54    55    48    47    137
element ShellMITC4     35     60    61    55    54    137
element ShellMITC4     36      4     7     6     2    137
element ShellMITC4     37      8     9     7     4    137
element ShellMITC4     38     12    14     9     8    137
element ShellMITC4     39     18    21    14    12    137
element ShellMITC4     40     27    30    21    18    137
element ShellMITC4     41     35    36    30    27    137
element ShellMITC4     42     42    44    36    35    137
element ShellMITC4     43     48    50    44    42    137
element ShellMITC4     44     55    56    50    48    137
element ShellMITC4     45     61    64    56    55    137
element ShellMITC4     46      7    13    10     6    137
element ShellMITC4     47      9    15    13     7    137
element ShellMITC4     48     14    20    15     9    137
element ShellMITC4     49     21    26    20    14    137
element ShellMITC4     50     30    32    26    21    137
element ShellMITC4     51     36    39    32    30    137
element ShellMITC4     52     44    45    39    36    137
element ShellMITC4     53     50    51    45    44    137
element ShellMITC4     54     56    58    51    50    137
element ShellMITC4     55     64    71    58    56    137
element ShellMITC4     56     13    19    16    10    137
element ShellMITC4     57     15    22    19    13    137
element ShellMITC4     58     20    23    22    15    137
element ShellMITC4     59     26    31    23    20    137
element ShellMITC4     60     32    37    31    26    137
element ShellMITC4     61     39    43    37    32    137
element ShellMITC4     62     45    49    43    39    137
element ShellMITC4     63     51    53    49    45    137
element ShellMITC4     64     58    59    53    51    137
element ShellMITC4     65     71    77    59    58    137
element ShellMITC4     66     19    28    25    16    137
element ShellMITC4     67     22    29    28    19    137
element ShellMITC4     68     23    33    29    22    137
element ShellMITC4     69     31    38    33    23    137
element ShellMITC4     70     37    41    38    31    137
element ShellMITC4     71     43    46    41    37    137
element ShellMITC4     72     49    52    46    43    137
element ShellMITC4     73     53    57    52    49    137
element ShellMITC4     74     59    68    57    53    137
element ShellMITC4     75     77    86    68    59    137

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 96 -dof 1 2 3 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 96 -dof 4 5 6 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 96 -dof 1 2 3 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 96 -dof 4 5 6 reaction

# recording the initial status
record

# Perform eigenvalue analysis

set numModes 3

# Record eigenvectors
for { set k 1 } { $k <= $numModes } { incr k } {
    recorder Node -file [format "Mode_%i.out" $k] -nodeRange 1 96 -dof 1 2 3 "eigen $k"
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