def make_matrix(size, value=0):
    inner = size[0] if isinstance(size, tuple) else size
    outer = size[1] if isinstance(size, tuple) else size
    return [[value for j in range(inner)] for x in range(outer)]


print(make_matrix(3))
print(make_matrix((4, 2), 1))
