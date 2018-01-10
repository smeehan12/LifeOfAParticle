######################################
# Sam Meehan 
#
# example of how to make a 2D histogram - more information found at
# https://root.cern.ch/doc/v608/classTH2.html
# https://root.cern.ch/doc/master/classTHistPainter.html
# https://root.cern.ch/doc/master/classTAttLine.html
#
######################################

# import necessary libraries
from ROOT import *

# make the histogram that you will store info in
# this creates a histogram named "h2" which has 
# x-bins : 10 bins going from  0 to 5, so each bin has a width of 0.5
# y-bins : 20 bins going from  -10 to 10, so each bin has a width of 1
h2 = TH1F("h2","h2",10,0,5,20,-10,10)

# fill data into the histogram somewhere in your code
# this is dummy data for illustration
h.Fill(1,4)
h.Fill(1.2,8)

h.Fill(2.1,-3) # filling this entry three times
h.Fill(2.1,-3)
h.Fill(2.1,-3)

# label the axes
h.GetXaxis().SetTitle( 'x axis label' )
h.GetYaxis().SetTitle( 'y axis label' )

# make output graphs
c = TCanvas("c","c",200,200)

# draw the histogram using a color gradient to represent the content of each bin
h.Draw('colz')

# save to output file valles example_hitogram.eps
c.SaveAs("example_histogram_2d.eps")



        
        