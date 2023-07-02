def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    pattern_hash = hash(pattern)
    for i in range(n - m + 1):
        if hash(text[i: i + m]) == pattern_hash:
            if text[i: i + m] == pattern:
                return i
    return -1
