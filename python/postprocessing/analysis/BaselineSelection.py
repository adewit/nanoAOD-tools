import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import sys

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import * 

class BaselineSelection(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("H_mass","F");
        self.out.branch("Jet_HT","F");
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = list(Collection(event,"Jet"))
        fatJets = list(Collection(event,"FatJet"))

        #apply some selection:
        selBJets = [x for x in jets if x.pt>20 and abs(x.eta)<2.5 and x.jetId>0 and x.btagDeepB>0.4941]
        selJets = [x for x in jets if x.pt>20 and abs(x.eta)<4.8 and x.jetId>0]


        if len(selBJets) < 2: #Require at least two b-tagged jets
            return False 

        Jet_HT=0.
        H_mass=0.
        reco_H = ROOT.TLorentzVector()
        reco_H=(selBJets[0].p4()+selBJets[1].p4())
        for j in selJets:
            Jet_HT+=(j.pt)

        self.out.fillBranch("H_mass",reco_H.M())
        self.out.fillBranch("Jet_HT",Jet_HT)


        return True

basesel = lambda: BaselineSelection()
