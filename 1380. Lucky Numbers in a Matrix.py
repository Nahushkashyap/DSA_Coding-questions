class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_num = []
        max_num = {}
        ans = []
        matrix_row_len = len(matrix)
        for row in matrix:
            min_row_index = 51
            min_row_num = 100000
            for index, num in enumerate(row):
                if min_row_num > num:
                    min_row_num = num
                    min_row_index = index
            min_num.append([min_row_index, min_row_num])
        for number in min_num:
            if number[0] not in max_num:
                max_column_num = 0
                for i in range(matrix_row_len):
                    max_column_num = max(matrix[i][number[0]], max_column_num)
                max_num[number[0]] = max_column_num

            if number[1] == max_num[number[0]]:
                ans.append(number[1])
        return ans
