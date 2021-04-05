[[FeView]](https://www.kim2kie.com/3_ach/FeView/FeView_webpage/FeView.php) 
[[SSL]](https://www.kim2kie.com) 

# FeView
FeView: A tool for finite element model (FEM) visualization and post-processing for OpenSees

<img align="right" src="https://github.com/motiurce/FeView/blob/5e5c3ab4463bce8f387f22f3e7d1034463a15923/FeView_LogoL.png" width=100px>
FeView (v1.0) Interface introduces a graphical user interface (GUI) for the popular open source finite element software OpenSees.

## Interactive Interface:

<p align="center">
<img src=https://github.com/motiurce/FeView/blob/5e5c3ab4463bce8f387f22f3e7d1034463a15923/20_story_building.png width=800px>
</p>
<p align="center">
Render view of a 20 story building
 </p>
<p align="center">
<img src=https://github.com/motiurce/FeView/blob/5e5c3ab4463bce8f387f22f3e7d1034463a15923/Soil_Foundation_Brick_Element.png width=800px>
</p>
<p align="center">
Deformation shape with undiform wire mesh view
 </p>
 
## Programming Language
Python 3.7
## Dependencies and its insrallation:
1. PyQt5==5.15.0
2. PyVista==0.25.3 & pyvistaqt==0.1.1
3. numpy==1.18.0
4. pandas==1.0.5
5.  matplotlib==3.2.0
6. xlwt==1.3.0
7. eqsig==1.2.0
### Install dependencies by the folloing command
```
pip install -r requirements.txt
```
## Running FeView
Firstly go to FeView folder >>
```
cd FeView
```
Run FeView
```
Python FeView.py
```
## Features of FeView
### Material: 
Support all types of material available in OpenSees (Version 3.2.1 64-Bit) 
### Analysis type: 
1. Static/pushover analysis
2. Modal Analysis
3. Transient analysis 
### Element type: Current version of FeView support 46 types of elements as listed
Beam-Column Elements >	
1. elasticBeamColumn
2. ElasticTimoshenkoBeam
3. forceBeamColumn
4. dispBeamColumn
5. dispBeamColumnInt
6. MVLEM
7. SFI_MVLEM
Quadrilateral Elements >	
1. quad
2. ShellMITC4
3. ShellDKGQ
4. ShellNLDKGQ
5. ShellNL
6. bbarQuad
7. enhancedQuad
8. SSPquad
9. VS3D4
10. AV3D4
Bearing Elements	> 
1. elastomericBearingPlasticity
2. elastomericBearingBoucWen
3. flatSliderBearing, 
4. singleFPBearing
5. TFP
6. TripleFrictionPendulum
7. multipleShearSpring
8. KikuchiBearing
9. YamamotoBiaxialHDR
10. ElastomericX
11. LeadRubberX
12. HDR
13. RJWatsonEqsBearing
14. FPBearingPTV
Brick Elements >	
1. stdBrick
2. bbarBrick
3. SSPbrick
4. brickUP
5. AC3D8
6. ASI3D8
7. bbarBrickWithSensitivity
Triangular Elements >
1. Tri31
2. ShellDKGT
3. ShellNLDKGT
Cable Elements >
1. CatenaryCable
Tetrahedron Elements >
1. FourNodeTetrahedron
Link Elements >	
1. twoNodeLink
Truss Element >	
1. truss
2. corotTruss
Note: As FeView is case sensitive user need to write exact element name as listed above.
### Recorder setting:
#### For 2D problem
```
recorder Node -file Node_displacements.out -time -nodeRange $1stNode $lastNode -dof 1 2 disp
recorder Node -file Node_rotations.out -time -nodeRange $1stNode $lastNode -dof 3 disp
recorder Node -file Node_forceReactions.out -time -nodeRange $1stNode $lastNode -dof 1 2 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange $1stNode $lastNode -dof 3 reaction
recorder Node -file Node_accelerations.out -time -nodeRange $1stNode $lastNode -dof 1 2 accel
recorder Node -file Node_velocities.out -time -nodeRange $1stNode $lastNode -dof 1 2 vel
```
#### For 3D problem
```
recorder Node -file Node_displacements.out -time -nodeRange $1stNode $lastNode -dof 1 2 3 disp
recorder Node -file Node_rotations.out -time -nodeRange $1stNode $lastNode -dof 4 5 6 disp
recorder Node -file Node_forceReactions.out -time -nodeRange $1stNode $lastNode -dof 1 2 3 reaction
recorder Node -file Node_momentReactions.out -time -nodeRange $1stNode $lastNode -dof 4 5 6 reaction
recorder Node -file Node_accelerations.out -time -nodeRange $1stNode $lastNode-dof 1 2 3 accel
recorder Node -file Node_velocities.out -time -nodeRange $1stNode $lastNode -dof 1 2 3 vel
```
Note: Current versin of FeView support only nodal responses. User need to define recorder as in above. Just replace $1stNode and $lastNode node as your pboblem.
### Mode number:
For eigenvalue analysis as prerequisit of FeView set mode number as>
```
set numModes 3
```

## Fore more detauils visit>> Manual>> Examples>>
https://www.kim2kie.com/3_ach/FeView/FeView_webpage/FeView.php
