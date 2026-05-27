def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j
def quick_sort(nums,low,high):
    if low<high:
        p_idx=partition(nums,low,high)
        quick_sort(nums,low,p_idx-1)
        quick_sort(nums,p_idx+1,high)
    return nums
#print(quick_sort([8,3,6,1,2,3,9,5],0,7))
#in best and avg case, TC=O(NlogN), SC=O(1)
#in worst case (when all list elements are equal), TC=O(N^2), SC=O(1)