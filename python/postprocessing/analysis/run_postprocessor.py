#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

#from PhysicsTools.NanoAODTools.postprocessing.analysis.higgs.vhbb.VHbbProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from  PhysicsTools.NanoAODTools.postprocessing.modules.jme.mht import *
from PhysicsTools.NanoAODTools.postprocessing.analysis.BaselineSelection import *

files=["file:///pnfs/desy.de/cms/tier2/store/user/adewit/SummerProjectSamples/WplusH_HToBB_WToQQ_M125.root"]

selection='''((Sum$((abs(Jet_eta)<2.5 && Jet_pt > 20 && Jet_jetId)) >= 2)||(Sum$((abs(FatJet_eta)<2.5 && FatJet_pt > 200 && FatJet_jetId)) >= 1))&&(Sum$(Electron_pt > 20 && Electron_mvaFall17V2Iso_WP90)<1)&&(Sum$(Muon_pt>20 && Muon_tightId)<1)'''

p=PostProcessor(".",files,selection.replace('\n',' '),branchsel="keep_and_drop.txt",modules=[basesel()],provenance=True,outputbranchsel="keep_and_drop.txt")

p.run()
