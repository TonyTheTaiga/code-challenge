def jumpingOnClouds(c):
    temp = list()
    steps = 0
    for cloud in c:
        if cloud == 0:
            temp.append(cloud)    
        else:
            div, rem = divmod(len(temp), 2)
            steps += div + 1
            temp = list()

    if len(temp) > 1:
        div, rem = divmod(len(temp), 2)
        steps += div

    return steps
