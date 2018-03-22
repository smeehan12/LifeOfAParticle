######################################
# Sam Meehan 
#
# Analyzing the particle in a box data for the case of a perfect detector
#
######################################

from ROOT import *
import MyRandomLibrary
import numpy as np
from array import array

def main():

    #####################################
    # read in data to make histogram of the observations
    #####################################
    fin = open("particle_in_a_box_v0_PerfectDetector.txt","r")
    
    hdata = TH1F("hdata","hdata",400,-2,2)
    
    for line in fin.readlines():
        event = line.strip().split()
        number   = event[0]
        position = float(event[1])
        hdata.Fill(position)
        
    c = TCanvas("c","c",200,200)
    
    hdata.Draw("pe")
    
    c.SaveAs("perfect_data.eps")
    
    #####################################
    # coefficients of initial state
    #####################################
    
    # values to test for c1 and c2
    c1vals = np.arange(0.1,2.0,0.1)
    c2vals = np.arange(0.8,1.2,0.1)  # limit these
    
    # for saving the outcome of the fits for plotting later
    c1array   = array('d')
    chi2array = array('d')
    
    # test all the c2 and c1 values
    # we are going to draw a graph for the chiSquare for each different c2 value
    for c2 in c2vals:
        for c1 in c1vals:
    
            print "Testing : c1=",c1,"  c2=",c2

            # length of box
            a  = 1

            # events to generate
            nevents = 5000

            # for inspection
            hgen = TH1F("hgen","hgen",400,-2,2)

            # event generation loop
            for i in range(nevents):

                # print out the progress
                if i%1000==0:
                    print "Processed (c2=",c2," , c1=",c1,": ",i

                # Obtain a single "true" position measurement from the probability
                # rule which includes the interference term
                pos = GetPositionInterference(c1,c2,a)

                # fill that position into the histogram
                hgen.Fill(pos)
    
            # draw the graph to the canvas
            c = TCanvas("c","c",200,200)

            hdata.Draw("pe")    

            hgen.SetLineColor(2)
            hgen.Draw("histsame")

            c.SaveAs("perfect_datagen_c1_"+str(c1)+"_c2_"+str(c2)+".eps")

            # calculate the ChiSquare value
            chi2 = GetChiSquare(hdata,hgen)

            # calculate ChiSquare also in root
            chi2root = hdata.Chi2Test(hgen,"UUCHI2")

            print "c1,c2    : ",c1,c2
            print "Chi2     : ",chi2
            print "Chi2Root : ",chi2root
        
            # save in the array for use in making the graph for this c2 value
            c1array.append(c1)
            chi2array.append(chi2)
        
        # make the graph of chiSquare versus c2
        gr = TGraph( len(c1vals), c1array, chi2array )
        gr.SetLineColor( 2 )
        gr.SetLineWidth( 4 )
        gr.SetMarkerColor( 1 )
        gr.SetMarkerStyle( 21 )
        gr.SetMarkerSize(0.4)
        gr.GetXaxis().SetTitle( 'c1Val [c2='+str(c2)+']' )
        gr.GetYaxis().SetTitle( 'ChiSquared' )
        gr.Draw( 'ALP' )
    
        c.SaveAs("chi2scan_c1_"+str(c1)+"_c2_"+str(c2)+".eps")
    
    
##########################################################

def GetChiSquare(h0,h1):

    #check that they have the same number of bins
    if h0.GetNbinsX() != h1.GetNbinsX():
        print "Unequal number of bins - CHECK SOMETHING!"
        return -1
        
    #loop over bins
    chi2 = 0
    for i in range(1, h0.GetNbinsX()):
    
        print i
        
        val0 = h0.GetBinContent(i)
        err0 = h0.GetBinError(i)
        val1 = h1.GetBinContent(i)
        err1 = h1.GetBinError(i)
        
        if val0==0 and val1==0:
            print "Skipping bin : ",i
            continue
        
        val = ((val0-val1)**2)/(err0**2+err1**2)

        chi2 += val
        
    return chi2
        
def GetMaxVal(harr):
    max=0
    for h in harr:
        test = h.GetBinContent(h.GetMaximumBin())
        if test>max:
            max=test
    
    return max

def EvalNoInterference(g1,g2,a,x):
    return (g1*np.sin(np.pi*x/a))**2 + (g2*np.sin(2*np.pi*x/a))**2


def EvalInterference(g1,g2,a,x):
    return (g1*np.sin(np.pi*x/a))**2 + (g2*np.sin(2*np.pi*x/a))**2 + 2*g1*g2*np.sin(np.pi*x/a)*np.sin(2*np.pi*x/a)


def GetPositionNoInterference(g1,g2,a):

    #get max val of function
    max=0
    for x in np.arange(0,a,0.1):
        test = EvalNoInterference(g1,g2,a,x)
        if test>max:
            max=test
            
    #print "MaxVal : ",max

    #generate random number
    while True:
        x = MyRandomLibrary.GetRangeUniform(0.0,a)
        y = MyRandomLibrary.GetRangeUniform(0.0,max)
        
        funcVal = EvalNoInterference(g1,g2,a,x)

        if y<funcVal:
            return x
            
            
            
def GetPositionInterference(g1,g2,a):

    #get max val of function
    max=0
    for x in np.arange(0,a,0.1):
        test = EvalInterference(g1,g2,a,x)
        if test>max:
            max=test
            
    #print "MaxVal : ",max

    #generate random number
    while True:
        x = MyRandomLibrary.GetRangeUniform(0.0,a)
        y = MyRandomLibrary.GetRangeUniform(0.0,max)
        
        funcVal = EvalInterference(g1,g2,a,x)

        if y<funcVal:
            return x
            
            
            
if __name__ == "__main__":
    # execute only if run as a script
    main()
            
            
            
            
            
            


















