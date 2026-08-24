# Question :- https://leetcode.com/problems/out-of-boundary-paths/description/
class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        memo = {}

        def path(m, n, currentMoves, currentColumn, currentRow):
            if currentRow > m - 1 or currentRow < 0:
                return 1
            if currentColumn > n - 1 or currentColumn < 0:
                return 1
            if currentMoves <= 0:
                return 0
            if (currentMoves, currentColumn, currentRow) in memo:
                return memo[(currentMoves, currentColumn, currentRow)]
            ans = 0
            ans += path(m, n, currentMoves - 1, currentColumn + 1, currentRow)
            ans += path(m, n, currentMoves - 1, currentColumn - 1, currentRow)
            ans += path(m, n, currentMoves - 1, currentColumn, currentRow + 1)
            ans += path(m, n, currentMoves - 1, currentColumn, currentRow - 1)
            memo[(currentMoves, currentColumn, currentRow)] = ans
            return memo[(currentMoves, currentColumn, currentRow)]

        ans = path(m, n, maxMove, startColumn, startRow)
        ans %= 10**9 + 7
        return ans
