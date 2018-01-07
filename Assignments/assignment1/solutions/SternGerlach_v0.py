######################################
# Sam Meehan : Stern-Gerlach Experiment Simulator
#
# This simulates the stern gerlach experiment 
# version 0 with classical assumptions
#
######################################

import random as r
import numpy as np
from ROOT import *

def main():

    # nevents
    nevents=1000

    # magnetic field gradient
    gradient = 5

    # for storing observation values
    vals_z_0 = []
    vals_x_0 = []

    vals_z_1 = []
    vals_x_1 = []

    vals_z_2 = []
    vals_x_2 = []

    vals_z_3 = []
    vals_x_3 = []

    # loop over the creation of events
    for i in range(nevents):

        ###################################
        # a new atom is produced
        # know = Have I observed the value of the spin?
        # val  = The value/state endowed by nature
        # obs  = The value I observe in my detection of it
        ###################################
        atom = {"z" : {"know":0 , "val":"?", "obs":"?"} , "x" : {"know":0 , "val":"?", "obs":"?"}}
    
        # it is born in the silver boiler
        atom["z"]["val"] = unpolarized()
        atom["x"]["val"] = unpolarized()
        
        # peep on its properties (not allowed in real life)
        print atom
    
        # send it through the first apparatus with Z magnetic field gradient
        atom = observe(atom, "z", gradient)
    
        # save observations on screen
        vals_z_0.append(atom["z"]["obs"])
        vals_x_0.append(atom["x"]["obs"])

        # only allow the atoms travelling in + direction to pass
        if atom["z"]["obs"]<0:
            continue
        
        # observe again in Z
        # send it through the first apparatus with Z magnetic field gradient
        atom = observe(atom, "z", gradient)
    
        # save observations on screen
        vals_z_1.append(atom["z"]["obs"])
        vals_x_1.append(atom["x"]["obs"])

        # now observe in X
        # send it through the first apparatus with Z magnetic field gradient
        atom = observe(atom, "x", gradient)

        # save observations on screen
        vals_z_2.append(atom["z"]["obs"])
        vals_x_2.append(atom["x"]["obs"])
    
        # only allow the atoms travelling in + direction to pass
        if atom["x"]["obs"]<0:
            continue
        
        # now observe in X
        # send it through the first apparatus with Z magnetic field gradient
        atom = observe(atom, "z", gradient)
    
        # save observations on screen
        vals_z_3.append(atom["z"]["obs"])
        vals_x_3.append(atom["x"]["obs"])


    print "Number of observations at each stage : "
    print "Stag0 x : ",len(vals_z_0)
    print "Stag0 z : ",len(vals_x_0)
    print "Stag1 x : ",len(vals_z_1)
    print "Stag1 z : ",len(vals_x_1)
    print "Stag2 x : ",len(vals_z_2)
    print "Stag2 z : ",len(vals_x_2)
    print "Stag3 x : ",len(vals_z_3)
    print "Stag3 z : ",len(vals_x_3)


    # fill the data into histograms to display

    # declare histograms to fill
    h0x = TH1F("h0x","h0x",100,-10,10)
    h0z = TH1F("h0z","h0z",100,-10,10)
    h1x = TH1F("h1x","h1x",100,-10,10)
    h1z = TH1F("h1z","h1z",100,-10,10)
    h2x = TH1F("h2x","h2x",100,-10,10)
    h2z = TH1F("h2z","h2z",100,-10,10)
    h3x = TH1F("h3x","h3x",100,-10,10)
    h3z = TH1F("h3z","h3z",100,-10,10)
    
    # put the data in them
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
        
    # change style and label axes
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
    
    # make canvas where you can draw them all
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
    
    c.SaveAs("result_v0.eps")
        
############################
# v0 : 
# generation  : 
#   - classical - fully random
# observation : 
#   - classical - state persists
############################
def unpolarized():
    val = r.uniform(-1.0,1.0)
    return val
    
def observe(atom, direction, gradient):
        
    if direction=="z":
        atom["z"]["obs"] = gradient*atom["z"]["val"]
        atom["x"]["obs"] = 0
    elif direction=="x":
        atom["x"]["obs"] = gradient*atom["x"]["val"]
        atom["z"]["obs"] = 0
        
    return atom

############################
# program will execute main by default
############################
if __name__ == "__main__":
    # execute only if run as a script
    main()













