def quick_sort_in_place(arr, low=None, high=None):
    # 初始化参数
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    # 递归终止
    if low >= high:
        return

    # 分区：返回基准最终位置
    pivot_index = partition(arr, low, high)

    # 递归左右
    quick_sort_in_place(arr, low, pivot_index - 1)
    quick_sort_in_place(arr, pivot_index + 1, high)


def partition(arr, low, high):
    # 选最后一个元素为基准
    pivot = arr[high]
    i = low - 1  # 小于区的边界

    for j in range(low, high):
        # 当前元素 <= 基准，放入小于区
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 把基准放到最终位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 测试
arr = [3, 6, 8, 10, 1, 2, 1]
quick_sort_in_place(arr)
print(arr)  # 输出: [1, 1, 2, 3, 6, 8, 10]
