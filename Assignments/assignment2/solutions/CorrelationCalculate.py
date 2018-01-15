######################################
# Sam Meehan 
# 
# For calculating the linear correlation coefficient for a set of
# data points (x,y)
# 
######################################

# we are importing and using the functions that we defined for the 
# calculation of the standard deviation
import StandardDeviation

def main():

    # store the data in two ordered lists that correspond to each other
    xin=[]
    yin=[]

    fin = open("random_x_y_pairs.txt","r")
    for line in fin.readlines():
        splitline=line.strip().split()
    
        if len(splitline)<=1:
            continue
    
        xin.append(float(splitline[0]))
        yin.append(float(splitline[1]))
    
    fin.close()

    # create another list which is the product of each (x,y) pair
    xyMult=[]
    for i in range(len(xin)):
        xyMult.append(xin[i]*yin[i])
    
    # mean of xy : E[xy]
    Exy = StdCalc.MyMean(xyMult)
    print "Exy : ",Exy

    # mean x
    meanX = StdCalc.MyMean(xin)
    print "meanX : ",meanX

    # sigma x
    sigmaX = StdCalc.MySigma(xin)
    print "sigmaX : ",sigmaX

    # mean y
    meanY = StdCalc.MyMean(yin)
    print "meanY : ",meanY

    # sigma y
    sigmaY = StdCalc.MySigma(yin)
    print "sigmaY : ",sigmaY

    # variance
    Vxy = Exy - meanX*meanY
    print "Vxy : ",Vxy

    # correlation
    rhoxy = Vxy/(sigmaX*sigmaY)
    print "rho(xy) : ",rhoxy

