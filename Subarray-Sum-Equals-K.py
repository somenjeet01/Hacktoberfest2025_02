def subarraySum(nums, k):
    count, curr_sum = 0, 0
    prefix = {0: 1}
    for n in nums:
        curr_sum += n
        if curr_sum - k in prefix:
            count += prefix[curr_sum - k]
        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
    return count
