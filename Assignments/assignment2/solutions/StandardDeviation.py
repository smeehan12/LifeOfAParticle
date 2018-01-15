######################################
# Sam Meehan 
#
# Calculation of the standard deviation using user defined functions
# for which there is no need to import any libraries
#
######################################


def main():

    # read in the data to the x and y lists
    # we will only use the "x" list in this problem
    xin=[]
    yin=[]

    fin = open("random_x_y_pairs.txt","r")
    for line in fin.readlines():
        splitline=line.strip().split()
    
        if len(splitline)<=1:
            continue
    
        xin.append(float(splitline[0]))
        yin.append(float(splitline[1]))
        
        
    # pass the list of x values to the function that calculates sigma
    std = MySigma(xin)
    
    print "Std(x) : ",std
    
    

# calculate the number of elements in the list
def MyN(list):
    print "List : ",list
    n=0
    for i in list:
        n = n+1
        
    print "Returning N : ",n
    return n

# calculates the sum of the elements of the list
def MySum(list):
    sum=0
    for i in list:
        print "type i : ",type(i)
        sum = sum+i
    return sum

# calculate the mean of the elements using the MySum and MyN functions
def MyMean(list):
    mean = 0
    
    sum = MySum(list)
    nel = MyN(list)
    
    if nel>0:
        mean=float(sum)/float(nel)
    else:
        print "How do you have a 0 or negative number of elements! - CHECK THIS"
        
    return mean
    
# for the calculation of the square root to gauge "distances"
def MyAbs(x):

    if x>=0:
        return x
    else:
        return -1.0*x
        
# this is the definition of the test function that is then used below in the sqrt function algorithm
def MyTestFunc(x):
    return x*x
    
# implementation of the square root
def MySqrt(y, precision):

    # make a list of all the values that you will test
    testingVals = []

    # there will be a number of elements in this list which depends on the desired
    # precision for the solution
    nVal = int(float(y)/precision)
    
    # test all values from (0,y) in steps of "precision"
    for i in range(nVal):
        testingVals.append(i*precision)
        
    # this will be the value which we keep as our temporary solution and is overwritten
    closest = 0

    # go through and find which value within our list gives the closest answer to being the square root    
    for x in testingVals:
        
        func_test  = MyTestFunc(x)
        func_close = MyTestFunc(closest)
        
        if MyAbs(func_test-y)<MyAbs(func_close-y):
            closest = x
                
    return closest
            
        

# calculate the standard deviation using these functions above
def MySigma(list):

    # print out the list of values for inspection
    print "List (MySigma) : ",list

    # the sum inside the square root
    sum2 = 0
    
    mean = MyMean(list)
    nel  = MyN(list)
    
    for i in list:
        sum2 = sum2 + (mean-i)*(mean-i)
        
    variance = float(sum2)/float(nel)

    std = MySqrt(variance,precision=0.0001)  # hardcoded precision - UGLY!
    
    return std

    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    