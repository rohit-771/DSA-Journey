class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        banned = set(banned)

        words = paragraph.split()

        freq = {}

        for word in words:
            if word not in banned:
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
        answer = ""
        max_count = 0

        for word in freq:
            if freq[word] > max_count:
                max_count = freq[word]
                answer = word

        return answer
        