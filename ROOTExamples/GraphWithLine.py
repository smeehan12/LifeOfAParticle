######################################
# Sam Meehan 
#
# example of how to make a graph of points and then draw a line
# more info found at :
# https://root.cern.ch/doc/v610/classTF1.html
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

arr_y.append(1)
arr_y.append(2)
arr_y.append(3)
arr_y.append(4)
arr_y.append(6)

# create the TGraph "graph" by telling it to create a graph with
# TGraph(npoints, array of x values, array of y values)
graph = TGraph( len(arr_x), arr_x, arr_y )

# make the function of a line to draw
# m*x+b = [0]*x+[1]
# m = [0]
# b = [1]
funcLine = TF1("funcLine", "[0]*x+[1]",0,10);
funcLine.SetParameter(0,1.1);  # set the value of the parameter [0]
funcLine.SetParameter(1,0.0);  # set the value of the parameter [1]

# change the style of the line
funcLine.SetLineWidth(2)
funcLine.SetLineColor(2)

# change the style options of the graph
graph.SetLineColor( 2 )
graph.SetLineWidth( 4 )
graph.SetMarkerColor( 1 )
graph.SetMarkerStyle( 21 )
graph.SetMarkerSize(0.4)

# label the axes
graph.GetXaxis().SetTitle( 'X Value' )
graph.GetYaxis().SetTitle( 'Y Value' )

# set the minimum and maximum y values
graph.SetMinimum(0.0)
graph.SetMaximum(10)

# make output graphs
c = TCanvas("c","c",200,200)

# draw the graph on the canvas with
# A = axes
# L = connect the points with straight lines
# P = draw the points themselves
graph.Draw('AP')

# draw the line
funcLine.Draw("same")

# now draw the function of a line

# save to output file valles example_graph.eps
c.SaveAs("example_graph_withline.eps")


        
        