class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return flowerbed.count(0) >= n

        for i in range(len(flowerbed)):
            if n == 0:
                break

            if flowerbed[i] == 1:
                continue

            if (
                (i == 0 or flowerbed[i-1] == 0) and
                (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1

        return n == 0
