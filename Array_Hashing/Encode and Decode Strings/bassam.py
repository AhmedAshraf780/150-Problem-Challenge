from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        strss=''
        
        for x in strs :
                strss+= str(len(x)) + "#" + x 
        return strss
        
        
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            decoded_list.append(s[i:i + length])
            i += length
        return decoded_list
