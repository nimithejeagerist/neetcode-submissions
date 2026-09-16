class Solution:

    def encode(self, strs: List[str]) -> str:
        # Length prefixing
        if len(strs) == 0:
            return ""
        result = "".join(f"{len(s)}#{s}" for s in strs)
        return result

    def decode(self, s: str) -> List[str]:
        # Two-pointer technique
        if len(s) == 0:
            return []
        delimiter = "#"
        start, end = 0, 1
        strs = []
        while start < len(s):
            if s[end] == delimiter:
                length = int(s[start:end])
                strs.append(s[end+1:end+length+1])
                
                # Update pointers
                start = end + length + 1
                end = start + 1
            else:
                end += 1
        return strs
