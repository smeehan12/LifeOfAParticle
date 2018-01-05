######################################
# Sam Meehan 
#
# example of how to make a graph - more information found at
# https://root.cern.ch/doc/v608/classTH1.html
# https://root.cern.ch/doc/master/classTHistPainter.html
# https://root.cern.ch/doc/master/classTAttLine.html
#
######################################

# import necessary libraries
from ROOT import *

# make the histogram that you will store info in
# this creates a histogram named "h" which has 10 bins going from 
# 0 to 5, so each bin has a width of 0.5
h = TH1F("h","h",10,0,5)

# fill data into the histogram somewhere in your code
# this is dummy data for illustration
h.Fill(1)
h.Fill(1.2)
h.Fill(2.1)

# you can also fill in weighted events if need be
h.Fill(3.1,4)

# can also directly set the absolute value of the content of a bin
h.SetBinContent(8,3.5)
h.SetBinError(8,1.0)

# change the style options of the graph
h.SetLineColor( 2 )
h.SetLineWidth( 4 )
h.SetLineStyle( 2 )

# label the axes
h.GetXaxis().SetTitle( 'position' )
h.GetYaxis().SetTitle( 'event counts' )

# set the minimum and maximum x values
h.GetXaxis().SetRangeUser(0,4)

# set the minimum and maximum y values
h.SetMinimum(0.0)
h.SetMaximum(10.0)

# make output graphs
c = TCanvas("c","c",200,200)

# draw the graph on the canvas as a histogram
h.Draw('hist')

# save to output file valles example_hitogram.eps
c.SaveAs("example_histogram.eps")

# redraw the graph on the canvas with markers and error bars
# by default, the error bars are
# (i) the square root of the sum of the weights
# (ii) whatever you se by hand using SetBinError
h.Draw('pe')

# save to output file valles example_histogram_error.eps
c.SaveAs("example_histogram_error.eps")



        
        