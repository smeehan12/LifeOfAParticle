######################################
# Sam Meehan 
# 
# calculating the error value S for the linear regression
# for a single choice of (m,b) parameters
# 
######################################

def main():

    # input data
    xPoints = [1.0,2.2,3.0,3.9,4.8]
    yPoints = [0.5,1.1,1.3,2.1,2.6]

    # values to guess for m and b
    mTest = 1.2
    bTest = 0.3
    
    # for storing the sum of the errors
    sum = 0
    
    for i in range(len(xPoints)):
    
        # get the data necessary for the Si calculation
        xi = xPoints[i]
        yi = yPoints[i]
        fi = EvalLine(mTest,bTest,xi)
        
        # calculate Si for this term
        Si = (fi-yi)**2
        
        # add to the sum
        sum = sum+Si
        
    print "S = ",sum
    
    

def EvalLine(m,b,x):
    f = m*x+b
    return f
    
    
if __name__ == "__main__":
    main()
    