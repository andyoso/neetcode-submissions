class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string = ""
        for string in strs:
            encode_string += str(len(string)) + '#' + string
        return encode_string
    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            decode_list.append(word)
            i = j + 1 + length
        return decode_list
    #TC: O(N), where N is the length of strs
    #SC: O(N)
        

