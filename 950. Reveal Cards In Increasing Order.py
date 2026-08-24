# Question : https://leetcode.com/problems/reveal-cards-in-increasing-order/
from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        deckLen = len(deck)
        indices = deque(range(deckLen))
        ans = [0] * deckLen
        for card in deck:
            index = indices.popleft()
            ans[index] = card
            if indices:
                indices.append(indices.popleft())
        return ans
