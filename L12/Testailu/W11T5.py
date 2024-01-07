import itertools


def main():

    testi = [1,2,3,4,5,6,10]

    testi2 = laske(12,testi)

    for sana in testi2:
        print(sana)
    return


def laske(n, vector):


    vectorlist = []



    for j in vector:
        if (j == n):
            new_vector = (j)
            vectorlist.append(new_vector)
            vector.remove(j)
        if (j > n):
            vector.remove(j)


    test = vector
    test.sort()

    for i in range(len(test)):
        for combo in itertools.combinations(test, i + 1):

            if sum(combo) == n:
                vectorlist.append(combo)

    return vectorlist

main()
