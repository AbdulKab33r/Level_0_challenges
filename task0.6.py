def max_out(a, b, c):
    if ( a >= b ) and ( a >= c ):
        largest = a
    if ( b >= a ) and ( b >= c ):
        largest = b
    if ( c >= a ) and (c >= b ):
        largest = c
    return largest
a = 3
b = 8
c = 5
print (max_out(a, b, c))

# This was me trying to fgure out the infinte amounts of numbers to get maximum value.
# I was unable to win as my time running out , i will still keeping trying/researching it.
#nums = []
#def max_out(nums):
#    if ( nums[0] >= nums[1] ) and ( nums[0] >= nums[2] ):
#        largest = nums[0]
#    if ( nums[1] >= 0 ) and ( nums[1] >= nums [2] ):
#        largest = nums[1]
#    if ( nums[2] >= nums[0] ) and ( nums[2] >= nums[1] ):
#        largest = nums[2]
#    return largest
#nums = [4, 5, 9]
#print (max_out(nums))