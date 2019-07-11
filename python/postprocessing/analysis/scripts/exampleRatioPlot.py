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

ele_pt_all = ROOT.TH1F("ele_pt_all","ele_pt_all",20,0,100) #For 20 bins between 0 and 100 GeV 
ele_pt_all.Sumw2()

ele_pt_ctr = ROOT.TH1F("ele_pt_ctr","ele_pt_ctr",20,0,100) #For 20 bins between 0 and 100 GeV 
ele_pt_ctr.Sumw2()



tree.Draw("Electron_pt>>ele_pt_all","")
tree.Draw("Electron_pt>>ele_pt_ctr","abs(Electron_eta)<1.5")

ele_pt_all.SetLineColor(ROOT.kRed)
ele_pt_all.SetMarkerColor(ROOT.kRed)
ele_pt_ctr.SetLineColor(ROOT.kGreen+3)
ele_pt_ctr.SetMarkerColor(ROOT.kGreen+3)

ratio_central = plot.MakeRatioHist(ele_pt_ctr,ele_pt_all,True,False)


canvas = ROOT.TCanvas("c1","c1")
pads = plot.TwoPadSplit(0.29,0.01,0.01)
axish = createAxisHists(2,ele_pt_all,ele_pt_all.GetXaxis().GetXmin(),ele_pt_all.GetXaxis().GetXmax()-0.01)

axish[0].GetYaxis().SetRangeUser(0,1.5*ele_pt_all.GetMaximum())
axish[0].GetYaxis().SetTitle("Entries")
axish[0].GetXaxis().SetTitleSize(0)
axish[0].GetXaxis().SetLabelSize(0)
axish[1].GetXaxis().SetTitle("Electron p_{T} [GeV]")
axish[1].GetYaxis().SetTitle("Ratio")
axish[1].GetYaxis().SetRangeUser(0.6,1.4)


pads[0].cd()
axish[0].Draw()
ele_pt_all.Draw("SAME")
ele_pt_ctr.Draw("SAME")
legend = plot.PositionedLegend(0.4, 0.15, 3, 0.015)
legend.AddEntry(ele_pt_all, "All electrons")
legend.AddEntry(ele_pt_ctr, "Electrons with |#eta|<1.5")
legend.Draw("SAME")

pads[1].cd()
axish[1].Draw()
ratio_central.SetLineColor(ROOT.kGreen+3)
ratio_central.SetMarkerColor(ROOT.kGreen+3)
ratio_central.Draw("SAME")

pads[0].cd()
pads[0].GetFrame().Draw()
pads[0].RedrawAxis()

canvas.SaveAs("electron_pt_with_ratio.pdf")

