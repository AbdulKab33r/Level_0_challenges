nums = []
def max_out(nums):
    if ( nums[0] >= nums[1] ) and ( nums[0] >= nums[2] ):
        largest = nums[0]
    if ( nums[1] >= 0 ) and ( nums[1] >= nums [2] ):
        largest = nums[1]
    if ( nums[2] >= nums[0] ) and ( nums[2] >= nums[1] ):
        largest = nums[2]
    return largest
nums = [12, 5, 8]
print (max_out(nums))

def max_out():list(12,5,8)
list = (12,5,8)
for x in list:
        if x >= range(1, 20):
            print(x)