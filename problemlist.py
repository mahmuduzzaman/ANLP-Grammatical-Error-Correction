import problemsolution as prbSoln

class ProblemTypeList:
    lstProblem     = None
    problemType    = None
    probStartEar   = None
    probEndEar     = None
    synErrorEar    = None
    
    def __init__(self,typeProb):
        self.problemType = typeProb
        self.lstProblem  = []
        
    def addProb(self,prb):
        probStart,probEnd,synError,errorType = prb
        #print(prb)
        
        if probStart ==self.probStartEar:
            self.updateLastProb(prb)
        else:
            self.lstProblem.append(prb)
        
        self.probStartEar = probStart
        self.probEndEar   = probEnd
        self.synErrorEar  = synError
        
    def updateLastProb(self,prb):
        self.lstProblem[len(self.lstProblem)-1]=prb
    
    def getProblemList(self):
        return self.lstProblem    
            
class ProblemList:
    lstProbSolnclassobj = None
    lstSolutions    = None
    lstProb         = None
    lstWords        = None
    
    #different lists for different error types
    lstArtChk       = None
    lstArt          = None
    lstSpel         = None
    lstSVABase      = None
    
    def __init__(self,lstWordval):
        self.lstProb             = []
        self.lstProbSolnclassobj = []
        self.lstSolutions        = []
        self.lstWords            = lstWordval
        #initiate lists
        self.lstArtChk           = ProblemTypeList("ArtChk")
        self.lstArt              = ProblemTypeList("ART")
        self.lstSpel             = ProblemTypeList("SPEL")
        self.lstSVABase          = ProblemTypeList("SVABASE")
        
    def AddToProblemListTypewise(self, errorType,prb):
        if errorType == "ART":
            self.lstArt.addProb(prb)
        elif errorType == "ArtChk":
            self.lstArtChk.addProb(prb)
        elif errorType == "SPEL":
            self.lstSpel.addProb(prb)
        elif errorType == "SVABASE":
            self.lstSVABase.addProb(prb)
            
    def getProbList(self):
        self.lstProb = self.lstArt.getProblemList() + self.lstArtChk.getProblemList() + self.lstSpel.getProblemList() + self.lstSVABase.getProblemList()
        self.genProbSolnObj()
        return self.lstProb
        
    def genProbSolnObj(self):
        #adding to problem list
        for start,end,typev,errorType in self.lstProb:
            #print(start,end,typev,errorType)
            self.lstProbSolnclassobj.append(prbSoln.ProblemSolution(start,end,typev,errorType,self.lstWords))
    
    def getSolutions(self):
        for prob in self.lstProbSolnclassobj:
            self.lstSolutions.append(prob.getSolution())
        return self.lstSolutions