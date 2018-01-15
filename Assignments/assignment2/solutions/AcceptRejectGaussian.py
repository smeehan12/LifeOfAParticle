######################################
# Sam Meehan 
# 
# For generating random numbers according to a gaussian PDF
# 
######################################

import random
import numpy as np
from ROOT import *

def main():

    # central value of Gaussian
    mean  = 2.0
    
    # width of gaussian
    width = 1.4
    
    # NGen 
    NGen = 10000
    
    # get maximum of gaussian function
    maxVal = 0
    
    # loop through a bunch of test values and evaluate the function at each
    testVals=np.arange(-10,10,0.01)
    for val in testVals:
        evalVal = EvaluateGaussian(val,mean,width)
        # if the evaluated function is bigger than our current maximum value --> replace it
        if evalVal>maxVal:
            maxVal = evalVal
            
    print "maxVal of Function : ",maxVal
    
    # array to store values for plotting
    savedVals=[]
    
    # continue generating until we have NGen values
    while len(savedVals)<NGen:
        
        # generate a point (xTest,yTest) within our box
        xTest = GetRangeUniform(-10,10)
        yTest = GetRangeUniform(0,1.1*maxVal)
        
        # evaluate the value of the function f(x) which is a gaussian
        gaussian = EvaluateGaussian(xTest,mean,width)
        
        # test the condition that the yTest point is below the evaluated gaussian
        if yTest<gaussian:
            savedVals.append(xTest)
        
    # make histogram for storing output values
    h = TH1F("h","h",100,-10,10)

    # store the values in a histogram
    for x in savedVals:
        h.Fill(x)
        
    # plot it
    c = TCanvas("c","c",200,200)
    
    h.GetXaxis().SetTitle("x Measurement")
    h.GetYaxis().SetTitle("Frequency")
    h.Draw("hist")
    
    c.SaveAs("gaussian.eps")

##############################################################
# evaluate the gaussian function
##############################################################
def EvaluateGaussian(x,mu,sigma):
    # calculate the coefficient in the gaussian
    coeff = (1.0/(sigma*(2*np.pi)**0.5))
    # calculate the argument of the exponential
    arg   = -1.0*(1.0/2.0)*(((x-mu)/sigma)**2)
    # calculate the gaussian itself
    gauss = coeff*np.exp(arg)
    return gauss

##############################################################
# uniform in range from min to max
##############################################################
def GetRangeUniform(min,max):
    # get uniform [0,1]
    x = random.random()
    # stretch
    val = x*(max-min)
    # shift by adding the minimum
    val = val + min
    return val

    
if __name__ == "__main__":
    main()