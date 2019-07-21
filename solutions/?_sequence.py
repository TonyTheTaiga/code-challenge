def get_next_val(x: int) -> int:
    if x == 1:
        return 1
    elif x % 2 == 0:
        return x / 2
    elif x % 2 == 1:
        return 3 * x + 1

def make_sequence(x: int) -> list:
    if x == 1:
        return [1]

    ret = [x]

    for x in ret:
        if get_next_val(x) != 1:
            ret.append(int(get_next_val(x)))
        else:
            ret.append(1)
            break
    
    return ret

def get_longest_chain(x: int) -> int:
    # storage = {}
    n_longet = 0
    longest_len = 0
    for y in range(1, x):
        # storage[len(make_sequence(y))] = y
        seq = make_sequence(y)
        if len(seq) > longest_len:
            longest_len = len(seq)
            n_longest = y

    # n_longest = storage[max(storage.keys())]
    
    return n_longest

if __name__ == "__main__":
    a = get_longest_chain(1000000)
    print(a)
    
