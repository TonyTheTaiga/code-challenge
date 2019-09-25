def sockMerchant(n, ar):
    temp = set()
    count = 0
    for x in ar:
        print(temp)
        if x not in temp:
            temp.add(x)
        else:
            temp.remove(x)
            count += 1
    return count