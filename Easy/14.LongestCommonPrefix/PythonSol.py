# checking all first values, if same add the value into the output string and remove the first index, if not same return.


from typing import List
import copy

def longestCommonPrefix(strs: List[str]) -> str:
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix: # if prefix is empty means all of the letters was removed 
                return ""
    return prefix

def main():
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))
    
if __name__ == "__main__":
    main()