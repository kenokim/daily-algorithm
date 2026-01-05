class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        count_neg = 0
        count_pos = 0
        
        total_abs = 0
        min_abs = 1000000

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] < 0:
                    count_neg += 1
                else:
                    count_pos += 1

                item_abs = abs(matrix[i][j])
                total_abs += item_abs
                if abs(matrix[i][j]) < min_abs:
                    min_abs = item_abs

        if count_neg % 2 == 0:
            return total_abs
        
        return total_abs - 2 * min_abs

# 250 X 250 -> pick 2