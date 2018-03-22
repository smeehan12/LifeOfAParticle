######################################
# Sam Meehan 
#
# the library of example functions for accept reject generation
# in this case for the stretch/shift and the exponential generation of accept reject
#
######################################

import random
import math

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

            
#############################################
# exponential function from accept reject
#############################################
def GetExponential_AcceptReject(tau,low,high):
    while True:
        x = GetRangeUniform(low,high)
        y = GetRangeUniform(0,math.exp(0))
        
        funcVal = math.exp(-(1.0/tau)*x)

        if y<funcVal:
            return x
            
            
#############################################
# exponential function from inverse transform
#############################################
def GetExponential_InverseTransform(tau,low,high):
    # upper bound for CDF generation
    rmin = exp_CDF(low,tau)
    rmax = exp_CDF(high,tau)
    
    r = GetRangeUniform(rmin,rmax)
    x = exp_CDFInv(r,tau)
    
    return x

def exp_PDF(xin,tau):
    val = math.exp(-(1.0/tau)*xin)
    return val
    
def exp_CDF(xin,tau):
    val = 1-math.exp(-(1.0/tau)*xin)
    return val
    
def exp_CDFInv(val,tau):
    xin = -1.0*tau*math.log(1.0-val)
    return xin
    
    
#############################################
# integer from (alpha)**n - geometrical function
#############################################
def GetBinomial(p,low=0,high=2):
    while True:
        x = math.floor(GetRangeUniform(low,high))
        y = GetRangeUniform(0,1.1)
        
        if x<1:
            funcVal = 1-p
        else:
            funcVal = p

        if y<funcVal:
            return x