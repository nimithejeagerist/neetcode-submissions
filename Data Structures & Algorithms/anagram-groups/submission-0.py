class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = dict()

        def index(ch: str) -> int:
            return ord(ch) - ord('a')
        
        def map(word: str) -> None:
            entry = [0] * 26

            for ch in word:
                idx = index(ch)
                entry[idx] += 1
            return tuple(entry)
        
        for word in strs:
            freq = map(word)
            if freq in mapped:
                mapped[freq].append(word)
                continue
            mapped[freq] = [word]
        return list(mapped.values())
