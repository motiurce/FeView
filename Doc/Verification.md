# 1. Verification (Linear Static Analysis):

## 1.1 Two Dimensional Problem:

### 1.1.1 Plane Frame:

#### 1.1.1.1 Verification Example 1: 

A cantilever concrete beam is subjected to a vertical load at the free
end. The resulting vertical displacement measured at the free end of the
beam obtained from the analysis program FeView is compared with SAP2000
results.

##### + Geometry, Properties and Loading

+----------------------------------+---------------------------------+
| **[Geometry and Loading:]{.ul}** | **[Material Properties:]{.ul}** |
|                                  |                                 |
|                                  | *E* = 30 GPa                    |
|                                  |                                 |
|                                  | *ν* = 0.2                       |
+----------------------------------+---------------------------------+

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**       **FeView (20 element)**   **SAP2000 (20 element)**
  -------------------------- ------------------------- --------------------------
  U~y,(free\ end)~ \[m\]     -0.03086                  -0.03094
  R~z,(free\ end)~ \[rad\]   -0.00926                  \- 0.00926
  RM~z,(support)~ \[kN-m\]   50                        50

##### + Comparison FeView & SAP2000 deform shape:

  **Shape Type**   **FeView**                                                           **SAP2000**
  ---------------- -------------------------------------------------------------------- ----------------------------------------------------------------------------------
  Deform shape     ![](media/image3.png){width="2.5in" height="0.8595199037620297in"}   ![](media/image4.png){width="1.9769225721784778in" height="1.564673009623797in"}

##### + Download TCL file:

<https://www.dropbox.com/s/6of2h6nvqus9mfq/Example_1.tcl?dl=0>

#### 1.1.1.2 Verification Example 2:

A three-element frame is subjected to five load cases with various load
types (point and distributed). Five different models have been created,
one for each load case. The resulting displacements at specified joints
obtained from analysis program FeView are compared with SAP200 results.

##### + Geometry, Properties and Loading

+----------------------+---------------------------------+
| **[Geometry:]{.ul}** | **[Material Properties:]{.ul}** |
|                      |                                 |
|                      | E = 24.81989 GPa                |
|                      |                                 |
|                      | **[Section Properties:]{.ul}**  |
|                      |                                 |
|                      | *A* = 0.0929 m^2^               |
|                      |                                 |
|                      | *I* = 7.1925e-4 m^4^            |
+======================+=================================+
|                      |                                 |
+----------------------+---------------------------------+

**[Modeling and Loading]{.ul}**

• **Load Case 1 :** Distributed gravity load on frame element 3 and
concentrated load on joint 4 (the uniform distributed load is inserted
as element load in the local y direction (F~y~= -26.27 kN/m) as the
concentrated load is applied as point force in the global Y direction
(F~y~ = -44.48 kN)

• **Load Case 2** Global point force and point moment at joint 2 (force
and moment are applied as permanent loads, in terms of forces (F~y~ =
-76.51 kN) and moments (M~z~ = 73.75 kNm) in the global Y and R~Z~
directions, respectively)

• **Load Case 3 :** Concentrated load on frame element 2 (it has been
decomposed in a vertical and a horizontal component, so they are applied
as permanent loads in terms of forces in the X and Y directions
respectively, F~x~ = 40.032 kN and F~z~ = -53.376 kN)

• **Load Case 4 :** Distributed gravity load (global Y axis) 23.249 kN/m
on frame element 2, applied as distributed load on the element local x
and y axes, F~x~ = -23.349·cosφ = -14.009 kN/m and F~y~ = -23.349·sinφ
=-18.679 kN/m, respectively. Element angle φ = arctan(1.83/2.44) = 36.9°

• **Load Case 5 :** Distributed horizontal load 29.186 kN/m on frame
element 1 (global X axis), applied on the element local y axis.
Distributed horizontal load -29.186 kN/m applied on frame element 2
local y axis.

##### + Results and Comparison

The most significant results are compared in the table below:

  **Load Case**   **Output Parameter**   **FeView**   **SAP2000**
  --------------- ---------------------- ------------ -------------
  Case 1          U~y,(node\ 3)~ \[m\]   0.001518     0.001599
  Case 2          U~y,(node\ 3)~ \[m\]   0.001517     0.001599
  Case 3          U~x,(node\ 2)~ \[m\]   0.000189     0.000165
  Case 4          U~y,(node\ 3)~ \[m\]   -0.007686    -0.007526
  Case 5          U~x,(node\ 2)~ \[m\]   0.008005     0.007938

##### + Comparison FeView & SAP2000 deform shape:

  **Load Case**   **FeView**                                                            **SAP2000**
  --------------- --------------------------------------------------------------------- ---------------------------------------------------------------------
  Case 1          ![](media/image7.png){width="2.3in" height="2.319325240594926in"}     ![](media/image8.png){width="2.1in" height="2.3033694225721786in"}
  Case 2          ![](media/image9.png){width="2.3in" height="2.3621620734908135in"}    ![](media/image10.png){width="1.7in" height="2.2779997812773405in"}
  Case 3          ![](media/image11.png){width="2.3in" height="2.2666054243219595in"}   ![](media/image12.png){width="1.7in" height="2.28587489063867in"}
  Case 4          ![](media/image13.png){width="2.3in" height="2.291353893263342in"}    ![](media/image14.png){width="1.85in" height="2.246428258967629in"}
  Case 5          ![](media/image15.png){width="2.3in" height="2.4165693350831146in"}   ![](media/image16.png){width="1.7in" height="2.3040113735783025in"}

##### + Download TCL file:

Load Case 1:
<https://www.dropbox.com/s/hv61vhuon2kbbv1/Example_2_LoadCase1.tcl?dl=0>

Load Case 2:
<https://www.dropbox.com/s/l0vopfcoif8r9v5/Example_2_LoadCase2.tcl?dl=0>

Load Case 3:
<https://www.dropbox.com/s/rn6y0new7b9z2kq/Example_2_LoadCase3.tcl?dl=0>

Load Case 4:
<https://www.dropbox.com/s/9ztk2xootkyoot3/Example_2_LoadCase4.tcl?dl=0>

Load Case 5:
<https://www.dropbox.com/s/ckfyj843mzv2q0s/Example_2_LoadCase5.tcl?dl=0>

#### 1.1.1.3 Verification Example 3:

This example tests FeView for settlement and rotation of normal supports
and spring supports on a portal frame. Two different models have been
created. The models are identical, except for the loading and the
support condition at joint 4. The results obtained with the FE analysis
program FeView at specified joints and in each model are compared with
SAP2000 results.

##### - Geometry, Properties and Model Configuration:

+----------------------+---------------------------------+
| **[Geometry:]{.ul}** | **[Material Properties:]{.ul}** |
|                      |                                 |
|                      | *E* = 199.938 GPa               |
|                      |                                 |
|                      | **[Section Properties:]{.ul}**  |
|                      |                                 |
|                      | *A* = 0.0929 m^2^               |
|                      |                                 |
|                      | *I* = 7.19248e-4 m^4^           |
+======================+=================================+
| [Model A]{.ul}       | [Model B]{.ul}                  |
+----------------------+---------------------------------+

##### Results and Comparison

The most significant results are compared in the table below:

  **Model**   **Output Parameter**       **FeView**   **SAP2000**
  ----------- -------------------------- ------------ -------------
  A           RF~y,(node\ 1)~ \[kN\]     27.96        27.994
              RM~z,(node\ 1)~ \[kN-m\]   -102.29      -102.393
  B           RF~y,(node\ 1)~ \[kN\]     -80.533      -80.624
              RM~z,(node\ 1)~ \[kN-m\]   294.59       294.890

##### + Comparison FeView & SAP2000 deform shape:

  **Model**   **FeView**                                                           **SAP2000**
  ----------- -------------------------------------------------------------------- ---------------------------------------------------------------------
  A           ![](media/image20.png){width="2.3in" height="2.3in"}                 ![](media/image21.png){width="2.1248982939632546in" height="2.3in"}
  B           ![](media/image22.png){width="2.3in" height="2.100193569553806in"}   ![](media/image23.png){width="2.6in" height="2.1011132983377077in"}

##### + Download TCL file:

Model A: <https://www.dropbox.com/s/6iiv7r22rqswmwf/Example_3A.tcl?dl=0>

Model B: <https://www.dropbox.com/s/r23lsrpfhc39u3y/Example_3B.tcl?dl=0>

### 1.1.2 Plane Truss:

#### 1.1.2.1 Verification Example 4: 

A steel truss is subjected to is subjected to vertical loads as shown in
figure below. The resulting maximum vertical displacement obtained from
the analysis program FeView is compared with ABAQUS results.

##### + Geometry, Properties and Loading

+----------------------------------+---------------------------------+
| **[Geometry and Loading:]{.ul}** | **[Material Properties:]{.ul}** |
|                                  |                                 |
|                                  | *E* = 200 GPa                   |
|                                  |                                 |
|                                  | *ν* = 0.2                       |
|                                  |                                 |
|                                  | **[Section Properties:]{.ul}**  |
|                                  |                                 |
|                                  | *A* = 0.002 m^2^                |
+----------------------------------+---------------------------------+

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**   **FeView**   **ABAQUS**
  ---------------------- ------------ ------------
  U~y,(max)~ \[m\]       -0.00181     -0.00181

##### + Comparison FeView & SAP2000 deform shape:

  **Software**   **Deform shape**
  -------------- ------------------------------------------------------------------------------------------------------------------
  FeView         ![](media/image25.png){width="3.2in" height="1.3476902887139108in"}
  ABAQUS         ![F:\\Download\\Annotation 2020-03-03 124609.png](media/image26.png){width="3.2in" height="1.551712598425197in"}

##### + Download TCL file:

<https://www.dropbox.com/s/08kx10068ozj9m2/Example_4.tcl?dl=0>

### 1.1.3 Planes:

#### 1.1.3.1 Verification Example 5: 

In this example, a straight cantilever beam, modelled with plane stress
elements, is subjected to forces at the tip in the X direction .The tip
displacements in the X direction obtained from the analysis program
FeView is compared with SAP2000 results.

##### + Geometry, Properties and Loading

+----------------------------------+-----------------------------------------+
| **[Geometry and Loading:]{.ul}** | **[Material Properties:]{.ul}**         |
|                                  |                                         |
|                                  | *E* = 68.95 GPa                         |
|                                  |                                         |
|                                  | *ν* = 0.3                               |
|                                  |                                         |
|                                  | G = 26.52 GPa                           |
|                                  |                                         |
|                                  | **[Section Properties:]{.ul}**          |
|                                  |                                         |
|                                  | Plane element thickness = 2.54×10^-3^ m |
+----------------------------------+-----------------------------------------+

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**    **FeView**   **SAP2000**
  ----------------------- ------------ -------------
  U~x,(node\ 13)~ \[m\]   0.00000075   0.00000076

##### + Comparison FeView & SAP2000 deform shape:

  **Software**   **Deform shape**
  -------------- ---------------------------------------------------------------------
  FeView         ![](media/image28.png){width="3.2in" height="0.6854702537182852in"}
  SAP2000        ![](media/image29.png){width="3.2in" height="1.375042650918635in"}

##### + Download TCL file:

<https://www.dropbox.com/s/7ges1lsvvi4m5tq/Example_5.tcl?dl=0>

#### 1.1.3.2 Verification Example 6: 

In this example, a rectangular plate with irregularly shaped elements is
subjected to prescribed displacements at the edges that theoretically
impose a constant stress field over the model. The geometry, properties
and loading are as described in MacNeal and Harder 1985. The plane
stress element is used in FeView and the membrane stress components
resulting from the prescribed displacements are compared with SAP2000.

The Ux and Uy degrees of freedom are active for the analysis. All other
degrees of freedom are inactive. Joints 1, 4, 7 and 8 are restrained for
translation in the X and Y directions. The prescribed displacements are
applied to the restrained degrees of freedom of those joints.

The plane section is modeled using the plane stress element.

##### + Geometry, Properties and

+----------------------------------+----------------------------------+
| **[Geometry and                  | **[Material Properties:]{.ul}**  |
| Coordinates:]{.ul}**             |                                  |
|                                  | *E* = 68.95 GPa                  |
|   Joint   X (m)     Y (m)        |                                  |
|   ------- --------- ---------    | *ν* = 0.25                       |
|   1       0.0061    0.00305      |                                  |
|   2       0.00406   0.00203      | **[Section Properties:]{.ul}**   |
|   3       0.00457   0.00076      |                                  |
|   4       0.0061    0.0          | Plane element thickness =        |
|   5       0.00203   0.00203      | 2.54×10^-3^ m                    |
|   6       0.00102   0.00051      |                                  |
|   7       0.0       0.00305      |                                  |
|   8       0.0       0.0          |                                  |
+----------------------------------+----------------------------------+

##### + Loading

The loading is provided in the form of prescribed edge displacements Ux
and Uy, which are imposed on joints 1, 4, 7 and 8. Those displacements
are defined by the following equations.

![](media/image31.png){width="2.2686570428696413in"
height="0.5811843832020998in"}

##### + Results and Comparison

The most significant results are compared in the table below:

  **Joint**   **FeView**   **SAP2000**              
  ----------- ------------ ------------- ---------- ----------
              **Ux**       **Uy**        **Ux**     **Uy**
  2           5.07e-06     4.06e-06      5.08E-06   4.06E-06
  3           4.95e-06     3.04e-06      4.95E-06   3.04E-06
  5           3.04e-06     3.04e-06      3.04E-06   3.04E-06
  6           1.27e-06     1.02e-06      1.27E-06   1.02E-06

##### + Comparison FeView & SAP2000 deform shape:

  **Software**   **Deform shape**
  -------------- ---------------------------------------------------------------------
  FeView         ![](media/image32.png){width="3.7in" height="2.0460695538057743in"}
  SAP2000        ![](media/image33.png){width="3.7in" height="1.8124464129483815in"}

##### + Download TCL file:

<https://www.dropbox.com/s/xp6ioyypotu9c1h/Example_6.tcl?dl=0>

## 1.2 Three Dimensional Problem:

### 1.2.1 Space Frame:

#### 1.2.1.1 Verification Example 7: 

A space frame is subjected to load on X and Y direction as shown in
figure. The displacements (Ux, Uy, Uz) measured at joint 1 end of the
beam are obtained from the analysis program FeView is compared with
SAP2000 results.

##### + Geometry, Properties and Loading

+----------------------------------+---------------------------------+
| **[Geometry and Loading:]{.ul}** | **[Material Properties:]{.ul}** |
|                                  |                                 |
|                                  | *E* = 30 GPa                    |
|                                  |                                 |
|                                  | *ν* = 0.2                       |
|                                  |                                 |
|                                  | **[Section Properties:]{.ul}**  |
|                                  |                                 |
|                                  | I = 1.33×10^4^ m                |
+----------------------------------+---------------------------------+

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**   **FeView**   **SAP2000**
  ---------------------- ------------ -------------
  U~x,(node\ 1)~ \[m\]   0.0125375    0.012612
  U~y,(node\ 1)~ \[m\]   0.0164007    0.016496
  U~z,(node\ 1)~ \[m\]   -3.74e-06    -3.73E-06

##### + Comparison FeView & SAP2000 deform shape:

  **Shape type**   **FeView**                                                            **SAP2000**
  ---------------- --------------------------------------------------------------------- --------------------------------------------------------------------
  Deform shape     ![](media/image35.png){width="1.9928576115485563in" height="1.8in"}   ![](media/image36.png){width="2.562617016622922in" height="1.8in"}

##### + Download TCL file:

<https://www.dropbox.com/s/it08gq0ps1zf5di/Example_7.tcl?dl=0>

### 1.2.2 Solid:

#### 1.2.2.1 Verification Example 8: 

A Solid simple beam is subjected to load on X and Y direction as shown
in figure. The displacements (Ux, Uy, Uz) measured at joint 1 end of the
beam are obtained from the analysis program FeView is compared with
SAP2000 results.

##### + Geometry, Properties and Loading

+----------------------------------+---------------------------------+
| **[Geometry and Loading:]{.ul}** | **[Material Properties:]{.ul}** |
|                                  |                                 |
|                                  | *E* = 30 GPa                    |
|                                  |                                 |
|                                  | *ν* = 0.2                       |
+----------------------------------+---------------------------------+

##### + Results and Comparison

The most significant results are compared in the table below:

+----------------------+-------------------------+-------------------------+
| **Output Parameter** | **FeView**              | **SAP2000**             |
|                      |                         |                         |
|                      | **(250 brick element)** | **(250 brick element)** |
+======================+=========================+=========================+
| U~z,(max)~ \[m\]     | -0.000481               | -0.000481               |
+----------------------+-------------------------+-------------------------+
| U~y,(node\ 1)~ \[m\] | 0.0164007               | 0.016496                |
+----------------------+-------------------------+-------------------------+
| U~z,(node\ 1)~ \[m\] | -3.74E-06               | -3.73E-06               |
+----------------------+-------------------------+-------------------------+

##### + Comparison FeView & SAP2000 deform shape:

+----------------+-------------------------+-------------------------+
| **Shape type** | **FeView**              | **SAP2000**             |
|                |                         |                         |
|                | **(250 brick element)** | **(250 brick element)** |
+================+=========================+=========================+
| Deform shape   | ![](m                   | ![](                    |
|                | edia/image38.png){width | media/image39.png){widt |
|                | ="2.0857141294838146in" | h="2.621806649168854in" |
|                | height="1.6in"}         | height="1.6in"}         |
+----------------+-------------------------+-------------------------+

##### + Download TCL file:

<https://www.dropbox.com/s/lw1m9xitclbvar2/Example_8.tcl?dl=0>

### 1.2.3 Shell:

#### 1.2.3.1 Example 9: 

A steel angle modled by shell element is loaded as shown in figure. The
maximum displacements is X and Z direction is measured at the loaded
point of the angle are obtained from the analysis program FeView is
compared with SAP2000 results.

##### + Geometry, Properties and Loading

+----------------------------------+---------------------------------+
| **[Geometry and Loading:]{.ul}** | **[Material Properties:]{.ul}** |
|                                  |                                 |
|                                  | *E* = 200 GPa                   |
|                                  |                                 |
|                                  | *ν* = 0.3                       |
|                                  |                                 |
|                                  | **[Section Properties:]{.ul}**  |
|                                  |                                 |
|                                  | Shell thickness = 0.02 m        |
+----------------------------------+---------------------------------+

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**   **FeView**   **SAP2000**
  ---------------------- ------------ -------------
  U~x,(max)~ \[m\]       0.0034       0.0034
  U~z,(max1)~ \[m\]      -0.0029      -0.0029

##### + Comparison FeView & SAP2000 deform shape:

  Shape type     FeView                                                                SAP2000
  -------------- --------------------------------------------------------------------- --------------------------------------------------------------------
  Deform shape   ![](media/image41.png){width="1.9365419947506561in" height="1.5in"}   ![](media/image42.png){width="2.187097550306212in" height="1.5in"}

##### + Download TCL file:

<https://www.dropbox.com/s/9v1rr8qqt1aj585/Example_9.tcl?dl=0>

### 1.2.4 Space Truss:

#### 1.2.4.1 Verification Example 10: 

A steel space truss is loaded in X and Z direction at joint 1.. The
displacements is X and Z direction is measured at joint 1 of the truss
obtained from the analysis program FeView is compared with SAP2000
results.

##### + Geometry, Properties and Loading

+----------------------------------+---------------------------------+
| **[Geometry and Loading:]{.ul}** | **[Material Properties:]{.ul}** |
|                                  |                                 |
|                                  | *E* = 200 GPa                   |
|                                  |                                 |
|                                  | **[Section Properties:]{.ul}**  |
|                                  |                                 |
|                                  | A = 0.001 m2                    |
+----------------------------------+---------------------------------+

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**   **FeView**   **SAP2000**
  ---------------------- ------------ -------------
  U~x,(node\ 1)~ \[m\]   3.40E-4      3.40E-4
  U~z,(node\ 1)~ \[m\]   -9.54E-5     -9.54e-5

##### + Comparison FeView & SAP2000 deform shape:

  Shape type     FeView                                                               SAP2000
  -------------- -------------------------------------------------------------------- --------------------------------------------------------------------
  Deform shape   ![](media/image44.png){width="2.223312554680665in" height="1.8in"}   ![](media/image45.png){width="2.423708442694663in" height="1.8in"}

##### + Download TCL file:

<https://www.dropbox.com/s/jla5tp5yjpxm8j6/Example_10.tcl?dl=0>

# 2. Verification (Modal Analysis):

## 2.1 Two Dimensional Problem:

### 2.1.1 Plane Frame:

#### 2.1.1.1 Verification Example 11: 

A ten bay, nine story, two dimensional frame structure solved in Bathe
and Wilson (1972) is analyzed for the first three eigenvalues. The
material and section properties, and the mass per unit length used for
all members, as shown below, are consistent with those used in the
above-mentioned reference.

The results obtained with the FE analysis program FeView are compared
with SAP2000 results.

##### + Geometry, Properties

+----------------------+---------------------------------+
| **[Geometry:]{.ul}** | **[Material Properties:]{.ul}** |
|                      |                                 |
|                      | *E = 20.6832410 GPa*            |
|                      |                                 |
|                      | **[Section Properties:]{.ul}**  |
|                      |                                 |
|                      | A = 0.279 m2                    |
|                      |                                 |
|                      | I = 0.008631 m4                 |
+----------------------+---------------------------------+

##### + Loading/Modeling

The frame objects are modeled through elastic frame elements with
specified Mass/Length\^3 = 514.81 ton/m3.

All the base nodes are fully restrained.

The FE model is presented below:

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**                 **GiD+OpenSees**   **SAP2000**
  ------------------------------------ ------------------ -------------
  Frequency F~1~ \[Hz\] (1^st^ mode)   0.122              0.122
  Frequency T~1~ \[Hz\] (2^nd^ mode)   0.375              0.375
  Frequency T~1~ \[Hz\] (3^rd^ mode)   0.652              0.0.652

##### + Comparison FeView & SAP2000 deform shape:

  **Mode**   **FeView**                                                            **SAP2000**
  ---------- --------------------------------------------------------------------- ---------------------------------------------------------------------
  1          ![](media/image48.png){width="2.552694663167104in" height="1.45in"}   ![](media/image49.png){width="2.987584208223972in" height="1.45in"}
  2          ![](media/image50.png){width="2.55in" height="1.37372375328084in"}    ![](media/image51.png){width="3.0in" height="1.3996784776902886in"}
  3          ![](media/image52.png){width="2.55in" height="1.37372375328084in"}    ![](media/image53.png){width="3.0in" height="1.4208344269466318in"}

##### + Download TCL file:

<https://www.dropbox.com/s/v09o6t13w8e7uw2/Example_11.tcl?dl=0>

### 2.1.2 Plane Truss:

#### 2.1.2.1 Verification Example 12: 

Example 4 with material density 7850 kg/m3 is considered for this
example analysed for the first three mode.

The results obtained with the FE analysis program FeView are compared
with ABAQUS results.

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**                 **FeView**   **ABAQUS**
  ------------------------------------ ------------ ------------
  Frequency F~1~ \[Hz\] (1^st^ mode)   44.661       44.661
  Frequency F~2~ \[Hz\] (2^nd^ mode)   82.732       82.732
  Frequency F~3~ \[Hz\] (3^rd^ mode)   174.04       174.04

##### + Comparison FeView & SAP2000 deform shape:

  **Mode**   **FeView**                                                            **ABAQUS**
  ---------- --------------------------------------------------------------------- ---------------------------------------------------------------------------------------------
  1          ![](media/image54.png){width="2.731061898512686in" height="1.4in"}    ![F:\\Download\\mode1.png](media/image55.png){width="2.042826990376203in" height="1.4in"}
  2          ![](media/image56.png){width="2.73in" height="1.375663823272091in"}   ![F:\\Download\\mode2.png](media/image57.png){width="2.04in" height="1.3196391076115486in"}
  3          ![](media/image58.png){width="2.73in" height="1.335845363079615in"}   ![F:\\Download\\mode3.png](media/image59.png){width="2.04in" height="1.2623272090988626in"}

##### + Download TCL file:

<https://www.dropbox.com/s/9zbd32k4zn7qgie/Example_12.tcl?dl=0>

### 2.1.3 Plane:

#### 2.1.3.1 Verification Example 13: 

In this example we consider an analysis of the Koyna dam which is
modelled by plain strain element and analysed for the first three mode.

The results obtained with the FE analysis program FeView are compared
with SAP2000 results.

##### + Geometry, Properties

+----------------------+---------------------------------+
| **[Geometry:]{.ul}** | **[Material Properties:]{.ul}** |
|                      |                                 |
|                      | *E = 31.027 GPa*                |
|                      |                                 |
|                      | ![](media/image1.gif)* *= 0.15  |
|                      |                                 |
|                      | *ρ* = 2643 kg/m3                |
|                      |                                 |
|                      | **[Section Properties:]{.ul}**  |
|                      |                                 |
|                      | Plane element thickness = 1 m   |
+----------------------+---------------------------------+

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**             **FeView**   **SAP2000**
  -------------------------------- ------------ -------------
  Frequency F1 \[Hz\] (1st mode)   3.057        3.057
  Frequency F2 \[Hz\] (2nd mode)   8.133        8.134
  Frequency F3 \[Hz\] (3rd mode)   10.977       0.0.652

##### + Comparison FeView & SAP2000 deform shape:

  **Mode**   **FeView**                                                            **SAP2000**
  ---------- --------------------------------------------------------------------- ---------------------------------------------------------------------
  1          ![](media/image61.png){width="2.464219160104987in" height="2.5in"}    ![](media/image62.png){width="3.0195483377077865in" height="2.5in"}
  2          ![](media/image63.png){width="2.46in" height="2.499756124234471in"}   ![](media/image64.png){width="2.7277919947506564in" height="2.5in"}
  3          ![](media/image65.png){width="2.46in" height="2.545521653543307in"}   ![](media/image66.png){width="2.7298851706036746in" height="2.5in"}

##### + Download TCL file:

<https://www.dropbox.com/s/s7jnuychejwfbs0/Example_13.tcl?dl=0>

## 2.2 Three Dimensional Problem:

### 2.2.1 Space Frame:

#### 2.2.1.1 Verification Example 14: 

A two-story, two- bay, three-dimensional frame structure is analyzed for
its four natural frequencies. The structure is doubly symmetric in plan,
except that the center of mass at each story level is eccentric, as
shown in the figure below. The entire story mass is applied at these
joints in the X and Y directions only.

The FeView results are compared with SAP2000 results.

##### + Geometry, Properties

+----------------------+---------------------------------+
| **[Geometry:]{.ul}** | **[Material Properties:]{.ul}** |
|                      |                                 |
|                      | *E = 16.757256 GPa (column)*    |
|                      |                                 |
|                      | *E = 23.938937 GPa (beam)*      |
|                      |                                 |
|                      | **[Column Properties:]{.ul}**   |
|                      |                                 |
|                      | *I* = 0.3716 m^2^               |
|                      |                                 |
|                      | *I~22~* = I33 = 0.010789 m^4^   |
|                      |                                 |
|                      | **[Beam Properties:]{.ul}**     |
|                      |                                 |
|                      | *A* = 0.4645 m^2^               |
|                      |                                 |
|                      | *I~22~* = 0.02253 m^4^          |
|                      |                                 |
|                      | *I~33~* = 0.01381 m^4^          |
+----------------------+---------------------------------+

##### + Loading/Modeling

A lumped mass is applied to joints 28 and 29 with a value of 90.64566
ton in the X and Y directions. Two rigid diaphragm constraints are
introduced (one at each floor level). All the base nodes are fully
restrained.

The FE model is presented below:

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**             **Output Parameter**   **FeView**   **SAP2000**
  -------------------------------- ---------------------- ------------ -------------
  Frequency F1 \[Hz\] (1st mode)   U~x,(node\ 1)~ \[m\]   0.0125375    0.012612
  Frequency F2 \[Hz\] (2nd mode)   U~y,(node\ 1)~ \[m\]   0.0164007    0.016496
  Frequency F3 \[Hz\] (3rd mode)   U~z,(node\ 1)~ \[m\]   -3.74e-06    -3.73E-06

##### + Comparison FeView & SAP2000 deform shape:

  **Mode**   **FeView**                                                            **SAP2000**
  ---------- --------------------------------------------------------------------- ---------------------------------------------------------------------
  1          ![](media/image69.png){width="2.021596675415573in" height="1.8in"}    ![](media/image70.png){width="2.430206692913386in" height="1.8in"}
  2          ![](media/image71.png){width="1.9910826771653543in" height="1.8in"}   ![](media/image72.png){width="2.366742125984252in" height="1.8in"}
  3          ![](media/image73.png){width="2.06919728783902in" height="1.8in"}     ![](media/image74.png){width="2.4080544619422573in" height="1.8in"}

##### + Download TCL file:

<https://www.dropbox.com/s/9utmgm698dhpuhd/Example_14.tcl?dl=0>

### 2.2.2 Solid:

#### 2.2.2.1 Verification Example 15: 

Example 8 with material density 2400 kg/m3 is considered for this
example and analysed for the first three modes.

The results obtained with the FE analysis program FeView are compared
with SAP2000 results..

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**           **FeView**   **SAP2000**
  ------------------------------ ------------ -------------
  Period T~1~ \[s\] (1st mode)   0.0120       0.0121
  Period T~2~ \[s\] (2nd mode)   0.0120       0.0121
  Period T~3~ \[s\] (3rd mode)   0.0046       0.0049

##### + Comparison FeView & SAP2000 deform shape:

  **Mode**   **FeView**                                                             **SAP2000**
  ---------- ---------------------------------------------------------------------- ----------------------------------------------------------------------
  1          ![](media/image75.png){width="2.129511154855643in" height="1.5in"}     ![](media/image76.png){width="2.316666666666667in" height="1.5in"}
  2          ![](media/image77.png){width="2.13in" height="1.3281200787401575in"}   ![](media/image78.png){width="2.0210050306211724in" height="1.33in"}
  3          ![](media/image79.png){width="2.13in" height="1.4765748031496062in"}   ![](media/image80.png){width="2.2552373140857394in" height="1.48in"}

##### + Download TCL file:

<https://www.dropbox.com/s/41e1cxxy8kzhavj/Example_15.tcl?dl=0>

### 2.2.3 Shell:

#### 2.2.3.1 Verification Example 16: 

Example 9 with material density 7850 kg/m3 is considered for this
example and analysed for the first three modes.

The results obtained with the FE analysis program FeView are compared
with SAP2000 results..

##### + Results and Comparison

The most significant results are compared in the table below:

  **Output Parameter**         **FeView**   **SAP2000**
  ---------------------------- ------------ -------------
  Period T1 \[s\] (1st mode)   0.0045       0.0045
  Period T2 \[s\] (2nd mode)   0.0018       0.0017
  Period T3 \[s\] (3rd mode)   0.0011       0.0011

##### + Comparison FeView & SAP2000 deform shape:

  Mode   FeView                                                                SAP2000
  ------ --------------------------------------------------------------------- ----------------------------------------------------------------------
  1      ![](media/image81.png){width="2.2in" height="1.841165791776028in"}    ![](media/image82.png){width="2.6949496937882764in" height="1.84in"}
  2      ![](media/image83.png){width="2.2in" height="1.9255446194225723in"}   ![](media/image84.png){width="2.7988320209973754in" height="1.93in"}
  3      ![](media/image85.png){width="2.2in" height="1.9255446194225723in"}   ![](media/image86.png){width="2.888568460192476in" height="1.93in"}

##### + Download TCL file:

<https://www.dropbox.com/s/lcdhco2f4q6rn4l/Example_16.tcl?dl=0>

### 2.2.4 Space Truss:

#### 2.2.4.1 Verification Example 17: 

Example 10 with material density 7850 kg/m3 is considered for this
example and analysed for the first three modes.

The results obtained with the FE analysis program FeView are compared
with SAP2000 results..

##### + Results and Comparison

The most significant results are compared in the table below:

  Output Parameter             **FeView**   **SAP2000**
  ---------------------------- ------------ -------------
  Period T1 \[s\] (1st mode)   0.01148      0.01148
  Period T2 \[s\] (2nd mode)   0.00862      0.00862
  Period T3 \[s\] (3rd mode)   0.00347      0.00347

##### + Comparison FeView & SAP2000 deform shape:

  **Mode**   **FeView**                                                            **SAP2000**
  ---------- --------------------------------------------------------------------- ----------------------------------------------------------------------
  1          ![](media/image87.png){width="2.2in" height="1.8488888888888888in"}   ![](media/image88.png){width="2.8836297025371826in" height="1.85in"}
  2          ![](media/image89.png){width="2.2in" height="2.129880796150481in"}    ![](media/image90.png){width="3.1724989063867017in" height="2.13in"}
  3          ![](media/image91.png){width="2.2in" height="2.173494094488189in"}    ![](media/image92.png){width="3.0617814960629923in" height="2.17in"}

##### + Download TCL file:

<https://www.dropbox.com/s/2etybjd3md1i4y6/Example_17.tcl?dl=0>
