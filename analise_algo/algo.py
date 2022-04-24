# [0,1,2,3,4,5,6,7,8] # = 5
# [0,1,2,3,4,5,6,8,9] # = 7

# Encontar os numeros que nao ser encontrão na razao n + 1 da lista abaixo.

myarr = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 20]  # = 7


def solucao(arr):
    first = 0
    second = 1
    result = []
    while second != len(myarr):
        razao = myarr[second] - myarr[first]
        if razao > 1:
            result.append((myarr[first] + 1))

        first += 1
        second += 1

    return result


print(solucao(myarr))
