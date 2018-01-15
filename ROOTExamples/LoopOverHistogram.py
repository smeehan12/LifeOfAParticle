######################################
# Sam Meehan 
#
# example of how to perform a loop to access the contents stored in a histogram
#
######################################

# import necessary libraries
from ROOT import *

# make an example histogram
h = TH1F("h","h",10,0,10)

# the i=1 bin has 3
h.Fill(0)
h.Fill(0)
h.Fill(0)

# the i=3 bin has 5
h.Fill(2)
h.Fill(2)
h.Fill(2)
h.Fill(2)
h.Fill(2)

# the i=7 bin has 1
h.Fill(6)

# unlike arrays, histograms start the bin counting at i=1
# this is typically confusing so be careful
for i in range(1,h.GetNbinsX()+1):
    # by default the errors are sqrt(nentries) in the bin
    print "Bin ",i," : Contents = ",h.GetBinContent(i)," : Error = ",h.GetBinError(i)