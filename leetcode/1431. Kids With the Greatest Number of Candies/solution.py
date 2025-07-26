class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        result: list[bool] = []

        for kid in candies:
            has_max = True if kid + extraCandies >= max_candies else False
            result.append(has_max)

        return result
        
