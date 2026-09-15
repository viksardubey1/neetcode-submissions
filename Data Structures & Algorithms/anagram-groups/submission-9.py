class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {"".join(sorted(string)): [] for string in strs}
        for string in strs:
            sorted_dict["".join(sorted(string))].append(string)
        return [l for l in sorted_dict.values()]

        