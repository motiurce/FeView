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

node      1            2            0            3
node      2          1.8            0            3
node      3            2          0.2            3
node      4            2            0          2.8
node      5            2          0.2          2.8
node      6          1.8          0.2            3
node      7          1.8            0          2.8
node      8          1.6            0            3
node      9            2            0          2.6
node     10            2          0.4            3
node     11          1.8            0          2.6
node     12            2          0.2          2.6
node     13            2          0.4          2.8
node     14          1.6          0.2            3
node     15          1.6            0          2.8
node     16          1.8          0.4            3
node     17          1.6            0          2.6
node     18            2          0.4          2.6
node     19          1.6          0.4            3
node     20            2          0.6            3
node     21            2            0          2.4
node     22          1.4            0            3
node     23          1.4          0.2            3
node     24          1.8          0.6            3
node     25            2          0.2          2.4
node     26          1.8            0          2.4
node     27            2          0.6          2.8
node     28          1.4            0          2.8
node     29          1.6          0.6            3
node     30            2          0.6          2.6
node     31          1.6            0          2.4
node     32          1.4            0          2.6
node     33            2          0.4          2.4
node     34          1.4          0.4            3
node     35            2            0          2.2
node     36          1.2            0            3
node     37            2          0.8            3
node     38            2          0.2          2.2
node     39          1.8            0          2.2
node     40          1.8          0.8            3
node     41          1.2            0          2.8
node     42            2          0.8          2.8
node     43          1.2          0.2            3
node     44          1.4          0.6            3
node     45            2          0.6          2.4
node     46          1.4            0          2.4
node     47          1.6            0          2.2
node     48            2          0.8          2.6
node     49            2          0.4          2.2
node     50          1.2            0          2.6
node     51          1.6          0.8            3
node     52          1.2          0.4            3
node     53            2          0.6          2.2
node     54          1.4            0          2.2
node     55            2          0.8          2.4
node     56            2            1            3
node     57            2            0            2
node     58            1            0            3
node     59          1.2          0.6            3
node     60          1.2            0          2.4
node     61          1.4          0.8            3
node     62            2            1          2.8
node     63          1.8            1            3
node     64            2          0.2            2
node     65          1.8            0            2
node     66            1            0          2.8
node     67            1          0.2            3
node     68          1.8          0.2            2
node     69          1.8            1          2.8
node     70          1.6            1            3
node     71          1.6            0            2
node     72            2            1          2.6
node     73            1            0          2.6
node     74            2          0.4            2
node     75            1          0.4            3
node     76          1.8            1          2.6
node     77          1.6            1          2.8
node     78          1.6          0.2            2
node     79          1.8          0.4            2
node     80          1.2            0          2.2
node     81            2          0.8          2.2
node     82          1.2          0.8            3
node     83          1.6            1          2.6
node     84          1.6          0.4            2
node     85            2          0.6            2
node     86            1            0          2.4
node     87            2            1          2.4
node     88          1.4            0            2
node     89          1.4            1            3
node     90            1          0.6            3
node     91          1.4          0.2            2
node     92          1.8          0.6            2
node     93          1.8            1          2.4
node     94          1.4            1          2.8
node     95          0.8            0            3
node     96            2            0          1.8
node     97            2          0.2          1.8
node     98          0.8            0          2.8
node     99          1.8            0          1.8
node    100          0.8          0.2            3
node    101          1.6          0.6            2
node    102          1.6            1          2.4
node    103          1.4            1          2.6
node    104          1.4          0.4            2
node    105          0.8            0          2.6
node    106            2          0.4          1.8
node    107          1.6            0          1.8
node    108          0.8          0.4            3
node    109            2            1          2.2
node    110            1            0          2.2
node    111          1.2            1            3
node    112          1.2            0            2
node    113            2          0.8            2
node    114            1          0.8            3
node    115          1.8            1          2.2
node    116          1.8          0.8            2
node    117          1.2            1          2.8
node    118          1.2          0.2            2
node    119          1.4          0.6            2
node    120          1.4            1          2.4
node    121          0.8          0.6            3
node    122            2          0.6          1.8
node    123          1.6            1          2.2
node    124          1.4            0          1.8
node    125          0.8            0          2.4
node    126          1.2            1          2.6
node    127          1.6          0.8            2
node    128          1.2          0.4            2
node    129          0.6            0            3
node    130            2            0          1.6
node    131          1.8            0          1.6
node    132          1.4            1          2.2
node    133            2          0.2          1.6
node    134          0.6            0          2.8
node    135          0.6          0.2            3
node    136            2            1            2
node    137            1            0            2
node    138            1            1            3
node    139          1.2            1          2.4
node    140          1.2          0.6            2
node    141          1.4          0.8            2
node    142            1            1          2.8
node    143          1.8            1            2
node    144            1          0.2            2
node    145          1.2            0          1.8
node    146          0.8            0          2.2
node    147            2          0.8          1.8
node    148          0.8          0.8            3
node    149          1.6            0          1.6
node    150            2          0.4          1.6
node    151          0.6            0          2.6
node    152          0.6          0.4            3
node    153            1            1          2.6
node    154          1.6            1            2
node    155            1          0.4            2
node    156          1.2            1          2.2
node    157          1.2          0.8            2
node    158          1.4            0          1.6
node    159          0.6            0          2.4
node    160            2          0.6          1.6
node    161          0.6          0.6            3
node    162          1.4            1            2
node    163            1            1          2.4
node    164            1          0.6            2
node    165          0.8            0            2
node    166            2            1          1.8
node    167          0.8            1            3
node    168            1            0          1.8
node    169          1.8            1          1.8
node    170          0.8            1          2.8
node    171          0.8          0.2            2
node    172          0.4            0            3
node    173            2            0          1.4
node    174          1.6            1          1.8
node    175            2          0.8          1.6
node    176          0.8            1          2.6
node    177          1.2            0          1.6
node    178          0.6            0          2.2
node    179          0.4            0          2.8
node    180          0.4          0.2            3
node    181          0.6          0.8            3
node    182            2          0.2          1.4
node    183          1.8            0          1.4
node    184          0.8          0.4            2
node    185            1            1          2.2
node    186          1.2            1            2
node    187            1          0.8            2
node    188          0.4            0          2.6
node    189          1.6            0          1.4
node    190          0.4          0.4            3
node    191            2          0.4          1.4
node    192          0.8          0.6            2
node    193          1.4            1          1.8
node    194          0.8            1          2.4
node    195          0.8            0          1.8
node    196          0.4          0.6            3
node    197            2          0.6          1.4
node    198          1.4            0          1.4
node    199          0.4            0          2.4
node    200            2            1          1.6
node    201          0.6            0            2
node    202            1            0          1.6
node    203          0.6            1            3
node    204          1.8            1          1.6
node    205            1            1            2
node    206          0.6          0.2            2
node    207          0.6            1          2.8
node    208          1.2            1          1.8
node    209          0.8            1          2.2
node    210          0.8          0.8            2
node    211          1.6            1          1.6
node    212          0.6          0.4            2
node    213          0.6            1          2.6
node    214          0.4            0          2.2
node    215          0.4          0.8            3
node    216          1.2            0          1.4
node    217            2          0.8          1.4
node    218            2            0          1.2
node    219          0.2            0            3
node    220          0.2            0          2.8
node    221          1.8            0          1.2
node    222          0.2          0.2            3
node    223            2          0.2          1.2
node    224          1.4            1          1.6
node    225          0.6          0.6            2
node    226          0.6            1          2.4
node    227          0.6            0          1.8
node    228          0.8            0          1.6
node    229          0.2          0.4            3
node    230            2          0.4          1.2
node    231          1.6            0          1.2
node    232          0.2            0          2.6
node    233          0.8            1            2
node    234            1            1          1.8
node    235          0.4            0            2
node    236          0.4            1            3
node    237            1            0          1.4
node    238            2            1          1.4
node    239          0.2          0.6            3
node    240          1.2            1          1.6
node    241          0.6            1          2.2
node    242            2          0.6          1.2
node    243          0.4          0.2            2
node    244          1.8            1          1.4
node    245          0.4            1          2.8
node    246          0.6          0.8            2
node    247          0.2            0          2.4
node    248          1.4            0          1.2
node    249          0.4            1          2.6
node    250          1.6            1          1.4
node    251          0.4          0.4            2
node    252          0.8            1          1.8
node    253          0.2            0          2.2
node    254            2          0.8          1.2
node    255          0.2          0.8            3
node    256          1.2            0          1.2
node    257          0.4          0.6            2
node    258          0.6            0          1.6
node    259          0.4            1          2.4
node    260          1.4            1          1.4
node    261          0.6            1            2
node    262            1            1          1.6
node    263          0.4            0          1.8
node    264          0.8            0          1.4
node    265            2            0            1
node    266            0            0            3
node    267            0          0.2            3
node    268            2          0.2            1
node    269            0            0          2.8
node    270          1.8            0            1
node    271            0          0.2          2.8
node    272          1.8          0.2            1
node    273          1.6            0            1
node    274            2          0.4            1
node    275            0          0.4            3
node    276            0            0          2.6
node    277            0          0.2          2.6
node    278          0.4          0.8            2
node    279            0          0.4          2.8
node    280          0.4            1          2.2
node    281          1.6          0.2            1
node    282          1.8          0.4            1
node    283          1.2            1          1.4
node    284            2            1          1.2
node    285          0.2            0            2
node    286          0.2            1            3
node    287            1            0          1.2
node    288          0.2          0.2            2
node    289          0.2            1          2.8
node    290          1.8            1          1.2
node    291          1.6          0.4            1
node    292            0          0.4          2.6
node    293            2          0.6            1
node    294          1.4            0            1
node    295            0          0.6            3
node    296            0            0          2.4
node    297            0          0.2          2.4
node    298            0          0.6          2.8
node    299          0.6            1          1.8
node    300          1.4          0.2            1
node    301          0.8            1          1.6
node    302          0.2          0.4            2
node    303          0.2            1          2.6
node    304          1.8          0.6            1
node    305          1.6            1          1.2
node    306          1.6          0.6            1
node    307            0          0.6          2.6
node    308          0.4            0          1.6
node    309          0.6            0          1.4
node    310            0          0.4          2.4
node    311          1.4          0.4            1
node    312            1            1          1.4
node    313          0.4            1            2
node    314          0.2          0.6            2
node    315          1.4            1          1.2
node    316          0.2            1          2.4
node    317            0            0          2.2
node    318          1.2            0            1
node    319            0          0.8            3
node    320            2          0.8            1
node    321          0.2            0          1.8
node    322            0          0.2          2.2
node    323          1.8          0.8            1
node    324          0.8            0          1.2
node    325          1.2          0.2            1
node    326            0          0.8          2.8
node    327            0          0.6          2.4
node    328          1.4          0.6            1
node    329            0          0.4          2.2
node    330          1.6          0.8            1
node    331          1.2          0.4            1
node    332            0          0.8          2.6
node    333            2            0          0.8
node    334            2          0.2          0.8
node    335          0.2            1          2.2
node    336          1.8            0          0.8
node    337          1.2            1          1.2
node    338          0.2          0.8            2
node    339          0.6            1          1.6
node    340            0          0.6          2.2
node    341            0            1            3
node    342          1.2          0.6            1
node    343          0.8            1          1.4
node    344            0            0            2
node    345            2            1            1
node    346            1            0            1
node    347          0.4            1          1.8
node    348            2          0.4          0.8
node    349          1.6            0          0.8
node    350            0          0.8          2.4
node    351          1.4          0.8            1
node    352            0            1          2.8
node    353          1.8            1            1
node    354            0          0.2            2
node    355            1          0.2            1
node    356          0.4            0          1.4
node    357            0          0.4            2
node    358          1.6            1            1
node    359            0            1          2.6
node    360            1          0.4            1
node    361            2          0.6          0.8
node    362          0.6            0          1.2
node    363          0.2            0          1.6
node    364          1.4            0          0.8
node    365          0.2            1            2
node    366            1            1          1.2
node    367            0          0.8          2.2
node    368          1.2          0.8            1
node    369          1.4            1            1
node    370            1          0.6            1
node    371            0          0.6            2
node    372            0            1          2.4
node    373            0            0          1.8
node    374          0.8            0            1
node    375          1.2            0          0.8
node    376            2          0.8          0.8
node    377          0.8          0.2            1
node    378            0          0.2          1.8
node    379          0.4            1          1.6
node    380          0.6            1          1.4
node    381            0          0.4          1.8
node    382          0.8          0.4            1
node    383            0            1          2.2
node    384            1          0.8            1
node    385            0          0.8            2
node    386          1.2            1            1
node    387          0.8            1          1.2
node    388          0.2            1          1.8
node    389            2            0          0.6
node    390            0          0.6          1.8
node    391          0.8          0.6            1
node    392          0.4            0          1.2
node    393            2          0.2          0.6
node    394          1.8            0          0.6
node    395          0.2            0          1.4
node    396            2            1          0.8
node    397            1            0          0.8
node    398          1.8            1          0.8
node    399          1.6            0          0.6
node    400            2          0.4          0.6
node    401          0.6            0            1
node    402            0            0          1.6
node    403          1.6            1          0.8
node    404            0          0.2          1.6
node    405            1            1            1
node    406            0            1            2
node    407          0.6          0.2            1
node    408          0.8          0.8            1
node    409            0          0.8          1.8
node    410            0          0.4          1.6
node    411          0.6          0.4            1
node    412            2          0.6          0.6
node    413          0.4            1          1.4
node    414          1.4            0          0.6
node    415          0.2            1          1.6
node    416          0.6            1          1.2
node    417          1.4            1          0.8
node    418          0.8            0          0.8
node    419            0          0.6          1.6
node    420          0.6          0.6            1
node    421          1.2            0          0.6
node    422            2          0.8          0.6
node    423          0.8            1            1
node    424            0            1          1.8
node    425          1.2            1          0.8
node    426          0.2            0          1.2
node    427          0.4            0            1
node    428            0            0          1.4
node    429          0.6          0.8            1
node    430            0          0.2          1.4
node    431            0          0.8          1.6
node    432          0.4          0.2            1
node    433          0.4          0.4            1
node    434            0          0.4          1.4
node    435            1            0          0.6
node    436            2            1          0.6
node    437            2            0          0.4
node    438          0.2            1          1.4
node    439          0.4            1          1.2
node    440          0.6            0          0.8
node    441            2          0.2          0.4
node    442          1.8            0          0.4
node    443          1.8            1          0.6
node    444            1            1          0.8
node    445          0.4          0.6            1
node    446            0          0.6          1.4
node    447            2          0.4          0.4
node    448          1.6            0          0.4
node    449          1.6            1          0.6
node    450          0.6            1            1
node    451            0            1          1.6
node    452          1.4            1          0.6
node    453            2          0.6          0.4
node    454          1.4            0          0.4
node    455          0.4          0.8            1
node    456            0          0.8          1.4
node    457          0.8            0          0.6
node    458            0            0          1.2
node    459          0.2            0            1
node    460          0.8            1          0.8
node    461          0.2          0.2            1
node    462            0          0.2          1.2
node    463          0.4            0          0.8
node    464          1.2            0          0.4
node    465          0.2          0.4            1
node    466            0          0.4          1.2
node    467            2          0.8          0.4
node    468          1.2            1          0.6
node    469          0.2            1          1.2
node    470          0.4            1            1
node    471            0            1          1.4
node    472          0.2          0.6            1
node    473            0          0.6          1.2
node    474          0.6            0          0.6
node    475            1            1          0.6
node    476            1            0          0.4
node    477            2            1          0.4
node    478          0.6            1          0.8
node    479          1.8            1          0.4
node    480            2            0          0.2
node    481          1.8            0          0.2
node    482            2          0.2          0.2
node    483          0.2          0.8            1
node    484            0          0.8          1.2
node    485          1.6            1          0.4
node    486            2          0.4          0.2
node    487          1.6            0          0.2
node    488            0            0            1
node    489            0          0.2            1
node    490          0.2            0          0.8
node    491          1.4            1          0.4
node    492            0          0.4            1
node    493          1.4            0          0.2
node    494          0.8            1          0.6
node    495            2          0.6          0.2
node    496          0.8            0          0.4
node    497            0            1          1.2
node    498          0.2            1            1
node    499          0.4            0          0.6
node    500            0          0.6            1
node    501          1.2            1          0.4
node    502          0.4            1          0.8
node    503            2          0.8          0.2
node    504          1.2            0          0.2
node    505            0          0.8            1
node    506          0.6            0          0.4
node    507          0.6            1          0.6
node    508            1            1          0.4
node    509            2            1          0.2
node    510            0            0          0.8
node    511            1            0          0.2
node    512          1.8            1          0.2
node    513            0          0.2          0.8
node    514          1.6            1          0.2
node    515            2            0            0
node    516            0          0.4          0.8
node    517            0            1            1
node    518          0.2            0          0.6
node    519          1.8            0            0
node    520            2          0.2            0
node    521          1.8          0.2            0
node    522          0.2            1          0.8
node    523          1.6            0            0
node    524            2          0.4            0
node    525            0          0.6          0.8
node    526          1.6          0.2            0
node    527          1.4            1          0.2
node    528          0.8            1          0.4
node    529          1.8          0.4            0
node    530          0.8            0          0.2
node    531          1.6          0.4            0
node    532          0.4            0          0.4
node    533          0.4            1          0.6
node    534          1.4            0            0
node    535            2          0.6            0
node    536          1.8          0.6            0
node    537          1.4          0.2            0
node    538          1.2            1          0.2
node    539            0          0.8          0.8
node    540          1.6          0.6            0
node    541          1.4          0.4            0
node    542            2          0.8            0
node    543          1.2            0            0
node    544          1.2          0.2            0
node    545          1.8          0.8            0
node    546          1.4          0.6            0
node    547          0.6            1          0.4
node    548            0            0          0.6
node    549          0.6            0          0.2
node    550            0          0.2          0.6
node    551          1.6          0.8            0
node    552          1.2          0.4            0
node    553            1            1          0.2
node    554            0            1          0.8
node    555            0          0.4          0.6
node    556          0.2            0          0.4
node    557            1            0            0
node    558          1.4          0.8            0
node    559          1.2          0.6            0
node    560            2            1            0
node    561          0.2            1          0.6
node    562          1.8            1            0
node    563            1          0.2            0
node    564            0          0.6          0.6
node    565            1          0.4            0
node    566          1.6            1            0
node    567          0.8            1          0.2
node    568          1.2          0.8            0
node    569          0.4            1          0.4
node    570            1          0.6            0
node    571          1.4            1            0
node    572          0.4            0          0.2
node    573            0          0.8          0.6
node    574          0.8            0            0
node    575          0.8          0.2            0
node    576          0.8          0.4            0
node    577            1          0.8            0
node    578          1.2            1            0
node    579            0            1          0.6
node    580            0            0          0.4
node    581          0.6            1          0.2
node    582          0.8          0.6            0
node    583            0          0.2          0.4
node    584            0          0.4          0.4
node    585          0.6            0            0
node    586          0.6          0.2            0
node    587          0.2            1          0.4
node    588            1            1            0
node    589          0.2            0          0.2
node    590          0.8          0.8            0
node    591            0          0.6          0.4
node    592          0.6          0.4            0
node    593          0.6          0.6            0
node    594          0.4            1          0.2
node    595            0          0.8          0.4
node    596          0.8            1            0
node    597          0.4            0            0
node    598          0.6          0.8            0
node    599          0.4          0.2            0
node    600          0.4          0.4            0
node    601            0            1          0.4
node    602            0            0          0.2
node    603            0          0.2          0.2
node    604          0.4          0.6            0
node    605          0.6            1            0
node    606            0          0.4          0.2
node    607          0.2            1          0.2
node    608            0          0.6          0.2
node    609          0.4          0.8            0
node    610          0.2            0            0
node    611          0.2          0.2            0
node    612          0.2          0.4            0
node    613            0          0.8          0.2
node    614          0.4            1            0
node    615          0.2          0.6            0
node    616            0            1          0.2
node    617          0.2          0.8            0
node    618            0            0            0
node    619            0          0.2            0
node    620            0          0.4            0
node    621          0.2            1            0
node    622            0          0.6            0
node    623            0          0.8            0
node    624            0            1            0

# --------------------------------------------------------------------------------------------------------------
# R E S T R A I N T S
# --------------------------------------------------------------------------------------------------------------

# fix $NodeTag x-transl y-transl z-transl x-rot y-rot z-rot

fix    515   1   1   1   1   1   1
fix    519   1   1   1   1   1   1
fix    520   1   1   1   1   1   1
fix    523   1   1   1   1   1   1
fix    524   1   1   1   1   1   1
fix    534   1   1   1   1   1   1
fix    535   1   1   1   1   1   1
fix    542   1   1   1   1   1   1
fix    543   1   1   1   1   1   1
fix    557   1   1   1   1   1   1
fix    560   1   1   1   1   1   1
fix    562   1   1   1   1   1   1
fix    566   1   1   1   1   1   1
fix    571   1   1   1   1   1   1
fix    574   1   1   1   1   1   1
fix    578   1   1   1   1   1   1
fix    585   1   1   1   1   1   1
fix    588   1   1   1   1   1   1
fix    596   1   1   1   1   1   1
fix    597   1   1   1   1   1   1
fix    605   1   1   1   1   1   1
fix    610   1   1   1   1   1   1
fix    614   1   1   1   1   1   1
fix    618   1   1   1   1   1   1
fix    619   1   1   1   1   1   1
fix    620   1   1   1   1   1   1
fix    621   1   1   1   1   1   1
fix    622   1   1   1   1   1   1
fix    623   1   1   1   1   1   1
fix    624   1   1   1   1   1   1

# --------------------------------------------------------------------------------------------------------------
# S H E L L M I T C 4   E L E M E N T S
# --------------------------------------------------------------------------------------------------------------

# Materials/Sections Definition used by shell elements

nDMaterial ElasticIsotropic 127 2e+08 0.15         7.85
section PlateFiber 137 127 0.01

# ShellMITC4 Elements Definition: element ShellMITC4 $eleTag $iNode $jNode $kNode $lNode $secTag

element ShellMITC4      1    619   603   602   618    137
element ShellMITC4      2    620   606   603   619    137
element ShellMITC4      3    622   608   606   620    137
element ShellMITC4      4    623   613   608   622    137
element ShellMITC4      5    624   616   613   623    137
element ShellMITC4      6    603   583   580   602    137
element ShellMITC4      7    606   584   583   603    137
element ShellMITC4      8    608   591   584   606    137
element ShellMITC4      9    613   595   591   608    137
element ShellMITC4     10    616   601   595   613    137
element ShellMITC4     11    583   550   548   580    137
element ShellMITC4     12    584   555   550   583    137
element ShellMITC4     13    591   564   555   584    137
element ShellMITC4     14    595   573   564   591    137
element ShellMITC4     15    601   579   573   595    137
element ShellMITC4     16    550   513   510   548    137
element ShellMITC4     17    555   516   513   550    137
element ShellMITC4     18    564   525   516   555    137
element ShellMITC4     19    573   539   525   564    137
element ShellMITC4     20    579   554   539   573    137
element ShellMITC4     21    513   489   488   510    137
element ShellMITC4     22    516   492   489   513    137
element ShellMITC4     23    525   500   492   516    137
element ShellMITC4     24    539   505   500   525    137
element ShellMITC4     25    554   517   505   539    137
element ShellMITC4     26    621   607   616   624    137
element ShellMITC4     27    614   594   607   621    137
element ShellMITC4     28    605   581   594   614    137
element ShellMITC4     29    596   567   581   605    137
element ShellMITC4     30    588   553   567   596    137
element ShellMITC4     31    578   538   553   588    137
element ShellMITC4     32    571   527   538   578    137
element ShellMITC4     33    566   514   527   571    137
element ShellMITC4     34    562   512   514   566    137
element ShellMITC4     35    560   509   512   562    137
element ShellMITC4     36    607   587   601   616    137
element ShellMITC4     37    594   569   587   607    137
element ShellMITC4     38    581   547   569   594    137
element ShellMITC4     39    567   528   547   581    137
element ShellMITC4     40    553   508   528   567    137
element ShellMITC4     41    538   501   508   553    137
element ShellMITC4     42    527   491   501   538    137
element ShellMITC4     43    514   485   491   527    137
element ShellMITC4     44    512   479   485   514    137
element ShellMITC4     45    509   477   479   512    137
element ShellMITC4     46    587   561   579   601    137
element ShellMITC4     47    569   533   561   587    137
element ShellMITC4     48    547   507   533   569    137
element ShellMITC4     49    528   494   507   547    137
element ShellMITC4     50    508   475   494   528    137
element ShellMITC4     51    501   468   475   508    137
element ShellMITC4     52    491   452   468   501    137
element ShellMITC4     53    485   449   452   491    137
element ShellMITC4     54    479   443   449   485    137
element ShellMITC4     55    477   436   443   479    137
element ShellMITC4     56    561   522   554   579    137
element ShellMITC4     57    533   502   522   561    137
element ShellMITC4     58    507   478   502   533    137
element ShellMITC4     59    494   460   478   507    137
element ShellMITC4     60    475   444   460   494    137
element ShellMITC4     61    468   425   444   475    137
element ShellMITC4     62    452   417   425   468    137
element ShellMITC4     63    449   403   417   452    137
element ShellMITC4     64    443   398   403   449    137
element ShellMITC4     65    436   396   398   443    137
element ShellMITC4     66    522   498   517   554    137
element ShellMITC4     67    502   470   498   522    137
element ShellMITC4     68    478   450   470   502    137
element ShellMITC4     69    460   423   450   478    137
element ShellMITC4     70    444   405   423   460    137
element ShellMITC4     71    425   386   405   444    137
element ShellMITC4     72    417   369   386   425    137
element ShellMITC4     73    403   358   369   417    137
element ShellMITC4     74    398   353   358   403    137
element ShellMITC4     75    396   345   353   398    137
element ShellMITC4     76    542   503   509   560    137
element ShellMITC4     77    535   495   503   542    137
element ShellMITC4     78    524   486   495   535    137
element ShellMITC4     79    520   482   486   524    137
element ShellMITC4     80    515   480   482   520    137
element ShellMITC4     81    503   467   477   509    137
element ShellMITC4     82    495   453   467   503    137
element ShellMITC4     83    486   447   453   495    137
element ShellMITC4     84    482   441   447   486    137
element ShellMITC4     85    480   437   441   482    137
element ShellMITC4     86    467   422   436   477    137
element ShellMITC4     87    453   412   422   467    137
element ShellMITC4     88    447   400   412   453    137
element ShellMITC4     89    441   393   400   447    137
element ShellMITC4     90    437   389   393   441    137
element ShellMITC4     91    422   376   396   436    137
element ShellMITC4     92    412   361   376   422    137
element ShellMITC4     93    400   348   361   412    137
element ShellMITC4     94    393   334   348   400    137
element ShellMITC4     95    389   333   334   393    137
element ShellMITC4     96    376   320   345   396    137
element ShellMITC4     97    361   293   320   376    137
element ShellMITC4     98    348   274   293   361    137
element ShellMITC4     99    334   268   274   348    137
element ShellMITC4    100    333   265   268   334    137
element ShellMITC4    101    519   481   480   515    137
element ShellMITC4    102    523   487   481   519    137
element ShellMITC4    103    534   493   487   523    137
element ShellMITC4    104    543   504   493   534    137
element ShellMITC4    105    557   511   504   543    137
element ShellMITC4    106    574   530   511   557    137
element ShellMITC4    107    585   549   530   574    137
element ShellMITC4    108    597   572   549   585    137
element ShellMITC4    109    610   589   572   597    137
element ShellMITC4    110    618   602   589   610    137
element ShellMITC4    111    481   442   437   480    137
element ShellMITC4    112    487   448   442   481    137
element ShellMITC4    113    493   454   448   487    137
element ShellMITC4    114    504   464   454   493    137
element ShellMITC4    115    511   476   464   504    137
element ShellMITC4    116    530   496   476   511    137
element ShellMITC4    117    549   506   496   530    137
element ShellMITC4    118    572   532   506   549    137
element ShellMITC4    119    589   556   532   572    137
element ShellMITC4    120    602   580   556   589    137
element ShellMITC4    121    442   394   389   437    137
element ShellMITC4    122    448   399   394   442    137
element ShellMITC4    123    454   414   399   448    137
element ShellMITC4    124    464   421   414   454    137
element ShellMITC4    125    476   435   421   464    137
element ShellMITC4    126    496   457   435   476    137
element ShellMITC4    127    506   474   457   496    137
element ShellMITC4    128    532   499   474   506    137
element ShellMITC4    129    556   518   499   532    137
element ShellMITC4    130    580   548   518   556    137
element ShellMITC4    131    394   336   333   389    137
element ShellMITC4    132    399   349   336   394    137
element ShellMITC4    133    414   364   349   399    137
element ShellMITC4    134    421   375   364   414    137
element ShellMITC4    135    435   397   375   421    137
element ShellMITC4    136    457   418   397   435    137
element ShellMITC4    137    474   440   418   457    137
element ShellMITC4    138    499   463   440   474    137
element ShellMITC4    139    518   490   463   499    137
element ShellMITC4    140    548   510   490   518    137
element ShellMITC4    141    336   270   265   333    137
element ShellMITC4    142    349   273   270   336    137
element ShellMITC4    143    364   294   273   349    137
element ShellMITC4    144    375   318   294   364    137
element ShellMITC4    145    397   346   318   375    137
element ShellMITC4    146    418   374   346   397    137
element ShellMITC4    147    440   401   374   418    137
element ShellMITC4    148    463   427   401   440    137
element ShellMITC4    149    490   459   427   463    137
element ShellMITC4    150    510   488   459   490    137
element ShellMITC4    151    489   462   458   488    137
element ShellMITC4    152    492   466   462   489    137
element ShellMITC4    153    500   473   466   492    137
element ShellMITC4    154    505   484   473   500    137
element ShellMITC4    155    517   497   484   505    137
element ShellMITC4    156    462   430   428   458    137
element ShellMITC4    157    466   434   430   462    137
element ShellMITC4    158    473   446   434   466    137
element ShellMITC4    159    484   456   446   473    137
element ShellMITC4    160    497   471   456   484    137
element ShellMITC4    161    430   404   402   428    137
element ShellMITC4    162    434   410   404   430    137
element ShellMITC4    163    446   419   410   434    137
element ShellMITC4    164    456   431   419   446    137
element ShellMITC4    165    471   451   431   456    137
element ShellMITC4    166    404   378   373   402    137
element ShellMITC4    167    410   381   378   404    137
element ShellMITC4    168    419   390   381   410    137
element ShellMITC4    169    431   409   390   419    137
element ShellMITC4    170    451   424   409   431    137
element ShellMITC4    171    378   354   344   373    137
element ShellMITC4    172    381   357   354   378    137
element ShellMITC4    173    390   371   357   381    137
element ShellMITC4    174    409   385   371   390    137
element ShellMITC4    175    424   406   385   409    137
element ShellMITC4    176    498   469   497   517    137
element ShellMITC4    177    470   439   469   498    137
element ShellMITC4    178    450   416   439   470    137
element ShellMITC4    179    423   387   416   450    137
element ShellMITC4    180    405   366   387   423    137
element ShellMITC4    181    386   337   366   405    137
element ShellMITC4    182    369   315   337   386    137
element ShellMITC4    183    358   305   315   369    137
element ShellMITC4    184    353   290   305   358    137
element ShellMITC4    185    345   284   290   353    137
element ShellMITC4    186    469   438   471   497    137
element ShellMITC4    187    439   413   438   469    137
element ShellMITC4    188    416   380   413   439    137
element ShellMITC4    189    387   343   380   416    137
element ShellMITC4    190    366   312   343   387    137
element ShellMITC4    191    337   283   312   366    137
element ShellMITC4    192    315   260   283   337    137
element ShellMITC4    193    305   250   260   315    137
element ShellMITC4    194    290   244   250   305    137
element ShellMITC4    195    284   238   244   290    137
element ShellMITC4    196    438   415   451   471    137
element ShellMITC4    197    413   379   415   438    137
element ShellMITC4    198    380   339   379   413    137
element ShellMITC4    199    343   301   339   380    137
element ShellMITC4    200    312   262   301   343    137
element ShellMITC4    201    283   240   262   312    137
element ShellMITC4    202    260   224   240   283    137
element ShellMITC4    203    250   211   224   260    137
element ShellMITC4    204    244   204   211   250    137
element ShellMITC4    205    238   200   204   244    137
element ShellMITC4    206    415   388   424   451    137
element ShellMITC4    207    379   347   388   415    137
element ShellMITC4    208    339   299   347   379    137
element ShellMITC4    209    301   252   299   339    137
element ShellMITC4    210    262   234   252   301    137
element ShellMITC4    211    240   208   234   262    137
element ShellMITC4    212    224   193   208   240    137
element ShellMITC4    213    211   174   193   224    137
element ShellMITC4    214    204   169   174   211    137
element ShellMITC4    215    200   166   169   204    137
element ShellMITC4    216    388   365   406   424    137
element ShellMITC4    217    347   313   365   388    137
element ShellMITC4    218    299   261   313   347    137
element ShellMITC4    219    252   233   261   299    137
element ShellMITC4    220    234   205   233   252    137
element ShellMITC4    221    208   186   205   234    137
element ShellMITC4    222    193   162   186   208    137
element ShellMITC4    223    174   154   162   193    137
element ShellMITC4    224    169   143   154   174    137
element ShellMITC4    225    166   136   143   169    137
element ShellMITC4    226    320   254   284   345    137
element ShellMITC4    227    293   242   254   320    137
element ShellMITC4    228    274   230   242   293    137
element ShellMITC4    229    268   223   230   274    137
element ShellMITC4    230    265   218   223   268    137
element ShellMITC4    231    254   217   238   284    137
element ShellMITC4    232    242   197   217   254    137
element ShellMITC4    233    230   191   197   242    137
element ShellMITC4    234    223   182   191   230    137
element ShellMITC4    235    218   173   182   223    137
element ShellMITC4    236    217   175   200   238    137
element ShellMITC4    237    197   160   175   217    137
element ShellMITC4    238    191   150   160   197    137
element ShellMITC4    239    182   133   150   191    137
element ShellMITC4    240    173   130   133   182    137
element ShellMITC4    241    175   147   166   200    137
element ShellMITC4    242    160   122   147   175    137
element ShellMITC4    243    150   106   122   160    137
element ShellMITC4    244    133    97   106   150    137
element ShellMITC4    245    130    96    97   133    137
element ShellMITC4    246    147   113   136   166    137
element ShellMITC4    247    122    85   113   147    137
element ShellMITC4    248    106    74    85   122    137
element ShellMITC4    249     97    64    74   106    137
element ShellMITC4    250     96    57    64    97    137
element ShellMITC4    251    270   221   218   265    137
element ShellMITC4    252    273   231   221   270    137
element ShellMITC4    253    294   248   231   273    137
element ShellMITC4    254    318   256   248   294    137
element ShellMITC4    255    346   287   256   318    137
element ShellMITC4    256    374   324   287   346    137
element ShellMITC4    257    401   362   324   374    137
element ShellMITC4    258    427   392   362   401    137
element ShellMITC4    259    459   426   392   427    137
element ShellMITC4    260    488   458   426   459    137
element ShellMITC4    261    221   183   173   218    137
element ShellMITC4    262    231   189   183   221    137
element ShellMITC4    263    248   198   189   231    137
element ShellMITC4    264    256   216   198   248    137
element ShellMITC4    265    287   237   216   256    137
element ShellMITC4    266    324   264   237   287    137
element ShellMITC4    267    362   309   264   324    137
element ShellMITC4    268    392   356   309   362    137
element ShellMITC4    269    426   395   356   392    137
element ShellMITC4    270    458   428   395   426    137
element ShellMITC4    271    183   131   130   173    137
element ShellMITC4    272    189   149   131   183    137
element ShellMITC4    273    198   158   149   189    137
element ShellMITC4    274    216   177   158   198    137
element ShellMITC4    275    237   202   177   216    137
element ShellMITC4    276    264   228   202   237    137
element ShellMITC4    277    309   258   228   264    137
element ShellMITC4    278    356   308   258   309    137
element ShellMITC4    279    395   363   308   356    137
element ShellMITC4    280    428   402   363   395    137
element ShellMITC4    281    131    99    96   130    137
element ShellMITC4    282    149   107    99   131    137
element ShellMITC4    283    158   124   107   149    137
element ShellMITC4    284    177   145   124   158    137
element ShellMITC4    285    202   168   145   177    137
element ShellMITC4    286    228   195   168   202    137
element ShellMITC4    287    258   227   195   228    137
element ShellMITC4    288    308   263   227   258    137
element ShellMITC4    289    363   321   263   308    137
element ShellMITC4    290    402   373   321   363    137
element ShellMITC4    291     99    65    57    96    137
element ShellMITC4    292    107    71    65    99    137
element ShellMITC4    293    124    88    71   107    137
element ShellMITC4    294    145   112    88   124    137
element ShellMITC4    295    168   137   112   145    137
element ShellMITC4    296    195   165   137   168    137
element ShellMITC4    297    227   201   165   195    137
element ShellMITC4    298    263   235   201   227    137
element ShellMITC4    299    321   285   235   263    137
element ShellMITC4    300    373   344   285   321    137
element ShellMITC4    301    354   322   317   344    137
element ShellMITC4    302    357   329   322   354    137
element ShellMITC4    303    371   340   329   357    137
element ShellMITC4    304    385   367   340   371    137
element ShellMITC4    305    406   383   367   385    137
element ShellMITC4    306    322   297   296   317    137
element ShellMITC4    307    329   310   297   322    137
element ShellMITC4    308    340   327   310   329    137
element ShellMITC4    309    367   350   327   340    137
element ShellMITC4    310    383   372   350   367    137
element ShellMITC4    311    297   277   276   296    137
element ShellMITC4    312    310   292   277   297    137
element ShellMITC4    313    327   307   292   310    137
element ShellMITC4    314    350   332   307   327    137
element ShellMITC4    315    372   359   332   350    137
element ShellMITC4    316    277   271   269   276    137
element ShellMITC4    317    292   279   271   277    137
element ShellMITC4    318    307   298   279   292    137
element ShellMITC4    319    332   326   298   307    137
element ShellMITC4    320    359   352   326   332    137
element ShellMITC4    321    271   267   266   269    137
element ShellMITC4    322    279   275   267   271    137
element ShellMITC4    323    298   295   275   279    137
element ShellMITC4    324    326   319   295   298    137
element ShellMITC4    325    352   341   319   326    137
element ShellMITC4    326    365   335   383   406    137
element ShellMITC4    327    313   280   335   365    137
element ShellMITC4    328    261   241   280   313    137
element ShellMITC4    329    233   209   241   261    137
element ShellMITC4    330    205   185   209   233    137
element ShellMITC4    331    186   156   185   205    137
element ShellMITC4    332    162   132   156   186    137
element ShellMITC4    333    154   123   132   162    137
element ShellMITC4    334    143   115   123   154    137
element ShellMITC4    335    136   109   115   143    137
element ShellMITC4    336    335   316   372   383    137
element ShellMITC4    337    280   259   316   335    137
element ShellMITC4    338    241   226   259   280    137
element ShellMITC4    339    209   194   226   241    137
element ShellMITC4    340    185   163   194   209    137
element ShellMITC4    341    156   139   163   185    137
element ShellMITC4    342    132   120   139   156    137
element ShellMITC4    343    123   102   120   132    137
element ShellMITC4    344    115    93   102   123    137
element ShellMITC4    345    109    87    93   115    137
element ShellMITC4    346    316   303   359   372    137
element ShellMITC4    347    259   249   303   316    137
element ShellMITC4    348    226   213   249   259    137
element ShellMITC4    349    194   176   213   226    137
element ShellMITC4    350    163   153   176   194    137
element ShellMITC4    351    139   126   153   163    137
element ShellMITC4    352    120   103   126   139    137
element ShellMITC4    353    102    83   103   120    137
element ShellMITC4    354     93    76    83   102    137
element ShellMITC4    355     87    72    76    93    137
element ShellMITC4    356    303   289   352   359    137
element ShellMITC4    357    249   245   289   303    137
element ShellMITC4    358    213   207   245   249    137
element ShellMITC4    359    176   170   207   213    137
element ShellMITC4    360    153   142   170   176    137
element ShellMITC4    361    126   117   142   153    137
element ShellMITC4    362    103    94   117   126    137
element ShellMITC4    363     83    77    94   103    137
element ShellMITC4    364     76    69    77    83    137
element ShellMITC4    365     72    62    69    76    137
element ShellMITC4    366    289   286   341   352    137
element ShellMITC4    367    245   236   286   289    137
element ShellMITC4    368    207   203   236   245    137
element ShellMITC4    369    170   167   203   207    137
element ShellMITC4    370    142   138   167   170    137
element ShellMITC4    371    117   111   138   142    137
element ShellMITC4    372     94    89   111   117    137
element ShellMITC4    373     77    70    89    94    137
element ShellMITC4    374     69    63    70    77    137
element ShellMITC4    375     62    56    63    69    137
element ShellMITC4    376    113    81   109   136    137
element ShellMITC4    377     85    53    81   113    137
element ShellMITC4    378     74    49    53    85    137
element ShellMITC4    379     64    38    49    74    137
element ShellMITC4    380     57    35    38    64    137
element ShellMITC4    381     81    55    87   109    137
element ShellMITC4    382     53    45    55    81    137
element ShellMITC4    383     49    33    45    53    137
element ShellMITC4    384     38    25    33    49    137
element ShellMITC4    385     35    21    25    38    137
element ShellMITC4    386     55    48    72    87    137
element ShellMITC4    387     45    30    48    55    137
element ShellMITC4    388     33    18    30    45    137
element ShellMITC4    389     25    12    18    33    137
element ShellMITC4    390     21     9    12    25    137
element ShellMITC4    391     48    42    62    72    137
element ShellMITC4    392     30    27    42    48    137
element ShellMITC4    393     18    13    27    30    137
element ShellMITC4    394     12     5    13    18    137
element ShellMITC4    395      9     4     5    12    137
element ShellMITC4    396     42    37    56    62    137
element ShellMITC4    397     27    20    37    42    137
element ShellMITC4    398     13    10    20    27    137
element ShellMITC4    399      5     3    10    13    137
element ShellMITC4    400      4     1     3     5    137
element ShellMITC4    401     65    39    35    57    137
element ShellMITC4    402     71    47    39    65    137
element ShellMITC4    403     88    54    47    71    137
element ShellMITC4    404    112    80    54    88    137
element ShellMITC4    405    137   110    80   112    137
element ShellMITC4    406    165   146   110   137    137
element ShellMITC4    407    201   178   146   165    137
element ShellMITC4    408    235   214   178   201    137
element ShellMITC4    409    285   253   214   235    137
element ShellMITC4    410    344   317   253   285    137
element ShellMITC4    411     39    26    21    35    137
element ShellMITC4    412     47    31    26    39    137
element ShellMITC4    413     54    46    31    47    137
element ShellMITC4    414     80    60    46    54    137
element ShellMITC4    415    110    86    60    80    137
element ShellMITC4    416    146   125    86   110    137
element ShellMITC4    417    178   159   125   146    137
element ShellMITC4    418    214   199   159   178    137
element ShellMITC4    419    253   247   199   214    137
element ShellMITC4    420    317   296   247   253    137
element ShellMITC4    421     26    11     9    21    137
element ShellMITC4    422     31    17    11    26    137
element ShellMITC4    423     46    32    17    31    137
element ShellMITC4    424     60    50    32    46    137
element ShellMITC4    425     86    73    50    60    137
element ShellMITC4    426    125   105    73    86    137
element ShellMITC4    427    159   151   105   125    137
element ShellMITC4    428    199   188   151   159    137
element ShellMITC4    429    247   232   188   199    137
element ShellMITC4    430    296   276   232   247    137
element ShellMITC4    431     11     7     4     9    137
element ShellMITC4    432     17    15     7    11    137
element ShellMITC4    433     32    28    15    17    137
element ShellMITC4    434     50    41    28    32    137
element ShellMITC4    435     73    66    41    50    137
element ShellMITC4    436    105    98    66    73    137
element ShellMITC4    437    151   134    98   105    137
element ShellMITC4    438    188   179   134   151    137
element ShellMITC4    439    232   220   179   188    137
element ShellMITC4    440    276   269   220   232    137
element ShellMITC4    441      7     2     1     4    137
element ShellMITC4    442     15     8     2     7    137
element ShellMITC4    443     28    22     8    15    137
element ShellMITC4    444     41    36    22    28    137
element ShellMITC4    445     66    58    36    41    137
element ShellMITC4    446     98    95    58    66    137
element ShellMITC4    447    134   129    95    98    137
element ShellMITC4    448    179   172   129   134    137
element ShellMITC4    449    220   219   172   179    137
element ShellMITC4    450    269   266   219   220    137
element ShellMITC4    451    219   222   267   266    137
element ShellMITC4    452    172   180   222   219    137
element ShellMITC4    453    129   135   180   172    137
element ShellMITC4    454     95   100   135   129    137
element ShellMITC4    455     58    67   100    95    137
element ShellMITC4    456     36    43    67    58    137
element ShellMITC4    457     22    23    43    36    137
element ShellMITC4    458      8    14    23    22    137
element ShellMITC4    459      2     6    14     8    137
element ShellMITC4    460      1     3     6     2    137
element ShellMITC4    461    222   229   275   267    137
element ShellMITC4    462    180   190   229   222    137
element ShellMITC4    463    135   152   190   180    137
element ShellMITC4    464    100   108   152   135    137
element ShellMITC4    465     67    75   108   100    137
element ShellMITC4    466     43    52    75    67    137
element ShellMITC4    467     23    34    52    43    137
element ShellMITC4    468     14    19    34    23    137
element ShellMITC4    469      6    16    19    14    137
element ShellMITC4    470      3    10    16     6    137
element ShellMITC4    471    229   239   295   275    137
element ShellMITC4    472    190   196   239   229    137
element ShellMITC4    473    152   161   196   190    137
element ShellMITC4    474    108   121   161   152    137
element ShellMITC4    475     75    90   121   108    137
element ShellMITC4    476     52    59    90    75    137
element ShellMITC4    477     34    44    59    52    137
element ShellMITC4    478     19    29    44    34    137
element ShellMITC4    479     16    24    29    19    137
element ShellMITC4    480     10    20    24    16    137
element ShellMITC4    481    239   255   319   295    137
element ShellMITC4    482    196   215   255   239    137
element ShellMITC4    483    161   181   215   196    137
element ShellMITC4    484    121   148   181   161    137
element ShellMITC4    485     90   114   148   121    137
element ShellMITC4    486     59    82   114    90    137
element ShellMITC4    487     44    61    82    59    137
element ShellMITC4    488     29    51    61    44    137
element ShellMITC4    489     24    40    51    29    137
element ShellMITC4    490     20    37    40    24    137
element ShellMITC4    491    255   286   341   319    137
element ShellMITC4    492    215   236   286   255    137
element ShellMITC4    493    181   203   236   215    137
element ShellMITC4    494    148   167   203   181    137
element ShellMITC4    495    114   138   167   148    137
element ShellMITC4    496     82   111   138   114    137
element ShellMITC4    497     61    89   111    82    137
element ShellMITC4    498     51    70    89    61    137
element ShellMITC4    499     40    63    70    51    137
element ShellMITC4    500     37    56    63    40    137
element ShellMITC4    501    285   288   354   344    137
element ShellMITC4    502    235   243   288   285    137
element ShellMITC4    503    201   206   243   235    137
element ShellMITC4    504    165   171   206   201    137
element ShellMITC4    505    137   144   171   165    137
element ShellMITC4    506    112   118   144   137    137
element ShellMITC4    507     88    91   118   112    137
element ShellMITC4    508     71    78    91    88    137
element ShellMITC4    509     65    68    78    71    137
element ShellMITC4    510     57    64    68    65    137
element ShellMITC4    511    288   302   357   354    137
element ShellMITC4    512    243   251   302   288    137
element ShellMITC4    513    206   212   251   243    137
element ShellMITC4    514    171   184   212   206    137
element ShellMITC4    515    144   155   184   171    137
element ShellMITC4    516    118   128   155   144    137
element ShellMITC4    517     91   104   128   118    137
element ShellMITC4    518     78    84   104    91    137
element ShellMITC4    519     68    79    84    78    137
element ShellMITC4    520     64    74    79    68    137
element ShellMITC4    521    302   314   371   357    137
element ShellMITC4    522    251   257   314   302    137
element ShellMITC4    523    212   225   257   251    137
element ShellMITC4    524    184   192   225   212    137
element ShellMITC4    525    155   164   192   184    137
element ShellMITC4    526    128   140   164   155    137
element ShellMITC4    527    104   119   140   128    137
element ShellMITC4    528     84   101   119   104    137
element ShellMITC4    529     79    92   101    84    137
element ShellMITC4    530     74    85    92    79    137
element ShellMITC4    531    314   338   385   371    137
element ShellMITC4    532    257   278   338   314    137
element ShellMITC4    533    225   246   278   257    137
element ShellMITC4    534    192   210   246   225    137
element ShellMITC4    535    164   187   210   192    137
element ShellMITC4    536    140   157   187   164    137
element ShellMITC4    537    119   141   157   140    137
element ShellMITC4    538    101   127   141   119    137
element ShellMITC4    539     92   116   127   101    137
element ShellMITC4    540     85   113   116    92    137
element ShellMITC4    541    338   365   406   385    137
element ShellMITC4    542    278   313   365   338    137
element ShellMITC4    543    246   261   313   278    137
element ShellMITC4    544    210   233   261   246    137
element ShellMITC4    545    187   205   233   210    137
element ShellMITC4    546    157   186   205   187    137
element ShellMITC4    547    141   162   186   157    137
element ShellMITC4    548    127   154   162   141    137
element ShellMITC4    549    116   143   154   127    137
element ShellMITC4    550    113   136   143   116    137
element ShellMITC4    551    459   461   489   488    137
element ShellMITC4    552    427   432   461   459    137
element ShellMITC4    553    401   407   432   427    137
element ShellMITC4    554    374   377   407   401    137
element ShellMITC4    555    346   355   377   374    137
element ShellMITC4    556    318   325   355   346    137
element ShellMITC4    557    294   300   325   318    137
element ShellMITC4    558    273   281   300   294    137
element ShellMITC4    559    270   272   281   273    137
element ShellMITC4    560    265   268   272   270    137
element ShellMITC4    561    461   465   492   489    137
element ShellMITC4    562    432   433   465   461    137
element ShellMITC4    563    407   411   433   432    137
element ShellMITC4    564    377   382   411   407    137
element ShellMITC4    565    355   360   382   377    137
element ShellMITC4    566    325   331   360   355    137
element ShellMITC4    567    300   311   331   325    137
element ShellMITC4    568    281   291   311   300    137
element ShellMITC4    569    272   282   291   281    137
element ShellMITC4    570    268   274   282   272    137
element ShellMITC4    571    465   472   500   492    137
element ShellMITC4    572    433   445   472   465    137
element ShellMITC4    573    411   420   445   433    137
element ShellMITC4    574    382   391   420   411    137
element ShellMITC4    575    360   370   391   382    137
element ShellMITC4    576    331   342   370   360    137
element ShellMITC4    577    311   328   342   331    137
element ShellMITC4    578    291   306   328   311    137
element ShellMITC4    579    282   304   306   291    137
element ShellMITC4    580    274   293   304   282    137
element ShellMITC4    581    472   483   505   500    137
element ShellMITC4    582    445   455   483   472    137
element ShellMITC4    583    420   429   455   445    137
element ShellMITC4    584    391   408   429   420    137
element ShellMITC4    585    370   384   408   391    137
element ShellMITC4    586    342   368   384   370    137
element ShellMITC4    587    328   351   368   342    137
element ShellMITC4    588    306   330   351   328    137
element ShellMITC4    589    304   323   330   306    137
element ShellMITC4    590    293   320   323   304    137
element ShellMITC4    591    483   498   517   505    137
element ShellMITC4    592    455   470   498   483    137
element ShellMITC4    593    429   450   470   455    137
element ShellMITC4    594    408   423   450   429    137
element ShellMITC4    595    384   405   423   408    137
element ShellMITC4    596    368   386   405   384    137
element ShellMITC4    597    351   369   386   368    137
element ShellMITC4    598    330   358   369   351    137
element ShellMITC4    599    323   353   358   330    137
element ShellMITC4    600    320   345   353   323    137
element ShellMITC4    601    610   611   619   618    137
element ShellMITC4    602    597   599   611   610    137
element ShellMITC4    603    585   586   599   597    137
element ShellMITC4    604    574   575   586   585    137
element ShellMITC4    605    557   563   575   574    137
element ShellMITC4    606    543   544   563   557    137
element ShellMITC4    607    534   537   544   543    137
element ShellMITC4    608    523   526   537   534    137
element ShellMITC4    609    519   521   526   523    137
element ShellMITC4    610    515   520   521   519    137
element ShellMITC4    611    611   612   620   619    137
element ShellMITC4    612    599   600   612   611    137
element ShellMITC4    613    586   592   600   599    137
element ShellMITC4    614    575   576   592   586    137
element ShellMITC4    615    563   565   576   575    137
element ShellMITC4    616    544   552   565   563    137
element ShellMITC4    617    537   541   552   544    137
element ShellMITC4    618    526   531   541   537    137
element ShellMITC4    619    521   529   531   526    137
element ShellMITC4    620    520   524   529   521    137
element ShellMITC4    621    612   615   622   620    137
element ShellMITC4    622    600   604   615   612    137
element ShellMITC4    623    592   593   604   600    137
element ShellMITC4    624    576   582   593   592    137
element ShellMITC4    625    565   570   582   576    137
element ShellMITC4    626    552   559   570   565    137
element ShellMITC4    627    541   546   559   552    137
element ShellMITC4    628    531   540   546   541    137
element ShellMITC4    629    529   536   540   531    137
element ShellMITC4    630    524   535   536   529    137
element ShellMITC4    631    615   617   623   622    137
element ShellMITC4    632    604   609   617   615    137
element ShellMITC4    633    593   598   609   604    137
element ShellMITC4    634    582   590   598   593    137
element ShellMITC4    635    570   577   590   582    137
element ShellMITC4    636    559   568   577   570    137
element ShellMITC4    637    546   558   568   559    137
element ShellMITC4    638    540   551   558   546    137
element ShellMITC4    639    536   545   551   540    137
element ShellMITC4    640    535   542   545   536    137
element ShellMITC4    641    617   621   624   623    137
element ShellMITC4    642    609   614   621   617    137
element ShellMITC4    643    598   605   614   609    137
element ShellMITC4    644    590   596   605   598    137
element ShellMITC4    645    577   588   596   590    137
element ShellMITC4    646    568   578   588   577    137
element ShellMITC4    647    558   571   578   568    137
element ShellMITC4    648    551   566   571   558    137
element ShellMITC4    649    545   562   566   551    137
element ShellMITC4    650    542   560   562   545    137

# --------------------------------------------------------------------------------------------------------------
#
# D O M A I N  C O M M O N S
#
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
# R E C O R D E R S
# --------------------------------------------------------------------------------------------------------------

recorder Node -file Node_displacements.out -time -nodeRange 1 624 -dof 1 2 3 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 624 -dof 4 5 6 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 624 -dof 1 2 3 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 624 -dof 4 5 6 reaction
recorder Element -file ShellMITC4_force.out -time -ele 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647 648 649 650 forces
recorder Element -file ShellMITC4_stress.out -time -ele 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647 648 649 650 stresses


pattern Plain 100 Linear {
load    266       10        0        0        0        0        0
load    341       10        0        0        0        0        0
load    344       10        0        0        0        0        0
load    406       10        0        0        0        0        0
load    488       10        0        0        0        0        0
load    517       10        0        0        0        0        0
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