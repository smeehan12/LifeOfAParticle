######################################
# Sam Meehan 
#
# How to generate the data for the particle in a box for the case of a 
# Smearing of the position
#
######################################

from ROOT import *
import MyRandomLibrary
import numpy as np

def main():
    
    # coefficients of initial state
    c1 = 1
    c2 = 1
    
    # length of box
    a = 1
    
    # detector smearing - width of the top hat
    det_smear = 0.2

    # events to generate
    nevents = 10000
    
    # for inspection
    h0 = TH1F("h0","h0",400,-2,2)
    
    # write out to file
    fout = open("particle_in_a_box_v1_RealDetector_N"+str(nevents)+".txt","w")
    
    # event generation loop
    for i in range(nevents):

        if i%1000==0:
            print "Processed : ",i

        # get the collapsed wave function of the particle assuming a specific (c1,c2) choice
        pos = GetPositionInterference(c1,c2,a)
        
        # a random smearing is added to the position independent of the true position of the particle
        smear = MyRandomLibrary.GetRangeUniform(-1*det_smear,det_smear)
    
        # calculate the measured position
        pos_det = pos+smear

        # fill into histogram for checking
        h0.Fill(pos_det)
        
        # write to text file for data
        lineout = "{0:10}   {1:10}\n".format(i,pos_det)
        fout.write(lineout)
        
    fout.close()
        
    # draw an save histogram
    c = TCanvas("c","c",200,200)
    h0.SetLineColor(1)
    h0.Draw("hist")
    c.SaveAs("datacheck_v1_smear.eps")
    
    
##########################################################

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
            
            
            
            
            
            


















