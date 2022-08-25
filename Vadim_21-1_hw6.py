def get_list() -> list:
    return list(range(0, 1000000, 2))

class Solution:
    """
            find_target -> YOUR_CODE
        """
    def find_target(self, list1, target):
        low = 0
        high = len(list1) - 1


        while low <= high:
            mid = (low + high) // 2
            guess = list1[mid]
            if guess == target:
                return mid

            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
        return None

list2 = Solution()
print(list2.find_target(get_list(), 10000))


