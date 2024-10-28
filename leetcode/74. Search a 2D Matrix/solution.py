class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_target_row():
            upper = len(matrix) - 1
            mid = upper // 2
            lower = 0

            while upper >= lower: 
                if matrix[mid][0] <= target:
                    if matrix[mid][-1] >= target:
                        return matrix[mid]

                    lower = mid + 1
                else:
                    upper = mid - 1

                mid = (upper - lower) // 2 + lower

            return None

        target_row = find_target_row()
        if target_row is None:
            return False

        upper = len(target_row) - 1
        mid = upper // 2
        lower = 0

        while upper >= lower:
            candidate = target_row[mid]

            if candidate == target:
                return True

            if candidate < target:
                lower = mid + 1
            else:
                upper = mid - 1

            mid = (upper - lower) // 2 + lower

        return False
        
