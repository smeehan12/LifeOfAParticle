######################################
# Sam Meehan 
#
# Numerical integration of the given function for a single choice
# of the number of divisions N
#
######################################

def main():

    ###################################
    # true value is hardcoded
    # f(x)      = 3*(x**3)     - 4*(x**2)+3.219*x
    # Int[f(x)] = (3/4)*(x**4) - (4/3)*(x**3) + (3.219/2)*(x**2)
    ###################################
    
    IntFa = EvalIntegral(1.0)
    IntFb = EvalIntegral(9.0)

    IntegralExact = IntFb-IntFa
    
    print "IntegralExact : ",IntegralExact

    # we will hold the full integral in "sum"
    sum = 0.0

    # specify the number of pieces to decompose the domain into
    N = 100
    
    # bounds
    a = 1.0
    b = 9.0
    
    # value of dx
    dx = (b-a)/N
    
    for i in range(N):
        
        # the current x position is the starting point (a)
        # plus the number of steps we have taken
        xi = a + dx*i
        
        # eval the function at the left hand side
        fi = EvalFunction(xi)
        
        # rectangle
        Ai = fi*dx
        
        # add to the sum
        sum = sum+Ai
        
    print "Integral : ",sum
    

def EvalFunction(x):
    # just for the evaluation of the function
    f = 3*(x**3)-4*(x**2)+3.219*x
    return f
    
def EvalIntegral(x):
    # hardcoded exact integral
    f = (3.0/4.0)*(x**4) - (4.0/3.0)*(x**3) + (3.219/2.0)*(x**2)
    return f
    
if __name__ == "__main__":
    main()
    