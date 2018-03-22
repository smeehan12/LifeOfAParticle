######################################
# Sam Meehan 
#
# How to generate the data for the particle in a box for the case of a 
# - Inefficiency of detector #2 on the right 
# - Smearing of detector #1 on the left
#
######################################

from ROOT import *
import MyRandomLibrary
import numpy as np

def main():
    
    # coefficients of initial state
    c1 = 0.7
    c2 = 1.0
    
    # length of box
    a  = 1
    
    # detector smearing
    det_smear = 0.1
    
    # detector efficiency if on right side
    det_eff = 0.3

    # events to generate
    nevents = 10000
    
    # for inspection
    h0 = TH1F("h0","h0",400,-2,2)
    
    # write out to file
    fout = open("particle_in_a_box_v3_RealDetector_N"+str(nevents)+".txt","w")
    
    # event generation loop
    for i in range(nevents):

        if i%1000==0:
            print "Processed : ",i

        # get the collapsed wave function of the particle assuming a specific (c1,c2) choice
        pos = GetPositionInterference(c1,c2,a)
        
        # if the true position is on the right side, the decision if it will get detected
        detect = MyRandomLibrary.GetBinomial(det_eff)

        # where the detected position would get smeared to
        smear = MyRandomLibrary.GetRangeUniform(-1*det_smear,det_smear)
        pos_det = pos+smear
    
        if pos>0.5:
            # if true position is on right side, then it may or may not be detected
            if detect==1:
                h0.Fill(pos_det)
                lineout = "{0:10}   {1:10}\n".format(i,pos_det)
                fout.write(lineout)
        else:
            # if it is on left side, it always gets detected
            h0.Fill(pos_det)        
            lineout = "{0:10}   {1:10}\n".format(i,pos_det)
            fout.write(lineout)
        
    fout.close()
        
    # draw histogram for checking
    c = TCanvas("c","c",200,200)
    h0.SetLineColor(1)
    h0.Draw("hist")
    c.SaveAs("datacheck_v3_effsmear.eps")
    
    
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
            
            
            
            
            
            


















