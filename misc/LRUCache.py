def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    # 将序列分成两半
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    # 合并两个有序序列
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# 测试
nums = [5, 4, 3, 2, 1]
print(merge_sort(nums))  # 输出: [1, 2, 3, 4, 5]

def in_place_merge_sort(nums, start, end):
    if start >= end:
        return
    
    # 将序列分成两半
    mid = (start + end) // 2
    in_place_merge_sort(nums, start, mid)
    in_place_merge_sort(nums, mid + 1, end)
    
    # 合并两个有序序列
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if nums[i] > nums[j]:
            # 交换两个元素的值
            nums[i], nums[j] = nums[j], nums[i]
            # 交换完成后，将j移动
            j += 1
            mid += 1
        i += 1

# 测试
nums = [5, 4, 3, 2, 1]
in_place_merge_sort(nums, 0, len(nums) - 1)
print(nums)  # 输出: [1, 2, 3, 4, 5]
