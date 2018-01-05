######################################
# Sam Meehan 
#
# example of how to make a graph - more information found at
# https://root.cern.ch/doc/master/classTGraph.html
# https://root.cern.ch/doc/master/classTGraphPainter.html
#
######################################

# import necessary libraries
import array
from ROOT import *

# for storing of final data to make graphs
arr_x = array.array('d')
arr_y = array.array('d')

# fill the array of x and y values to go into the graph
# this would happen somewhere in your program and this is just
# dummy data for illustration
arr_x.append(1)
arr_x.append(2)
arr_x.append(3)
arr_x.append(4)
arr_x.append(5)

arr_y.append(100)
arr_y.append(50)
arr_y.append(25)
arr_y.append(12)
arr_y.append(6)

# create the TGraph "graph" by telling it to create a graph with
# TGraph(npoints, array of x values, array of y values)
graph = TGraph( len(arr_x), arr_x, arr_y )

# change the style options of the graph
graph.SetLineColor( 2 )
graph.SetLineWidth( 4 )
graph.SetMarkerColor( 1 )
graph.SetMarkerStyle( 21 )
graph.SetMarkerSize(0.4)

# label the axes
graph.GetXaxis().SetTitle( 'NEvents' )
graph.GetYaxis().SetTitle( 'PiAverage' )

# set the minimum and maximum y values
graph.SetMinimum(0.0)
graph.SetMaximum(120)

# make output graphs
c = TCanvas("c","c",200,200)

# draw the graph on the canvas with
# A = axes
# L = connect the points with straight lines
# P = draw the points themselves
graph.Draw('ALP')

# save to output file valles example_graph.eps
c.SaveAs("example_graph.eps")


        
        