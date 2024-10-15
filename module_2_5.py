import random
def get_matrix(n, m, value):
    matrix = []
    for i in range(0,n):
        matrix.append([])
        for j in range(0, m):
            matrix[i].append(value)
    return matrix

result = get_matrix(random.randint(2,5), random.randint(1,5), random.randint(-50,50))
print(result)