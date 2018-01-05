################################
# Sam Meehan - quiz1
# 
# Calculate the sum of numbers from 0 to some number Q
# make sure it works for positive and negative Q
#
################################

# the input parameter Q
Q = 50


# form the set of numbers you are going to add together
rangeOfSum=[]
if Q<0:
    rangeOfSum=range(Q,0)
elif Q>0:
    rangeOfSum=range(0,Q)
    rangeOfSum.append(Q)
else:
    print "How did you get here! - Check your code."
    
# perform the sum
sum=0
for x in rangeOfSum:
    sum += x # this is the same as saying "sum = sum+x"
    
print "The sum between 0 and ",Q," is : ",sum

