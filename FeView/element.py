from OpenTCLFile import *
def element_info(TCLFile):
    # Brick element
    elemInfo_stdBrick = OpenSeesTclRead(TCLFile, 'element stdBrick', 11)
    elemInfo_bbarBrick = OpenSeesTclRead(TCLFile, 'element bbarBrick', 11)
    elemInfo_SSPbrick = OpenSeesTclRead(TCLFile, 'element SSPbrick', 11)
    # Beam Column Elements
    elemInfo_elasticBeamColumn = OpenSeesTclRead(TCLFile, 'element elasticBeamColumn', 5)
    elemInfo_ElasticTimoshenkoBeam = OpenSeesTclRead(TCLFile, 'element ElasticTimoshenkoBeam', 5)
    elemInfo_beamWithHinges = OpenSeesTclRead(TCLFile, 'element beamWithHinges', 5)
    elemInfo_dispBeamColumn = OpenSeesTclRead(TCLFile, 'element dispBeamColumn', 5)
    elemInfo_forceBeamColumn = OpenSeesTclRead(TCLFile, 'element forceBeamColumn', 5)
    elemInfo_dispBeamColumnInt = OpenSeesTclRead(TCLFile, 'element dispBeamColumnInt', 5)
    elemInfo_MVLEM = OpenSeesTclRead(TCLFile, 'element MVLEM', 5)
    elemInfo_SFI_MVLEM = OpenSeesTclRead(TCLFile, 'element SFI_MVLEM', 5)
    # Link Elements
    elemInfo_twoNodeLink = OpenSeesTclRead(TCLFile, 'element twoNodeLink', 5)
    # Bearing Elements
    elemInfo_elastomericBearingPlasticity = OpenSeesTclRead(TCLFile, 'element elastomericBearingPlasticity', 5)
    elemInfo_elastomericBearingBoucWen = OpenSeesTclRead(TCLFile, 'element elastomericBearingBoucWen', 5)
    elemInfo_flatSliderBearing = OpenSeesTclRead(TCLFile, 'element flatSliderBearing', 5)
    elemInfo_singleFPBearing = OpenSeesTclRead(TCLFile, 'element singleFPBearing', 5)
    elemInfo_TripleFrictionPendulum = OpenSeesTclRead(TCLFile, 'element TripleFrictionPendulum', 5)
    elemInfo_multipleShearSpring = OpenSeesTclRead(TCLFile, 'element multipleShearSpring', 5)
    elemInfo_KikuchiBearing = OpenSeesTclRead(TCLFile, 'element KikuchiBearing', 5)
    elemInfo_YamamotoBiaxialHDR = OpenSeesTclRead(TCLFile, 'element YamamotoBiaxialHDR', 5)
    elemInfo_ElastomericX = OpenSeesTclRead(TCLFile, 'element ElastomericX', 5)
    elemInfo_LeadRubberX = OpenSeesTclRead(TCLFile, 'element LeadRubberX', 5)
    elemInfo_HDR = OpenSeesTclRead(TCLFile, 'element HDR', 5)
    elemInfo_RJWatsonEqsBearing = OpenSeesTclRead(TCLFile, 'element RJWatsonEqsBearing', 5)
    elemInfo_FPBearingPTV = OpenSeesTclRead(TCLFile, 'element FPBearingPTV', 5)
    # Shell Elements
    elemInfo_ShellMITC4 = OpenSeesTclRead(TCLFile, 'element ShellMITC4', 7)
    elemInfo_ShellDKGQ = OpenSeesTclRead(TCLFile, 'element ShellDKGQ', 7)
    elemInfo_ShellNLDKGQ = OpenSeesTclRead(TCLFile, 'element ShellNLDKGQ', 7)
    elemInfo_ShellNL = OpenSeesTclRead(TCLFile, 'element ShellNL', 7)
    # Quadrilateral Elements
    elemInfo_quad = OpenSeesTclRead(TCLFile, 'element quad', 7)
    elemInfo_bbarQuad = OpenSeesTclRead(TCLFile, 'element bbarQuad', 7)
    elemInfo_enhancedQuad = OpenSeesTclRead(TCLFile, 'element enhancedQuad', 7)
    elemInfo_SSPquad = OpenSeesTclRead(TCLFile, 'element SSPquad', 7)
    # u-p Elements
    elemInfo_brickUP = OpenSeesTclRead(TCLFile, 'element brickUP', 11)
    # acoustic elements
    elemInfo_AC3D8 = OpenSeesTclRead(TCLFile, 'element AC3D8', 11)
    # acoustic-structure interface elements
    elemInfo_ASI3D8 = OpenSeesTclRead(TCLFile, 'element ASI3D8', 11)
    # CatenaryCable Element
    elemInfo_CatenaryCable = OpenSeesTclRead(TCLFile, 'element CatenaryCable', 5)
    # Truss Elements
    elemInfo_truss = OpenSeesTclRead(TCLFile, 'element truss', 5)
    elemInfo_corotTruss = OpenSeesTclRead(TCLFile, 'element corotTruss', 5)
    #tetrahedron
    elemInfo_FourNodeTetrahedron = OpenSeesTclRead(TCLFile, 'elemnt FourNodeTetrahedron', 7)
    #triangle
    elemInfo_tri31 = OpenSeesTclRead(TCLFile, 'element tri31', 6)
    elemInfo_ShellDKGT = OpenSeesTclRead(TCLFile, 'element ShellDKGT', 6)
    elemInfo_ShellNLDKGT  = OpenSeesTclRead(TCLFile, 'element ShellNLDKGT', 6)

    # Element for Sensitivity Computation
    elemInfo_dispBeamColumnWithSensitivity = OpenSeesTclRead(TCLFile, 'element dispBeamColumnWithSensitivity', 5)
    elemInfo_quadWithSensitivity = OpenSeesTclRead(TCLFile, 'element quadWithSensitivity', 7)
    elemInfo_bbarBrickWithSensitivity = OpenSeesTclRead(TCLFile, 'element bbarBrickWithSensitivity', 11)

    # Misc. Element
    elemInfo_VS3D4  = OpenSeesTclRead(TCLFile, 'element VS3D4 ', 7)
    elemInfo_AV3D4 = OpenSeesTclRead(TCLFile, 'element AV3D4 ', 7)










    return elemInfo_stdBrick, elemInfo_bbarBrick, elemInfo_SSPbrick, elemInfo_elasticBeamColumn,\
           elemInfo_ElasticTimoshenkoBeam, elemInfo_beamWithHinges, elemInfo_dispBeamColumn, elemInfo_forceBeamColumn,\
           elemInfo_dispBeamColumnInt, elemInfo_MVLEM, elemInfo_SFI_MVLEM, elemInfo_twoNodeLink, \
           elemInfo_elastomericBearingPlasticity, elemInfo_elastomericBearingBoucWen, elemInfo_flatSliderBearing,\
           elemInfo_singleFPBearing, elemInfo_TripleFrictionPendulum, elemInfo_multipleShearSpring, \
           elemInfo_KikuchiBearing, elemInfo_YamamotoBiaxialHDR, elemInfo_ElastomericX, elemInfo_LeadRubberX, \
           elemInfo_HDR, elemInfo_RJWatsonEqsBearing, elemInfo_FPBearingPTV, elemInfo_ShellMITC4,elemInfo_ShellDKGQ,\
           elemInfo_ShellNLDKGQ, elemInfo_ShellNL, elemInfo_quad, elemInfo_bbarQuad, elemInfo_enhancedQuad, \
           elemInfo_SSPquad, elemInfo_brickUP, elemInfo_AC3D8, elemInfo_ASI3D8, elemInfo_CatenaryCable, elemInfo_truss, \
           elemInfo_corotTruss, elemInfo_FourNodeTetrahedron, elemInfo_tri31, elemInfo_ShellDKGT, elemInfo_ShellNLDKGT, \
           elemInfo_dispBeamColumnWithSensitivity, elemInfo_quadWithSensitivity, elemInfo_bbarBrickWithSensitivity, \
           elemInfo_VS3D4, elemInfo_AV3D4



def total_element(TCLFile):
    t_element = OpenSeesTclRead(TCLFile, 'element', 2)
    t_element_num=str(len(t_element[:,0]))
    return t_element_num