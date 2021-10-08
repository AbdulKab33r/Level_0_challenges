#This will print out the maximum number of three digits provided.
#Im really battling to get to do it to print more than three digits.
#I watched many other lessons online to try to find a way but still nothing yet.
nums = []
def max_out(nums):
    if ( nums[0] >= nums[1] ) and ( nums[0] >= nums[2] ):
        largest = nums[0]
    if ( nums[1] >= 0 ) and ( nums[1] >= nums [2] ):
        largest = nums[1]
    if ( nums[2] >= nums[0] ) and ( nums[2] >= nums[1] ):
        largest = nums[2]
    return largest
nums = [4, 5, 9]
print('The maximum number is:')
print (max_out(nums))