"""  
    Calcular o volume de agua dentro do maior conteiner possivel.

    You are given an array of positive integers where each integer represent
    the height of a vertical line  on a chart. Find two lines which together
    with the x-axis forms a container that would hold the greatest amount of water. 
    Return the area of water it would hold.

    This is the 'Maximum Value Answer'
        The best solution of all soluctions.
"""

# Brute Force Method
# resposta e 28.
heights = [7, 1, 2, 3, 9]


def get_max_water_container(heights):
    max_area = 0
    p1 = 0
    heights_len = len(heights)
    while p1 != heights_len:
        p2 = p1 + 1
        while p2 != heights_len:
            height = min(heights[p1], heights[p2])
            width = p2 - p1
            area = height * width
            max_area = max(max_area, area)
            p2 += 1
        p1 += 1
    return max_area


print(get_max_water_container(heights))
