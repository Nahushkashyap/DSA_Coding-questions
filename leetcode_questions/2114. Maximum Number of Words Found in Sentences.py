class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for sentence in sentences:
            if sentence == "":
                continue
            no_of_words = 1
            for character in sentence:
                if character == " ":
                    no_of_words += 1
            ans = max(ans, no_of_words)
        return ans
