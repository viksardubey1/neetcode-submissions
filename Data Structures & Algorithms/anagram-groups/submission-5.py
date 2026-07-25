class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {"".join(sorted(string)): [] for string in strs}
        for string in strs:
            strs_dict["".join(sorted(string))].append(string)
        return [value for value in strs_dict.values()]
        