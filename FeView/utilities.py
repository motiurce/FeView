import pyvista as pv
from nodes import*
from frame import*
def point_load(TCLFile,p,load_arrow_size, load_font_size,load_arrow_color,load_font_color):
    if ndm_v(TCLFile)==3:
        LoadInfo = (OpenSeesTclRead(TCLFile, 'load', 5))
        print(LoadInfo)
        if (LoadInfo.size > 0):
            def point_load_n(LoadList, nodeList):
                nodeiRow = []
                for i in range(len(LoadList[:, 0])):
                    nodeiRow.append((int(np.argwhere(nodeList[:, 1] == LoadList[i, 1]))))
                return np.array(nodeiRow)
            load_nodes = (point_load_n(LoadInfo, node(TCLFile)))
            initNodeCoords = NodeCoords(TCLFile)
            LoadNodeCoords = initNodeCoords[load_nodes]
            point_loads = LoadInfo[:, 2:5].astype(float)
            dic = []
            cent = []
            load_values = []
            for i in range (len(LoadNodeCoords[:,0])):
                if point_loads[i,0]>0:
                    dic.append(([load_arrow_size,0,0]))
                    cent.append((LoadNodeCoords[i,0]-load_arrow_size,LoadNodeCoords[i,1],LoadNodeCoords[i,2]) )
                    load_values.append(point_loads[i,0])
                elif point_loads[i,0]<0:
                    dic.append(([-load_arrow_size,0,0]))
                    cent.append((LoadNodeCoords[i,0]+load_arrow_size,LoadNodeCoords[i,1],LoadNodeCoords[i,2]) )
                    load_values.append(np.abs(point_loads[i, 0]))
                if point_loads[i,1]>0:
                    dic.append(([0,load_arrow_size,0]))
                    cent.append((LoadNodeCoords[i,0],LoadNodeCoords[i,1]-load_arrow_size,LoadNodeCoords[i,2]) )
                    load_values.append(point_loads[i, 1])
                elif point_loads[i,1]<0:
                    dic.append(([0,-load_arrow_size,0]))
                    #dic3=[]
                    cent.append((LoadNodeCoords[i,0],LoadNodeCoords[i,1]+load_arrow_size,LoadNodeCoords[i,2]) )
                    load_values.append(np.abs(point_loads[i, 1]))
                if point_loads[i,2]>0:
                    dic.append(([0,0,load_arrow_size]))
                    #doc6=[]
                    cent.append((LoadNodeCoords[i,0],LoadNodeCoords[i,1],LoadNodeCoords[i,2]-load_arrow_size) )
                    load_values.append(point_loads[i, 2])
                elif point_loads[i,2]<0:
                    dic.append(([0,0,-load_arrow_size]))
                    cent.append((LoadNodeCoords[i,0],LoadNodeCoords[i,1],LoadNodeCoords[i,2]+load_arrow_size) )
                    load_values.append(np.abs(point_loads[i, 2]))
                p.add_arrows(np.asarray(cent), np.asarray(dic), color=load_arrow_color)
                p.add_point_labels(np.asarray(cent),
                                   load_values, font_size=load_font_size, shape_opacity=0, text_color=load_font_color, show_points=False,
                                   point_color=load_arrow_color, point_size=0.1)
    elif ndm_v(TCLFile) == 2:
        LoadInfo = (OpenSeesTclRead(TCLFile, 'load', 4))
        if (LoadInfo.size > 0):
            def point_load_n(LoadList, nodeList):
                nodeiRow = []
                for i in range(len(LoadList[:, 0])):
                    nodeiRow.append((int(np.argwhere(nodeList[:, 1] == LoadList[i, 1]))))
                return np.array(nodeiRow)
            load_nodes = (point_load_n(LoadInfo, node(TCLFile)))
            initNodeCoords = NodeCoords(TCLFile)
            LoadNodeCoords = initNodeCoords[load_nodes]
            point_loads = LoadInfo[:, 2:5].astype(float)
            dic = []
            cent = []
            load_values = []
            for i in range(len(LoadNodeCoords[:, 0])):
                if point_loads[i, 0] > 0:
                    dic.append(([load_arrow_size, 0, 0]))
                    cent.append((LoadNodeCoords[i, 0] - load_arrow_size, LoadNodeCoords[i, 1], LoadNodeCoords[i, 2]))
                    load_values.append(point_loads[i, 0])
                elif point_loads[i, 0] < 0:
                    dic.append(([-load_arrow_size, 0, 0]))
                    cent.append((LoadNodeCoords[i, 0] + load_arrow_size, LoadNodeCoords[i, 1], LoadNodeCoords[i, 2]))
                    load_values.append(np.abs(point_loads[i, 0]))
                if point_loads[i, 1] > 0:
                    dic.append(([0, load_arrow_size, 0]))
                    cent.append((LoadNodeCoords[i, 0], LoadNodeCoords[i, 1] - load_arrow_size, LoadNodeCoords[i, 2]))
                    load_values.append(point_loads[i, 1])            #
                elif point_loads[i, 1] < 0:
                    dic.append(([0, -load_arrow_size, 0]))
                    cent.append((LoadNodeCoords[i, 0], LoadNodeCoords[i, 1] + load_arrow_size, LoadNodeCoords[i, 2]))
                    load_values.append(np.abs(point_loads[i, 1]))
                p.add_arrows(np.asarray(cent), np.asarray(dic), color=load_arrow_color)
                p.add_point_labels(np.asarray(cent),
                                   load_values, font_size=load_font_size, shape_opacity=0, text_color=load_font_color, show_points=False,
                                   point_color=load_arrow_color, point_size=0.1)
    return p
def support(TCLFile,p):
    #if ndm_v(TCLFile)==3:
    supInfo = (OpenSeesTclRead(TCLFile, 'fix', 4))
    if (supInfo.size > 0):
        def SupNode_n(SupList, nodeList):
            nodeiRow = []
            for i in range(len(SupList[:, 0])):
                nodeiRow.append((int(np.argwhere(nodeList[:, 1] == SupList[i, 1]))))
            return np.array(nodeiRow)
        sup_nodes = (SupNode_n(supInfo, node(TCLFile)))
        initNodeCoords = NodeCoords(TCLFile)
        SupNodeCoords = initNodeCoords[sup_nodes]
        SupportPoint = pv.PolyData(SupNodeCoords)
        p.add_mesh(SupportPoint, color='k', point_size=10)
    return p

def support_disp(TCLFile,p,disp_node_coords):
    #if ndm_v(TCLFile)==3:
    supInfo = (OpenSeesTclRead(TCLFile, 'fix', 4))
    if (supInfo.size > 0):
        def SupNode_n(SupList, nodeList):
            nodeiRow = []
            for i in range(len(SupList[:, 0])):
                nodeiRow.append((int(np.argwhere(nodeList[:, 1] == SupList[i, 1]))))
            return np.array(nodeiRow)
        sup_nodes = (SupNode_n(supInfo, node(TCLFile)))
        #initNodeCoords = NodeCoords(TCLFile)
        SupNodeCoords = disp_node_coords[sup_nodes]
        SupportPoint = pv.PolyData(SupNodeCoords)
        p.add_mesh(SupportPoint, color='k', point_size=10)
    return p

def NodesLabel(p,TCLFile,Node_coord,nl):
    nodeInfo=node(TCLFile)
    Node_Label = nodeInfo[:, 1].astype(int)
    if nl==1:
        p.add_point_labels(Node_coord, Node_Label.tolist(), font_size=12, shape_opacity=0.0)
    if nl==0:
        p.add_point_labels(Node_coord, Node_Label.tolist(), font_size=0, text_color='4c4c4c',point_color='#4c4c4c', shape_opacity=0,show_points=False,point_size=1,fill_shape=False)

def NodesCoordinate(p,Node_coord, def_Node_coord,nc):
    if nc == 1:
        p.add_point_labels(Node_coord,def_Node_coord.tolist(), font_size=12, shape_opacity=0.0)
    if nc == 0:
        p.add_point_labels(Node_coord, def_Node_coord.tolist(), font_size=0, text_color='#4c4c4c',
                           point_color='#4c4c4c', shape_opacity=0, show_points=False, point_size=1,
                           fill_shape=False)

def rigiddiaphram_info(TCLFile):
    # Brick element
    rigid_diaphram = OpenSeesTcl_2nodes(TCLFile, 'rigidDiaphragm')
    return rigid_diaphram

def plotter_rigiddiaphram(p,TCLFile,NodeCoord):
    offset = np.array([0, 0])
    rigiddia_info=rigiddiaphram_info(TCLFile)
    print(rigiddia_info)

    if (rigiddia_info.size > 0):
        cells = frame_cell(rigiddia_info, node(TCLFile))
        print(cells)
        cell_type = (cell_type_frame(rigiddia_info))
        grid = pv.UnstructuredGrid(offset, cells, cell_type, NodeCoord)
        p.add_mesh(grid, lighting=False, color='gold', show_edges=True, line_width=0.5)

