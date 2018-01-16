######################################
# Sam Meehan 
#
# put the main distance calculation in a function
# perform many simulations and take the average
#
######################################

import random
import numpy as np
from ROOT import *

def main():

    # canvas for drawing
    c = TCanvas("c","c",200,200)

    # make initial histogram of the distances
    hdata = TH1F("hdata","hdata",100,0,100)
    fin = open("coach_and_player_distances.txt","r")
    for line in fin.readlines():
        x = float(line)
        hdata.Fill(x)
    
    # draw the data histogram
    hdata.Draw("pe")
    c.SaveAs("check_data.eps")
        
    # get the mean value of the observations
    data_mean = hdata.GetMean()
        
    # value to test
    n_mm_test = 30
    
    # bookkeeping of distances in histogram
    hpred = TH1F("hpred","hpred",100,0,100)
    
    # perform 1000 simulations and take their average
    for i in range(1000):
    
        # reset the n_mm to be the value you are testing
        n_mm     = n_mm_test
    
        # put the calculation of the distance in a function 
        dis = PerformExercise(n_mm)
        
        # fill the histogram with the distance of this exercise
        hpred.Fill(dis)
        
    # get the mean value of the prediction
    pred_mean = hpred.GetMean()
        
    print "Distance(predicted)  : ",pred_mean
    print "Distance(observed)   : ",data_mean
    
    # plot them on top of each other with different styles
    hdata.SetMarkerSize(0.3)
    hdata.SetMarkerStyle(20)
    hdata.SetMarkerColor(4)
    hdata.SetLineColor(1)
    hdata.GetXaxis().SetTitle("distance [m]")
    hdata.GetYaxis().SetTitle("N Exercise Days")
    
    hpred.SetMarkerSize(0.3)
    hpred.SetMarkerStyle(22)
    hpred.SetMarkerColor(2)
    hpred.SetLineColor(1)
    
    hdata.Draw("pe")
    hpred.Draw("pesame")
    
    c.SaveAs("Travel_Solution_v1.eps")

        
        
def PerformExercise(number_of_mm):
    
    # these parameters we have chosen to not change
    timestep = 1
    distance = 0.0
    
    # keep looping until there are no more mm's
    while number_of_mm>0: 
        eatmm = 1.0 + np.floor(random.uniform(0,5))
        speed = 1.0 + np.floor(random.uniform(0,5))

        distance     = distance + speed*timestep
        number_of_mm = number_of_mm - eatmm
    
        print "mm left : ",number_of_mm
        if number_of_mm<0:
            print "STOPPING MY WALK"
    
    print "distance : ",distance
    
    return distance
    

############################
# program will execute main by default
############################
if __name__ == "__main__":
    # execute only if run as a script
    main()