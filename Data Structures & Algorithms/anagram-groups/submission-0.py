class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        output = []
        for string in strs:
            count_pattern = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                count_pattern[index] += 1
            count_pattern = tuple(count_pattern)
            if count_pattern not in hash_map:
                hash_map[count_pattern] = []
            hash_map[count_pattern].append(string)
        for key, value in hash_map.items():
            output.append(value)
        return output
