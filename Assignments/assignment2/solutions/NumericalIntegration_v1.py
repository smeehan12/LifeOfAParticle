######################################
# Sam Meehan 
#
# Numerical integration of the given function for many different
# choices of the number of divisions N and plotting the solutions
# for each
#
######################################

import array
from ROOT import *

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

    # specify the number of pieces to decompose the domain into
    N = 100

    # try many different increasing values
    NTests=[10,50,100,200,1000]
    
    # lists to store the information in for making a graph with
    arr_N = array.array('d')
    arr_I = array.array('d')

    # test many different N values
    for N in NTests:

        # we will hold the full integral in "sum"
        # reset this to be zero from the previous calculation
        sum = 0.0
    
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
    
        arr_N.append(N)
        arr_I.append(sum)
        
        
    # make a graph of the results
    # make the graph
    c = TCanvas("c","c",200,200)
    graph = TGraph( len(arr_N), arr_N, arr_I )

    graph.SetLineColor( 2 )
    graph.SetLineWidth( 4 )
    graph.SetMarkerColor( 1 )
    graph.SetMarkerStyle( 21 )
    graph.SetMarkerSize(0.4)

    graph.GetXaxis().SetTitle( 'N Slices' )
    graph.GetYaxis().SetTitle( 'Evaluated Integral' )
    
    graph.SetMinimum(3200)
    graph.SetMaximum(4200)

    graph.Draw('ALP')
    
    line1 = TLine(0,4078.09333333,1000,4078.09333333)
    line1.SetLineColor(4)
    line1.SetLineWidth(3)
    line1.SetLineStyle(2)
    line1.Draw()
    xlabel = TText();
    xlabel.SetNDC();
    xlabel.SetTextColor(4);
    xlabel.SetTextSize(0.03);
    xlabel.SetTextAlign(22);
    xlabel.SetTextAngle(0);
    xlabel.DrawText(0.48, 0.85, "AnalyticValue = 4078.09333333");
    
    c.SetRightMargin(0.15)

    c.SaveAs("NumericalIntegration_v1.eps")

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
    