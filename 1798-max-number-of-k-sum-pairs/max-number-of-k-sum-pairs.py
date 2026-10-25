class Solution:
    def maxOperations(self, nums, k):
        seen = {}
        operations = 0

        for num in nums:
            complement = k - num

            if complement in seen and seen[complement] > 0:
                operations += 1
                seen[complement] -= 1
            else:
                seen[num] = seen.get(num, 0) + 1

        return operations
        