import random as r
import numpy as np
from ROOT import *

def main():

    nevents=1000

    gradient = 5

    vals_z_0 = []
    vals_x_0 = []

    vals_z_1 = []
    vals_x_1 = []

    vals_z_2 = []
    vals_x_2 = []

    vals_z_3 = []
    vals_x_3 = []

    for i in range(nevents):

        atom = {"z" : {"know":0 , "val":"?", "obs":"?"} , "x" : {"know":0 , "val":"?", "obs":"?"}}
    
        atom["z"]["val"] = unpolarized()
        atom["x"]["val"] = unpolarized()
        
        print atom
    
        atom = observe(atom, "z", gradient)
    
        vals_z_0.append(atom["z"]["obs"])
        vals_x_0.append(atom["x"]["obs"])

        if atom["z"]["obs"]<0:
            continue
        
        atom = observe(atom, "z", gradient)
    
        vals_z_1.append(atom["z"]["obs"])
        vals_x_1.append(atom["x"]["obs"])

        atom = observe(atom, "x", gradient)

        vals_z_2.append(atom["z"]["obs"])
        vals_x_2.append(atom["x"]["obs"])
    
        if atom["x"]["obs"]<0:
            continue
        
        atom = observe(atom, "z", gradient)
    
        vals_z_3.append(atom["z"]["obs"])
        vals_x_3.append(atom["x"]["obs"])


    print "Number of observations at each stage : "
    print "Stage0 x : ",len(vals_z_0)
    print "Stage0 z : ",len(vals_x_0)
    print "Stage1 x : ",len(vals_z_1)
    print "Stage1 z : ",len(vals_x_1)
    print "Stage2 x : ",len(vals_z_2)
    print "Stage2 z : ",len(vals_x_2)
    print "Stage3 x : ",len(vals_z_3)
    print "Stage3 z : ",len(vals_x_3)

    h0x = TH1F("h0x","h0x",100,-10,10)
    h0z = TH1F("h0z","h0z",100,-10,10)
    h1x = TH1F("h1x","h1x",100,-10,10)
    h1z = TH1F("h1z","h1z",100,-10,10)
    h2x = TH1F("h2x","h2x",100,-10,10)
    h2z = TH1F("h2z","h2z",100,-10,10)
    h3x = TH1F("h3x","h3x",100,-10,10)
    h3z = TH1F("h3z","h3z",100,-10,10)
    
    for pos in vals_x_0:
        h0x.Fill(pos)
    for pos in vals_z_0:
        h0z.Fill(pos)

    for pos in vals_x_1:
        h1x.Fill(pos)
    for pos in vals_z_1:
        h1z.Fill(pos)

    for pos in vals_x_2:
        h2x.Fill(pos)
    for pos in vals_z_2:
        h2z.Fill(pos)

    for pos in vals_x_3:
        h3x.Fill(pos)
    for pos in vals_z_3:
        h3z.Fill(pos)
        
    h0x.GetXaxis().SetTitle("X Deflection")
    h0x.GetYaxis().SetTitle("N Observed")
    h0z.GetXaxis().SetTitle("Z Deflection")
    h0z.GetYaxis().SetTitle("N Observed")

    h1x.GetXaxis().SetTitle("X Deflection")
    h1x.GetYaxis().SetTitle("N Observed")
    h1z.GetXaxis().SetTitle("Z Deflection")
    h1z.GetYaxis().SetTitle("N Observed")

    h2x.GetXaxis().SetTitle("X Deflection")
    h2x.GetYaxis().SetTitle("N Observed")
    h2z.GetXaxis().SetTitle("Z Deflection")
    h2z.GetYaxis().SetTitle("N Observed")

    h3x.GetXaxis().SetTitle("X Deflection")
    h3x.GetYaxis().SetTitle("N Observed")
    h3z.GetXaxis().SetTitle("Z Deflection")
    h3z.GetYaxis().SetTitle("N Observed")
    
    c = TCanvas("c","c",800,400)
    c.Divide(4,2)
    
    c.cd(1)
    h0x.Draw("hist")
    c.cd(5)
    h0z.Draw("hist")

    c.cd(2)
    h1x.Draw("hist")
    c.cd(6)
    h1z.Draw("hist")

    c.cd(3)
    h2x.Draw("hist")
    c.cd(7)
    h2z.Draw("hist")

    c.cd(4)
    h3x.Draw("hist")
    c.cd(8)
    h3z.Draw("hist")
    
    c.SaveAs("result_v3.eps")
        

def unpolarized():
    val = "?"
    return val
    
def observe(atom, direction, gradient):
        
    if direction=="z":
        if atom["z"]["val"]=="?":
            val = r.uniform(-1.0,1.0)
            if val>=0:
                val=1
            else:
                val=-1
            atom["z"]["obs"] = gradient*val
            atom["x"]["obs"] = 0
            atom["z"]["val"] = val
        else:
            atom["z"]["obs"] = gradient*atom["z"]["val"]
            atom["x"]["obs"] = 0

        atom["x"]["val"] = "?"
    elif direction=="x":
        if atom["x"]["val"]=="?":
            val = r.uniform(-1.0,1.0)
            if val>=0:
                val=1
            else:
                val=-1
            atom["x"]["obs"] = gradient*val
            atom["z"]["obs"] = 0
            atom["x"]["val"] = val
        else:
            atom["x"]["obs"] = gradient*atom["x"]["val"]
            atom["z"]["obs"] = 0

        atom["z"]["val"] = "?"
        
    return atom


if __name__ == "__main__":
    main()













