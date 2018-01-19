import random
import array
from ROOT import *

# canvas for plotting
c = TCanvas("c","c",200,200)

# appreciation
mu    = 0.2 

# volatility
sigma = 0.01




# perform this procedure for many different values of tend
tendTests=[0.1,0.2,0.5,1.0,2.0,5.0,10.0]

# store the mean and the width of the final output distribution
arr_tend   = array.array('d')
arr_mean   = array.array('d')
arr_width  = array.array('d')

for itend in range(len(tendTests)):

    # get the current tend that we want to test
    tend = tendTests[itend]
    
    # total time and time step size
    dt     = 0.01
    nsteps = int(tend/dt)

    # perform this procedure N times
    N = 1000

    # keep track of final price of stock
    s_final=[]

    for irun in range(N):

        # print out to keep track
        if irun%10==0:
            print "Run : ",irun

        # for plotting later - these arrays are reset every run
        arr_time = array.array('d')
        arr_val  = array.array('d')

        # initial time and initial value of the asset at that time
        t = 0
        s = 10

        for istep in range(nsteps):

            # put on the current time and value
            arr_time.append(t)
            arr_val.append(s)
    
            # calculate the next time
            t = t+dt
    
            # calculate the next value step
            ds = s*mu*dt + s*random.gauss(0,sigma)
            s  = s+ds
    
        # make output graphs
        gr = TGraph( len(arr_time), arr_time, arr_val )
        gr.SetLineColor( 2 )
        gr.SetLineWidth( 4 )
        gr.SetMarkerColor( 1 )
        gr.SetMarkerStyle( 21 )
        gr.SetMarkerSize(0.1)
        gr.GetXaxis().SetTitle( 'time' )
        gr.GetYaxis().SetTitle( 'Value of Stock' )
        gr.Draw( 'ALP' )

        if irun%100==0:
            c.SaveAs("stock_single_"+str(irun)+".eps")
        
        # store the final price in the list
        s_final.append(arr_val[-1])
    

    # graph the histogram of the final price
    h = TH1F("h","h",100,0,200)

    for val in s_final:
        h.Fill(val)
    
    h.SetLineColor(1)
    h.GetXaxis().SetTitle("Final Value of Asset")
    h.GetYaxis().SetTitle("Frequency")
    h.Scale(1.0/h.Integral())
    h.SetMinimum(0.0)
    h.Draw("hist")

    c.SaveAs("acceptreject_exponential_tend"+str(tend)+".eps")
    
    # calculate mean and width of this spectrum and store it in the arrays
    mean  = h.GetMean()
    width = h.GetRMS()
    
    arr_tend.append(tend)
    arr_mean.append(mean)
    arr_width.append(width)
    
    
# make output graphs
gr1 = TGraph( len(arr_tend), arr_tend, arr_mean )
gr1.SetLineColor( 2 )
gr1.SetLineWidth( 4 )
gr1.SetMarkerColor( 1 )
gr1.SetMarkerStyle( 21 )
gr1.SetMarkerSize(0.1)
gr1.SetMinimum(0)
gr1.SetMaximum(100)
gr1.GetXaxis().SetTitle( 'Running Time' )
gr1.GetYaxis().SetTitle( 'Mean of Price' )
gr1.Draw( 'ALP' )

c.SaveAs("predicted_mean_versus_runtime.eps")
    
# make output graphs
gr2 = TGraph( len(arr_tend), arr_tend, arr_width )
gr2.SetLineColor( 4 )
gr2.SetLineWidth( 4 )
gr2.SetMarkerColor( 1 )
gr2.SetMarkerStyle( 21 )
gr2.SetMarkerSize(0.1)
gr2.SetMinimum(0)
gr2.SetMaximum(100)
gr2.GetXaxis().SetTitle( 'Running Time' )
gr2.GetYaxis().SetTitle( 'Spread of Price' )
gr2.Draw( 'ALP' )

c.SaveAs("predicted_spread_versus_runtime.eps")