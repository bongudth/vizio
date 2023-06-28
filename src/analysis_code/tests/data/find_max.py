def find_max(nums):
    if len(nums) == 0:
        raise ValueError("nums is empty")
    max_num = nums[0]
    for x in nums:
        if x > max_num:
            max_num = x
    return max_num
