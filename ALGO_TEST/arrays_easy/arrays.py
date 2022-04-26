""" 
    Given a array of integers, return the indices of the two 
        numbers that add up to a given target.
"""


def match_target(myarray, target):
    v1 = 0
    v2 = 1
    valor_soma = 0

    while valor_soma != target:
        valor_soma = myarray[v1] + myarray[v2]
        if valor_soma == target:
            print(" O valor foi encontrado = > ", valor_soma)
            print(v1, myarray[v1])
            print(v2, myarray[v2])
            break

        v1 += 1
        v2 += 1


myarray = [1, 3, 7, 9, 2]

target = 11

match_target(myarray, target)
