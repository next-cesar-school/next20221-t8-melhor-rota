
ESC1 = ESC2 = ESC3 = DESC1 = DESC2 = DESC3 = INT1 = INT2 = INT3 = INT4 = INT5 = INT6 = INT7 = INT8 = INT9 = INT10 = INT11 = INT12 = INT13 = 0
ESC1INT4 = INT4INT5 = INT1INT3 = 200
ESC2INT11 = 160
ESC3INT7 = DESC3INT12 = 190
DESC1INT1 = INT5INT6 = 100 
DESC2INT10 = 140
INT1INT2 = 270
INT2INT3 = INT8INT9 = 250
INT2INT8 = INT7INT13 = 260
INT3INT4 = INT6INT7 = 120
INT7INT8 = 210
INT9INT10 = INT9INT11 = 130
INT9INT13 = 90
INT11INT12 = 170
INT12INT13 = 300

V = {ESC1, ESC2, ESC3, DESC1, DESC2, DESC3, INT1, INT2, INT3, INT4, INT5, INT6, INT7, INT8, INT9, INT10, INT11, INT12, INT13}
E = {ESC1INT4, ESC2INT11, ESC3INT7, DESC1INT1, DESC2INT10, DESC3INT12, INT1INT2, INT1INT3, INT2INT3, INT2INT8, INT3INT4, INT4INT5, INT5INT6, INT6INT7, INT7INT8, INT7INT13, INT8INT9, INT9INT10, INT9INT11, INT9INT13, INT11INT12, INT12INT13}

GRAPH = { 
    "ESC1" : ["INT4"],
	"ESC2" : ["INT11"],
	"ESC3" : ["INT7"],
	"DESC1" : ["INT1"],
	"DESC2" : ["INT10"],
	"DESC3" : ["INT12"],
	"INT1" : ["INT2", "INT3"],
	"INT2" : ["INT3", "INT8"],
	"INT3" : ["INT4"],
	"INT4" : ["INT5"],
	"INT5" : ["INT6"],
	"INT6" : ["INT7"],
	"INT7" : ["INT8", "INT13"],
	"INT8" : ["INT9"],
	"INT9" : ["INT10", "INT11", "INT13"],
	"INT10" : ["DESC2", "INT9"],
	"INT11" : ["INT12"],
	"INT12" : ["INT13"],
	"INT13" : ["INT7", "INT9", "INT12"]
}

print(GRAPH)

class GRAPH:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

graph_elements = { 
    "ESC1" : ["INT4"],
	"ESC2" : ["INT11"],
	"ESC3" : ["INT7"],
	"DESC1" : ["INT1"],
	"DESC2" : ["INT10"],
	"DESC3" : ["INT12"],
	"INT1" : ["INT2", "INT3"],
	"INT2" : ["INT3", "INT8"],
	"INT3" : ["INT4"],
	"INT4" : ["INT5"],
	"INT5" : ["INT6"],
	"INT6" : ["INT7"],
	"INT7" : ["INT8", "INT13"],
	"INT8" : ["INT9"],
	"INT9" : ["INT10", "INT11", "INT13"],
	"INT10" : ["DESC2", "INT9"],
	"INT11" : ["INT12"],
	"INT12" : ["INT13"],
	"INT13" : ["INT7", "INT9", "INT12"]
}

g = GRAPH(graph_elements)
print(g.getVertices())

class graph_edges:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if (nxtvrtx, vrtx) not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

graph_elements = { 
    "ESC1" : ["INT4"],
	"ESC2" : ["INT11"],
	"ESC3" : ["INT7"],
	"DESC1" : ["INT1"],
	"DESC2" : ["INT10"],
	"DESC3" : ["INT12"],
	"INT1" : ["INT2", "INT3"],
	"INT2" : ["INT3", "INT8"],
	"INT3" : ["INT4"],
	"INT4" : ["INT5"],
	"INT5" : ["INT6"],
	"INT6" : ["INT7"],
	"INT7" : ["INT8", "INT13"],
	"INT8" : ["INT9"],
	"INT9" : ["INT10", "INT11", "INT13"],
	"INT10" : ["DESC2", "INT9"],
	"INT11" : ["INT12"],
	"INT12" : ["INT13"],
	"INT13" : ["INT7", "INT9", "INT12"]
}

g = graph_edges(graph_elements)
print(g.edges())                