######################################
# Sam Meehan 
# 
# For generating the original set of random numbers for the correlation
# question.  This implements the accept/reject method in two dimensions
# 
# The correlation coefficient is hardcoded and can be found below to be 0.6
# 
######################################

import random
import numpy as np
from ROOT import *

def main():

    # lists to store the generated x and y pairs
    xgen=[]
    ygen=[]

    # continue generating until we have 1000 values
    while len(xgen)<1000:
        
        print "Generated : ",len(xgen)
        
        xTest=0
        yTest=0
        
        # using the accept reject method in 2D
        while True:
            
            # generate the uniformly distributed (x,y) pairs
            xTest = random.uniform(-10,10)
            yTest = random.uniform(-10,10)
            
            # generate "z" as the auxiliary variable
            zTest = random.uniform(0,1)
            
            # evaluate the function value of the 2D gaussian
            fEval = EvalGauss(xTest,yTest)
            
            # if the auxiliary value "z" is below the gaussian, then accept the (x,y) pair
            if zTest<fEval:
                break
        
        # if it broke out of the loop above, then its a good pair and we add it to the list
        xgen.append(xTest)
        ygen.append(yTest)
        
    
    # make a histogram for plotting
    h = TH2F("h","h",200,-10,10,200,-10,10)
    
    # store for assignment
    fout = open("random_x_y_pairs.txt","w")
    
    # fill the (x,y) pairs into the 2D histogram
    for i in range(len(xgen)):
        h.Fill(xgen[i],ygen[i])
        fout.write("{0:10} {1:10}\n".format(round(xgen[i],4), round(ygen[i],4)))
        
    # close the output file
    fout.close()
        
    # save it on a canvas
    c = TCanvas("c","c",200,200)
    h.Draw("colz")
    c.SaveAs("correlation_gen_check.eps")
        
        

def EvalGauss(x1,x2):

    # hardcode the values of the parameter
    mu1=0
    mu2=0
    s1=2
    s2=2
    rho=0.6
    
    # calculate the coefficient in the gaussian
    coeff = (1.0/(2*np.pi*s1*s2*(1.0-rho**2)**0.5))

    # calculate the argument of the exponential
    arg   = -1.0*(1.0/(2*1-rho**2))*(  ((x1-mu1)/s1)**2 + ((x2-mu2)/s2)**2 - 2*rho*((x1-mu1)/s1)*((x2-mu2)/s2) )
    
    # calculate the gaussian itself
    gauss = coeff*np.exp(arg)
    
    # return that value
    return gauss
    
    
    
    
if __name__ == "__main__":
    main()