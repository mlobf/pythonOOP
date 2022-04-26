import pdb

"""  
    Calcular o volume de agua dentro do maior conteiner possivel.

    You are given an array of positive integers where each integer represent
    the height of a vertical line  on a chart. Find two lines which together
    with the x-axis forms a container that would hold the greatest amount of water. 
    Return the area of water it would hold.

    This is the 'Maximum Value Answer'
        The best solution of all soluctions.
"""

# resposta e 28.

myarray = [7, 5, 2, 3, 9]

p1 = 0
p2 = 1
lista_volumes = []
max_vol_main = 0

# Como avaliar o volume ?
# O valor do elemento v1 * pela posicao do p2
# myarray = [7, 1, 2, 3, 9]

v1 = myarray[p1]
v2 = myarray[p2]


# print([lista_volumes.append(x) for x in myarray[1:]])

for x in myarray:
    print("-----")
    print("v1", v1)
    print("x", x)
    print("v1 * x", v1 * x)
    print("-----")

print("00000000000000000")
print(len(myarray))
