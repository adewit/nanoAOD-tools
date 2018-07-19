import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import sys

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import * 

class BaseSelection(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("my_fun_var","F");
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        taus = Collection(event, "Tau")
        jets = list(Collection(event,"Jet"))


        selElectrons = [x for x in electrons if x.mvaSpring16GP_WP80 and x.pt >30 and x.pfRelIso03_all < 0.15]
        selTaus = [x for x in taus if x.pt >30]

        my_fun_var=0.
        for e in selElectrons:
           for t in selTaus:
               if e.charge != t.charge:
                   my_fun_var+=(e.pt+t.pt)

        self.out.fillBranch("my_fun_var",my_fun_var)


        return True

basesel = lambda: BaseSelection()
