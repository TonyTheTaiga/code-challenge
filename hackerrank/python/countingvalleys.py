def countingValleys(n, s):
    m = {
        'D': -1, 
        'U': 1
    }
    v_flag = False
    v_count = 0
    height = 0

    for step in s:
        height += m[step]

        if height < 0:
            v_flag = True

        if height - m[step] == -1 and height >= 0 and v_flag:
            v_count += 1

    return v_count