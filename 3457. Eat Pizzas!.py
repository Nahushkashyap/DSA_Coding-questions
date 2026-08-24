from collections import *


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        pizzas = deque(pizzas)
        max_pizza = len(pizzas) / 4
        ans = 0
        for i in range(1, int((max_pizza + 1) / 2 + 1)):
            ans += pizzas.pop()
        for i in range(1, int(max_pizza // 2 + 1)):
            pizzas.pop()
            ans += pizzas.pop()
        return ans
