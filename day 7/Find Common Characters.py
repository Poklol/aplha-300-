def commonChars(words: list[str]) -> list[str]:
    min_freq = {}
    for c in words[0]:
        min_freq[c] = min_freq.get(c, 0) + 1
        
    for w in words[1:]:
        curr_freq = {}
        for c in w:
            curr_freq[c] = curr_freq.get(c, 0) + 1
        for c in list(min_freq.keys()):
            if c not in curr_freq:
                del min_freq[c]
            else:
                if curr_freq[c] < min_freq[c]:
                    min_freq[c] = curr_freq[c]
                    
    res = []
    for c, cnt in min_freq.items():
        for _ in range(cnt):
            res.append(c)
    return res
