# # nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
nums = [2,7,11,15]
target = int(input("enter the target :"))

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]+nums[j] == target:
            return [i,j]
