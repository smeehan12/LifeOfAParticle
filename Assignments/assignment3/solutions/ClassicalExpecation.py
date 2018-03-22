######################################
# Sam Meehan 
#
# classical expectation for the particle in a box
#
######################################

from ROOT import *
import MyRandomLibrary
import numpy as np
from array import array

def main():

    # velocity of particle
    v = 1
    
    # maximum amount of time that you can wait
    max_waittime = 100
    
    # width of the box
    box_width = 2
    
    # for storing the outcome in a histogram
    h = TH1F("h","h",20,0,2)
    
    for i in range(100000):
        
        # print the progress every once in a while
        if i%1000==0: 
            print "Event : ",i
        
        # the amount of time you wait after closing your eyes
        t = MyRandomLibrary.GetRangeUniform(0,max_waittime)
        
        # the total distance travelled for that single experiment
        x = v*t
        
        # the number of bounces to know if the modulus will extend from the left or the right
        n_bounces = int(x/box_width)
        
        # the modulus after the final bounce in the box
        x_leftover = x%box_width
        
        # print the progress every once in a while
        if i%1000==0: 
            print "{0:15} {1:5} {2:15}".format(x,n_bounces,x_leftover)
        
        if n_bounces%2 == 0:
            h.Fill(x_leftover)
        else:
            h.Fill(box_width - x_leftover)
        
        
    # draw the histogram
    c = TCanvas("c","c",200,200)
    
    h.SetMinimum(0)
    h.SetMaximum(h.GetBinContent(h.GetMaximumBin())*2.0)
    h.GetXaxis().SetTitle("x measured")
    h.GetYaxis().SetTitle("Frequency")
    
    h.Draw("hist")
    
    c.SaveAs("classical.eps")
            
            
            
if __name__ == "__main__":
    # execute only if run as a script
    main()
            
            
            
            
            
            


















