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
node      1           70            0
node      2         66.5            0
node      3      67.4625        3.325
node      4      63.9966        3.325
node      5           63            0
node      6       64.925         6.65
node      7        60.56        3.325
node      8         59.5            0
node      9      61.5225         6.65
node     10      62.3875        9.975
node     11      57.1495        3.325
node     12      58.1694         6.65
node     13           56            0
node     14      59.0745        9.975
node     15      54.8601         6.65
node     16      53.7617        3.325
node     17        59.85         13.3
node     18      55.8226        9.975
node     19         52.5            0
node     20      56.6492         13.3
node     21      51.5892         6.65
node     22      50.3935        3.325
node     23      52.6251        9.975
node     24      57.3125       16.625
node     25           49            0
node     26      53.5142         13.3
node     27      48.3512         6.65
node     28      49.4752        9.975
node     29      54.2435       16.625
node     30      47.0415        3.325
node     31      50.4377         13.3
node     32         45.5            0
node     33      51.2387       16.625
node     34       54.775        19.95
node     35       46.366        9.975
node     36      45.1406         6.65
node     37      47.4123         13.3
node     38      43.7026        3.325
node     39       51.854        19.95
node     40       48.291       16.625
node     41           42            0
node     42      43.2908        9.975
node     43      44.4308         13.3
node     44      41.9519         6.65
node     45      48.9906        19.95
node     46      52.2375       23.275
node     47      45.3933       16.625
node     48      40.3734        3.325
node     49      49.4776       23.275
node     50      46.1783        19.95
node     51      40.2427        9.975
node     52      41.4858         13.3
node     53         38.5            0
node     54      38.7796         6.65
node     55      42.5383       16.625
node     56      46.7644       23.275
node     57      37.0507        3.325
node     58      43.4108        19.95
node     59         49.7         26.6
node     60        38.57         13.3
node     61      37.2151        9.975
node     62      39.7191       16.625
node     63      44.0927       23.275
node     64           35            0
node     65      35.6183         6.65
node     66      47.1109         26.6
node     67      40.6816        19.95
node     68      33.7313        3.325
node     69      35.6761         13.3
node     70      44.5546         26.6
node     71      41.4575       23.275
node     72      36.9284       16.625
node     73       34.201        9.975
node     74      47.1625       29.925
node     75      37.9844        19.95
node     76      32.4625         6.65
node     77         31.5            0
node     78      42.0276         26.6
node     79      38.8534       23.275
node     80      44.7507       29.925
node     81      34.1591       16.625
node     82      32.7969         13.3
node     83      30.4118        3.325
node     84      35.3128        19.95
node     85      31.1938        9.975
node     86      39.5261         26.6
node     87      42.3558       29.925
node     88      36.2753       23.275
node     89      29.3067         6.65
node     90       44.625        33.25
node     91           28            0
node     92      31.4041       16.625
node     93       29.925         13.3
node     94      32.6604        19.95
node     95      37.0466         26.6
node     96       39.976       29.925
node     97      28.1865        9.975
node     98      27.0891        3.325
node     99       33.718       23.275
node    100      42.3937        33.25
node    101      37.6094       29.925
node    102      34.5854         26.6
node    103      26.1454         6.65
node    104      28.6563       16.625
node    105      40.1625        33.25
node    106      30.0207        19.95
node    107      27.0531         13.3
node    108      31.1762       23.275
node    109         24.5            0
node    110      35.2541       29.925
node    111      25.1724        9.975
node    112      42.0875       36.575
node    113      37.9312        33.25
node    114      32.1387         26.6
node    115      23.7599        3.325
node    116      27.3875        19.95
node    117      25.9084       16.625
node    118      40.0368       36.575
node    119      28.6449       23.275
node    120      22.9731         6.65
node    121      32.9082       29.925
node    122      24.1739         13.3
node    123         35.7        33.25
node    124      29.7031         26.6
node    125      37.9692       36.575
node    126      22.1448        9.975
node    127           21            0
node    128      33.4688        33.25
node    129      24.7543        19.95
node    130      30.5699       29.925
node    131      26.1188       23.275
node    132       20.421        3.325
node    133      23.1534       16.625
node    134      35.8865       36.575
node    135        39.55         39.9
node    136      27.2747         26.6
node    137        21.28         13.3
node    138      19.7844         6.65
node    139      31.2375        33.25
node    140      37.6766         39.9
node    141      28.2372       29.925
node    142      33.7906       36.575
node    143      19.0967        9.975
node    144      22.1146        19.95
node    145      23.5926       23.275
node    146      20.3841       16.625
node    147        24.85         26.6
node    148         17.5            0
node    149      35.7704         39.9
node    150      29.0062        33.25
node    151      31.6834       36.575
node    152       17.069        3.325
node    153      25.9083       29.925
node    154      18.3642         13.3
node    155      16.5738         6.65
node    156      33.8349         39.9
node    157      21.0613       23.275
node    158      19.4622        19.95
node    159      37.0125       43.225
node    160      22.4253         26.6
node    161      29.5668       36.575
node    162       26.775        33.25
node    163      16.0215        9.975
node    164      17.5934       16.625
node    165      31.8739         39.9
node    166      23.5813       29.925
node    167      35.3099       43.225
node    168           14            0
node    169      27.4426       36.575
node    170      15.4193         13.3
node    171      24.5438        33.25
node    172      13.7008        3.325
node    173      18.5195       23.275
node    174      33.5606       43.225
node    175      29.8909         39.9
node    176      19.9969         26.6
node    177      16.7906        19.95
node    178      13.3358         6.65
node    179      21.2542       29.925
node    180      14.7742       16.625
node    181      31.7698       43.225
node    182      25.3128       36.575
node    183      12.9123        9.975
node    184      27.8896         39.9
node    185      22.3125        33.25
node    186       34.475        46.55
node    187      17.5613         26.6
node    188      15.9622       23.275
node    189      29.9425       43.225
node    190      12.4377         13.3
node    191      18.9253       29.925
node    192      14.0934        19.95
node    193      23.1792       36.575
node    194      25.8738         39.9
node    195         10.5            0
node    196      32.9335        46.55
node    197       10.313        3.325
node    198      20.0813        33.25
node    199      28.0841       43.225
node    200      10.0649         6.65
node    201      11.9193       16.625
node    202      31.3344        46.55
node    203      15.1146         26.6
node    204      23.8469         39.9
node    205      9.76238        9.975
node    206      21.0437       36.575
node    207      13.3841       23.275
node    208      16.5926       29.925
node    209      26.1997       43.225
node    210      29.6842        46.55
node    211        17.85        33.25
node    212      11.3642        19.95
node    213      9.41233         13.3
node    214      21.8128         39.9
node    215      27.9892        46.55
node    216      31.9375       49.875
node    217      18.9083       36.575
node    218      24.2945       43.225
node    219            7            0
node    220      6.90246        3.325
node    221      9.02151       16.625
node    222      12.6534         26.6
node    223      14.2543       29.925
node    224      6.75559         6.65
node    225       30.544       49.875
node    226        10.78       23.275
node    227      15.6188        33.25
node    228      26.2559        46.55
node    229       19.775         39.9
node    230      6.56487        9.975
node    231      22.3738       43.225
node    232      29.0863       49.875
node    233      8.59672        19.95
node    234      16.7747       36.575
node    235      6.33578         13.3
node    236      24.4906        46.55
node    237      11.9084       29.925
node    238      10.1739         26.6
node    239      27.5715       49.875
node    240      13.3875        33.25
node    241      17.7372         39.9
node    242      20.4426       43.225
node    243      6.07381       16.625
node    244      8.14476       23.275
node    245      14.6449       36.575
node    246      22.6997        46.55
node    247          3.5            0
node    248      26.0068       49.875
node    249      3.46587        3.325
node    250         29.4         53.2
node    251      3.40246         6.65
node    252      18.5063       43.225
node    253      5.78444        19.95
node    254      15.7031         39.9
node    255      3.31301        9.975
node    256      9.55308       29.925
node    257      24.3992       49.875
node    258      11.1563        33.25
node    259      20.8896        46.55
node    260      28.1383         53.2
node    261      7.67241         26.6
node    262      3.20078         13.3
node    263      12.5207       36.575
node    264      26.8108         53.2
node    265      5.47314       23.275
node    266      22.7559       49.875
node    267      16.5699       43.225
node    268      3.06902       16.625
node    269      19.0668        46.55
node    270      13.6762         39.9
node    271      25.4248         53.2
node    272        8.925        33.25
node    273      7.18648       29.925
node    274      21.0841       49.875
node    275      10.4041       36.575
node    276      2.92099        19.95
node    277            0            0
node    278            0        3.325
node    279      5.14539         26.6
node    280      14.6387       43.225
node    281            0         6.65
node    282      23.9877         53.2
node    283      17.2375        46.55
node    284      11.6604         39.9
node    285            0        9.975
node    286      19.3909       49.875
node    287      26.8625       56.525
node    288      2.75995       23.275
node    289            0         13.3
node    290      22.5068         53.2
node    291      6.69375        33.25
node    292      8.29692       36.575
node    293      4.80669       29.925
node    294      15.4082        46.55
node    295       12.718       43.225
node    296       25.713       56.525
node    297            0       16.625
node    298      17.6834       49.875
node    299      20.9892         53.2
node    300      9.65912         39.9
node    301      2.58914         26.6
node    302      24.5024       56.525
node    303            0        19.95
node    304      13.5854        46.55
node    305      10.8128       43.225
node    306      23.2374       56.525
node    307      19.4425         53.2
node    308       4.4625        33.25
node    309      15.9688       49.875
node    310      6.20102       36.575
node    311            0       23.275
node    312      2.41182       29.925
node    313      7.67614         39.9
node    314      21.9248       56.525
node    315      17.8739         53.2
node    316      11.7753        46.55
node    317      14.2541       49.875
node    318       8.9284       43.225
node    319            0         26.6
node    320      20.5715       56.525
node    321       24.325        59.85
node    322      4.11831       36.575
node    323      2.23125        33.25
node    324      16.2906         53.2
node    325      5.71509         39.9
node    326       23.265        59.85
node    327      9.98441        46.55
node    328      19.1842       56.525
node    329      12.5466       49.875
node    330            0       29.925
node    331      7.06999       43.225
node    332      22.1556        59.85
node    333         14.7         53.2
node    334      17.7698       56.525
node    335      2.05068       36.575
node    336      3.77961         39.9
node    337      21.0024        59.85
node    338      8.21909        46.55
node    339      10.8534       49.875
node    340            0        33.25
node    341      5.24274       43.225
node    342      13.1094         53.2
node    343      16.3349       56.525
node    344      19.8108        59.85
node    345      9.18159       49.875
node    346      6.48575        46.55
node    347      18.5863        59.85
node    348      14.8865       56.525
node    349      1.87336         39.9
node    350            0       36.575
node    351      11.5261         53.2
node    352      3.45186       43.225
node    353      21.7875       63.175
node    354      17.3344        59.85
node    355      7.53833       49.875
node    356      13.4313       56.525
node    357      20.7909       63.175
node    358      4.79078        46.55
node    359      9.95749         53.2
node    360      16.0606        59.85
node    361            0         39.9
node    362       19.765       63.175
node    363      1.70255       43.225
node    364       11.976       56.525
node    365      5.93075       49.875
node    366       18.713       63.175
node    367      8.41075         53.2
node    368      14.7704        59.85
node    369      3.14056        46.55
node    370      10.5276       56.525
node    371      17.6383       63.175
node    372            0       43.225
node    373      13.4692        59.85
node    374      4.36599       49.875
node    375      6.89325         53.2
node    376       16.544       63.175
node    377      1.54151        46.55
node    378      9.09274       56.525
node    379      12.1625        59.85
node    380      15.4335       63.175
node    381      2.85119       49.875
node    382        19.25         66.5
node    383      5.41229         53.2
node    384            0        46.55
node    385      7.67828       56.525
node    386      10.8558        59.85
node    387      14.3099       63.175
node    388      18.2875         66.5
node    389      3.97517         53.2
node    390      1.39348       49.875
node    391       17.325         66.5
node    392      13.1766       63.175
node    393      9.55461        59.85
node    394      6.29099       56.525
node    395      16.3625         66.5
node    396      12.0368       63.175
node    397      2.58922         53.2
node    398            0       49.875
node    399      8.26436        59.85
node    400         15.4         66.5
node    401      4.93767       56.525
node    402      10.8937       63.175
node    403      14.4375         66.5
node    404       18.805        70.15
node    405      6.99056        59.85
node    406      1.26172         53.2
node    407      3.62512       56.525
node    408       13.475         66.5
node    409      9.75068       63.175
node    410      17.8511        70.15
node    411      5.73869        59.85
node    412      12.5125         66.5
node    413            0         53.2
node    414      16.9014        70.15
node    415      8.61086       63.175
node    416      2.36013       56.525
node    417        11.55         66.5
node    418      15.9557        70.15
node    419      4.51422        59.85
node    420      7.47755       63.175
node    421      1.14949       56.525
node    422      15.0132        70.15
node    423      10.5875         66.5
node    424      3.32263        59.85
node    425      6.35401       63.175
node    426      14.0737        70.15
node    427        9.625         66.5
node    428            0       56.525
node    429        18.36         73.8
node    430      13.1366        70.15
node    431      2.16941        59.85
node    432      5.24348       63.175
node    433       8.6625         66.5
node    434      17.4237         73.8
node    435      12.2014        70.15
node    436          7.7         66.5
node    437      16.4932         73.8
node    438      4.14922       63.175
node    439      1.06004        59.85
node    440      11.2676        70.15
node    441      15.5679         73.8
node    442       6.7375         66.5
node    443      3.07449       63.175
node    444      10.3348        70.15
node    445            0        59.85
node    446       14.647         73.8
node    447        5.775         66.5
node    448       9.4025        70.15
node    449      2.02254       63.175
node    450      13.7299         73.8
node    451       4.8125         66.5
node    452      8.47018        70.15
node    453       17.915        77.45
node    454      12.8161         73.8
node    455     0.996626       63.175
node    456         3.85         66.5
node    457      17.0033        77.45
node    458      11.9048         73.8
node    459      7.53738        70.15
node    460            0       63.175
node    461      16.0966        77.45
node    462       2.8875         66.5
node    463      10.9955         73.8
node    464      6.60362        70.15
node    465      15.1944        77.45
node    466      10.0874         73.8
node    467        1.925         66.5
node    468      5.66841        70.15
node    469      14.2961        77.45
node    470         9.18         73.8
node    471      4.73129        70.15
node    472       0.9625         66.5
node    473      13.4012        77.45
node    474      8.27257         73.8
node    475      12.5091        77.45
node    476      3.79176        70.15
node    477            0         66.5
node    478        17.47         81.1
node    479      7.36451         73.8
node    480      11.6192        77.45
node    481      16.5874         81.1
node    482      2.84935        70.15
node    483      6.45516         73.8
node    484      10.7311        77.45
node    485      15.7076         81.1
node    486      1.90357        70.15
node    487      5.54388         73.8
node    488        9.844        77.45
node    489      14.8304         81.1
node    490     0.953947        70.15
node    491      13.9555         81.1
node    492      4.63005         73.8
node    493       8.9575        77.45
node    494      13.0825         81.1
node    495            0        70.15
node    496        8.071        77.45
node    497      3.71301         73.8
node    498      12.2111         81.1
node    499      7.18394        77.45
node    500      2.79213         73.8
node    501       17.025        84.75
node    502      11.3409         81.1
node    503      6.29576        77.45
node    504      16.1737        84.75
node    505      1.86676         73.8
node    506      10.4717         81.1
node    507       5.4059        77.45
node    508      15.3225        84.75
node    509     0.936263         73.8
node    510      9.60321         81.1
node    511      14.4713        84.75
node    512      4.51379        77.45
node    513        8.735         81.1
node    514            0         73.8
node    515        13.62        84.75
node    516      3.61888        77.45
node    517      7.86679         81.1
node    518      12.7688        84.75
node    519      2.72061        77.45
node    520      6.99825         81.1
node    521      11.9175        84.75
node    522      1.81841        77.45
node    523      11.0663        84.75
node    524      6.12908         81.1
node    525        16.58         88.4
node    526      15.7601         88.4
node    527       10.215        84.75
node    528      5.25894         81.1
node    529      0.91173        77.45
node    530      14.9374         88.4
node    531      9.36375        84.75
node    532      4.38753         81.1
node    533            0        77.45
node    534      14.1121         88.4
node    535       8.5125        84.75
node    536      3.51451         81.1
node    537      13.2845         88.4
node    538      7.66125        84.75
node    539      2.63956         81.1
node    540       12.455         88.4
node    541         6.81        84.75
node    542      11.6239         88.4
node    543      1.76238         81.1
node    544      5.95875        84.75
node    545      10.7916         88.4
node    546     0.882631         81.1
node    547       16.135        92.05
node    548       5.1075        84.75
node    549      9.95825         88.4
node    550      15.3442        92.05
node    551            0         81.1
node    552      4.25625        84.75
node    553      9.12429         88.4
node    554      14.5484        92.05
node    555        3.405        84.75
node    556         8.29         88.4
node    557      13.7481        92.05
node    558      7.45571         88.4
node    559      12.9439        92.05
node    560      2.55375        84.75
node    561      12.1363        92.05
node    562      6.62175         88.4
node    563       1.7025        84.75
node    564      11.3259        92.05
node    565      5.78842         88.4
node    566      0.85125        84.75
node    567      10.5133        92.05
node    568      4.95606         88.4
node    569            0        84.75
node    570        15.69         95.7
node    571      9.69894        92.05
node    572      4.12497         88.4
node    573      14.9238         95.7
node    574       8.8835        92.05
node    575      3.29549         88.4
node    576      14.1518         95.7
node    577       8.0675        92.05
node    578      13.3746         95.7
node    579      2.46794         88.4
node    580       7.2515        92.05
node    581       12.593         95.7
node    582      1.64262         88.4
node    583      6.43606        92.05
node    584      11.8075         95.7
node    585     0.819869         88.4
node    586      5.62174        92.05
node    587      11.0189         95.7
node    588            0         88.4
node    589       4.8091        92.05
node    590      10.2277         95.7
node    591      9.43451         95.7
node    592      3.99871        92.05
node    593       15.245        99.35
node    594      8.64007         95.7
node    595      3.19112        92.05
node    596      14.4964        99.35
node    597        7.845         95.7
node    598      13.7436        99.35
node    599      2.38689        92.05
node    600      12.9868        99.35
node    601      7.04993         95.7
node    602      1.58659        92.05
node    603      12.2268        99.35
node    604      6.25549         95.7
node    605      0.79077        92.05
node    606      11.4638        99.35
node    607      5.46234         95.7
node    608            0        92.05
node    609      10.6984        99.35
node    610      4.67112         95.7
node    611      9.93112        99.35
node    612      3.88245         95.7
node    613      9.16238        99.35
node    614      3.09699         95.7
node    615         14.8          103
node    616      8.39268        99.35
node    617        14.06          103
node    618      2.31537         95.7
node    619       7.6225        99.35
node    620        13.32          103
node    621      1.53824         95.7
node    622      6.85232        99.35
node    623        12.58          103
node    624     0.766237         95.7
node    625      6.08262        99.35
node    626        11.84          103
node    627      5.31388        99.35
node    628            0         95.7
node    629         11.1          103
node    630      4.54659        99.35
node    631        10.36          103
node    632         9.62          103
node    633      3.78121        99.35
node    634         8.88          103
node    635      3.01824        99.35
node    636         8.14          103
node    637      2.25815        99.35
node    638          7.4          103
node    639      1.50143        99.35
node    640         6.66          103
node    641     0.748553        99.35
node    642         5.92          103
node    643            0        99.35
node    644         5.18          103
node    645         4.44          103
node    646          3.7          103
node    647         2.96          103
node    648         2.22          103
node    649         1.48          103
node    650         0.74          103
node    651            0          103

# R E S T R A I N T S
# fix $NodeTag x-transl y-transl
fix      1   1   1
fix      2   1   1
fix      5   1   1
fix      8   1   1
fix     13   1   1
fix     19   1   1
fix     25   1   1
fix     32   1   1
fix     41   1   1
fix     53   1   1
fix     64   1   1
fix     77   1   1
fix     91   1   1
fix    109   1   1
fix    127   1   1
fix    148   1   1
fix    168   1   1
fix    195   1   1
fix    219   1   1
fix    247   1   1
fix    277   1   1

# Q U A D   E L E M E N T S
# nDMaterial Definition used by Quad Elements
# (ïnly if they have not already been defined on this model domain)
nDMaterial ElasticIsotropic 127 3.1027e+07 0.15        2.643
# Quad elements Definition : element quad $EleTag $Nodei $Nodej Nodek $Nodel $thick $type $MatTag
element quad      1    247   249   278   277        1  PlaneStrain 127        0        0        0        0
element quad      2    219   220   249   247        1  PlaneStrain 127        0        0        0        0
element quad      3    195   197   220   219        1  PlaneStrain 127        0        0        0        0
element quad      4    168   172   197   195        1  PlaneStrain 127        0        0        0        0
element quad      5    148   152   172   168        1  PlaneStrain 127        0        0        0        0
element quad      6    127   132   152   148        1  PlaneStrain 127        0        0        0        0
element quad      7    109   115   132   127        1  PlaneStrain 127        0        0        0        0
element quad      8     91    98   115   109        1  PlaneStrain 127        0        0        0        0
element quad      9     77    83    98    91        1  PlaneStrain 127        0        0        0        0
element quad     10     64    68    83    77        1  PlaneStrain 127        0        0        0        0
element quad     11     53    57    68    64        1  PlaneStrain 127        0        0        0        0
element quad     12     41    48    57    53        1  PlaneStrain 127        0        0        0        0
element quad     13     32    38    48    41        1  PlaneStrain 127        0        0        0        0
element quad     14     25    30    38    32        1  PlaneStrain 127        0        0        0        0
element quad     15     19    22    30    25        1  PlaneStrain 127        0        0        0        0
element quad     16     13    16    22    19        1  PlaneStrain 127        0        0        0        0
element quad     17      8    11    16    13        1  PlaneStrain 127        0        0        0        0
element quad     18      5     7    11     8        1  PlaneStrain 127        0        0        0        0
element quad     19      2     4     7     5        1  PlaneStrain 127        0        0        0        0
element quad     20      1     3     4     2        1  PlaneStrain 127        0        0        0        0
element quad     21    249   251   281   278        1  PlaneStrain 127        0        0        0        0
element quad     22    220   224   251   249        1  PlaneStrain 127        0        0        0        0
element quad     23    197   200   224   220        1  PlaneStrain 127        0        0        0        0
element quad     24    172   178   200   197        1  PlaneStrain 127        0        0        0        0
element quad     25    152   155   178   172        1  PlaneStrain 127        0        0        0        0
element quad     26    132   138   155   152        1  PlaneStrain 127        0        0        0        0
element quad     27    115   120   138   132        1  PlaneStrain 127        0        0        0        0
element quad     28     98   103   120   115        1  PlaneStrain 127        0        0        0        0
element quad     29     83    89   103    98        1  PlaneStrain 127        0        0        0        0
element quad     30     68    76    89    83        1  PlaneStrain 127        0        0        0        0
element quad     31     57    65    76    68        1  PlaneStrain 127        0        0        0        0
element quad     32     48    54    65    57        1  PlaneStrain 127        0        0        0        0
element quad     33     38    44    54    48        1  PlaneStrain 127        0        0        0        0
element quad     34     30    36    44    38        1  PlaneStrain 127        0        0        0        0
element quad     35     22    27    36    30        1  PlaneStrain 127        0        0        0        0
element quad     36     16    21    27    22        1  PlaneStrain 127        0        0        0        0
element quad     37     11    15    21    16        1  PlaneStrain 127        0        0        0        0
element quad     38      7    12    15    11        1  PlaneStrain 127        0        0        0        0
element quad     39      4     9    12     7        1  PlaneStrain 127        0        0        0        0
element quad     40      3     6     9     4        1  PlaneStrain 127        0        0        0        0
element quad     41    251   255   285   281        1  PlaneStrain 127        0        0        0        0
element quad     42    224   230   255   251        1  PlaneStrain 127        0        0        0        0
element quad     43    200   205   230   224        1  PlaneStrain 127        0        0        0        0
element quad     44    178   183   205   200        1  PlaneStrain 127        0        0        0        0
element quad     45    155   163   183   178        1  PlaneStrain 127        0        0        0        0
element quad     46    138   143   163   155        1  PlaneStrain 127        0        0        0        0
element quad     47    120   126   143   138        1  PlaneStrain 127        0        0        0        0
element quad     48    103   111   126   120        1  PlaneStrain 127        0        0        0        0
element quad     49     89    97   111   103        1  PlaneStrain 127        0        0        0        0
element quad     50     76    85    97    89        1  PlaneStrain 127        0        0        0        0
element quad     51     65    73    85    76        1  PlaneStrain 127        0        0        0        0
element quad     52     54    61    73    65        1  PlaneStrain 127        0        0        0        0
element quad     53     44    51    61    54        1  PlaneStrain 127        0        0        0        0
element quad     54     36    42    51    44        1  PlaneStrain 127        0        0        0        0
element quad     55     27    35    42    36        1  PlaneStrain 127        0        0        0        0
element quad     56     21    28    35    27        1  PlaneStrain 127        0        0        0        0
element quad     57     15    23    28    21        1  PlaneStrain 127        0        0        0        0
element quad     58     12    18    23    15        1  PlaneStrain 127        0        0        0        0
element quad     59      9    14    18    12        1  PlaneStrain 127        0        0        0        0
element quad     60      6    10    14     9        1  PlaneStrain 127        0        0        0        0
element quad     61    255   262   289   285        1  PlaneStrain 127        0        0        0        0
element quad     62    230   235   262   255        1  PlaneStrain 127        0        0        0        0
element quad     63    205   213   235   230        1  PlaneStrain 127        0        0        0        0
element quad     64    183   190   213   205        1  PlaneStrain 127        0        0        0        0
element quad     65    163   170   190   183        1  PlaneStrain 127        0        0        0        0
element quad     66    143   154   170   163        1  PlaneStrain 127        0        0        0        0
element quad     67    126   137   154   143        1  PlaneStrain 127        0        0        0        0
element quad     68    111   122   137   126        1  PlaneStrain 127        0        0        0        0
element quad     69     97   107   122   111        1  PlaneStrain 127        0        0        0        0
element quad     70     85    93   107    97        1  PlaneStrain 127        0        0        0        0
element quad     71     73    82    93    85        1  PlaneStrain 127        0        0        0        0
element quad     72     61    69    82    73        1  PlaneStrain 127        0        0        0        0
element quad     73     51    60    69    61        1  PlaneStrain 127        0        0        0        0
element quad     74     42    52    60    51        1  PlaneStrain 127        0        0        0        0
element quad     75     35    43    52    42        1  PlaneStrain 127        0        0        0        0
element quad     76     28    37    43    35        1  PlaneStrain 127        0        0        0        0
element quad     77     23    31    37    28        1  PlaneStrain 127        0        0        0        0
element quad     78     18    26    31    23        1  PlaneStrain 127        0        0        0        0
element quad     79     14    20    26    18        1  PlaneStrain 127        0        0        0        0
element quad     80     10    17    20    14        1  PlaneStrain 127        0        0        0        0
element quad     81    262   268   297   289        1  PlaneStrain 127        0        0        0        0
element quad     82    235   243   268   262        1  PlaneStrain 127        0        0        0        0
element quad     83    213   221   243   235        1  PlaneStrain 127        0        0        0        0
element quad     84    190   201   221   213        1  PlaneStrain 127        0        0        0        0
element quad     85    170   180   201   190        1  PlaneStrain 127        0        0        0        0
element quad     86    154   164   180   170        1  PlaneStrain 127        0        0        0        0
element quad     87    137   146   164   154        1  PlaneStrain 127        0        0        0        0
element quad     88    122   133   146   137        1  PlaneStrain 127        0        0        0        0
element quad     89    107   117   133   122        1  PlaneStrain 127        0        0        0        0
element quad     90     93   104   117   107        1  PlaneStrain 127        0        0        0        0
element quad     91     82    92   104    93        1  PlaneStrain 127        0        0        0        0
element quad     92     69    81    92    82        1  PlaneStrain 127        0        0        0        0
element quad     93     60    72    81    69        1  PlaneStrain 127        0        0        0        0
element quad     94     52    62    72    60        1  PlaneStrain 127        0        0        0        0
element quad     95     43    55    62    52        1  PlaneStrain 127        0        0        0        0
element quad     96     37    47    55    43        1  PlaneStrain 127        0        0        0        0
element quad     97     31    40    47    37        1  PlaneStrain 127        0        0        0        0
element quad     98     26    33    40    31        1  PlaneStrain 127        0        0        0        0
element quad     99     20    29    33    26        1  PlaneStrain 127        0        0        0        0
element quad    100     17    24    29    20        1  PlaneStrain 127        0        0        0        0
element quad    101    268   276   303   297        1  PlaneStrain 127        0        0        0        0
element quad    102    243   253   276   268        1  PlaneStrain 127        0        0        0        0
element quad    103    221   233   253   243        1  PlaneStrain 127        0        0        0        0
element quad    104    201   212   233   221        1  PlaneStrain 127        0        0        0        0
element quad    105    180   192   212   201        1  PlaneStrain 127        0        0        0        0
element quad    106    164   177   192   180        1  PlaneStrain 127        0        0        0        0
element quad    107    146   158   177   164        1  PlaneStrain 127        0        0        0        0
element quad    108    133   144   158   146        1  PlaneStrain 127        0        0        0        0
element quad    109    117   129   144   133        1  PlaneStrain 127        0        0        0        0
element quad    110    104   116   129   117        1  PlaneStrain 127        0        0        0        0
element quad    111     92   106   116   104        1  PlaneStrain 127        0        0        0        0
element quad    112     81    94   106    92        1  PlaneStrain 127        0        0        0        0
element quad    113     72    84    94    81        1  PlaneStrain 127        0        0        0        0
element quad    114     62    75    84    72        1  PlaneStrain 127        0        0        0        0
element quad    115     55    67    75    62        1  PlaneStrain 127        0        0        0        0
element quad    116     47    58    67    55        1  PlaneStrain 127        0        0        0        0
element quad    117     40    50    58    47        1  PlaneStrain 127        0        0        0        0
element quad    118     33    45    50    40        1  PlaneStrain 127        0        0        0        0
element quad    119     29    39    45    33        1  PlaneStrain 127        0        0        0        0
element quad    120     24    34    39    29        1  PlaneStrain 127        0        0        0        0
element quad    121    276   288   311   303        1  PlaneStrain 127        0        0        0        0
element quad    122    253   265   288   276        1  PlaneStrain 127        0        0        0        0
element quad    123    233   244   265   253        1  PlaneStrain 127        0        0        0        0
element quad    124    212   226   244   233        1  PlaneStrain 127        0        0        0        0
element quad    125    192   207   226   212        1  PlaneStrain 127        0        0        0        0
element quad    126    177   188   207   192        1  PlaneStrain 127        0        0        0        0
element quad    127    158   173   188   177        1  PlaneStrain 127        0        0        0        0
element quad    128    144   157   173   158        1  PlaneStrain 127        0        0        0        0
element quad    129    129   145   157   144        1  PlaneStrain 127        0        0        0        0
element quad    130    116   131   145   129        1  PlaneStrain 127        0        0        0        0
element quad    131    106   119   131   116        1  PlaneStrain 127        0        0        0        0
element quad    132     94   108   119   106        1  PlaneStrain 127        0        0        0        0
element quad    133     84    99   108    94        1  PlaneStrain 127        0        0        0        0
element quad    134     75    88    99    84        1  PlaneStrain 127        0        0        0        0
element quad    135     67    79    88    75        1  PlaneStrain 127        0        0        0        0
element quad    136     58    71    79    67        1  PlaneStrain 127        0        0        0        0
element quad    137     50    63    71    58        1  PlaneStrain 127        0        0        0        0
element quad    138     45    56    63    50        1  PlaneStrain 127        0        0        0        0
element quad    139     39    49    56    45        1  PlaneStrain 127        0        0        0        0
element quad    140     34    46    49    39        1  PlaneStrain 127        0        0        0        0
element quad    141    288   301   319   311        1  PlaneStrain 127        0        0        0        0
element quad    142    265   279   301   288        1  PlaneStrain 127        0        0        0        0
element quad    143    244   261   279   265        1  PlaneStrain 127        0        0        0        0
element quad    144    226   238   261   244        1  PlaneStrain 127        0        0        0        0
element quad    145    207   222   238   226        1  PlaneStrain 127        0        0        0        0
element quad    146    188   203   222   207        1  PlaneStrain 127        0        0        0        0
element quad    147    173   187   203   188        1  PlaneStrain 127        0        0        0        0
element quad    148    157   176   187   173        1  PlaneStrain 127        0        0        0        0
element quad    149    145   160   176   157        1  PlaneStrain 127        0        0        0        0
element quad    150    131   147   160   145        1  PlaneStrain 127        0        0        0        0
element quad    151    119   136   147   131        1  PlaneStrain 127        0        0        0        0
element quad    152    108   124   136   119        1  PlaneStrain 127        0        0        0        0
element quad    153     99   114   124   108        1  PlaneStrain 127        0        0        0        0
element quad    154     88   102   114    99        1  PlaneStrain 127        0        0        0        0
element quad    155     79    95   102    88        1  PlaneStrain 127        0        0        0        0
element quad    156     71    86    95    79        1  PlaneStrain 127        0        0        0        0
element quad    157     63    78    86    71        1  PlaneStrain 127        0        0        0        0
element quad    158     56    70    78    63        1  PlaneStrain 127        0        0        0        0
element quad    159     49    66    70    56        1  PlaneStrain 127        0        0        0        0
element quad    160     46    59    66    49        1  PlaneStrain 127        0        0        0        0
element quad    161    301   312   330   319        1  PlaneStrain 127        0        0        0        0
element quad    162    279   293   312   301        1  PlaneStrain 127        0        0        0        0
element quad    163    261   273   293   279        1  PlaneStrain 127        0        0        0        0
element quad    164    238   256   273   261        1  PlaneStrain 127        0        0        0        0
element quad    165    222   237   256   238        1  PlaneStrain 127        0        0        0        0
element quad    166    203   223   237   222        1  PlaneStrain 127        0        0        0        0
element quad    167    187   208   223   203        1  PlaneStrain 127        0        0        0        0
element quad    168    176   191   208   187        1  PlaneStrain 127        0        0        0        0
element quad    169    160   179   191   176        1  PlaneStrain 127        0        0        0        0
element quad    170    147   166   179   160        1  PlaneStrain 127        0        0        0        0
element quad    171    136   153   166   147        1  PlaneStrain 127        0        0        0        0
element quad    172    124   141   153   136        1  PlaneStrain 127        0        0        0        0
element quad    173    114   130   141   124        1  PlaneStrain 127        0        0        0        0
element quad    174    102   121   130   114        1  PlaneStrain 127        0        0        0        0
element quad    175     95   110   121   102        1  PlaneStrain 127        0        0        0        0
element quad    176     86   101   110    95        1  PlaneStrain 127        0        0        0        0
element quad    177     78    96   101    86        1  PlaneStrain 127        0        0        0        0
element quad    178     70    87    96    78        1  PlaneStrain 127        0        0        0        0
element quad    179     66    80    87    70        1  PlaneStrain 127        0        0        0        0
element quad    180     59    74    80    66        1  PlaneStrain 127        0        0        0        0
element quad    181    312   323   340   330        1  PlaneStrain 127        0        0        0        0
element quad    182    293   308   323   312        1  PlaneStrain 127        0        0        0        0
element quad    183    273   291   308   293        1  PlaneStrain 127        0        0        0        0
element quad    184    256   272   291   273        1  PlaneStrain 127        0        0        0        0
element quad    185    237   258   272   256        1  PlaneStrain 127        0        0        0        0
element quad    186    223   240   258   237        1  PlaneStrain 127        0        0        0        0
element quad    187    208   227   240   223        1  PlaneStrain 127        0        0        0        0
element quad    188    191   211   227   208        1  PlaneStrain 127        0        0        0        0
element quad    189    179   198   211   191        1  PlaneStrain 127        0        0        0        0
element quad    190    166   185   198   179        1  PlaneStrain 127        0        0        0        0
element quad    191    153   171   185   166        1  PlaneStrain 127        0        0        0        0
element quad    192    141   162   171   153        1  PlaneStrain 127        0        0        0        0
element quad    193    130   150   162   141        1  PlaneStrain 127        0        0        0        0
element quad    194    121   139   150   130        1  PlaneStrain 127        0        0        0        0
element quad    195    110   128   139   121        1  PlaneStrain 127        0        0        0        0
element quad    196    101   123   128   110        1  PlaneStrain 127        0        0        0        0
element quad    197     96   113   123   101        1  PlaneStrain 127        0        0        0        0
element quad    198     87   105   113    96        1  PlaneStrain 127        0        0        0        0
element quad    199     80   100   105    87        1  PlaneStrain 127        0        0        0        0
element quad    200     74    90   100    80        1  PlaneStrain 127        0        0        0        0
element quad    201    323   335   350   340        1  PlaneStrain 127        0        0        0        0
element quad    202    308   322   335   323        1  PlaneStrain 127        0        0        0        0
element quad    203    291   310   322   308        1  PlaneStrain 127        0        0        0        0
element quad    204    272   292   310   291        1  PlaneStrain 127        0        0        0        0
element quad    205    258   275   292   272        1  PlaneStrain 127        0        0        0        0
element quad    206    240   263   275   258        1  PlaneStrain 127        0        0        0        0
element quad    207    227   245   263   240        1  PlaneStrain 127        0        0        0        0
element quad    208    211   234   245   227        1  PlaneStrain 127        0        0        0        0
element quad    209    198   217   234   211        1  PlaneStrain 127        0        0        0        0
element quad    210    185   206   217   198        1  PlaneStrain 127        0        0        0        0
element quad    211    171   193   206   185        1  PlaneStrain 127        0        0        0        0
element quad    212    162   182   193   171        1  PlaneStrain 127        0        0        0        0
element quad    213    150   169   182   162        1  PlaneStrain 127        0        0        0        0
element quad    214    139   161   169   150        1  PlaneStrain 127        0        0        0        0
element quad    215    128   151   161   139        1  PlaneStrain 127        0        0        0        0
element quad    216    123   142   151   128        1  PlaneStrain 127        0        0        0        0
element quad    217    113   134   142   123        1  PlaneStrain 127        0        0        0        0
element quad    218    105   125   134   113        1  PlaneStrain 127        0        0        0        0
element quad    219    100   118   125   105        1  PlaneStrain 127        0        0        0        0
element quad    220     90   112   118   100        1  PlaneStrain 127        0        0        0        0
element quad    221    335   349   361   350        1  PlaneStrain 127        0        0        0        0
element quad    222    322   336   349   335        1  PlaneStrain 127        0        0        0        0
element quad    223    310   325   336   322        1  PlaneStrain 127        0        0        0        0
element quad    224    292   313   325   310        1  PlaneStrain 127        0        0        0        0
element quad    225    275   300   313   292        1  PlaneStrain 127        0        0        0        0
element quad    226    263   284   300   275        1  PlaneStrain 127        0        0        0        0
element quad    227    245   270   284   263        1  PlaneStrain 127        0        0        0        0
element quad    228    234   254   270   245        1  PlaneStrain 127        0        0        0        0
element quad    229    217   241   254   234        1  PlaneStrain 127        0        0        0        0
element quad    230    206   229   241   217        1  PlaneStrain 127        0        0        0        0
element quad    231    193   214   229   206        1  PlaneStrain 127        0        0        0        0
element quad    232    182   204   214   193        1  PlaneStrain 127        0        0        0        0
element quad    233    169   194   204   182        1  PlaneStrain 127        0        0        0        0
element quad    234    161   184   194   169        1  PlaneStrain 127        0        0        0        0
element quad    235    151   175   184   161        1  PlaneStrain 127        0        0        0        0
element quad    236    142   165   175   151        1  PlaneStrain 127        0        0        0        0
element quad    237    134   156   165   142        1  PlaneStrain 127        0        0        0        0
element quad    238    125   149   156   134        1  PlaneStrain 127        0        0        0        0
element quad    239    118   140   149   125        1  PlaneStrain 127        0        0        0        0
element quad    240    112   135   140   118        1  PlaneStrain 127        0        0        0        0
element quad    241    349   363   372   361        1  PlaneStrain 127        0        0        0        0
element quad    242    336   352   363   349        1  PlaneStrain 127        0        0        0        0
element quad    243    325   341   352   336        1  PlaneStrain 127        0        0        0        0
element quad    244    313   331   341   325        1  PlaneStrain 127        0        0        0        0
element quad    245    300   318   331   313        1  PlaneStrain 127        0        0        0        0
element quad    246    284   305   318   300        1  PlaneStrain 127        0        0        0        0
element quad    247    270   295   305   284        1  PlaneStrain 127        0        0        0        0
element quad    248    254   280   295   270        1  PlaneStrain 127        0        0        0        0
element quad    249    241   267   280   254        1  PlaneStrain 127        0        0        0        0
element quad    250    229   252   267   241        1  PlaneStrain 127        0        0        0        0
element quad    251    214   242   252   229        1  PlaneStrain 127        0        0        0        0
element quad    252    204   231   242   214        1  PlaneStrain 127        0        0        0        0
element quad    253    194   218   231   204        1  PlaneStrain 127        0        0        0        0
element quad    254    184   209   218   194        1  PlaneStrain 127        0        0        0        0
element quad    255    175   199   209   184        1  PlaneStrain 127        0        0        0        0
element quad    256    165   189   199   175        1  PlaneStrain 127        0        0        0        0
element quad    257    156   181   189   165        1  PlaneStrain 127        0        0        0        0
element quad    258    149   174   181   156        1  PlaneStrain 127        0        0        0        0
element quad    259    140   167   174   149        1  PlaneStrain 127        0        0        0        0
element quad    260    135   159   167   140        1  PlaneStrain 127        0        0        0        0
element quad    261    363   377   384   372        1  PlaneStrain 127        0        0        0        0
element quad    262    352   369   377   363        1  PlaneStrain 127        0        0        0        0
element quad    263    341   358   369   352        1  PlaneStrain 127        0        0        0        0
element quad    264    331   346   358   341        1  PlaneStrain 127        0        0        0        0
element quad    265    318   338   346   331        1  PlaneStrain 127        0        0        0        0
element quad    266    305   327   338   318        1  PlaneStrain 127        0        0        0        0
element quad    267    295   316   327   305        1  PlaneStrain 127        0        0        0        0
element quad    268    280   304   316   295        1  PlaneStrain 127        0        0        0        0
element quad    269    267   294   304   280        1  PlaneStrain 127        0        0        0        0
element quad    270    252   283   294   267        1  PlaneStrain 127        0        0        0        0
element quad    271    242   269   283   252        1  PlaneStrain 127        0        0        0        0
element quad    272    231   259   269   242        1  PlaneStrain 127        0        0        0        0
element quad    273    218   246   259   231        1  PlaneStrain 127        0        0        0        0
element quad    274    209   236   246   218        1  PlaneStrain 127        0        0        0        0
element quad    275    199   228   236   209        1  PlaneStrain 127        0        0        0        0
element quad    276    189   215   228   199        1  PlaneStrain 127        0        0        0        0
element quad    277    181   210   215   189        1  PlaneStrain 127        0        0        0        0
element quad    278    174   202   210   181        1  PlaneStrain 127        0        0        0        0
element quad    279    167   196   202   174        1  PlaneStrain 127        0        0        0        0
element quad    280    159   186   196   167        1  PlaneStrain 127        0        0        0        0
element quad    281    377   390   398   384        1  PlaneStrain 127        0        0        0        0
element quad    282    369   381   390   377        1  PlaneStrain 127        0        0        0        0
element quad    283    358   374   381   369        1  PlaneStrain 127        0        0        0        0
element quad    284    346   365   374   358        1  PlaneStrain 127        0        0        0        0
element quad    285    338   355   365   346        1  PlaneStrain 127        0        0        0        0
element quad    286    327   345   355   338        1  PlaneStrain 127        0        0        0        0
element quad    287    316   339   345   327        1  PlaneStrain 127        0        0        0        0
element quad    288    304   329   339   316        1  PlaneStrain 127        0        0        0        0
element quad    289    294   317   329   304        1  PlaneStrain 127        0        0        0        0
element quad    290    283   309   317   294        1  PlaneStrain 127        0        0        0        0
element quad    291    269   298   309   283        1  PlaneStrain 127        0        0        0        0
element quad    292    259   286   298   269        1  PlaneStrain 127        0        0        0        0
element quad    293    246   274   286   259        1  PlaneStrain 127        0        0        0        0
element quad    294    236   266   274   246        1  PlaneStrain 127        0        0        0        0
element quad    295    228   257   266   236        1  PlaneStrain 127        0        0        0        0
element quad    296    215   248   257   228        1  PlaneStrain 127        0        0        0        0
element quad    297    210   239   248   215        1  PlaneStrain 127        0        0        0        0
element quad    298    202   232   239   210        1  PlaneStrain 127        0        0        0        0
element quad    299    196   225   232   202        1  PlaneStrain 127        0        0        0        0
element quad    300    186   216   225   196        1  PlaneStrain 127        0        0        0        0
element quad    301    390   406   413   398        1  PlaneStrain 127        0        0        0        0
element quad    302    381   397   406   390        1  PlaneStrain 127        0        0        0        0
element quad    303    374   389   397   381        1  PlaneStrain 127        0        0        0        0
element quad    304    365   383   389   374        1  PlaneStrain 127        0        0        0        0
element quad    305    355   375   383   365        1  PlaneStrain 127        0        0        0        0
element quad    306    345   367   375   355        1  PlaneStrain 127        0        0        0        0
element quad    307    339   359   367   345        1  PlaneStrain 127        0        0        0        0
element quad    308    329   351   359   339        1  PlaneStrain 127        0        0        0        0
element quad    309    317   342   351   329        1  PlaneStrain 127        0        0        0        0
element quad    310    309   333   342   317        1  PlaneStrain 127        0        0        0        0
element quad    311    298   324   333   309        1  PlaneStrain 127        0        0        0        0
element quad    312    286   315   324   298        1  PlaneStrain 127        0        0        0        0
element quad    313    274   307   315   286        1  PlaneStrain 127        0        0        0        0
element quad    314    266   299   307   274        1  PlaneStrain 127        0        0        0        0
element quad    315    257   290   299   266        1  PlaneStrain 127        0        0        0        0
element quad    316    248   282   290   257        1  PlaneStrain 127        0        0        0        0
element quad    317    239   271   282   248        1  PlaneStrain 127        0        0        0        0
element quad    318    232   264   271   239        1  PlaneStrain 127        0        0        0        0
element quad    319    225   260   264   232        1  PlaneStrain 127        0        0        0        0
element quad    320    216   250   260   225        1  PlaneStrain 127        0        0        0        0
element quad    321    406   421   428   413        1  PlaneStrain 127        0        0        0        0
element quad    322    397   416   421   406        1  PlaneStrain 127        0        0        0        0
element quad    323    389   407   416   397        1  PlaneStrain 127        0        0        0        0
element quad    324    383   401   407   389        1  PlaneStrain 127        0        0        0        0
element quad    325    375   394   401   383        1  PlaneStrain 127        0        0        0        0
element quad    326    367   385   394   375        1  PlaneStrain 127        0        0        0        0
element quad    327    359   378   385   367        1  PlaneStrain 127        0        0        0        0
element quad    328    351   370   378   359        1  PlaneStrain 127        0        0        0        0
element quad    329    342   364   370   351        1  PlaneStrain 127        0        0        0        0
element quad    330    333   356   364   342        1  PlaneStrain 127        0        0        0        0
element quad    331    324   348   356   333        1  PlaneStrain 127        0        0        0        0
element quad    332    315   343   348   324        1  PlaneStrain 127        0        0        0        0
element quad    333    307   334   343   315        1  PlaneStrain 127        0        0        0        0
element quad    334    299   328   334   307        1  PlaneStrain 127        0        0        0        0
element quad    335    290   320   328   299        1  PlaneStrain 127        0        0        0        0
element quad    336    282   314   320   290        1  PlaneStrain 127        0        0        0        0
element quad    337    271   306   314   282        1  PlaneStrain 127        0        0        0        0
element quad    338    264   302   306   271        1  PlaneStrain 127        0        0        0        0
element quad    339    260   296   302   264        1  PlaneStrain 127        0        0        0        0
element quad    340    250   287   296   260        1  PlaneStrain 127        0        0        0        0
element quad    341    421   439   445   428        1  PlaneStrain 127        0        0        0        0
element quad    342    416   431   439   421        1  PlaneStrain 127        0        0        0        0
element quad    343    407   424   431   416        1  PlaneStrain 127        0        0        0        0
element quad    344    401   419   424   407        1  PlaneStrain 127        0        0        0        0
element quad    345    394   411   419   401        1  PlaneStrain 127        0        0        0        0
element quad    346    385   405   411   394        1  PlaneStrain 127        0        0        0        0
element quad    347    378   399   405   385        1  PlaneStrain 127        0        0        0        0
element quad    348    370   393   399   378        1  PlaneStrain 127        0        0        0        0
element quad    349    364   386   393   370        1  PlaneStrain 127        0        0        0        0
element quad    350    356   379   386   364        1  PlaneStrain 127        0        0        0        0
element quad    351    348   373   379   356        1  PlaneStrain 127        0        0        0        0
element quad    352    343   368   373   348        1  PlaneStrain 127        0        0        0        0
element quad    353    334   360   368   343        1  PlaneStrain 127        0        0        0        0
element quad    354    328   354   360   334        1  PlaneStrain 127        0        0        0        0
element quad    355    320   347   354   328        1  PlaneStrain 127        0        0        0        0
element quad    356    314   344   347   320        1  PlaneStrain 127        0        0        0        0
element quad    357    306   337   344   314        1  PlaneStrain 127        0        0        0        0
element quad    358    302   332   337   306        1  PlaneStrain 127        0        0        0        0
element quad    359    296   326   332   302        1  PlaneStrain 127        0        0        0        0
element quad    360    287   321   326   296        1  PlaneStrain 127        0        0        0        0
element quad    361    439   455   460   445        1  PlaneStrain 127        0        0        0        0
element quad    362    431   449   455   439        1  PlaneStrain 127        0        0        0        0
element quad    363    424   443   449   431        1  PlaneStrain 127        0        0        0        0
element quad    364    419   438   443   424        1  PlaneStrain 127        0        0        0        0
element quad    365    411   432   438   419        1  PlaneStrain 127        0        0        0        0
element quad    366    405   425   432   411        1  PlaneStrain 127        0        0        0        0
element quad    367    399   420   425   405        1  PlaneStrain 127        0        0        0        0
element quad    368    393   415   420   399        1  PlaneStrain 127        0        0        0        0
element quad    369    386   409   415   393        1  PlaneStrain 127        0        0        0        0
element quad    370    379   402   409   386        1  PlaneStrain 127        0        0        0        0
element quad    371    373   396   402   379        1  PlaneStrain 127        0        0        0        0
element quad    372    368   392   396   373        1  PlaneStrain 127        0        0        0        0
element quad    373    360   387   392   368        1  PlaneStrain 127        0        0        0        0
element quad    374    354   380   387   360        1  PlaneStrain 127        0        0        0        0
element quad    375    347   376   380   354        1  PlaneStrain 127        0        0        0        0
element quad    376    344   371   376   347        1  PlaneStrain 127        0        0        0        0
element quad    377    337   366   371   344        1  PlaneStrain 127        0        0        0        0
element quad    378    332   362   366   337        1  PlaneStrain 127        0        0        0        0
element quad    379    326   357   362   332        1  PlaneStrain 127        0        0        0        0
element quad    380    321   353   357   326        1  PlaneStrain 127        0        0        0        0
element quad    381    455   472   477   460        1  PlaneStrain 127        0        0        0        0
element quad    382    449   467   472   455        1  PlaneStrain 127        0        0        0        0
element quad    383    443   462   467   449        1  PlaneStrain 127        0        0        0        0
element quad    384    438   456   462   443        1  PlaneStrain 127        0        0        0        0
element quad    385    432   451   456   438        1  PlaneStrain 127        0        0        0        0
element quad    386    425   447   451   432        1  PlaneStrain 127        0        0        0        0
element quad    387    420   442   447   425        1  PlaneStrain 127        0        0        0        0
element quad    388    415   436   442   420        1  PlaneStrain 127        0        0        0        0
element quad    389    409   433   436   415        1  PlaneStrain 127        0        0        0        0
element quad    390    402   427   433   409        1  PlaneStrain 127        0        0        0        0
element quad    391    396   423   427   402        1  PlaneStrain 127        0        0        0        0
element quad    392    392   417   423   396        1  PlaneStrain 127        0        0        0        0
element quad    393    387   412   417   392        1  PlaneStrain 127        0        0        0        0
element quad    394    380   408   412   387        1  PlaneStrain 127        0        0        0        0
element quad    395    376   403   408   380        1  PlaneStrain 127        0        0        0        0
element quad    396    371   400   403   376        1  PlaneStrain 127        0        0        0        0
element quad    397    366   395   400   371        1  PlaneStrain 127        0        0        0        0
element quad    398    362   391   395   366        1  PlaneStrain 127        0        0        0        0
element quad    399    357   388   391   362        1  PlaneStrain 127        0        0        0        0
element quad    400    353   382   388   357        1  PlaneStrain 127        0        0        0        0
element quad    401    472   490   495   477        1  PlaneStrain 127        0        0        0        0
element quad    402    467   486   490   472        1  PlaneStrain 127        0        0        0        0
element quad    403    462   482   486   467        1  PlaneStrain 127        0        0        0        0
element quad    404    456   476   482   462        1  PlaneStrain 127        0        0        0        0
element quad    405    451   471   476   456        1  PlaneStrain 127        0        0        0        0
element quad    406    447   468   471   451        1  PlaneStrain 127        0        0        0        0
element quad    407    442   464   468   447        1  PlaneStrain 127        0        0        0        0
element quad    408    436   459   464   442        1  PlaneStrain 127        0        0        0        0
element quad    409    433   452   459   436        1  PlaneStrain 127        0        0        0        0
element quad    410    427   448   452   433        1  PlaneStrain 127        0        0        0        0
element quad    411    423   444   448   427        1  PlaneStrain 127        0        0        0        0
element quad    412    417   440   444   423        1  PlaneStrain 127        0        0        0        0
element quad    413    412   435   440   417        1  PlaneStrain 127        0        0        0        0
element quad    414    408   430   435   412        1  PlaneStrain 127        0        0        0        0
element quad    415    403   426   430   408        1  PlaneStrain 127        0        0        0        0
element quad    416    400   422   426   403        1  PlaneStrain 127        0        0        0        0
element quad    417    395   418   422   400        1  PlaneStrain 127        0        0        0        0
element quad    418    391   414   418   395        1  PlaneStrain 127        0        0        0        0
element quad    419    388   410   414   391        1  PlaneStrain 127        0        0        0        0
element quad    420    382   404   410   388        1  PlaneStrain 127        0        0        0        0
element quad    421    490   509   514   495        1  PlaneStrain 127        0        0        0        0
element quad    422    486   505   509   490        1  PlaneStrain 127        0        0        0        0
element quad    423    482   500   505   486        1  PlaneStrain 127        0        0        0        0
element quad    424    476   497   500   482        1  PlaneStrain 127        0        0        0        0
element quad    425    471   492   497   476        1  PlaneStrain 127        0        0        0        0
element quad    426    468   487   492   471        1  PlaneStrain 127        0        0        0        0
element quad    427    464   483   487   468        1  PlaneStrain 127        0        0        0        0
element quad    428    459   479   483   464        1  PlaneStrain 127        0        0        0        0
element quad    429    452   474   479   459        1  PlaneStrain 127        0        0        0        0
element quad    430    448   470   474   452        1  PlaneStrain 127        0        0        0        0
element quad    431    444   466   470   448        1  PlaneStrain 127        0        0        0        0
element quad    432    440   463   466   444        1  PlaneStrain 127        0        0        0        0
element quad    433    435   458   463   440        1  PlaneStrain 127        0        0        0        0
element quad    434    430   454   458   435        1  PlaneStrain 127        0        0        0        0
element quad    435    426   450   454   430        1  PlaneStrain 127        0        0        0        0
element quad    436    422   446   450   426        1  PlaneStrain 127        0        0        0        0
element quad    437    418   441   446   422        1  PlaneStrain 127        0        0        0        0
element quad    438    414   437   441   418        1  PlaneStrain 127        0        0        0        0
element quad    439    410   434   437   414        1  PlaneStrain 127        0        0        0        0
element quad    440    404   429   434   410        1  PlaneStrain 127        0        0        0        0
element quad    441    509   529   533   514        1  PlaneStrain 127        0        0        0        0
element quad    442    505   522   529   509        1  PlaneStrain 127        0        0        0        0
element quad    443    500   519   522   505        1  PlaneStrain 127        0        0        0        0
element quad    444    497   516   519   500        1  PlaneStrain 127        0        0        0        0
element quad    445    492   512   516   497        1  PlaneStrain 127        0        0        0        0
element quad    446    487   507   512   492        1  PlaneStrain 127        0        0        0        0
element quad    447    483   503   507   487        1  PlaneStrain 127        0        0        0        0
element quad    448    479   499   503   483        1  PlaneStrain 127        0        0        0        0
element quad    449    474   496   499   479        1  PlaneStrain 127        0        0        0        0
element quad    450    470   493   496   474        1  PlaneStrain 127        0        0        0        0
element quad    451    466   488   493   470        1  PlaneStrain 127        0        0        0        0
element quad    452    463   484   488   466        1  PlaneStrain 127        0        0        0        0
element quad    453    458   480   484   463        1  PlaneStrain 127        0        0        0        0
element quad    454    454   475   480   458        1  PlaneStrain 127        0        0        0        0
element quad    455    450   473   475   454        1  PlaneStrain 127        0        0        0        0
element quad    456    446   469   473   450        1  PlaneStrain 127        0        0        0        0
element quad    457    441   465   469   446        1  PlaneStrain 127        0        0        0        0
element quad    458    437   461   465   441        1  PlaneStrain 127        0        0        0        0
element quad    459    434   457   461   437        1  PlaneStrain 127        0        0        0        0
element quad    460    429   453   457   434        1  PlaneStrain 127        0        0        0        0
element quad    461    529   546   551   533        1  PlaneStrain 127        0        0        0        0
element quad    462    522   543   546   529        1  PlaneStrain 127        0        0        0        0
element quad    463    519   539   543   522        1  PlaneStrain 127        0        0        0        0
element quad    464    516   536   539   519        1  PlaneStrain 127        0        0        0        0
element quad    465    512   532   536   516        1  PlaneStrain 127        0        0        0        0
element quad    466    507   528   532   512        1  PlaneStrain 127        0        0        0        0
element quad    467    503   524   528   507        1  PlaneStrain 127        0        0        0        0
element quad    468    499   520   524   503        1  PlaneStrain 127        0        0        0        0
element quad    469    496   517   520   499        1  PlaneStrain 127        0        0        0        0
element quad    470    493   513   517   496        1  PlaneStrain 127        0        0        0        0
element quad    471    488   510   513   493        1  PlaneStrain 127        0        0        0        0
element quad    472    484   506   510   488        1  PlaneStrain 127        0        0        0        0
element quad    473    480   502   506   484        1  PlaneStrain 127        0        0        0        0
element quad    474    475   498   502   480        1  PlaneStrain 127        0        0        0        0
element quad    475    473   494   498   475        1  PlaneStrain 127        0        0        0        0
element quad    476    469   491   494   473        1  PlaneStrain 127        0        0        0        0
element quad    477    465   489   491   469        1  PlaneStrain 127        0        0        0        0
element quad    478    461   485   489   465        1  PlaneStrain 127        0        0        0        0
element quad    479    457   481   485   461        1  PlaneStrain 127        0        0        0        0
element quad    480    453   478   481   457        1  PlaneStrain 127        0        0        0        0
element quad    481    546   566   569   551        1  PlaneStrain 127        0        0        0        0
element quad    482    543   563   566   546        1  PlaneStrain 127        0        0        0        0
element quad    483    539   560   563   543        1  PlaneStrain 127        0        0        0        0
element quad    484    536   555   560   539        1  PlaneStrain 127        0        0        0        0
element quad    485    532   552   555   536        1  PlaneStrain 127        0        0        0        0
element quad    486    528   548   552   532        1  PlaneStrain 127        0        0        0        0
element quad    487    524   544   548   528        1  PlaneStrain 127        0        0        0        0
element quad    488    520   541   544   524        1  PlaneStrain 127        0        0        0        0
element quad    489    517   538   541   520        1  PlaneStrain 127        0        0        0        0
element quad    490    513   535   538   517        1  PlaneStrain 127        0        0        0        0
element quad    491    510   531   535   513        1  PlaneStrain 127        0        0        0        0
element quad    492    506   527   531   510        1  PlaneStrain 127        0        0        0        0
element quad    493    502   523   527   506        1  PlaneStrain 127        0        0        0        0
element quad    494    498   521   523   502        1  PlaneStrain 127        0        0        0        0
element quad    495    494   518   521   498        1  PlaneStrain 127        0        0        0        0
element quad    496    491   515   518   494        1  PlaneStrain 127        0        0        0        0
element quad    497    489   511   515   491        1  PlaneStrain 127        0        0        0        0
element quad    498    485   508   511   489        1  PlaneStrain 127        0        0        0        0
element quad    499    481   504   508   485        1  PlaneStrain 127        0        0        0        0
element quad    500    478   501   504   481        1  PlaneStrain 127        0        0        0        0
element quad    501    566   585   588   569        1  PlaneStrain 127        0        0        0        0
element quad    502    563   582   585   566        1  PlaneStrain 127        0        0        0        0
element quad    503    560   579   582   563        1  PlaneStrain 127        0        0        0        0
element quad    504    555   575   579   560        1  PlaneStrain 127        0        0        0        0
element quad    505    552   572   575   555        1  PlaneStrain 127        0        0        0        0
element quad    506    548   568   572   552        1  PlaneStrain 127        0        0        0        0
element quad    507    544   565   568   548        1  PlaneStrain 127        0        0        0        0
element quad    508    541   562   565   544        1  PlaneStrain 127        0        0        0        0
element quad    509    538   558   562   541        1  PlaneStrain 127        0        0        0        0
element quad    510    535   556   558   538        1  PlaneStrain 127        0        0        0        0
element quad    511    531   553   556   535        1  PlaneStrain 127        0        0        0        0
element quad    512    527   549   553   531        1  PlaneStrain 127        0        0        0        0
element quad    513    523   545   549   527        1  PlaneStrain 127        0        0        0        0
element quad    514    521   542   545   523        1  PlaneStrain 127        0        0        0        0
element quad    515    518   540   542   521        1  PlaneStrain 127        0        0        0        0
element quad    516    515   537   540   518        1  PlaneStrain 127        0        0        0        0
element quad    517    511   534   537   515        1  PlaneStrain 127        0        0        0        0
element quad    518    508   530   534   511        1  PlaneStrain 127        0        0        0        0
element quad    519    504   526   530   508        1  PlaneStrain 127        0        0        0        0
element quad    520    501   525   526   504        1  PlaneStrain 127        0        0        0        0
element quad    521    585   605   608   588        1  PlaneStrain 127        0        0        0        0
element quad    522    582   602   605   585        1  PlaneStrain 127        0        0        0        0
element quad    523    579   599   602   582        1  PlaneStrain 127        0        0        0        0
element quad    524    575   595   599   579        1  PlaneStrain 127        0        0        0        0
element quad    525    572   592   595   575        1  PlaneStrain 127        0        0        0        0
element quad    526    568   589   592   572        1  PlaneStrain 127        0        0        0        0
element quad    527    565   586   589   568        1  PlaneStrain 127        0        0        0        0
element quad    528    562   583   586   565        1  PlaneStrain 127        0        0        0        0
element quad    529    558   580   583   562        1  PlaneStrain 127        0        0        0        0
element quad    530    556   577   580   558        1  PlaneStrain 127        0        0        0        0
element quad    531    553   574   577   556        1  PlaneStrain 127        0        0        0        0
element quad    532    549   571   574   553        1  PlaneStrain 127        0        0        0        0
element quad    533    545   567   571   549        1  PlaneStrain 127        0        0        0        0
element quad    534    542   564   567   545        1  PlaneStrain 127        0        0        0        0
element quad    535    540   561   564   542        1  PlaneStrain 127        0        0        0        0
element quad    536    537   559   561   540        1  PlaneStrain 127        0        0        0        0
element quad    537    534   557   559   537        1  PlaneStrain 127        0        0        0        0
element quad    538    530   554   557   534        1  PlaneStrain 127        0        0        0        0
element quad    539    526   550   554   530        1  PlaneStrain 127        0        0        0        0
element quad    540    525   547   550   526        1  PlaneStrain 127        0        0        0        0
element quad    541    605   624   628   608        1  PlaneStrain 127        0        0        0        0
element quad    542    602   621   624   605        1  PlaneStrain 127        0        0        0        0
element quad    543    599   618   621   602        1  PlaneStrain 127        0        0        0        0
element quad    544    595   614   618   599        1  PlaneStrain 127        0        0        0        0
element quad    545    592   612   614   595        1  PlaneStrain 127        0        0        0        0
element quad    546    589   610   612   592        1  PlaneStrain 127        0        0        0        0
element quad    547    586   607   610   589        1  PlaneStrain 127        0        0        0        0
element quad    548    583   604   607   586        1  PlaneStrain 127        0        0        0        0
element quad    549    580   601   604   583        1  PlaneStrain 127        0        0        0        0
element quad    550    577   597   601   580        1  PlaneStrain 127        0        0        0        0
element quad    551    574   594   597   577        1  PlaneStrain 127        0        0        0        0
element quad    552    571   591   594   574        1  PlaneStrain 127        0        0        0        0
element quad    553    567   590   591   571        1  PlaneStrain 127        0        0        0        0
element quad    554    564   587   590   567        1  PlaneStrain 127        0        0        0        0
element quad    555    561   584   587   564        1  PlaneStrain 127        0        0        0        0
element quad    556    559   581   584   561        1  PlaneStrain 127        0        0        0        0
element quad    557    557   578   581   559        1  PlaneStrain 127        0        0        0        0
element quad    558    554   576   578   557        1  PlaneStrain 127        0        0        0        0
element quad    559    550   573   576   554        1  PlaneStrain 127        0        0        0        0
element quad    560    547   570   573   550        1  PlaneStrain 127        0        0        0        0
element quad    561    624   641   643   628        1  PlaneStrain 127        0        0        0        0
element quad    562    621   639   641   624        1  PlaneStrain 127        0        0        0        0
element quad    563    618   637   639   621        1  PlaneStrain 127        0        0        0        0
element quad    564    614   635   637   618        1  PlaneStrain 127        0        0        0        0
element quad    565    612   633   635   614        1  PlaneStrain 127        0        0        0        0
element quad    566    610   630   633   612        1  PlaneStrain 127        0        0        0        0
element quad    567    607   627   630   610        1  PlaneStrain 127        0        0        0        0
element quad    568    604   625   627   607        1  PlaneStrain 127        0        0        0        0
element quad    569    601   622   625   604        1  PlaneStrain 127        0        0        0        0
element quad    570    597   619   622   601        1  PlaneStrain 127        0        0        0        0
element quad    571    594   616   619   597        1  PlaneStrain 127        0        0        0        0
element quad    572    591   613   616   594        1  PlaneStrain 127        0        0        0        0
element quad    573    590   611   613   591        1  PlaneStrain 127        0        0        0        0
element quad    574    587   609   611   590        1  PlaneStrain 127        0        0        0        0
element quad    575    584   606   609   587        1  PlaneStrain 127        0        0        0        0
element quad    576    581   603   606   584        1  PlaneStrain 127        0        0        0        0
element quad    577    578   600   603   581        1  PlaneStrain 127        0        0        0        0
element quad    578    576   598   600   578        1  PlaneStrain 127        0        0        0        0
element quad    579    573   596   598   576        1  PlaneStrain 127        0        0        0        0
element quad    580    570   593   596   573        1  PlaneStrain 127        0        0        0        0
element quad    581    641   650   651   643        1  PlaneStrain 127        0        0        0        0
element quad    582    639   649   650   641        1  PlaneStrain 127        0        0        0        0
element quad    583    637   648   649   639        1  PlaneStrain 127        0        0        0        0
element quad    584    635   647   648   637        1  PlaneStrain 127        0        0        0        0
element quad    585    633   646   647   635        1  PlaneStrain 127        0        0        0        0
element quad    586    630   645   646   633        1  PlaneStrain 127        0        0        0        0
element quad    587    627   644   645   630        1  PlaneStrain 127        0        0        0        0
element quad    588    625   642   644   627        1  PlaneStrain 127        0        0        0        0
element quad    589    622   640   642   625        1  PlaneStrain 127        0        0        0        0
element quad    590    619   638   640   622        1  PlaneStrain 127        0        0        0        0
element quad    591    616   636   638   619        1  PlaneStrain 127        0        0        0        0
element quad    592    613   634   636   616        1  PlaneStrain 127        0        0        0        0
element quad    593    611   632   634   613        1  PlaneStrain 127        0        0        0        0
element quad    594    609   631   632   611        1  PlaneStrain 127        0        0        0        0
element quad    595    606   629   631   609        1  PlaneStrain 127        0        0        0        0
element quad    596    603   626   629   606        1  PlaneStrain 127        0        0        0        0
element quad    597    600   623   626   603        1  PlaneStrain 127        0        0        0        0
element quad    598    598   620   623   600        1  PlaneStrain 127        0        0        0        0
element quad    599    596   617   620   598        1  PlaneStrain 127        0        0        0        0
element quad    600    593   615   617   596        1  PlaneStrain 127        0        0        0        0

# --------------------------------------------------------------------------------------------------------------
#
# D O M A I N  C O M M O N S
#
# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
# R E C O R D E R S
# --------------------------------------------------------------------------------------------------------------

recorder Node -file Node_displacements.out -time -nodeRange 1 651 -dof 1 2 disp
recorder Node -file Node_rotations.out -time -nodeRange 1 651 -dof 3 disp
recorder Node -file Node_forceReactions.out -time -nodeRange 1 651 -dof 1 2 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange 1 651 -dof 3 reaction

# recording the initial status
record

# Perform eigenvalue analysis
set numModes 3

# Record eigenvectors
for { set k 1 } { $k <= $numModes } { incr k } {
    recorder Node -file [format "Mode_%i.out" $k] -nodeRange 1 651 -dof 1 2 "eigen $k"
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