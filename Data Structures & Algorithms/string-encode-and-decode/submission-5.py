class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        if not strs:
            return encoded_str

        for i in range(len(strs)):
            reversed_s = strs[i][::-1]
            encoded_str += reversed_s + "$%"
        
        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        if not s:
            return decoded_strs

        for item in s.split("$%")[: -1]:
            if item:
                decoded_strs.append(item[::-1])
            else:
                decoded_strs.append("")
        
        return decoded_strs