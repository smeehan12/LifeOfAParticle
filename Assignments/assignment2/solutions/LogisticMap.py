######################################
# Sam Meehan 
#
# the logistic map transformation and evaluation of the "randomness"
#
######################################

import numpy as np
from ROOT import *

def main():

    # histogram for storing the x values from the logistic map directly
    hx = TH1F("hx","hx",100,0,1)
    
    # histogram for storing the yi values which are derived from the output
    # of the logistic map
    hy = TH1F("hy","hy",100,0,1)

    # 2D distribution of the (x_i,x_i+1) values 
    hcorr = TH2F("hcorr","hcorr",100,0,1,100,0,1)

    # lambda controls the chaotic behavior of progression
    L = 1
    
    # x as the initial seed
    x = 0.7
    
    # the initial y value
    y = (2.0/np.pi)*np.arcsin(x**0.5)

    for i in range(100000):
        # store the previous iterations values somwhere
        x0 = x
        y0 = y
    
        # create n+1 x value
        x = LogisticTransform(L,x0)

        # transform the n+1 x-value to give y value that will be uniform distributed
        y = RecastTransform(x)
    
        print "Inspecting generation : ",x,y
    
        # fill into histograms for inspection
        hx.Fill(x)
        hy.Fill(y)
        hcorr.Fill(y,y0)
        


    # for drawing to canvas
    c = TCanvas("c","c",400,400)

    # raw numbers
    hx.SetLineColor(1)
    hx.Scale(1.0/hx.Integral())
    hx.Draw("hist")

    hy.SetLineColor(2)
    hy.Scale(1.0/hy.Integral())
    hy.Draw("histsame")
    
    leg = TLegend(0.5,0.5,0.9,0.9)
    leg.AddEntry(hx,"Generated","L")
    leg.AddEntry(hy,"Transformed","L")
    leg.Draw()
    
    c.SaveAs("logistic.eps")

    # autocorrelations
    hautocorr.Draw("colz")
    c.SaveAs("logistic_2d_correlations.eps")



def LogisticTransform(Lin, xin):
    outval = 4.0*Lin*xin*(1-xin)
    return outval
    
def RecastTransform(xin):
    yout = (2.0/np.pi)*np.arcsin(xin**0.5)
    return yout



############################
# program will execute main by default
############################
if __name__ == "__main__":
    # execute only if run as a script
    main()