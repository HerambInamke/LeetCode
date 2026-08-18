class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort() # Sort the array to efficiently handle duplicates and use two pointers

        # Iterate through the array with 'i' as the first element of the triplet
        for i in range(len(nums) - 2):
            # Skip duplicate values for nums[i]
            # This ensures that we don't process the same 'first' number multiple times
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Initialize two pointers for the remaining part of the array
            left, right = i + 1, len(nums) - 1

            # Use the two-pointer technique to find pairs that sum to -nums[i]
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet that sums to zero
                    result.append([nums[i], nums[left], nums[right]])

                    # Move pointers inward
                    left += 1
                    right -= 1

                    # Skip duplicate values for nums[left]
                    # This avoids adding duplicate triplets with the same 'middle' number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate values for nums[right]
                    # This avoids adding duplicate triplets with the same 'last' number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < 0:
                    # Sum is too small, need a larger value
                    left += 1
                else: # current_sum > 0
                    # Sum is too large, need a smaller value
                    right -= 1
        
        return result