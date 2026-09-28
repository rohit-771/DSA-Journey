class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_count = {}

        for ch in chars:
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1

        ans = 0

        for word in words:
            word_count = {}
            good = True

            for ch in word:
                if ch in word_count:
                    word_count[ch] += 1
                else:
                    word_count[ch] = 1

                if word_count[ch] > char_count.get(ch, 0):
                    good = False
                    break

            if good:
                ans += len(word)

        return ans
        