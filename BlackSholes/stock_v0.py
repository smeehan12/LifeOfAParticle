import random
import array
from ROOT import *


# appreciation
mu    = 0.2 

# volatility
sigma = 0.01

# total time and time step size
dt     = 0.01
tend   = 10
nsteps = int(tend/dt)

# for plotting later
arr_time = array.array('d')
arr_val  = array.array('d')

# initial time and initial value of the asset at that time
t = 0
s = 10

for i in range(nsteps):

    # put on the current time and value
    arr_time.append(t)
    arr_val.append(s)
    
    # calculate the next time
    t = t+dt
    
    # calculate the next value step
    ds = s*mu*dt + s*random.gauss(0,sigma)
    s  = s+ds
    
# make output graphs
c = TCanvas("c","c",200,200)

gr = TGraph( len(arr_time), arr_time, arr_val )
gr.SetLineColor( 2 )
gr.SetLineWidth( 4 )
gr.SetMarkerColor( 1 )
gr.SetMarkerStyle( 21 )
gr.SetMarkerSize(0.1)
gr.GetXaxis().SetTitle( 'time [s]' )
gr.GetYaxis().SetTitle( 'Value of Stock' )
gr.Draw( 'ALP' )

c.SaveAs("stock_single.eps")