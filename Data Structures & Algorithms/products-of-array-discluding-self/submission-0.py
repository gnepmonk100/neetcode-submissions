class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        product_without_zero = 1
        zero_count = 0
        all_products = [0] * nums_len

        for num in nums:
            if num != 0:
                product_without_zero *= num
            else:
                zero_count += 1

        if zero_count >= 2:
            return [0] * nums_len

        elif zero_count == 1:
            for idx in range(nums_len):
                if nums[idx] != 0:
                    all_products[idx] = 0
                else:
                    all_products[idx] = product_without_zero

        elif zero_count == 0:
            for idx in range(nums_len):
                all_products[idx] = int(product_without_zero/nums[idx])

        return all_products








