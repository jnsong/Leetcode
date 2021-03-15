
def removeDuplicates(nums):
    if len(nums)==0:
        return 0
    s = 0

    for j in range(1,len(nums)):
        if nums[s]!=nums[j]:
            s+=1
            nums[s] = nums[j]
    return s+1


result = removeDuplicates([1,1,2])
