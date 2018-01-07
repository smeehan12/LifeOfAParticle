######################################
# Sam Meehan 
#
# Make many pseudoexperiments of the travel
#
######################################

import random
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    # bookkeeping of distances 
    arr_distances=[]
    
    # perform some number of pseudoexperiments
    for i in range(1000):
    
        timestep = 1
        distance = 0.0
        n_mm = 20
    
        while n_mm>0: 
            eatmm = 1.0 + np.floor(random.uniform(0,5))
            speed = 1.0 + np.floor(random.uniform(0,5))

            distance = distance + speed*timestep
            n_mm     = n_mm - eatmm
        
            print "mm left : ",n_mm
            if n_mm==0:
                print "STOPPING MY WALK"
        
        print "distance : ",distance
        arr_distances.append(distance)

    plt.hist(arr_distances, bins=50, range=(0,50), normed=1, facecolor='green', alpha=0.75)
    plt.show()
    
    fout = open("coach_and_player_distances.txt","w")
    for i in arr_distances:
        lineout = str(int(i))+"\n"
        fout.write(lineout)
    fout.close()
        
        
    
    

############################
# program will execute main by default
############################
if __name__ == "__main__":
    # execute only if run as a script
    main()