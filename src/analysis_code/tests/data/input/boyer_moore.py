def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0

    skip = {}
    for k in range(m):
        skip[pattern[k]] = m - k - 1

    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1

        skip_val = skip.get(text[k])
        if skip_val is not None:
            k += max(1, skip_val)
        else:
            k += m

    return -1
