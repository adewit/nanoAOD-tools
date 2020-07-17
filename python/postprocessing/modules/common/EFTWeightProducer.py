import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from PhysicsTools.NanoAODTools.postprocessing.modules.common.standalone_reweight import *

class EFTWeightProducer(Module):
    def __init__(self,dirname,pdgsout):
        self.dirname = dirname
        self.pdgsout = pdgsout
        self.rw = StandaloneReweight(dirname)

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("nEFTWeights","I")
        self.out.branch("EFTWeights","F",1,"nEFTWeights")
        self.out.branch("EFTWeightsUntransformed","F",1,"nEFTWeights")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        lheparts = list(Collection(event, "LHEPart"))
        lheinfo = Object(event,"LHE")
        nrwlheparts = [x for x in lheparts if not (x.status > 0 and (abs(x.pdgId) not in self.pdgsout))]
        pdgs = [x.pdgId for x in nrwlheparts]
        helicities = [x.spin for x in nrwlheparts]
        status = [x.status for x in nrwlheparts]
        alphas = lheinfo.AlphaS
        useSpin = True
        if helicities[0]>3:
            useSpin = False
        parts = []
        for part in nrwlheparts:
            lhe = ROOT.TLorentzVector()
            lhe.SetPtEtaPhiM(part.pt,part.eta,part.phi,part.mass)
            if part.status<0:
                energy = math.sqrt(part.incomingpz*part.incomingpz+part.mass*part.mass)
                parts.append([energy,0.,0.,part.incomingpz])
            else:
                parts.append([lhe.E(),lhe.Px(),lhe.Py(),lhe.Pz()])

       
        weights = self.rw.ComputeWeights(parts, pdgs, helicities, status, alphas, useSpin)
        transformedweights = self.rw.TransformWeights(weights)
        
        self.out.fillBranch("nEFTWeights",len(transformedweights))
        self.out.fillBranch("EFTWeights",transformedweights)
        self.out.fillBranch("EFTWeightsUntransformed",weights)
        return True

eftweightszh = lambda : EFTWeightProducer('rw_zh-HEL',[11,12,13,14,15,16,25])


