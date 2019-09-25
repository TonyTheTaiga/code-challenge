def repeatedString(s, n):
    if s == 'a':
        return n
    
    a_count = 0

    for char in s:
        if char == 'a':
            a_count += 1

    count = a_count * math.floor(n//len(s))

    for char in s[:n % len(s)]:
        if char == 'a':
            count += 1

    return count