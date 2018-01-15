######################################
# Sam Meehan 
# 
# calculating the error value S for many different
# parameter choices with a subsequent plotting in the 2D space
# of (m,b)
#
######################################

import numpy
from ROOT import *

def main():

    # input data
    xPoints = [1.0,2.2,3.0,3.9,4.8]
    yPoints = [0.5,1.1,1.3,2.1,2.6]

    # many values of m and b to test
    mTestPoints=numpy.arange(0,1,0.01)
    bTestPoints=numpy.arange(-1,1,0.01)
    
    # histogram for storing minimization data
    m_n   = len(mTestPoints)
    m_min = min(mTestPoints)
    m_max = max(mTestPoints)
    b_n   = len(bTestPoints)
    b_min = min(bTestPoints)
    b_max = max(bTestPoints)
    h = TH2F("h","h",m_n,m_min,m_max,b_n,b_min,b_max)
    
    # sizes of m and b arrays
    print "m points : ",len(mTestPoints)
    print "b points : ",len(bTestPoints)
    
    # test all possible (mTest,bTest) combinations
    for im in range(len(mTestPoints)):
        for ib in range(len(bTestPoints)):
        
            # get the values for m and b to test
            mTest=mTestPoints[im]
            bTest=bTestPoints[ib]
            
            # for storing the sum of the errors
            sum = 0
    
            # loop through all the data points you have to calculate the sum of the errors
            for i in range(len(xPoints)):
    
                # get the data necessary for the Si calculation
                xi = xPoints[i]
                yi = yPoints[i]
                fi = EvalLine(mTest,bTest,xi)
        
                # calculate Si for this term
                Si = (fi-yi)**2
        
                # add to the sum
                sum = sum+Si
        
            print "m={0:5}  b={1:5}  ==> S = {2:5}".format(mTest,bTest,sum)
            
            # store this value in the histogram
            h.SetBinContent(im+1,ib+1,sum)
            
            
    # find the minimum value by searching the histogram
    minS=100000
    mBest=-100.0
    bBest=-100.0
    for im in range(1,len(mTestPoints)):
        for ib in range(1,len(bTestPoints)):
            current = h.GetBinContent(im,ib)
            print "Current : ",im,ib,current
            if current<minS:
                minS=current
                mBest=mTestPoints[im]
                bBest=bTestPoints[ib]
                print "New Min : ",minS,mBest,bBest
            
    # make a marker to plot the best fit central value
    print "mBest,bBest : ",mBest,bBest
    marker = TMarker(mBest,bBest,20)
    marker.SetMarkerSize(0.5)
    marker.SetMarkerColor(2)
            
    # plot the result
    c = TCanvas("c","c",200,200)
    c.SetRightMargin(0.02)
    c.SetLeftMargin(0.15)
    c.SetBottomMargin(0.15)
    c.SetRightMargin(0.15)
    
    h.SetTitle("Line Fitting")
    h.GetXaxis().SetTitle("m Value Tested")
    h.GetYaxis().SetTitle("y Value Tested")
    h.GetZaxis().SetTitle("S Error")
    h.GetXaxis().SetLabelSize(0.04)
    h.GetYaxis().SetLabelSize(0.04)
    h.GetXaxis().SetTitleOffset(1.5)
    h.GetYaxis().SetTitleOffset(1.5)
    h.GetZaxis().SetTitleOffset(1.5)
    h.SetStats(0)
    h.SetLineColor(1)
    h.SetLineWidth(3)
    h.SetMarkerStyle(20)
    h.SetMarkerSize(0.5)
    h.SetContour(1000);
    h.SetMaximum(50);
    
    xlabel = TText();
    xlabel.SetNDC();
    xlabel.SetTextColor(2);
    xlabel.SetTextSize(0.03);
    xlabel.SetTextAlign(22);
    xlabel.SetTextAngle(0);
    
    h.Draw("cont1")
    marker.Draw("same")
    xlabel.DrawText(0.48, 0.5, "Best Fit Value");
    c.SaveAs("line_minimization_contour.pdf")
    
    h.Draw("colz")
    marker.Draw("same")
    xlabel.DrawText(0.48, 0.5, "Best Fit Value");
    c.SaveAs("line_minimization_color.pdf")
    
    

def EvalLine(m,b,x):
    f = m*x+b
    return f
    
    
if __name__ == "__main__":
    main()
    