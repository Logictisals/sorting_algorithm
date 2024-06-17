def binary_search(arr, val, start, end):
    """折半查找，找到val应该插入的位置"""
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid
    return start

def binary_insertion_sort(arr):
    """折半插入排序"""
    for i in range(1, len(arr)):
        val = arr[i]  # 取出当前元素
        # 折半查找找到val应该插入的位置
        pos = binary_search(arr, val, 0, i)
        
        # 将所有大于val的元素向后移动一位
        arr = arr[:pos] + [val] + arr[pos:i] + arr[i+1:]
    
    return arr

# 示例数组
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = binary_insertion_sort(arr)
print("Sorted array:", sorted_arr)