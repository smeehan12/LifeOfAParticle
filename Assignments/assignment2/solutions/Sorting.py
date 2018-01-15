######################################
# Sam Meehan 
#
# A basic bubble sort of the given list
#
######################################

def main():

    # the initial list that we want to sort
    x=[71, 51, 32, 62, 84, 109, 43, 92, 72, 41, 102, 80, 72, 69, 46, 94, 52, 95, 90, 72, 63, 70, 34, 80, 78, 34, 31, 37, 26, 41, 42, 107, 33, 108, 108, 75, 66, 23, 90, 53, 24, 70, 26, 41, 93, 24, 71, 39, 48, 66, 97, 107, 77, 71, 67, 39, 38, 107, 96, 92, 84, 46, 60, 95, 87, 90, 92, 63, 78, 78, 84, 107, 70, 108, 32, 36, 93, 108, 49, 72, 56, 43, 30, 56, 51, 97, 45, 92, 40, 43, 49, 83, 98, 28, 99, 97, 102, 89, 58, 87]

    print "CheckList : ",CheckList(x)
    
    # keep track of how many times we have started from the beginning of the list
    iCheck=0
    while CheckList(x)==False:
        print "iCheck : ",iCheck
        iCheck+=1
        
        # keep track of the current element in the sort
        iElement=0
        
        # go through each element in the list once, making swaps where necessary
        for i in range(len(x)-1):
            print "iCheck,iElement : ",iCheck,iElement
            iElement+=1
            # if the two elements are out of order, then swap them
            if x[i]>x[i+1]:
                w = x[i]
                u = x[i+1]
                x[i] = u
                x[i+1] = w
                
            print "Current List : ",x

# function to check whether the list is sorted already or not
def CheckList(listIn):

    # check each of the elements in the list to see if it is in the "right" place
    for i in range(len(listIn)-1):
    
        # if at any point it finds an element out of place then return false
        if listIn[i]>listIn[i+1]:
            return False
            
    # if it makes it all the way through, the list must be sorted
    return True

    
if __name__ == "__main__":
    main()
    