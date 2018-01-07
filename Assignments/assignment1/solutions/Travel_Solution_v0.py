######################################
# Sam Meehan 
#
# perform all calculations manually and only do one test
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
    n_mm_test = 20
    
    # start at distance of 0
    distance = 0
    
    # each time you run for 1 second
    timestep = 1
    
    # keep taking steps until you have no more mms
    while n_mm_test>0: 
        eatmm = 1.0 + np.floor(random.uniform(0,5))
        speed = 1.0 + np.floor(random.uniform(0,5))

        distance  = distance + speed*timestep
        n_mm_test = n_mm_test - eatmm
    
        print "mm left : ",n_mm_test
        if n_mm_test<0:
            print "STOPPING MY WALK"
    
    print "Distance(predicted)  : ",distance
    print "Distance(observed)   : ",data_mean
        


        
        
def PerformExercise(number_of_mm):
    

    
    return distance
    

############################
# program will execute main by default
############################
if __name__ == "__main__":
    # execute only if run as a script
    main()