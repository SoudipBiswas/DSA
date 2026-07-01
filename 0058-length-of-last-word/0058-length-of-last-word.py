class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        end_index = len(s) - 1

        while end_index >= 0 and s[end_index] == ' ':
            end_index -= 1

        last_word_end = end_index

        start_index = last_word_end
        while start_index >= 0 and s[start_index] != ' ':
            start_index -= 1

        return last_word_end - start_index