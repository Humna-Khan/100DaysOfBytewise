def maxSubarraySum(nums):
    if not nums:
        return 0
    
    maxSum = nums[0]  
    sum = nums[0]  
    
    for num in nums[1:]:
        sum = max(num, sum + num)
        maxSum = max(maxSum, sum)
    
    return maxSum

if __name__ == "__main__":
    input_nums = input("Enter elements: ")
    nums = list(map(int, input_nums.split()))
    resultofsum = maxSubarraySum(nums)

    print("Maximum sum of subarray:", resultofsum)
