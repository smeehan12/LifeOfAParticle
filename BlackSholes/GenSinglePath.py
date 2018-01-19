OAfrom ROOT import *
import random
import array

print "Random : ",random.gauss(0,1)


val_finals = []

NExperiments = 1000


for iexp in range(NExperiments):


	s = 10.0
	t = 0.0 
	mu = 5 
	sigma = 0.1 
	tend = 2.0 
	dt = 0.05

	N = int(tend/dt)

	arr_time = array.array('d')
	arr_val = array.array('d')

	for i in range(N):

		print "==========================="

		arr_time.append(t)
		arr_val.append(s)

	        t = t+dt

	        print "s_before = ",s

	        ds_det = s*mu*dt
	        ds_random = s*sigma*random.gauss(0,1)
                
	        ds = ds_det + ds_random
        
	        print "dsdet : ",ds_det
	        print "dsran : ",ds_random
	        print "ds = ",ds
                
	        s = s + ds
                
	        print "s_after = ",s


        c = TCanvas("c","c",200,200)
                
        gr = TGraph( len(arr_time), arr_time, arr_val )
        gr.SetLineColor( 2 )
        gr.SetLineWidth( 4 )
        gr.SetMarkerColor( 4 )
        gr.SetMarkerStyle( 21 )
        gr.SetMarkerSize(0.1)
        gr.SetTitle( 'Stock Value' )
        gr.GetXaxis().SetTitle( 'time [s]' )
        gr.GetYaxis().SetTitle( 'stock price' )
        gr.Draw( 'ALP' )


        c.SaveAs("stockprice0_"+str(iexp)+".eps")

        val_finals.append(s)



h = TH1F("h","h",100,0,100000)

for val in val_finals:
        h.Fill(val)

h.GetXaxis().SetTitle("Final Stock Value")
h.GetYaxis().SetTitle("Frequency")

h.SetLineWidth(2)

h.Draw("hist")

c.SaveAs("FinalStockPrices.eps")


