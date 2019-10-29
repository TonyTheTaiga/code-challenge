# Complete the permutationEquation function below.

p = [5,2,1,3,4]

def permutationEquation(p): 
    ret = []
    for x in p:
        ret.append(p[x-1])
    return ret

if __name__ == "__main__":
    print(permutationEquation(p))