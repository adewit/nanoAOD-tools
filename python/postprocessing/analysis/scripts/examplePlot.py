import ROOT
import PhysicsTools.NanoAODTools.plotting as plot
import os
import numpy as np

ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(ROOT.kTRUE)
#ROOT.TH1.AddDirectory(False)
plot.ModTDRStyle()


def createAxisHists(n,src,xmin=0,xmax=499):
  result = []
  for i in range(0,n):
    res = src.Clone()
    res.Reset()
    res.SetTitle("")
    res.SetName("axis%(i)d"%vars())
    res.SetAxisRange(xmin,xmax)
    res.SetStats(0)
    result.append(res)
  return result

infile = ROOT.TFile.Open("/afs/desy.de/user/d/dewita/public/output_ZH125_ZLL_powheg_1.root")
tree = infile.Get("Events")

xbins = [0.,10.,20.,30.,40.,50.,60.,70.,80.,90.,100.,110.,120.,130.,140.,150.,160.,170.,180.,190.,200.,210.,220.,240.,260.,280.,300.,350.,400.,450.,500.]
ele_pt = ROOT.TH1F("ele_pt","ele_pt",20,0,100) #For 20 bins between 0 and 100 GeV 
ele_pt.Sumw2()
h_mass = ROOT.TH1F("h_mass","h_mass",len(xbins)-1,np.array(xbins)) #To use variable bin width based on the array xbins
h_mass.Sumw2()



tree.Draw("Electron_pt>>ele_pt","")
tree.Draw("H_mass>>h_mass","")

ele_pt.SetLineColor(ROOT.kRed)
h_mass.SetLineColor(ROOT.kBlue)


canvas = ROOT.TCanvas("c1","c1")
pads = plot.OnePad()
axish = createAxisHists(1,ele_pt,ele_pt.GetXaxis().GetXmin(),ele_pt.GetXaxis().GetXmax()-0.01)
axish[0].GetYaxis().SetRangeUser(0,1.5*ele_pt.GetMaximum())
axish[0].GetXaxis().SetTitle("Electron p_{T} [GeV]")
axish[0].GetYaxis().SetTitle("Entries")

pads[0].cd()
axish[0].Draw()
ele_pt.Draw("LSAME")
legend = plot.PositionedLegend(0.2, 0.15,3,0.015)
legend.AddEntry(ele_pt,"Z(ll)H(bb)")
legend.Draw("SAME")

canvas.SaveAs("Ele_pt.pdf")

canvas1 = ROOT.TCanvas("c2","c2")
pads1 = plot.OnePad()
axish1 = createAxisHists(1,h_mass,h_mass.GetXaxis().GetXmin(),h_mass.GetXaxis().GetXmax()-0.01)
axish1[0].GetYaxis().SetRangeUser(0,1.5*h_mass.GetMaximum())
axish1[0].GetXaxis().SetTitle("Di-jet mass [GeV]")
axish1[0].GetYaxis().SetTitle("Entries")

pads1[0].cd()
axish1[0].Draw()
h_mass.Draw("LSAME")
legend1 = plot.PositionedLegend(0.2, 0.15,3,0.015)
legend1.AddEntry(h_mass,"Z(ll)H(bb)")
legend1.Draw("SAME")

canvas1.SaveAs("h_mass.pdf")
