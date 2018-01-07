######################################
# Sam Meehan 
#
# Perform many pseudoexperiments and compare the distributions
# using a chisquare similarity test and plot the chi-square versus
# the number of mm's tested
#
######################################

import random
import numpy as np
import array
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
        
    # loop over many different values of the number of mm to test
    n_mm_test_values = np.arange(1,50,1)
    
    # bookkeeping of distances in histogram
    hpred = TH1F("hpred","hpred",100,0,100)
    
    # for storing the chiSquare values for the different n_mm_tests
    arr_n_mm_test = array.array('d')
    arr_chisquare = array.array('d')
        
    # perform test for each n_mm_test value
    for n_mm_test in n_mm_test_values:
    
        # clear the histogram for the next experiment
        hpred.Reset()
    
        # perform 1000 simulations and take their average
        for i in range(1000):

            # reset the n_mm to be the value you are testing
            n_mm     = n_mm_test

            # put the calculation of the distance in a function 
            dis = PerformExercise(n_mm, False)
    
            # fill the histogram with the distance of this exercise
            hpred.Fill(dis)
    
        # get the mean value of the prediction
        pred_mean = hpred.GetMean()
    
        print "Testing : ",n_mm_test
        print "Distance(predicted)  : ",pred_mean
        print "Distance(observed)   : ",data_mean
        
        # calculate the ChiSquare (whatever that is!)
        chiSquare = hpred.Chi2Test(hdata,"UUCHI2")
        
        # fill this data in for eventual creation of a graph
        arr_n_mm_test.append(n_mm_test)
        arr_chisquare.append(chiSquare)
        
    # make the graph
    graph = TGraph( len(arr_n_mm_test), arr_n_mm_test, arr_chisquare )

    graph.SetLineColor( 2 )
    graph.SetLineWidth( 4 )
    graph.SetMarkerColor( 1 )
    graph.SetMarkerStyle( 21 )
    graph.SetMarkerSize(0.4)

    graph.GetXaxis().SetTitle( 'N(mm to test)' )
    graph.GetYaxis().SetTitle( 'ChiSquare' )

    maxval = max(arr_chisquare)
    print "MaxVal : ",maxval
    
    graph.SetMinimum(0.0)
    graph.SetMaximum(0.5*maxval)

    graph.Draw('ALP')

    c.SaveAs("Travel_Solution_v2.eps")


        
        
def PerformExercise(number_of_mm, debug=False):
    #########################    
    # Function to perform the exercise where a player runs in bouts of speed equal
    # to a uniform random number dictated by a die throw [1,6].  Each time the player
    # eats some number of candies equal to a random die throw [1,6].  The run lasts
    # for one second.  The player continues to run until all the "number_of_mm"'s
    # are gone.  The distance the player has run is returned
    #
    # Input : number of mm's 
    # Output : distance ran
    #########################    
    
    # these parameters we have chosen to not change
    timestep = 1
    distance = 0.0
    
    # keep looping until there are no more mm's
    while number_of_mm>0: 
        eatmm = 1.0 + np.floor(random.uniform(0,5))
        speed = 1.0 + np.floor(random.uniform(0,5))

        distance     = distance + speed*timestep
        number_of_mm = number_of_mm - eatmm
    
        if debug: print "mm left : ",number_of_mm
        if number_of_mm<0:
            if debug: print "STOPPING MY WALK"
    
    if debug: print "distance : ",distance
    
    return distance
    

############################
# program will execute main by default
############################
if __name__ == "__main__":
    # execute only if run as a script
    main()