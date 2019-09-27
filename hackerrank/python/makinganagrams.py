def makeAnagram(a, b):
    if len(a) >= len(b):
        longer = a
        shorter = b
    else:
        longer = b
        shorter = a

    anaC = len(shorter) + len(longer)

    p_index = dict()

    for char in shorter:
        if char in list(p_index.keys()):
            prev = p_index[char]
            if char in longer[prev + 1:]:
                p_index[char] = prev + 1 + longer[prev + 1:].find(char)
                anaC -=2

        elif char in longer:
            p_index[char] = longer.find(char)
            anaC -= 2

    return anaC
