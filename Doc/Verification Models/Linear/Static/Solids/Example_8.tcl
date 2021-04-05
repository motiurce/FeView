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
node      1            0          0.5          0.5
node      2            0          0.4          0.5
node      3            0          0.5          0.4
node      4            0          0.4          0.4
node      5            0          0.5          0.3
node      6            0          0.3          0.5
node      7            0          0.4          0.3
node      8            0          0.3          0.4
node      9            0          0.3          0.3
node     10            0          0.5          0.2
node     11            0          0.2          0.5
node     12            0          0.2          0.4
node     13            0          0.4          0.2
node     14            0          0.2          0.3
node     15            0          0.3          0.2
node     16            0          0.1          0.5
node     17            0          0.5          0.1
node     18            0          0.4          0.1
node     19            0          0.1          0.4
node     20            0          0.2          0.2
node     21            0          0.3          0.1
node     22            0          0.1          0.3
node     23            0          0.5            0
node     24            0            0          0.5
node     25            0          0.2          0.1
node     26          0.5          0.5          0.5
node     27            0          0.1          0.2
node     28            0          0.4            0
node     29            0            0          0.4
node     30          0.5          0.4          0.5
node     31          0.5          0.5          0.4
node     32          0.5          0.4          0.4
node     33          0.5          0.5          0.3
node     34            0            0          0.3
node     35            0          0.3            0
node     36          0.5          0.3          0.5
node     37          0.5          0.3          0.4
node     38          0.5          0.4          0.3
node     39            0          0.1          0.1
node     40          0.5          0.3          0.3
node     41            0          0.2            0
node     42            0            0          0.2
node     43          0.5          0.2          0.5
node     44          0.5          0.5          0.2
node     45          0.5          0.2          0.4
node     46          0.5          0.4          0.2
node     47          0.5          0.2          0.3
node     48          0.5          0.3          0.2
node     49          0.5          0.1          0.5
node     50            0            0          0.1
node     51            0          0.1            0
node     52          0.5          0.5          0.1
node     53          0.5          0.1          0.4
node     54          0.5          0.4          0.1
node     55          0.5          0.2          0.2
node     56          0.5          0.1          0.3
node     57          0.5          0.3          0.1
node     58          0.5          0.1          0.2
node     59          0.5            0          0.5
node     60          0.5          0.5            0
node     61            0            0            0
node     62          0.5          0.2          0.1
node     63          0.5            0          0.4
node     64          0.5          0.4            0
node     65          0.5            0          0.3
node     66          0.5          0.3            0
node     67          0.5          0.1          0.1
node     68          0.5            0          0.2
node     69          0.5          0.2            0
node     70          0.5          0.1            0
node     71          0.5            0          0.1
node     72          0.5            0            0
node     73            1          0.5          0.5
node     74            1          0.4          0.5
node     75            1          0.5          0.4
node     76            1          0.4          0.4
node     77            1          0.5          0.3
node     78            1          0.3          0.5
node     79            1          0.4          0.3
node     80            1          0.3          0.4
node     81            1          0.3          0.3
node     82            1          0.2          0.5
node     83            1          0.5          0.2
node     84            1          0.4          0.2
node     85            1          0.2          0.4
node     86            1          0.2          0.3
node     87            1          0.3          0.2
node     88            1          0.1          0.5
node     89            1          0.5          0.1
node     90            1          0.4          0.1
node     91            1          0.1          0.4
node     92            1          0.2          0.2
node     93            1          0.1          0.3
node     94            1          0.3          0.1
node     95            1          0.1          0.2
node     96            1            0          0.5
node     97            1          0.5            0
node     98            1          0.2          0.1
node     99            1          0.4            0
node    100            1            0          0.4
node    101            1            0          0.3
node    102            1          0.3            0
node    103            1          0.1          0.1
node    104            1            0          0.2
node    105            1          0.2            0
node    106            1          0.1            0
node    107            1            0          0.1
node    108            1            0            0
node    109          1.5          0.5          0.5
node    110          1.5          0.4          0.5
node    111          1.5          0.5          0.4
node    112          1.5          0.4          0.4
node    113          1.5          0.5          0.3
node    114          1.5          0.3          0.5
node    115          1.5          0.4          0.3
node    116          1.5          0.3          0.4
node    117          1.5          0.3          0.3
node    118          1.5          0.5          0.2
node    119          1.5          0.2          0.5
node    120          1.5          0.4          0.2
node    121          1.5          0.2          0.4
node    122          1.5          0.2          0.3
node    123          1.5          0.3          0.2
node    124          1.5          0.1          0.5
node    125          1.5          0.5          0.1
node    126          1.5          0.4          0.1
node    127          1.5          0.1          0.4
node    128          1.5          0.2          0.2
node    129          1.5          0.1          0.3
node    130          1.5          0.3          0.1
node    131          1.5          0.1          0.2
node    132          1.5            0          0.5
node    133          1.5          0.5            0
node    134          1.5          0.2          0.1
node    135          1.5          0.4            0
node    136          1.5            0          0.4
node    137          1.5            0          0.3
node    138          1.5          0.3            0
node    139          1.5          0.1          0.1
node    140          1.5          0.2            0
node    141          1.5            0          0.2
node    142          1.5          0.1            0
node    143          1.5            0          0.1
node    144          1.5            0            0
node    145            2          0.5          0.5
node    146            2          0.5          0.4
node    147            2          0.4          0.5
node    148            2          0.4          0.4
node    149            2          0.5          0.3
node    150            2          0.3          0.5
node    151            2          0.3          0.4
node    152            2          0.4          0.3
node    153            2          0.3          0.3
node    154            2          0.5          0.2
node    155            2          0.2          0.5
node    156            2          0.2          0.4
node    157            2          0.4          0.2
node    158            2          0.2          0.3
node    159            2          0.3          0.2
node    160            2          0.5          0.1
node    161            2          0.1          0.5
node    162            2          0.1          0.4
node    163            2          0.4          0.1
node    164            2          0.2          0.2
node    165            2          0.3          0.1
node    166            2          0.1          0.3
node    167            2          0.2          0.1
node    168            2            0          0.5
node    169            2          0.1          0.2
node    170            2          0.5            0
node    171            2            0          0.4
node    172            2          0.4            0
node    173            2          0.3            0
node    174            2            0          0.3
node    175            2          0.1          0.1
node    176            2          0.2            0
node    177            2            0          0.2
node    178            2          0.1            0
node    179            2            0          0.1
node    180            2            0            0
node    181          2.5          0.5          0.5
node    182          2.5          0.4          0.5
node    183          2.5          0.5          0.4
node    184          2.5          0.4          0.4
node    185          2.5          0.3          0.5
node    186          2.5          0.5          0.3
node    187          2.5          0.3          0.4
node    188          2.5          0.4          0.3
node    189          2.5          0.3          0.3
node    190          2.5          0.2          0.5
node    191          2.5          0.5          0.2
node    192          2.5          0.4          0.2
node    193          2.5          0.2          0.4
node    194          2.5          0.2          0.3
node    195          2.5          0.3          0.2
node    196          2.5          0.1          0.5
node    197          2.5          0.5          0.1
node    198          2.5          0.4          0.1
node    199          2.5          0.1          0.4
node    200          2.5          0.2          0.2
node    201          2.5          0.3          0.1
node    202          2.5          0.1          0.3
node    203          2.5          0.2          0.1
node    204          2.5          0.1          0.2
node    205          2.5            0          0.5
node    206          2.5          0.5            0
node    207          2.5          0.4            0
node    208          2.5            0          0.4
node    209          2.5          0.3            0
node    210          2.5            0          0.3
node    211          2.5          0.1          0.1
node    212          2.5          0.2            0
node    213          2.5            0          0.2
node    214          2.5          0.1            0
node    215          2.5            0          0.1
node    216          2.5            0            0
node    217            3          0.5          0.5
node    218            3          0.5          0.4
node    219            3          0.4          0.5
node    220            3          0.4          0.4
node    221            3          0.5          0.3
node    222            3          0.3          0.5
node    223            3          0.3          0.4
node    224            3          0.4          0.3
node    225            3          0.3          0.3
node    226            3          0.5          0.2
node    227            3          0.2          0.5
node    228            3          0.4          0.2
node    229            3          0.2          0.4
node    230            3          0.3          0.2
node    231            3          0.2          0.3
node    232            3          0.5          0.1
node    233            3          0.1          0.5
node    234            3          0.4          0.1
node    235            3          0.1          0.4
node    236            3          0.2          0.2
node    237            3          0.3          0.1
node    238            3          0.1          0.3
node    239            3          0.5            0
node    240            3            0          0.5
node    241            3          0.1          0.2
node    242            3          0.2          0.1
node    243            3            0          0.4
node    244            3          0.4            0
node    245            3            0          0.3
node    246            3          0.3            0
node    247            3          0.1          0.1
node    248            3            0          0.2
node    249            3          0.2            0
node    250            3            0          0.1
node    251            3          0.1            0
node    252            3            0            0
node    253          3.5          0.5          0.5
node    254          3.5          0.5          0.4
node    255          3.5          0.4          0.5
node    256          3.5          0.4          0.4
node    257          3.5          0.5          0.3
node    258          3.5          0.3          0.5
node    259          3.5          0.3          0.4
node    260          3.5          0.4          0.3
node    261          3.5          0.3          0.3
node    262          3.5          0.5          0.2
node    263          3.5          0.2          0.5
node    264          3.5          0.4          0.2
node    265          3.5          0.2          0.4
node    266          3.5          0.3          0.2
node    267          3.5          0.2          0.3
node    268          3.5          0.5          0.1
node    269          3.5          0.1          0.5
node    270          3.5          0.4          0.1
node    271          3.5          0.1          0.4
node    272          3.5          0.2          0.2
node    273          3.5          0.3          0.1
node    274          3.5          0.1          0.3
node    275          3.5            0          0.5
node    276          3.5          0.5            0
node    277          3.5          0.2          0.1
node    278          3.5          0.1          0.2
node    279          3.5          0.4            0
node    280          3.5            0          0.4
node    281          3.5            0          0.3
node    282          3.5          0.3            0
node    283          3.5          0.1          0.1
node    284          3.5            0          0.2
node    285          3.5          0.2            0
node    286          3.5            0          0.1
node    287          3.5          0.1            0
node    288          3.5            0            0
node    289            4          0.5          0.5
node    290            4          0.5          0.4
node    291            4          0.4          0.5
node    292            4          0.4          0.4
node    293            4          0.5          0.3
node    294            4          0.3          0.5
node    295            4          0.3          0.4
node    296            4          0.4          0.3
node    297            4          0.3          0.3
node    298            4          0.2          0.5
node    299            4          0.5          0.2
node    300            4          0.2          0.4
node    301            4          0.4          0.2
node    302            4          0.3          0.2
node    303            4          0.2          0.3
node    304            4          0.5          0.1
node    305            4          0.1          0.5
node    306            4          0.4          0.1
node    307            4          0.1          0.4
node    308            4          0.2          0.2
node    309            4          0.3          0.1
node    310            4          0.1          0.3
node    311            4          0.5            0
node    312            4            0          0.5
node    313            4          0.2          0.1
node    314            4          0.1          0.2
node    315            4          0.4            0
node    316            4            0          0.4
node    317            4            0          0.3
node    318            4          0.3            0
node    319            4          0.1          0.1
node    320            4            0          0.2
node    321            4          0.2            0
node    322            4            0          0.1
node    323            4          0.1            0
node    324            4            0            0
node    325          4.5          0.5          0.5
node    326          4.5          0.5          0.4
node    327          4.5          0.4          0.5
node    328          4.5          0.4          0.4
node    329          4.5          0.5          0.3
node    330          4.5          0.3          0.5
node    331          4.5          0.4          0.3
node    332          4.5          0.3          0.4
node    333          4.5          0.3          0.3
node    334          4.5          0.5          0.2
node    335          4.5          0.2          0.5
node    336          4.5          0.4          0.2
node    337          4.5          0.2          0.4
node    338          4.5          0.3          0.2
node    339          4.5          0.2          0.3
node    340          4.5          0.5          0.1
node    341          4.5          0.1          0.5
node    342          4.5          0.4          0.1
node    343          4.5          0.1          0.4
node    344          4.5          0.2          0.2
node    345          4.5          0.1          0.3
node    346          4.5          0.3          0.1
node    347          4.5          0.5            0
node    348          4.5            0          0.5
node    349          4.5          0.2          0.1
node    350          4.5          0.1          0.2
node    351          4.5            0          0.4
node    352          4.5          0.4            0
node    353          4.5            0          0.3
node    354          4.5          0.3            0
node    355          4.5          0.1          0.1
node    356          4.5            0          0.2
node    357          4.5          0.2            0
node    358          4.5            0          0.1
node    359          4.5          0.1            0
node    360          4.5            0            0
node    361            5          0.5          0.5
node    362            5          0.5          0.4
node    363            5          0.4          0.5
node    364            5          0.4          0.4
node    365            5          0.5          0.3
node    366            5          0.3          0.5
node    367            5          0.3          0.4
node    368            5          0.4          0.3
node    369            5          0.3          0.3
node    370            5          0.2          0.5
node    371            5          0.5          0.2
node    372            5          0.4          0.2
node    373            5          0.2          0.4
node    374            5          0.2          0.3
node    375            5          0.3          0.2
node    376            5          0.5          0.1
node    377            5          0.1          0.5
node    378            5          0.1          0.4
node    379            5          0.4          0.1
node    380            5          0.2          0.2
node    381            5          0.3          0.1
node    382            5          0.1          0.3
node    383            5          0.1          0.2
node    384            5          0.5            0
node    385            5          0.2          0.1
node    386            5            0          0.5
node    387            5            0          0.4
node    388            5          0.4            0
node    389            5          0.3            0
node    390            5            0          0.3
node    391            5          0.1          0.1
node    392            5          0.2            0
node    393            5            0          0.2
node    394            5            0          0.1
node    395            5          0.1            0
node    396            5            0            0

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl z-transl
fix      1   1   1   1
fix      2   1   1   1
fix      3   1   1   1
fix      4   1   1   1
fix      5   1   1   1
fix      6   1   1   1
fix      7   1   1   1
fix      8   1   1   1
fix      9   1   1   1
fix     10   1   1   1
fix     11   1   1   1
fix     12   1   1   1
fix     13   1   1   1
fix     14   1   1   1
fix     15   1   1   1
fix     16   1   1   1
fix     17   1   1   1
fix     18   1   1   1
fix     19   1   1   1
fix     20   1   1   1
fix     21   1   1   1
fix     22   1   1   1
fix     23   1   1   1
fix     24   1   1   1
fix     25   1   1   1
fix     27   1   1   1
fix     28   1   1   1
fix     29   1   1   1
fix     34   1   1   1
fix     35   1   1   1
fix     39   1   1   1
fix     41   1   1   1
fix     42   1   1   1
fix     50   1   1   1
fix     51   1   1   1
fix     61   1   1   1
fix    361   1   1   1
fix    362   1   1   1
fix    363   1   1   1
fix    364   1   1   1
fix    365   1   1   1
fix    366   1   1   1
fix    367   1   1   1
fix    368   1   1   1
fix    369   1   1   1
fix    370   1   1   1
fix    371   1   1   1
fix    372   1   1   1
fix    373   1   1   1
fix    374   1   1   1
fix    375   1   1   1
fix    376   1   1   1
fix    377   1   1   1
fix    378   1   1   1
fix    379   1   1   1
fix    380   1   1   1
fix    381   1   1   1
fix    382   1   1   1
fix    383   1   1   1
fix    384   1   1   1
fix    385   1   1   1
fix    386   1   1   1
fix    387   1   1   1
fix    388   1   1   1
fix    389   1   1   1
fix    390   1   1   1
fix    391   1   1   1
fix    392   1   1   1
fix    393   1   1   1
fix    394   1   1   1
fix    395   1   1   1
fix    396   1   1   1

# S T A N D A R D   B R I C K   E L E M E N T S
# nDMaterial Definition used by stdBrick Elements
# (if they have not already been defined on this model domain)
nDMaterial ElasticIsotropic 127 3e+07 0.2            0
# stdBrick element definition: element stdBrick $eleTag $node1 $node2 $node3 $node4 $node5 $node6 $node7 $node8 $matTag <$b1 $b2 $b3>
element stdBrick      1     67     39     51     70     71     50     61     72    127        0        0        0
element stdBrick      2    103     67     70    106    107     71     72    108    127        0        0        0
element stdBrick      3    139    103    106    142    143    107    108    144    127        0        0        0
element stdBrick      4    175    139    142    178    179    143    144    180    127        0        0        0
element stdBrick      5    211    175    178    214    215    179    180    216    127        0        0        0
element stdBrick      6    247    211    214    251    250    215    216    252    127        0        0        0
element stdBrick      7    283    247    251    287    286    250    252    288    127        0        0        0
element stdBrick      8    319    283    287    323    322    286    288    324    127        0        0        0
element stdBrick      9    355    319    323    359    358    322    324    360    127        0        0        0
element stdBrick     10    391    355    359    395    394    358    360    396    127        0        0        0
element stdBrick     11     58     27     39     67     68     42     50     71    127        0        0        0
element stdBrick     12     95     58     67    103    104     68     71    107    127        0        0        0
element stdBrick     13    131     95    103    139    141    104    107    143    127        0        0        0
element stdBrick     14    169    131    139    175    177    141    143    179    127        0        0        0
element stdBrick     15    204    169    175    211    213    177    179    215    127        0        0        0
element stdBrick     16    241    204    211    247    248    213    215    250    127        0        0        0
element stdBrick     17    278    241    247    283    284    248    250    286    127        0        0        0
element stdBrick     18    314    278    283    319    320    284    286    322    127        0        0        0
element stdBrick     19    350    314    319    355    356    320    322    358    127        0        0        0
element stdBrick     20    383    350    355    391    393    356    358    394    127        0        0        0
element stdBrick     21     56     22     27     58     65     34     42     68    127        0        0        0
element stdBrick     22     93     56     58     95    101     65     68    104    127        0        0        0
element stdBrick     23    129     93     95    131    137    101    104    141    127        0        0        0
element stdBrick     24    166    129    131    169    174    137    141    177    127        0        0        0
element stdBrick     25    202    166    169    204    210    174    177    213    127        0        0        0
element stdBrick     26    238    202    204    241    245    210    213    248    127        0        0        0
element stdBrick     27    274    238    241    278    281    245    248    284    127        0        0        0
element stdBrick     28    310    274    278    314    317    281    284    320    127        0        0        0
element stdBrick     29    345    310    314    350    353    317    320    356    127        0        0        0
element stdBrick     30    382    345    350    383    390    353    356    393    127        0        0        0
element stdBrick     31     53     19     22     56     63     29     34     65    127        0        0        0
element stdBrick     32     91     53     56     93    100     63     65    101    127        0        0        0
element stdBrick     33    127     91     93    129    136    100    101    137    127        0        0        0
element stdBrick     34    162    127    129    166    171    136    137    174    127        0        0        0
element stdBrick     35    199    162    166    202    208    171    174    210    127        0        0        0
element stdBrick     36    235    199    202    238    243    208    210    245    127        0        0        0
element stdBrick     37    271    235    238    274    280    243    245    281    127        0        0        0
element stdBrick     38    307    271    274    310    316    280    281    317    127        0        0        0
element stdBrick     39    343    307    310    345    351    316    317    353    127        0        0        0
element stdBrick     40    378    343    345    382    387    351    353    390    127        0        0        0
element stdBrick     41     49     16     19     53     59     24     29     63    127        0        0        0
element stdBrick     42     88     49     53     91     96     59     63    100    127        0        0        0
element stdBrick     43    124     88     91    127    132     96    100    136    127        0        0        0
element stdBrick     44    161    124    127    162    168    132    136    171    127        0        0        0
element stdBrick     45    196    161    162    199    205    168    171    208    127        0        0        0
element stdBrick     46    233    196    199    235    240    205    208    243    127        0        0        0
element stdBrick     47    269    233    235    271    275    240    243    280    127        0        0        0
element stdBrick     48    305    269    271    307    312    275    280    316    127        0        0        0
element stdBrick     49    341    305    307    343    348    312    316    351    127        0        0        0
element stdBrick     50    377    341    343    378    386    348    351    387    127        0        0        0
element stdBrick     51     62     25     41     69     67     39     51     70    127        0        0        0
element stdBrick     52     98     62     69    105    103     67     70    106    127        0        0        0
element stdBrick     53    134     98    105    140    139    103    106    142    127        0        0        0
element stdBrick     54    167    134    140    176    175    139    142    178    127        0        0        0
element stdBrick     55    203    167    176    212    211    175    178    214    127        0        0        0
element stdBrick     56    242    203    212    249    247    211    214    251    127        0        0        0
element stdBrick     57    277    242    249    285    283    247    251    287    127        0        0        0
element stdBrick     58    313    277    285    321    319    283    287    323    127        0        0        0
element stdBrick     59    349    313    321    357    355    319    323    359    127        0        0        0
element stdBrick     60    385    349    357    392    391    355    359    395    127        0        0        0
element stdBrick     61     55     20     25     62     58     27     39     67    127        0        0        0
element stdBrick     62     92     55     62     98     95     58     67    103    127        0        0        0
element stdBrick     63    128     92     98    134    131     95    103    139    127        0        0        0
element stdBrick     64    164    128    134    167    169    131    139    175    127        0        0        0
element stdBrick     65    200    164    167    203    204    169    175    211    127        0        0        0
element stdBrick     66    236    200    203    242    241    204    211    247    127        0        0        0
element stdBrick     67    272    236    242    277    278    241    247    283    127        0        0        0
element stdBrick     68    308    272    277    313    314    278    283    319    127        0        0        0
element stdBrick     69    344    308    313    349    350    314    319    355    127        0        0        0
element stdBrick     70    380    344    349    385    383    350    355    391    127        0        0        0
element stdBrick     71     47     14     20     55     56     22     27     58    127        0        0        0
element stdBrick     72     86     47     55     92     93     56     58     95    127        0        0        0
element stdBrick     73    122     86     92    128    129     93     95    131    127        0        0        0
element stdBrick     74    158    122    128    164    166    129    131    169    127        0        0        0
element stdBrick     75    194    158    164    200    202    166    169    204    127        0        0        0
element stdBrick     76    231    194    200    236    238    202    204    241    127        0        0        0
element stdBrick     77    267    231    236    272    274    238    241    278    127        0        0        0
element stdBrick     78    303    267    272    308    310    274    278    314    127        0        0        0
element stdBrick     79    339    303    308    344    345    310    314    350    127        0        0        0
element stdBrick     80    374    339    344    380    382    345    350    383    127        0        0        0
element stdBrick     81     45     12     14     47     53     19     22     56    127        0        0        0
element stdBrick     82     85     45     47     86     91     53     56     93    127        0        0        0
element stdBrick     83    121     85     86    122    127     91     93    129    127        0        0        0
element stdBrick     84    156    121    122    158    162    127    129    166    127        0        0        0
element stdBrick     85    193    156    158    194    199    162    166    202    127        0        0        0
element stdBrick     86    229    193    194    231    235    199    202    238    127        0        0        0
element stdBrick     87    265    229    231    267    271    235    238    274    127        0        0        0
element stdBrick     88    300    265    267    303    307    271    274    310    127        0        0        0
element stdBrick     89    337    300    303    339    343    307    310    345    127        0        0        0
element stdBrick     90    373    337    339    374    378    343    345    382    127        0        0        0
element stdBrick     91     43     11     12     45     49     16     19     53    127        0        0        0
element stdBrick     92     82     43     45     85     88     49     53     91    127        0        0        0
element stdBrick     93    119     82     85    121    124     88     91    127    127        0        0        0
element stdBrick     94    155    119    121    156    161    124    127    162    127        0        0        0
element stdBrick     95    190    155    156    193    196    161    162    199    127        0        0        0
element stdBrick     96    227    190    193    229    233    196    199    235    127        0        0        0
element stdBrick     97    263    227    229    265    269    233    235    271    127        0        0        0
element stdBrick     98    298    263    265    300    305    269    271    307    127        0        0        0
element stdBrick     99    335    298    300    337    341    305    307    343    127        0        0        0
element stdBrick    100    370    335    337    373    377    341    343    378    127        0        0        0
element stdBrick    101     57     21     35     66     62     25     41     69    127        0        0        0
element stdBrick    102     94     57     66    102     98     62     69    105    127        0        0        0
element stdBrick    103    130     94    102    138    134     98    105    140    127        0        0        0
element stdBrick    104    165    130    138    173    167    134    140    176    127        0        0        0
element stdBrick    105    201    165    173    209    203    167    176    212    127        0        0        0
element stdBrick    106    237    201    209    246    242    203    212    249    127        0        0        0
element stdBrick    107    273    237    246    282    277    242    249    285    127        0        0        0
element stdBrick    108    309    273    282    318    313    277    285    321    127        0        0        0
element stdBrick    109    346    309    318    354    349    313    321    357    127        0        0        0
element stdBrick    110    381    346    354    389    385    349    357    392    127        0        0        0
element stdBrick    111     48     15     21     57     55     20     25     62    127        0        0        0
element stdBrick    112     87     48     57     94     92     55     62     98    127        0        0        0
element stdBrick    113    123     87     94    130    128     92     98    134    127        0        0        0
element stdBrick    114    159    123    130    165    164    128    134    167    127        0        0        0
element stdBrick    115    195    159    165    201    200    164    167    203    127        0        0        0
element stdBrick    116    230    195    201    237    236    200    203    242    127        0        0        0
element stdBrick    117    266    230    237    273    272    236    242    277    127        0        0        0
element stdBrick    118    302    266    273    309    308    272    277    313    127        0        0        0
element stdBrick    119    338    302    309    346    344    308    313    349    127        0        0        0
element stdBrick    120    375    338    346    381    380    344    349    385    127        0        0        0
element stdBrick    121     40      9     15     48     47     14     20     55    127        0        0        0
element stdBrick    122     81     40     48     87     86     47     55     92    127        0        0        0
element stdBrick    123    117     81     87    123    122     86     92    128    127        0        0        0
element stdBrick    124    153    117    123    159    158    122    128    164    127        0        0        0
element stdBrick    125    189    153    159    195    194    158    164    200    127        0        0        0
element stdBrick    126    225    189    195    230    231    194    200    236    127        0        0        0
element stdBrick    127    261    225    230    266    267    231    236    272    127        0        0        0
element stdBrick    128    297    261    266    302    303    267    272    308    127        0        0        0
element stdBrick    129    333    297    302    338    339    303    308    344    127        0        0        0
element stdBrick    130    369    333    338    375    374    339    344    380    127        0        0        0
element stdBrick    131     37      8      9     40     45     12     14     47    127        0        0        0
element stdBrick    132     80     37     40     81     85     45     47     86    127        0        0        0
element stdBrick    133    116     80     81    117    121     85     86    122    127        0        0        0
element stdBrick    134    151    116    117    153    156    121    122    158    127        0        0        0
element stdBrick    135    187    151    153    189    193    156    158    194    127        0        0        0
element stdBrick    136    223    187    189    225    229    193    194    231    127        0        0        0
element stdBrick    137    259    223    225    261    265    229    231    267    127        0        0        0
element stdBrick    138    295    259    261    297    300    265    267    303    127        0        0        0
element stdBrick    139    332    295    297    333    337    300    303    339    127        0        0        0
element stdBrick    140    367    332    333    369    373    337    339    374    127        0        0        0
element stdBrick    141     36      6      8     37     43     11     12     45    127        0        0        0
element stdBrick    142     78     36     37     80     82     43     45     85    127        0        0        0
element stdBrick    143    114     78     80    116    119     82     85    121    127        0        0        0
element stdBrick    144    150    114    116    151    155    119    121    156    127        0        0        0
element stdBrick    145    185    150    151    187    190    155    156    193    127        0        0        0
element stdBrick    146    222    185    187    223    227    190    193    229    127        0        0        0
element stdBrick    147    258    222    223    259    263    227    229    265    127        0        0        0
element stdBrick    148    294    258    259    295    298    263    265    300    127        0        0        0
element stdBrick    149    330    294    295    332    335    298    300    337    127        0        0        0
element stdBrick    150    366    330    332    367    370    335    337    373    127        0        0        0
element stdBrick    151     54     18     28     64     57     21     35     66    127        0        0        0
element stdBrick    152     90     54     64     99     94     57     66    102    127        0        0        0
element stdBrick    153    126     90     99    135    130     94    102    138    127        0        0        0
element stdBrick    154    163    126    135    172    165    130    138    173    127        0        0        0
element stdBrick    155    198    163    172    207    201    165    173    209    127        0        0        0
element stdBrick    156    234    198    207    244    237    201    209    246    127        0        0        0
element stdBrick    157    270    234    244    279    273    237    246    282    127        0        0        0
element stdBrick    158    306    270    279    315    309    273    282    318    127        0        0        0
element stdBrick    159    342    306    315    352    346    309    318    354    127        0        0        0
element stdBrick    160    379    342    352    388    381    346    354    389    127        0        0        0
element stdBrick    161     46     13     18     54     48     15     21     57    127        0        0        0
element stdBrick    162     84     46     54     90     87     48     57     94    127        0        0        0
element stdBrick    163    120     84     90    126    123     87     94    130    127        0        0        0
element stdBrick    164    157    120    126    163    159    123    130    165    127        0        0        0
element stdBrick    165    192    157    163    198    195    159    165    201    127        0        0        0
element stdBrick    166    228    192    198    234    230    195    201    237    127        0        0        0
element stdBrick    167    264    228    234    270    266    230    237    273    127        0        0        0
element stdBrick    168    301    264    270    306    302    266    273    309    127        0        0        0
element stdBrick    169    336    301    306    342    338    302    309    346    127        0        0        0
element stdBrick    170    372    336    342    379    375    338    346    381    127        0        0        0
element stdBrick    171     38      7     13     46     40      9     15     48    127        0        0        0
element stdBrick    172     79     38     46     84     81     40     48     87    127        0        0        0
element stdBrick    173    115     79     84    120    117     81     87    123    127        0        0        0
element stdBrick    174    152    115    120    157    153    117    123    159    127        0        0        0
element stdBrick    175    188    152    157    192    189    153    159    195    127        0        0        0
element stdBrick    176    224    188    192    228    225    189    195    230    127        0        0        0
element stdBrick    177    260    224    228    264    261    225    230    266    127        0        0        0
element stdBrick    178    296    260    264    301    297    261    266    302    127        0        0        0
element stdBrick    179    331    296    301    336    333    297    302    338    127        0        0        0
element stdBrick    180    368    331    336    372    369    333    338    375    127        0        0        0
element stdBrick    181     32      4      7     38     37      8      9     40    127        0        0        0
element stdBrick    182     76     32     38     79     80     37     40     81    127        0        0        0
element stdBrick    183    112     76     79    115    116     80     81    117    127        0        0        0
element stdBrick    184    148    112    115    152    151    116    117    153    127        0        0        0
element stdBrick    185    184    148    152    188    187    151    153    189    127        0        0        0
element stdBrick    186    220    184    188    224    223    187    189    225    127        0        0        0
element stdBrick    187    256    220    224    260    259    223    225    261    127        0        0        0
element stdBrick    188    292    256    260    296    295    259    261    297    127        0        0        0
element stdBrick    189    328    292    296    331    332    295    297    333    127        0        0        0
element stdBrick    190    364    328    331    368    367    332    333    369    127        0        0        0
element stdBrick    191     30      2      4     32     36      6      8     37    127        0        0        0
element stdBrick    192     74     30     32     76     78     36     37     80    127        0        0        0
element stdBrick    193    110     74     76    112    114     78     80    116    127        0        0        0
element stdBrick    194    147    110    112    148    150    114    116    151    127        0        0        0
element stdBrick    195    182    147    148    184    185    150    151    187    127        0        0        0
element stdBrick    196    219    182    184    220    222    185    187    223    127        0        0        0
element stdBrick    197    255    219    220    256    258    222    223    259    127        0        0        0
element stdBrick    198    291    255    256    292    294    258    259    295    127        0        0        0
element stdBrick    199    327    291    292    328    330    294    295    332    127        0        0        0
element stdBrick    200    363    327    328    364    366    330    332    367    127        0        0        0
element stdBrick    201     52     17     23     60     54     18     28     64    127        0        0        0
element stdBrick    202     89     52     60     97     90     54     64     99    127        0        0        0
element stdBrick    203    125     89     97    133    126     90     99    135    127        0        0        0
element stdBrick    204    160    125    133    170    163    126    135    172    127        0        0        0
element stdBrick    205    197    160    170    206    198    163    172    207    127        0        0        0
element stdBrick    206    232    197    206    239    234    198    207    244    127        0        0        0
element stdBrick    207    268    232    239    276    270    234    244    279    127        0        0        0
element stdBrick    208    304    268    276    311    306    270    279    315    127        0        0        0
element stdBrick    209    340    304    311    347    342    306    315    352    127        0        0        0
element stdBrick    210    376    340    347    384    379    342    352    388    127        0        0        0
element stdBrick    211     44     10     17     52     46     13     18     54    127        0        0        0
element stdBrick    212     83     44     52     89     84     46     54     90    127        0        0        0
element stdBrick    213    118     83     89    125    120     84     90    126    127        0        0        0
element stdBrick    214    154    118    125    160    157    120    126    163    127        0        0        0
element stdBrick    215    191    154    160    197    192    157    163    198    127        0        0        0
element stdBrick    216    226    191    197    232    228    192    198    234    127        0        0        0
element stdBrick    217    262    226    232    268    264    228    234    270    127        0        0        0
element stdBrick    218    299    262    268    304    301    264    270    306    127        0        0        0
element stdBrick    219    334    299    304    340    336    301    306    342    127        0        0        0
element stdBrick    220    371    334    340    376    372    336    342    379    127        0        0        0
element stdBrick    221     33      5     10     44     38      7     13     46    127        0        0        0
element stdBrick    222     77     33     44     83     79     38     46     84    127        0        0        0
element stdBrick    223    113     77     83    118    115     79     84    120    127        0        0        0
element stdBrick    224    149    113    118    154    152    115    120    157    127        0        0        0
element stdBrick    225    186    149    154    191    188    152    157    192    127        0        0        0
element stdBrick    226    221    186    191    226    224    188    192    228    127        0        0        0
element stdBrick    227    257    221    226    262    260    224    228    264    127        0        0        0
element stdBrick    228    293    257    262    299    296    260    264    301    127        0        0        0
element stdBrick    229    329    293    299    334    331    296    301    336    127        0        0        0
element stdBrick    230    365    329    334    371    368    331    336    372    127        0        0        0
element stdBrick    231     31      3      5     33     32      4      7     38    127        0        0        0
element stdBrick    232     75     31     33     77     76     32     38     79    127        0        0        0
element stdBrick    233    111     75     77    113    112     76     79    115    127        0        0        0
element stdBrick    234    146    111    113    149    148    112    115    152    127        0        0        0
element stdBrick    235    183    146    149    186    184    148    152    188    127        0        0        0
element stdBrick    236    218    183    186    221    220    184    188    224    127        0        0        0
element stdBrick    237    254    218    221    257    256    220    224    260    127        0        0        0
element stdBrick    238    290    254    257    293    292    256    260    296    127        0        0        0
element stdBrick    239    326    290    293    329    328    292    296    331    127        0        0        0
element stdBrick    240    362    326    329    365    364    328    331    368    127        0        0        0
element stdBrick    241     26      1      3     31     30      2      4     32    127        0        0        0
element stdBrick    242     73     26     31     75     74     30     32     76    127        0        0        0
element stdBrick    243    109     73     75    111    110     74     76    112    127        0        0        0
element stdBrick    244    145    109    111    146    147    110    112    148    127        0        0        0
element stdBrick    245    181    145    146    183    182    147    148    184    127        0        0        0
element stdBrick    246    217    181    183    218    219    182    184    220    127        0        0        0
element stdBrick    247    253    217    218    254    255    219    220    256    127        0        0        0
element stdBrick    248    289    253    254    290    291    255    256    292    127        0        0        0
element stdBrick    249    325    289    290    326    327    291    292    328    127        0        0        0
element stdBrick    250    361    325    326    362    363    327    328    364    127        0        0        0

# R E C O R D E R S
recorder Node -file Node_displacements.out -time -nodeRange 1 396 -dof 1 2 3 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 396 -dof 4 5 6 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 396 -dof 1 2 3 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 396 -dof 4 5 6 reaction

# Loads - Plain Pattern
pattern Plain 100 Linear {
load      1        0        0       -5
load      2        0        0       -5
load      6        0        0       -5
load     11        0        0       -5
load     16        0        0       -5
load     24        0        0       -5
load     26        0        0       -5
load     30        0        0       -5
load     36        0        0       -5
load     43        0        0       -5
load     49        0        0       -5
load     59        0        0       -5
load     73        0        0       -5
load     74        0        0       -5
load     78        0        0       -5
load     82        0        0       -5
load     88        0        0       -5
load     96        0        0       -5
load    109        0        0       -5
load    110        0        0       -5
load    114        0        0       -5
load    119        0        0       -5
load    124        0        0       -5
load    132        0        0       -5
load    145        0        0       -5
load    147        0        0       -5
load    150        0        0       -5
load    155        0        0       -5
load    161        0        0       -5
load    168        0        0       -5
load    181        0        0       -5
load    182        0        0       -5
load    185        0        0       -5
load    190        0        0       -5
load    196        0        0       -5
load    205        0        0       -5
load    217        0        0       -5
load    219        0        0       -5
load    222        0        0       -5
load    227        0        0       -5
load    233        0        0       -5
load    240        0        0       -5
load    253        0        0       -5
load    255        0        0       -5
load    258        0        0       -5
load    263        0        0       -5
load    269        0        0       -5
load    275        0        0       -5
load    289        0        0       -5
load    291        0        0       -5
load    294        0        0       -5
load    298        0        0       -5
load    305        0        0       -5
load    312        0        0       -5
load    325        0        0       -5
load    327        0        0       -5
load    330        0        0       -5
load    335        0        0       -5
load    341        0        0       -5
load    348        0        0       -5
load    361        0        0       -5
load    363        0        0       -5
load    366        0        0       -5
load    370        0        0       -5
load    377        0        0       -5
load    386        0        0       -5
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