################################
# Sam Meehan - quiz1
# 
# Calculate the minimum and the maximum of a set of numbers
#
################################

# the input set of numbers
x=[71, 51, 32, 62, 84, 109, 43, 92, 72, 41, 102, 80, 72, 69, 46, 94, 52, 95, 90, 72, 63, 70, 34, 80, 78, 34, 31, 37, 26, 41, 42, 107, 33, 108, 108, 75, 66, 23, 90, 53, 24, 70, 26, 41, 93, 24, 71, 39, 48, 66, 97, 107, 77, 71, 67, 39, 38, 107, 96, 92, 84, 46, 60, 95, 87, 90, 92, 63, 78, 78, 84, 107, 70, 108, 32, 36, 93, 108, 49, 72, 56, 43, 30, 56, 51, 97, 45, 92, 40, 43, 49, 83, 98, 28, 99, 97, 102, 89, 58, 87]

# minimum
minval = 1000 # start with a very high number
for i in x:
    # ask if the current number is less than the one that you think is the minimum
    if i<minval:
        # if it is less then you replace the best guess of the minimum with that number
        minval=i
        
print "minval = ",minval
print "minval(fast) = ",min(x)

# minimum
maxval = -1000 # start with a very low
for i in x:
    if i>maxval:
        maxval=i
        
print "maxval = ",maxval
print "maxval(fast) = ",max(x)
