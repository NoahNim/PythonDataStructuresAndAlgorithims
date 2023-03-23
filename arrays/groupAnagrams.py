# find a way to create hashes based on the amount of elements/string in each list?
# make empty array groupList
# loop through list and put word in hash where kley is that word sorted
# each key will be an array of the words that fit that sort
# loop through that hash and push each keys value in the groupList
# return group list


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaSortHash = {}
        if len(strs) == 1:
            groupList = []
            groupList.append([strs[0]])
            return groupList
        for string in strs:
            if "".join(sorted(string)) in anaSortHash:
                anaSortHash["".join(sorted(string))].append(string)
            else:
                anaSortHash["".join(sorted(string))] = [string]
        anaList = list(anaSortHash.values())
        return anaList
