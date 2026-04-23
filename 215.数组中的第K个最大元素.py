#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30402
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def min_heapify(nums, i, heap_size):
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i
            if l < heap_size and nums[l] < nums[largest]:
                largest = l
            if r < heap_size and nums[r] < nums[largest]:
                largest = r

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                min_heapify(nums, largest, heap_size)

        def build_heap(nums):
            for i in range(len(nums) // 2 - 1, -1, -1):
                min_heapify(nums, i, len(nums))

        heap_size = len(nums)
        build_heap(nums)

        for i in range(len(nums) - k):
            nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
            heap_size -= 1
            min_heapify(nums, 0, heap_size)

        return nums[0]


# @lc code=end


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. Move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            i = left
            j = right - 1

            # 2. Move elements smaller than pivot to the left and larger to the right
            while i <= j:
                if nums[i] < pivot:
                    i += 1
                elif nums[j] > pivot:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

            # 3. Move pivot to its final place
            nums[right], nums[i] = nums[i], nums[right]

            return i

        def quickselect(left, right, k_smallest):
            if left == right:  # Only one element
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return quickselect(left, pivot_index - 1, k_smallest)
            else:
                return quickselect(pivot_index + 1, right, k_smallest)

        n = len(nums)
        return quickselect(0, n - 1, n - k)


#
# @lcpr case=start
# [3,2,1,5,6,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,1,2,4,5,5,6]\n4\n
# @lcpr case=end

#
