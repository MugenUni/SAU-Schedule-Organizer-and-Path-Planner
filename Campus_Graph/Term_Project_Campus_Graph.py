class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, vertex, weight):
        if vertex not in self.neighbors:
            self.neighbors.update({vertex: weight})

class Graph:
    def __init__(self):
        self.vertices = {}
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))
    def add_vertex(self, vertex):
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

    def add_edge(self, v1 : str , v2 : str,  weight : float):
        if v1 in self.vertices and v2 in self.vertices:
            for key, value in self.vertices.items():
                if key == v1:
                    value.add_neighbor(v2, weight)
                if key == v2:
                    value.add_neighbor(v1, weight)


'''
Key:
The campus is split into 4 parts: North, East, West, and Center.  All combine to make one graph of the campus.
dst; destination vertex.  Used to represent a building that the user wants to reach or is leaving from.
PVert; path vertex.  Path vertices are placed along the path that a user could take to reach a destination.
    West:
UCA = University Court Apartments
EIH = Eichenberger Hall
ENG = Engineering Building
WNB = Warton Nursing Building
BLN = Blanchard
EDU = Education Building
SCI = Science Building
AGR = Agriculture Building
    North:
BHH = Burns Harsh Hall
MAH = Magnolia Hall
ARH = Arkansas Hall
COH = Columbia Hall
    East:
DCH = Dolph Camp Hall
BUH = Bussey Hall
PEH = Peace Hall
FIH = Fincher Hall
UAP = University Village Apartments
MAL = Mallory Hall
    Center:
OVR = Overstreet Hall
HAT = Harton Theatre
WIL = Wilson Hall
CRO = Cross Hall
HAH = Harrod Hall
NEL = Nelson Hall
BAB = Brinson Fine Arts Building
BCT = Bruce Center
REY = Reynolds Center
MAG = Magale Library
TAB = Talbot Hall
TAL = Talley Hall
GRH = Greene Hall
HOH = Honors Hall
    * I recommend importing this file into a separate program instead of adding on to it *
'''
SAU_Campus = Graph()

# init dst vertex West
UCA = Vertex('UCA')
EIH = Vertex('EIH')
ENG1 = Vertex('ENG 1')
ENG2 = Vertex('ENG 2')
WNB1 = Vertex('WNB 1')
WNB2 = Vertex('WNB 2')
WNB3 = Vertex('WNB 3')
BLN1 = Vertex('BLN 1')
BLN2 = Vertex('BLN 2')
EDU = Vertex('EDU')
SCI1 = Vertex('SCI 1')
SCI2 = Vertex('SCI 2')
AGR = Vertex('AGR')

# init dst vertex North
BHH = Vertex('BHH')
MAH1 = Vertex('MAH 1')
MAH2 = Vertex('MAH 2')
ARH = Vertex('ARH')
COH = Vertex('COH')

# init dst vertex East
DCH1 = Vertex('DCH 1')
DCH2 = Vertex('DCH 2')
BUH1 = Vertex('BUH 1')
BUH2 = Vertex('BUH 2')
PEH1 = Vertex('PEH 1')
PEH2 = Vertex('PEH 2')
FIH1 = Vertex('FIH 1')
FIH2 = Vertex('FIH 2')
UAP = Vertex('UAP')
MAL = Vertex('MAL')

# init dst vertex Center
OVR1 = Vertex('OVR 1')
OVR2 = Vertex('OVR 2')
OVR3 = Vertex('OVR 3')
HAT = Vertex('HAT')
WIL1 = Vertex('WIL 1')
WIL2 = Vertex('WIL 2')
WIL3 = Vertex('WIL 3')
CRO1 = Vertex('CRO 1')
CRO2 = Vertex('CRO 2')
CRO3 = Vertex('CRO 3')
HAH1 = Vertex('HAH 1')
HAH2 = Vertex('HAH 2')
HAH3 = Vertex('HAH 3')
NEL1 = Vertex('NEL 1')
NEL2 = Vertex('NEL 2')
NEL3 = Vertex('NEL 3')
NEL4 = Vertex('NEL 4')
BAB1 = Vertex('BAB 1')
BAB2 = Vertex('BAB 2')
BCT1 = Vertex('BCT 1')
BCT2 = Vertex('BCT 2')
BCT3 = Vertex('BCT 3')
BCT4 = Vertex('BCT 4')
REY1 = Vertex('REY 1')
REY2 = Vertex('REY 2')
REY3 = Vertex('REY 3')
REY4 = Vertex('REY 4')
MAG = Vertex('MAG')
TAB = Vertex('TAB')
TAL = Vertex('TAL')
GRH = Vertex('GRH')
HOH1 = Vertex('HOH 1')
HOH2 = Vertex('HOH 2')

# add dst vertex West
SAU_Campus.add_vertex(UCA)
SAU_Campus.add_vertex(EIH)
SAU_Campus.add_vertex(ENG1)
SAU_Campus.add_vertex(ENG2)
SAU_Campus.add_vertex(WNB1)
SAU_Campus.add_vertex(WNB2)
SAU_Campus.add_vertex(WNB3)
SAU_Campus.add_vertex(BLN1)
SAU_Campus.add_vertex(BLN2)
SAU_Campus.add_vertex(EDU)
SAU_Campus.add_vertex(SCI1)
SAU_Campus.add_vertex(SCI2)
SAU_Campus.add_vertex(AGR)

# add dst vertex North
SAU_Campus.add_vertex(BHH)
SAU_Campus.add_vertex(MAH1)
SAU_Campus.add_vertex(MAH2)
SAU_Campus.add_vertex(ARH)
SAU_Campus.add_vertex(COH)

# add dst vertex East
SAU_Campus.add_vertex(DCH1)
SAU_Campus.add_vertex(DCH2)
SAU_Campus.add_vertex(BUH1)
SAU_Campus.add_vertex(BUH2)
SAU_Campus.add_vertex(PEH1)
SAU_Campus.add_vertex(PEH2)
SAU_Campus.add_vertex(FIH1)
SAU_Campus.add_vertex(FIH2)
SAU_Campus.add_vertex(UAP)
SAU_Campus.add_vertex(MAL)

# add dst vertex Center
SAU_Campus.add_vertex(OVR1)
SAU_Campus.add_vertex(OVR2)
SAU_Campus.add_vertex(OVR3)
SAU_Campus.add_vertex(HAT)
SAU_Campus.add_vertex(WIL1)
SAU_Campus.add_vertex(WIL2)
SAU_Campus.add_vertex(WIL3)
SAU_Campus.add_vertex(CRO1)
SAU_Campus.add_vertex(CRO2)
SAU_Campus.add_vertex(CRO3)
SAU_Campus.add_vertex(HAH1)
SAU_Campus.add_vertex(HAH2)
SAU_Campus.add_vertex(HAH3)
SAU_Campus.add_vertex(NEL1)
SAU_Campus.add_vertex(NEL2)
SAU_Campus.add_vertex(NEL3)
SAU_Campus.add_vertex(NEL4)
SAU_Campus.add_vertex(BAB1)
SAU_Campus.add_vertex(BAB2)
SAU_Campus.add_vertex(BCT1)
SAU_Campus.add_vertex(BCT2)
SAU_Campus.add_vertex(BCT3)
SAU_Campus.add_vertex(BCT4)
SAU_Campus.add_vertex(REY1)
SAU_Campus.add_vertex(REY2)
SAU_Campus.add_vertex(REY3)
SAU_Campus.add_vertex(REY4)
SAU_Campus.add_vertex(MAG)
SAU_Campus.add_vertex(TAB)
SAU_Campus.add_vertex(TAL)
SAU_Campus.add_vertex(GRH)
SAU_Campus.add_vertex(HOH1)
SAU_Campus.add_vertex(HOH2)

# init path vertex West
PVert_2 = Vertex('PVert 2')
PVert_3 = Vertex('PVert 3')
PVert_4 = Vertex('PVert 4')
PVert_5 = Vertex('PVert 5')
PVert_6 = Vertex('PVert 6')
PVert_7 = Vertex('PVert 7')
PVert_8 = Vertex('PVert 8')
PVert_9 = Vertex('PVert 9')
PVert_10 = Vertex('PVert 10')
PVert_11 = Vertex('PVert 11')

# init path vertex North
PVert_12 = Vertex('PVert 12')
PVert_13 = Vertex('PVert 13')
PVert_14 = Vertex('PVert 14')
PVert_15 = Vertex('PVert 15')
PVert_16 = Vertex('PVert 16')
PVert_17 = Vertex('PVert 17')
PVert_18 = Vertex('PVert 18')
PVert_19 = Vertex('PVert 19')
PVert_20 = Vertex('PVert 20')
PVert_21 = Vertex('PVert 21')
PVert_22 = Vertex('PVert 22')
PVert_23 = Vertex('PVert 23')

# init path vertex East
PVert_1 = Vertex('PVert 1')
PVert_24 = Vertex('PVert 24')
PVert_25 = Vertex('PVert 25')
PVert_26 = Vertex('PVert 26')
PVert_27 = Vertex('PVert 27')
PVert_28 = Vertex('PVert 28')
PVert_29 = Vertex('PVert 29')
PVert_30 = Vertex('PVert 30')
PVert_31 = Vertex('PVert 31')
PVert_32 = Vertex('PVert 32')
PVert_33 = Vertex('PVert 33')

# init path vertex Center
PVert_34 = Vertex('PVert 34')
PVert_35 = Vertex('PVert 35')
PVert_36 = Vertex('PVert 36')
PVert_38 = Vertex('PVert 38')
PVert_39 = Vertex('PVert 39')
PVert_40 = Vertex('PVert 40')
PVert_41 = Vertex('PVert 41')
PVert_42 = Vertex('PVert 42')
PVert_45 = Vertex('PVert 45')
PVert_48 = Vertex('PVert 48')
PVert_49 = Vertex('PVert 49')
PVert_51 = Vertex('PVert 51')
PVert_53 = Vertex('PVert 53')
PVert_55 = Vertex('PVert 55')
PVert_57 = Vertex('PVert 57')
PVert_58 = Vertex('PVert 58')
PVert_59 = Vertex('PVert 59')
PVert_60 = Vertex('PVert 60')
PVert_63 = Vertex('PVert 63')
PVert_65 = Vertex('PVert 65')
PVert_67 = Vertex('PVert 67')
PVert_71 = Vertex('PVert 71')
PVert_72 = Vertex('PVert 72')
PVert_73 = Vertex('PVert 73')
PVert_74 = Vertex('PVert 74')
PVert_75 = Vertex('PVert 75')
PVert_76 = Vertex('PVert 76')
PVert_78 = Vertex('PVert 78')
PVert_79 = Vertex('PVert 79')
PVert_81 = Vertex('PVert 81')
PVert_83 = Vertex('PVert 83')
PVert_84 = Vertex('PVert 84')
PVert_85 = Vertex('PVert 85')
PVert_86 = Vertex('PVert 86')
PVert_87 = Vertex('PVert 87')
PVert_88 = Vertex('PVert 88')
PVert_89 = Vertex('PVert 89')
PVert_90 = Vertex('PVert 90')
PVert_91 = Vertex('PVert 91')
PVert_92 = Vertex('PVert 92')
PVert_93 = Vertex('PVert 93')
PVert_94 = Vertex('PVert 94')
PVert_96 = Vertex('PVert 96')
PVert_97 = Vertex('PVert 97')
PVert_99 = Vertex('PVert 99')
PVert_101 = Vertex('PVert 101')
PVert_103 = Vertex('PVert 103')
PVert_105 = Vertex('PVert 105')
PVert_108 = Vertex('PVert 108')
PVert_110 = Vertex('PVert 110')
PVert_112 = Vertex('PVert 112')
PVert_113 = Vertex('PVert 113')
PVert_114 = Vertex('PVert 114')
PVert_115 = Vertex('PVert 115')
PVert_116 = Vertex('PVert 116')
PVert_117 = Vertex('PVert 117')
PVert_119 = Vertex('PVert 119')
PVert_120 = Vertex('PVert 120')
PVert_122 = Vertex('PVert 122')
PVert_123 = Vertex('PVert 123')
PVert_124 = Vertex('PVert 124')
PVert_125 = Vertex('PVert 125')
PVert_127 = Vertex('PVert 127')
PVert_128 = Vertex('PVert 128')
PVert_130 = Vertex('PVert 130')
PVert_131 = Vertex('PVert 131')
PVert_132 = Vertex('PVert 132')
PVert_133 = Vertex('PVert 133')
PVert_134 = Vertex('PVert 134')
PVert_135 = Vertex('PVert 135')
PVert_136 = Vertex('PVert 136')

# add path vertex West
SAU_Campus.add_vertex(PVert_2)
SAU_Campus.add_vertex(PVert_3)
SAU_Campus.add_vertex(PVert_4)
SAU_Campus.add_vertex(PVert_5)
SAU_Campus.add_vertex(PVert_6)
SAU_Campus.add_vertex(PVert_7)
SAU_Campus.add_vertex(PVert_8)
SAU_Campus.add_vertex(PVert_9)
SAU_Campus.add_vertex(PVert_10)
SAU_Campus.add_vertex(PVert_11)

# add path vertex North
SAU_Campus.add_vertex(PVert_12)
SAU_Campus.add_vertex(PVert_13)
SAU_Campus.add_vertex(PVert_14)
SAU_Campus.add_vertex(PVert_15)
SAU_Campus.add_vertex(PVert_16)
SAU_Campus.add_vertex(PVert_17)
SAU_Campus.add_vertex(PVert_18)
SAU_Campus.add_vertex(PVert_19)
SAU_Campus.add_vertex(PVert_20)
SAU_Campus.add_vertex(PVert_21)
SAU_Campus.add_vertex(PVert_22)
SAU_Campus.add_vertex(PVert_23)

# add path vertex East
SAU_Campus.add_vertex(PVert_1)
SAU_Campus.add_vertex(PVert_24)
SAU_Campus.add_vertex(PVert_25)
SAU_Campus.add_vertex(PVert_26)
SAU_Campus.add_vertex(PVert_27)
SAU_Campus.add_vertex(PVert_28)
SAU_Campus.add_vertex(PVert_29)
SAU_Campus.add_vertex(PVert_30)
SAU_Campus.add_vertex(PVert_31)
SAU_Campus.add_vertex(PVert_32)
SAU_Campus.add_vertex(PVert_33)

# add path vertex Center
SAU_Campus.add_vertex(PVert_34)
SAU_Campus.add_vertex(PVert_35)
SAU_Campus.add_vertex(PVert_36)
SAU_Campus.add_vertex(PVert_38)
SAU_Campus.add_vertex(PVert_39)
SAU_Campus.add_vertex(PVert_40)
SAU_Campus.add_vertex(PVert_41)
SAU_Campus.add_vertex(PVert_42)
SAU_Campus.add_vertex(PVert_45)
SAU_Campus.add_vertex(PVert_48)
SAU_Campus.add_vertex(PVert_49)
SAU_Campus.add_vertex(PVert_51)
SAU_Campus.add_vertex(PVert_53)
SAU_Campus.add_vertex(PVert_55)
SAU_Campus.add_vertex(PVert_57)
SAU_Campus.add_vertex(PVert_58)
SAU_Campus.add_vertex(PVert_59)
SAU_Campus.add_vertex(PVert_60)
SAU_Campus.add_vertex(PVert_63)
SAU_Campus.add_vertex(PVert_65)
SAU_Campus.add_vertex(PVert_67)
SAU_Campus.add_vertex(PVert_71)
SAU_Campus.add_vertex(PVert_72)
SAU_Campus.add_vertex(PVert_73)
SAU_Campus.add_vertex(PVert_74)
SAU_Campus.add_vertex(PVert_75)
SAU_Campus.add_vertex(PVert_76)
SAU_Campus.add_vertex(PVert_78)
SAU_Campus.add_vertex(PVert_79)
SAU_Campus.add_vertex(PVert_81)
SAU_Campus.add_vertex(PVert_83)
SAU_Campus.add_vertex(PVert_84)
SAU_Campus.add_vertex(PVert_85)
SAU_Campus.add_vertex(PVert_86)
SAU_Campus.add_vertex(PVert_87)
SAU_Campus.add_vertex(PVert_88)
SAU_Campus.add_vertex(PVert_89)
SAU_Campus.add_vertex(PVert_90)
SAU_Campus.add_vertex(PVert_91)
SAU_Campus.add_vertex(PVert_92)
SAU_Campus.add_vertex(PVert_93)
SAU_Campus.add_vertex(PVert_94)
SAU_Campus.add_vertex(PVert_96)
SAU_Campus.add_vertex(PVert_97)
SAU_Campus.add_vertex(PVert_99)
SAU_Campus.add_vertex(PVert_101)
SAU_Campus.add_vertex(PVert_103)
SAU_Campus.add_vertex(PVert_105)
SAU_Campus.add_vertex(PVert_108)
SAU_Campus.add_vertex(PVert_110)
SAU_Campus.add_vertex(PVert_112)
SAU_Campus.add_vertex(PVert_113)
SAU_Campus.add_vertex(PVert_114)
SAU_Campus.add_vertex(PVert_115)
SAU_Campus.add_vertex(PVert_116)
SAU_Campus.add_vertex(PVert_117)
SAU_Campus.add_vertex(PVert_119)
SAU_Campus.add_vertex(PVert_120)
SAU_Campus.add_vertex(PVert_122)
SAU_Campus.add_vertex(PVert_123)
SAU_Campus.add_vertex(PVert_124)
SAU_Campus.add_vertex(PVert_125)
SAU_Campus.add_vertex(PVert_127)
SAU_Campus.add_vertex(PVert_128)
SAU_Campus.add_vertex(PVert_130)
SAU_Campus.add_vertex(PVert_131)
SAU_Campus.add_vertex(PVert_132)
SAU_Campus.add_vertex(PVert_133)
SAU_Campus.add_vertex(PVert_134)
SAU_Campus.add_vertex(PVert_135)
SAU_Campus.add_vertex(PVert_136)

# West
SAU_Campus.add_edge('EIH', 'UCA', 86.86)
SAU_Campus.add_edge('EIH', 'PVert 2', 44.24)
SAU_Campus.add_edge('SCI 2', 'UCA', 71.49)
SAU_Campus.add_edge('WNB 1', 'PVert 2', 33.38)
SAU_Campus.add_edge('WNB 2', 'PVert 2', 88.89)
SAU_Campus.add_edge('WNB 1', 'WNB 3', 80.00)
SAU_Campus.add_edge('WNB 2', 'WNB 3', 88.89)
SAU_Campus.add_edge('WNB 1', 'ENG 1', 53.27)
SAU_Campus.add_edge('ENG 1', 'PVert 3', 40.92)
SAU_Campus.add_edge('WNB 1', 'PVert 3', 50.08)
SAU_Campus.add_edge('EDU', 'PVert 3', 32.51)
SAU_Campus.add_edge('EDU', 'PVert 4', 39.31)
SAU_Campus.add_edge('PVert 5', 'PVert 4', 51.57)
SAU_Campus.add_edge('WNB 3', 'PVert 5', 74.01)
SAU_Campus.add_edge('ENG 1', 'PVert 6', 86.83)
SAU_Campus.add_edge('PVert 4', 'PVert 6', 45.06)
SAU_Campus.add_edge('BLN 2', 'PVert 4', 22.18)
SAU_Campus.add_edge('ENG 2', 'PVert 6', 34.33)
SAU_Campus.add_edge('ENG 2', 'PVert 7', 57.73)
SAU_Campus.add_edge('SCI 2', 'PVert 7', 53.19)
SAU_Campus.add_edge('SCI 1', 'PVert 7', 69.03)
SAU_Campus.add_edge('SCI 1', 'PVert 6', 116.09)
SAU_Campus.add_edge('SCI 1', 'BLN 1', 130.12)
SAU_Campus.add_edge('SCI 1', 'AGR', 100.02)
SAU_Campus.add_edge('BLN 1', 'AGR', 168.59)
SAU_Campus.add_edge('AGR', 'PVert 8', 170.66)
SAU_Campus.add_edge('AGR', 'PVert 9', 78.58)
SAU_Campus.add_edge('PVert 10', 'PVert 9', 90.80)
SAU_Campus.add_edge('PVert 10', 'PVert 8', 134.44)
SAU_Campus.add_edge('PVert 5', 'PVert 11', 67.91)
SAU_Campus.add_edge('BLN 1', 'PVert 8', 67.74)
SAU_Campus.add_edge('BLN 1', 'PVert 11', 45.20)
SAU_Campus.add_edge('PVert 8', 'PVert 11', 54.51)

# North
SAU_Campus.add_edge('PVert 10', 'PVert 12', 65.83)
SAU_Campus.add_edge('PVert 10', 'PVert 13', 72.20)
SAU_Campus.add_edge('PVert 13', 'PVert 133', 42.76)
SAU_Campus.add_edge('PVert 133', 'PVert 17', 55.50)
SAU_Campus.add_edge('PVert 16', 'PVert 13', 88.55)
SAU_Campus.add_edge('PVert 12', 'PVert 15', 81.57)
SAU_Campus.add_edge('PVert 14', 'PVert 12', 99.45)
SAU_Campus.add_edge('PVert 14', 'PVert 15', 50.27)
SAU_Campus.add_edge('PVert 18', 'PVert 15', 30.17)
SAU_Campus.add_edge('PVert 19', 'PVert 15', 64.05)
SAU_Campus.add_edge('PVert 16', 'PVert 15', 53.61)
SAU_Campus.add_edge('PVert 16', 'PVert 17', 66.36)
SAU_Campus.add_edge('PVert 16', 'PVert 18', 58.22)
SAU_Campus.add_edge('PVert 16', 'PVert 19', 33.19)
SAU_Campus.add_edge('PVert 18', 'PVert 19', 53.56)
SAU_Campus.add_edge('PVert 14', 'PVert 20', 98.29)
SAU_Campus.add_edge('PVert 18', 'PVert 21', 66.37)
SAU_Campus.add_edge('PVert 19', 'PVert 22', 55.35)
SAU_Campus.add_edge('PVert 17', 'PVert 23', 79.80)
SAU_Campus.add_edge('PVert 20', 'PVert 21', 64.07)
SAU_Campus.add_edge('PVert 21', 'PVert 22', 54.65)
SAU_Campus.add_edge('PVert 22', 'PVert 23', 67.72)
SAU_Campus.add_edge('PVert 20', 'BHH', 65.76)
SAU_Campus.add_edge('PVert 20', 'MAH 2', 94.26)
SAU_Campus.add_edge('PVert 21', 'BHH', 101.47)
SAU_Campus.add_edge('PVert 21', 'MAH 2', 67.31)
SAU_Campus.add_edge('PVert 21', 'MAH 1', 70.41)
SAU_Campus.add_edge('PVert 23', 'COH', 83.80)
SAU_Campus.add_edge('COH', 'MAH 1', 32.37)
SAU_Campus.add_edge('PVert 23', 'ARH', 119.04)
SAU_Campus.add_edge('ARH', 'MAH 1', 36.51)
SAU_Campus.add_edge('BHH', 'MAH 2', 78.86)

# East
SAU_Campus.add_edge('PVert 1', 'PVert 24', 101.97)
SAU_Campus.add_edge('PVert 1', 'PVert 26', 117.30)
SAU_Campus.add_edge('PVert 24', 'PVert 25', 44.55)
SAU_Campus.add_edge('PVert 25', 'PVert 26', 62.04)
SAU_Campus.add_edge('PVert 26', 'MAL', 213.53)
SAU_Campus.add_edge('MAL', 'PVert 30', 64.24)
SAU_Campus.add_edge('PVert 30', 'UAP', 70.11)
SAU_Campus.add_edge('PVert 30', 'PVert 29', 107.15)
SAU_Campus.add_edge('UAP', 'PVert 32', 89.39)
SAU_Campus.add_edge('PVert 26', 'FIH 2', 86.77)
SAU_Campus.add_edge('FIH 2', 'PVert 29', 56.35)
SAU_Campus.add_edge('PVert 29', 'PVert 32', 36.52)
SAU_Campus.add_edge('PVert 29', 'BUH 2', 111.90)
SAU_Campus.add_edge('PVert 32', 'DCH 2', 119.68)
SAU_Campus.add_edge('PVert 25', 'PEH 2', 37.83)
SAU_Campus.add_edge('PEH 2', 'FIH 1', 63.24)
SAU_Campus.add_edge('FIH 1', 'PVert 28', 50.46)
SAU_Campus.add_edge('FIH 1', 'BUH 2', 55.35)
SAU_Campus.add_edge('PEH 2', 'PVert 28', 32.54)
SAU_Campus.add_edge('PVert 28', 'PVert 27', 58.17)
SAU_Campus.add_edge('PVert 28', 'BUH 2', 33.40)
SAU_Campus.add_edge('BUH 2', 'DCH 2', 51.11)
SAU_Campus.add_edge('DCH 2', 'PVert 31', 57.00)
SAU_Campus.add_edge('PVert 24', 'PEH 1', 20.66)
SAU_Campus.add_edge('PVert 27', 'PVert 58', 20.28)
SAU_Campus.add_edge('PVert 58', 'PEH 1', 12.16)
SAU_Campus.add_edge('PVert 27', 'BUH 1', 38.97)
SAU_Campus.add_edge('PVert 31', 'PVert 89', 23.20)
SAU_Campus.add_edge('PVert 89', 'BUH 1', 23.12)
SAU_Campus.add_edge('PVert 31', 'DCH 1', 30.31)
SAU_Campus.add_edge('DCH 1', 'PVert 33', 33.52)

# Center
SAU_Campus.add_edge('WNB 2', 'PVert 34', 97.27)
SAU_Campus.add_edge('PVert 34', 'PVert 35', 50.42)
SAU_Campus.add_edge('PVert 35', 'PVert 1', 114.48)
SAU_Campus.add_edge('WNB 3', 'PVert 36', 96.05)
SAU_Campus.add_edge('PVert 36', 'PVert 34', 76.54)
SAU_Campus.add_edge('PVert 34', 'OVR 1', 79.60)
SAU_Campus.add_edge('OVR 1', 'PVert 36', 30.70)
SAU_Campus.add_edge('OVR 1', 'PVert 39', 32.00)
SAU_Campus.add_edge('OVR 1', 'PVert 35', 79.38)
SAU_Campus.add_edge('PVert 35', 'PVert 38', 56.22)
SAU_Campus.add_edge('PVert 39', 'PVert 38', 20.07)
SAU_Campus.add_edge('PVert 38', 'PVert 40', 38.80)
SAU_Campus.add_edge('PVert 40', 'HAH 3', 76.41)
SAU_Campus.add_edge('PVert 36', 'PVert 42', 35.19)
SAU_Campus.add_edge('PVert 39', 'PVert 45', 28.95)
SAU_Campus.add_edge('PVert 5', 'WIL 1', 15.46)
SAU_Campus.add_edge('WIL 1', 'PVert 41', 28.72)
SAU_Campus.add_edge('PVert 41', 'PVert 42', 79.93)
SAU_Campus.add_edge('PVert 42', 'OVR 2', 13.79)
SAU_Campus.add_edge('OVR 2', 'WIL 3', 33.56)
SAU_Campus.add_edge('OVR 3', 'PVert 53', 35.60)
SAU_Campus.add_edge('OVR 3', 'PVert 45', 12.55)
SAU_Campus.add_edge('PVert 45', 'HAH 3', 78.21)
SAU_Campus.add_edge('HAH 3', 'PVert 24', 34.11)
SAU_Campus.add_edge('HAH 3', 'PVert 57', 24.14)
SAU_Campus.add_edge('WIL 1', 'PVert 48', 13.05)
SAU_Campus.add_edge('PVert 48', 'PVert 49', 18.44)
SAU_Campus.add_edge('PVert 49', 'WIL 2', 19.95)
SAU_Campus.add_edge('WIL 2', 'PVert 51', 29.72)
SAU_Campus.add_edge('PVert 51', 'WIL 3', 22.80)
SAU_Campus.add_edge('PVert 53', 'HAH 1', 28.57)
SAU_Campus.add_edge('HAH 1', 'PVert 55', 38.68)
SAU_Campus.add_edge('PVert 55', 'HAH 2', 14.47)
SAU_Campus.add_edge('HAH 2', 'PVert 57', 23.35)
SAU_Campus.add_edge('PVert 57', 'PVert 58', 20.87)
SAU_Campus.add_edge('PVert 49', 'PVert 59', 19.71)
SAU_Campus.add_edge('PVert 59', 'PVert 60', 18.49)
SAU_Campus.add_edge('PVert 60', 'CRO 1', 10.82)
SAU_Campus.add_edge('CRO 1', 'CRO 2', 17.52)
SAU_Campus.add_edge('CRO 2', 'PVert 63', 22.82)
SAU_Campus.add_edge('PVert 57', 'CRO 3', 21.86)
SAU_Campus.add_edge('CRO 3', 'PVert 63', 14.46)
SAU_Campus.add_edge('CRO 3', 'PVert 65', 22.77)
SAU_Campus.add_edge('PVert 65', 'HAT', 17.91)
SAU_Campus.add_edge('PVert 65', 'PVert 74', 30.91)
SAU_Campus.add_edge('HAT', 'PVert 74', 31.95)
SAU_Campus.add_edge('HAT', 'PVert 67', 16.73)
SAU_Campus.add_edge('HAT', 'PVert 75', 35.71)
SAU_Campus.add_edge('PVert 67', 'NEL 1', 9.56)
SAU_Campus.add_edge('PVert 67', 'PVert 53', 27.46)
SAU_Campus.add_edge('PVert 65', 'WIL 3', 28.42)
SAU_Campus.add_edge('NEL 1', 'HAH 1', 28.33)
SAU_Campus.add_edge('NEL 1', 'PVert 75', 32.18)
SAU_Campus.add_edge('NEL 1', 'NEL 2', 38.83)
SAU_Campus.add_edge('HAH 2', 'NEL 4', 25.17)
SAU_Campus.add_edge('PVert 11', 'PVert 71', 39.17)
SAU_Campus.add_edge('PVert 71', 'PVert 60', 18.70)
SAU_Campus.add_edge('PVert 71', 'PVert 72', 30.02)
SAU_Campus.add_edge('PVert 72', 'CRO 2', 15.87)
SAU_Campus.add_edge('PVert 72', 'PVert 73', 22.28)
SAU_Campus.add_edge('PVert 73', 'PVert 63', 16.31)
SAU_Campus.add_edge('PVert 73', 'PVert 74', 20.56)
SAU_Campus.add_edge('PVert 74', 'PVert 75', 45.71)
SAU_Campus.add_edge('PVert 75', 'PVert 76', 42.38)
SAU_Campus.add_edge('PVert 76', 'NEL 2', 19.94)
SAU_Campus.add_edge('PVert 76', 'NEL 3', 15.55)
SAU_Campus.add_edge('NEL 3', 'PVert 78', 15.90)
SAU_Campus.add_edge('PVert 78', 'NEL 4', 44.83)
SAU_Campus.add_edge('PVert 78', 'PVert 79', 35.08)
SAU_Campus.add_edge('PVert 79', 'BUH 1', 13.05)
SAU_Campus.add_edge('PVert 71', 'BAB 1', 25.74)
SAU_Campus.add_edge('BAB 1', 'PVert 97', 33.41)
SAU_Campus.add_edge('BAB 1', 'PVert 81', 36.17)
SAU_Campus.add_edge('PVert 81', 'BAB 2', 9.53)
SAU_Campus.add_edge('BAB 2', 'PVert 73', 25.76)
SAU_Campus.add_edge('BAB 2', 'PVert 83', 19.82)
SAU_Campus.add_edge('PVert 83', 'PVert 84', 46.98)
SAU_Campus.add_edge('PVert 84', 'PVert 75', 25.80)
SAU_Campus.add_edge('PVert 84', 'PVert 85', 40.80)
SAU_Campus.add_edge('PVert 85', 'PVert 76', 24.37)
SAU_Campus.add_edge('PVert 85', 'PVert 94', 22.49)
SAU_Campus.add_edge('PVert 94', 'PVert 86', 24.06)
SAU_Campus.add_edge('PVert 86', 'PVert 78', 26.13)
SAU_Campus.add_edge('PVert 86', 'PVert 87', 20.23)
SAU_Campus.add_edge('PVert 78', 'PVert 87', 19.96)
SAU_Campus.add_edge('PVert 87', 'PVert 79', 20.44)
SAU_Campus.add_edge('PVert 87', 'PVert 88', 25.97)
SAU_Campus.add_edge('PVert 88', 'PVert 89', 16.45)
SAU_Campus.add_edge('PVert 88', 'PVert 96', 23.48)
SAU_Campus.add_edge('PVert 96', 'PVert 86', 26.10)
SAU_Campus.add_edge('PVert 96', 'BCT 3', 24.74)
SAU_Campus.add_edge('BCT 3', 'PVert 108', 19.82)
SAU_Campus.add_edge('PVert 96', 'BCT 4', 30.14)
SAU_Campus.add_edge('BCT 4', 'PVert 94', 8.71)
SAU_Campus.add_edge('BCT 4', 'PVert 93', 13.75)
SAU_Campus.add_edge('PVert 94', 'PVert 93', 13.97)
SAU_Campus.add_edge('PVert 93', 'PVert 92', 22.26)
SAU_Campus.add_edge('PVert 92', 'PVert 91', 22.66)
SAU_Campus.add_edge('PVert 92', 'PVert 105', 37.75)
SAU_Campus.add_edge('PVert 91', 'PVert 84', 20.21)
SAU_Campus.add_edge('PVert 91', 'PVert 105', 28.91)
SAU_Campus.add_edge('PVert 83', 'PVert 103', 48.28)
SAU_Campus.add_edge('BAB 2', 'PVert 90', 19.47)
SAU_Campus.add_edge('PVert 90', 'REY 3', 22.24)
SAU_Campus.add_edge('PVert 90', 'PVert 99', 17.33)
SAU_Campus.add_edge('PVert 90', 'PVert 103', 36.25)
SAU_Campus.add_edge('PVert 5', 'PVert 97', 127.73)
SAU_Campus.add_edge('PVert 49', 'PVert 8', 120.79)
SAU_Campus.add_edge('PVert 8', 'PVert 97', 49.13)
SAU_Campus.add_edge('PVert 97', 'REY 3', 37.45)
SAU_Campus.add_edge('REY 3', 'PVert 101', 24.07)
SAU_Campus.add_edge('REY 3', 'PVert 99', 12.77)
SAU_Campus.add_edge('PVert 99', 'REY 2', 16.22)
SAU_Campus.add_edge('PVert 8', 'REY 1', 31.45)
SAU_Campus.add_edge('REY 1', 'PVert 101', 76.29)
SAU_Campus.add_edge('PVert 101', 'REY 2', 14.52)
SAU_Campus.add_edge('REY 2', 'PVert 103', 22.41)
SAU_Campus.add_edge('PVert 103', 'MAG', 26.68)
SAU_Campus.add_edge('MAG', 'PVert 105', 24.12)
SAU_Campus.add_edge('PVert 101', 'PVert 110', 34.29)
SAU_Campus.add_edge('REY 2', 'REY 4', 39.50)
SAU_Campus.add_edge('PVert 110', 'REY 4', 10.32)
SAU_Campus.add_edge('REY 4', 'PVert 112', 14.56)
SAU_Campus.add_edge('PVert 112', 'PVert 117', 13.16)
SAU_Campus.add_edge('PVert 112', 'PVert 113', 68.77)
SAU_Campus.add_edge('PVert 113', 'PVert 105', 52.12)
SAU_Campus.add_edge('PVert 105', 'BCT 1', 24.91)
SAU_Campus.add_edge('BCT 1', 'PVert 113', 38.35)
SAU_Campus.add_edge('BCT 1', 'BCT 2', 41.59)
SAU_Campus.add_edge('BCT 2', 'PVert 108', 29.49)
SAU_Campus.add_edge('PVert 108', 'PVert 114', 52.62)
SAU_Campus.add_edge('PVert 33', 'PVert 114', 53.80)
SAU_Campus.add_edge('BCT 1', 'PVert 114', 84.40)
SAU_Campus.add_edge('PVert 113', 'PVert 119', 22.33)
SAU_Campus.add_edge('PVert 119', 'PVert 120', 65.53)
SAU_Campus.add_edge('PVert 114', 'PVert 120', 18.98)
SAU_Campus.add_edge('PVert 119', 'TAB', 41.52)
SAU_Campus.add_edge('PVert 117', 'TAB', 27.57)
SAU_Campus.add_edge('PVert 117', 'PVert 116', 19.78)
SAU_Campus.add_edge('PVert 116', 'PVert 115', 37.37)
SAU_Campus.add_edge('PVert 115', 'REY 1', 68.35)
SAU_Campus.add_edge('REY 1', 'PVert 10', 102.15)
SAU_Campus.add_edge('PVert 115', 'TAL', 53.82)
SAU_Campus.add_edge('PVert 116', 'TAL', 54.36)
SAU_Campus.add_edge('PVert 116', 'PVert 123', 38.45)
SAU_Campus.add_edge('PVert 117', 'PVert 124', 34.79)
SAU_Campus.add_edge('TAB', 'PVert 125', 32.22)
SAU_Campus.add_edge('PVert 119', 'HOH 2', 32.91)
SAU_Campus.add_edge('PVert 10', 'TAL', 61.98)
SAU_Campus.add_edge('TAL', 'PVert 122', 18.57)
SAU_Campus.add_edge('PVert 122', 'PVert 123', 27.31)
SAU_Campus.add_edge('PVert 123', 'PVert 124', 15.42)
SAU_Campus.add_edge('PVert 124', 'PVert 125', 26.20)
SAU_Campus.add_edge('PVert 125', 'HOH 2', 24.99)
SAU_Campus.add_edge('TAL', 'PVert 127', 30.12)
SAU_Campus.add_edge('PVert 122', 'PVert 128', 28.51)
SAU_Campus.add_edge('PVert 123', 'PVert 130', 50.05)
SAU_Campus.add_edge('PVert 125', 'PVert 131', 44.66)
SAU_Campus.add_edge('HOH 2', 'PVert 131', 49.36)
SAU_Campus.add_edge('PVert 120', 'HOH 1', 58.07)
SAU_Campus.add_edge('HOH 1', 'PVert 132', 66.48)
SAU_Campus.add_edge('PVert 127', 'PVert 13', 31.85)
SAU_Campus.add_edge('PVert 127', 'PVert 128', 26.79)
SAU_Campus.add_edge('PVert 128', 'GRH', 29.61)
SAU_Campus.add_edge('GRH', 'PVert 130', 10.48)
SAU_Campus.add_edge('PVert 130', 'PVert 131', 25.14)
SAU_Campus.add_edge('PVert 131', 'PVert 132', 48.86)
SAU_Campus.add_edge('PVert 132', 'GRH', 62.00)
SAU_Campus.add_edge('GRH', 'PVert 134', 26.79)
SAU_Campus.add_edge('GRH', 'PVert 135', 33.39)
SAU_Campus.add_edge('PVert 133', 'PVert 134', 32.71)
SAU_Campus.add_edge('PVert 134', 'PVert 135', 25.52)
SAU_Campus.add_edge('PVert 135', 'PVert 136', 27.98)
SAU_Campus.add_edge('PVert 132', 'PVert 136', 40.18)
SAU_Campus.add_edge('PVert 136', 'PVert 17', 69.24)

if __name__ == '__main__':
    SAU_Campus.print_graph()
    print(SAU_Campus.vertices)

