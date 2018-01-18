from ROOT import *

fin = open("particle_in_a_box_v0_PerfectDetector_N10000.txt","r")

lines = fin.readlines()

print "These are the lines"
#print lines

xList = []

for line in lines:
	print "This is a new printing iteration : "
#	print line

	stripline = line.strip()

	print stripline

	splitline = stripline.split()

	print splitline

	eventNumber = splitline[0]
	xMeasurement = float(splitline[1])
	
	xList.append(xMeasurement)

print "these are x measurements:"
print xList

h = TH1F("h","h",100,0,1)

for x in xList:

	print "Type of x : ",type(x)

	h.Fill(x)

c = TCanvas("c","c",200,200)

h.Draw("pe")

c.SaveAs("plot.eps")
