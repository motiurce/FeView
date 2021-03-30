from nodes import*
from element import*
from frame import*
from quad_shell import *
from triangle import*
from tetrahedron import*
from brick import*
import numpy as np
import pyvista as pv


def plotter(p,TCLFile,showType,NodeCoord,scalars,stitle):
    offset = np.array([0, 0])
    elemInfo_stdBrick, elemInfo_bbarBrick, elemInfo_SSPbrick, elemInfo_elasticBeamColumn,\
    elemInfo_ElasticTimoshenkoBeam, elemInfo_beamWithHinges, elemInfo_dispBeamColumn, elemInfo_forceBeamColumn,\
    elemInfo_dispBeamColumnInt, elemInfo_MVLEM, elemInfo_SFI_MVLEM, elemInfo_twoNodeLink, \
    elemInfo_elastomericBearingPlasticity, elemInfo_elastomericBearingBoucWen, elemInfo_flatSliderBearing,\
    elemInfo_singleFPBearing, elemInfo_TripleFrictionPendulum, elemInfo_multipleShearSpring, \
    elemInfo_KikuchiBearing, elemInfo_YamamotoBiaxialHDR, elemInfo_ElastomericX, elemInfo_LeadRubberX, \
    elemInfo_HDR, elemInfo_RJWatsonEqsBearing, elemInfo_FPBearingPTV, elemInfo_ShellMITC4,elemInfo_ShellDKGQ,\
    elemInfo_ShellNLDKGQ, elemInfo_ShellNL, elemInfo_quad, elemInfo_bbarQuad, elemInfo_enhancedQuad, \
    elemInfo_SSPquad, elemInfo_brickUP, elemInfo_AC3D8, elemInfo_ASI3D8, elemInfo_CatenaryCable, elemInfo_truss, \
    elemInfo_corotTruss, elemInfo_FourNodeTetrahedron, elemInfo_tri31, elemInfo_ShellDKGT, elemInfo_ShellNLDKGT,\
    elemInfo_dispBeamColumnWithSensitivity,elemInfo_quadWithSensitivity, elemInfo_bbarBrickWithSensitivity,\
    elemInfo_VS3D4, elemInfo_AV3D4=element_info(TCLFile)

    sargs = dict(title_font_size=10,label_font_size=10, n_labels=5,italic=True,font_family="arial",color='k')
    if (elemInfo_stdBrick.size > 0):
        cells = brick_cell(elemInfo_stdBrick,  node(TCLFile))
        cell_type = (cell_type_brick(elemInfo_stdBrick))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)

        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='cyan', cmap="jet", show_edges=True, opacity=1,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='cyan', cmap="jet", show_edges=False, opacity=1,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe', line_width=0.1)


    if (elemInfo_bbarBrick.size > 0):
        cells = brick_cell(elemInfo_bbarBrick,  node(TCLFile))
        cell_type = (cell_type_brick(elemInfo_bbarBrick))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)

        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='g', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='g', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_SSPbrick.size > 0):
        cells = brick_cell(elemInfo_SSPbrick,  node(TCLFile))
        cell_type = (cell_type_brick(elemInfo_SSPbrick))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='lime', cmap="jet", show_edges=True,  annotations='r',scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='lime', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_elasticBeamColumn.size > 0):
        cells = frame_cell(elemInfo_elasticBeamColumn, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_elasticBeamColumn))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='seagreen',cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='seagreen', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_ElasticTimoshenkoBeam.size > 0):
        cells = frame_cell(elemInfo_ElasticTimoshenkoBeam, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_ElasticTimoshenkoBeam))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='pink',cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='pink',cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_beamWithHinges.size > 0):
        cells = frame_cell(elemInfo_beamWithHinges, node(TCLFile))

        cell_type = (cell_type_frame(elemInfo_beamWithHinges))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='turquoise',cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='turquoise', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_dispBeamColumn.size > 0):
        cells = frame_cell(elemInfo_dispBeamColumn, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_dispBeamColumn))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='purple', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='purple', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', cmap="jet", show_edges=True, style='wireframe')

    if (elemInfo_forceBeamColumn.size > 0):
        cells = frame_cell(elemInfo_forceBeamColumn, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_forceBeamColumn))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='violet', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='violet', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_dispBeamColumnInt.size > 0):
        cells = frame_cell(elemInfo_dispBeamColumnInt, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_dispBeamColumnInt))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='navy', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='navy', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_MVLEM.size > 0):
        cells = frame_cell(elemInfo_MVLEM, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_MVLEM))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='deeppink', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='deeppink', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_SFI_MVLEM.size > 0):
        cells = frame_cell(elemInfo_SFI_MVLEM, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_SFI_MVLEM))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='indigo', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='indigo', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_twoNodeLink.size > 0):
        cells = frame_cell(elemInfo_twoNodeLink, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_twoNodeLink))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='orchid', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='orchid', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_elastomericBearingPlasticity.size > 0):
        cells = frame_cell(elemInfo_elastomericBearingPlasticity, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_elastomericBearingPlasticity))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='cornflowerblue', cmap="jet", show_edges=True, line_width=15 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='cornflowerblue', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_elastomericBearingBoucWen.size > 0):
        cells = frame_cell(elemInfo_elastomericBearingBoucWen, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_elastomericBearingBoucWen))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='slateblue', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='slateblue', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_flatSliderBearing.size > 0):
        cells = frame_cell(elemInfo_flatSliderBearing, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_flatSliderBearing))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='dodgerblue', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='dodgerblue', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_singleFPBearing.size > 0):
        cells = frame_cell(elemInfo_singleFPBearing, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_singleFPBearing))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='steelblue', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='steelblue', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_TripleFrictionPendulum.size > 0):
        cells = frame_cell(elemInfo_TripleFrictionPendulum, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_TripleFrictionPendulum))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='deepskyblue', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='deepskyblue', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_multipleShearSpring.size > 0):
        cells = frame_cell(elemInfo_multipleShearSpring, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_multipleShearSpring))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='teal', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='teal', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_KikuchiBearing.size > 0):
        cells = frame_cell(elemInfo_KikuchiBearing, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_KikuchiBearing))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='cadetblue', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='cadetblue', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_YamamotoBiaxialHDR.size > 0):
        cells = frame_cell(elemInfo_YamamotoBiaxialHDR, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_YamamotoBiaxialHDR))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='yellowgreen', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='yellowgreen', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_ElastomericX.size > 0):
        cells = frame_cell(elemInfo_ElastomericX, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_ElastomericX))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='greenyellow', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='greenyellow', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_LeadRubberX.size > 0):
        cells = frame_cell(elemInfo_LeadRubberX, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_LeadRubberX))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='olivedrab', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='olivedrab', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_HDR.size > 0):
        cells = frame_cell(elemInfo_HDR, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_HDR))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='peru', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='peru', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_RJWatsonEqsBearing.size > 0):
        cells = frame_cell(elemInfo_RJWatsonEqsBearing, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_RJWatsonEqsBearing))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='tomato', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='tomato', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_FPBearingPTV.size > 0):
        cells = frame_cell(elemInfo_FPBearingPTV, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_FPBearingPTV))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='darkred', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='darkred', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_ShellMITC4.size > 0):
        cells = quad_cell(elemInfo_ShellMITC4, node(TCLFile))
        cell_type = (cell_type_quad(elemInfo_ShellMITC4))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='brown', cmap="jet", show_edges=True,  opacity=1,scalars=scalars,stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='brown', cmap="jet", show_edges=False,opacity=1, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe', line_width=0.1)

    if (elemInfo_ShellDKGQ.size > 0):
        cells = quad_cell(elemInfo_ShellDKGQ, node(TCLFile))
        cell_type = (cell_type_quad(elemInfo_ShellDKGQ))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='lightcoral', cmap="jet", show_edges=True,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='lightcoral', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_ShellNLDKGQ.size > 0):
        cells = quad_cell(elemInfo_ShellNLDKGQ, node(TCLFile))
        cell_type = (cell_type_quad(elemInfo_ShellNLDKGQ))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='coral', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='coral', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_ShellNL.size > 0):
        cells = quad_cell(elemInfo_ShellNL, node(TCLFile))
        cell_type = (cell_type_quad(elemInfo_ShellNL))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='salmon', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='salmon', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_quad.size > 0):
        cells = quad_cell(elemInfo_quad, node(TCLFile))
        cell_type = (cell_type_quad(elemInfo_quad))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='b', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='b', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_bbarQuad.size > 0):
        cells = quad_cell(elemInfo_bbarQuad, node(TCLFile))
        cell_type = (cell_type_quad(elemInfo_bbarQuad))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='skyblue', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='skyblue', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_enhancedQuad.size > 0):
        cells = quad_cell(elemInfo_enhancedQuad, node(TCLFile))
        cell_type = (cell_type_quad(elemInfo_enhancedQuad))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='lightgreen', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='lightgreen', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_SSPquad.size > 0):
        cells = quad_cell(elemInfo_SSPquad, node(TCLFile))
        cell_type = (cell_type_quad(elemInfo_SSPquad))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='mediumpurple', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='mediumpurple', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_brickUP.size > 0):
        cells = brick_cell(elemInfo_brickUP,  node(TCLFile))
        cell_type = (cell_type_brick(elemInfo_brickUP))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='silver', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='silver', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_AC3D8.size > 0):
        cells = brick_cell(elemInfo_AC3D8,  node(TCLFile))
        cell_type = (cell_type_brick(elemInfo_AC3D8))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='lightgray', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='lightgray', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')


    if (elemInfo_ASI3D8.size > 0):
        cells = brick_cell(elemInfo_ASI3D8,  node(TCLFile))
        cell_type = (cell_type_brick(elemInfo_ASI3D8))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='mintcream', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='mintcream', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_CatenaryCable.size > 0):
        cells = frame_cell(elemInfo_CatenaryCable, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_CatenaryCable))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='gold', cmap="jet", show_edges=True, line_width=1 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='gold', cmap="jet", show_edges=False, line_width=1, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_truss.size > 0):
        cells = frame_cell(elemInfo_truss, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_truss))
        grid = pv.UnstructuredGrid(offset, cells, cell_type,NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='b', cmap="jet", show_edges=True, line_width=1 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='b',  cmap="jet",show_edges=False, line_width=1, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_corotTruss.size > 0):
        cells = frame_cell(elemInfo_corotTruss, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_corotTruss))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='darkkhaki', cmap="jet", show_edges=True, line_width=1 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='darkkhaki', cmap="jet", show_edges=False, line_width=1, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_FourNodeTetrahedron.size > 0):
        cells = tetra4_cell(elemInfo_FourNodeTetrahedron,  node(TCLFile))
        cell_type = (cell_type_tetra4(elemInfo_FourNodeTetrahedron))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='aqua', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='aqua', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_tri31.size > 0):
        cells = tri_cell(elemInfo_tri31,  node(TCLFile))
        cell_type = (cell_type_tri(elemInfo_tri31))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='c', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='c', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_ShellDKGT.size > 0):
        cells = tri_cell(elemInfo_ShellDKGT,  node(TCLFile))
        cell_type = (cell_type_tri(elemInfo_ShellDKGT))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='cadetblue', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='cadetblue', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_ShellNLDKGT.size > 0):
        cells = tri_cell(elemInfo_ShellNLDKGT,  node(TCLFile))
        cell_type = (cell_type_tri(elemInfo_ShellNLDKGT))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='darkcyan', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='darkcyan', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_dispBeamColumnWithSensitivity.size > 0):
        cells = frame_cell(elemInfo_dispBeamColumnWithSensitivity, node(TCLFile))
        cell_type = (cell_type_frame(elemInfo_dispBeamColumnWithSensitivity))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='b', cmap="jet", show_edges=True, line_width=3 ,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='b', cmap="jet", show_edges=False, line_width=3, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_quadWithSensitivity.size > 0):
        cells = quad_cell(elemInfo_quadWithSensitivity, node(TCLFile))
        cell_type = (cell_type_quad(elemInfo_quadWithSensitivity))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='yellowgreen', cmap="jet", show_edges=True,scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='yellowgreen', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_bbarBrickWithSensitivity.size > 0):
        cells = brick_cell(elemInfo_bbarBrickWithSensitivity, node(TCLFile))
        cell_type = (cell_type_brick(elemInfo_bbarBrickWithSensitivity))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='green', cmap="jet", show_edges=True, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='green', cmap="jet", show_edges=False, scalars=scalars, stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_VS3D4.size > 0):
        cells = quad_cell(elemInfo_VS3D4, node(TCLFile))
        cell_type = (cell_type_quad(elemInfo_VS3D4))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='forestgreen', cmap="jet", show_edges=True, scalars=scalars,
                       stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='forestgreen', cmap="jet", show_edges=False, scalars=scalars,
                       stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')

    if (elemInfo_AV3D4.size > 0):
        cells = quad_cell(elemInfo_AV3D4, node(TCLFile))
        cell_type = (cell_type_quad(elemInfo_AV3D4))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        if showType == 'mesh_view':
            p.add_mesh(grid, lighting=False, color='greenyellow', cmap="jet", show_edges=True, scalars=scalars,
                       stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'smooth_view':
            p.add_mesh(grid, lighting=False, color='greenyellow', cmap="jet", show_edges=False, scalars=scalars,
                       stitle=stitle,scalar_bar_args=sargs)
        elif showType == 'wireframe':
            p.add_mesh(grid, lighting=False, color='w', show_edges=True, style='wireframe')


