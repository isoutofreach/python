l = [1, 2, 3, 4, 5, 6]
l1 = [i * i for i in l if i % 2 == 0]
print(l1)

l = ["1", "2", "3"]
print([int(i) for i in l])

old = [[1, 2], [3, 4], [5, 6]]
print([j for i in old for j in i])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
ret = [[i, j] for i in l1 for j in l2]
print(ret)

d = {"k1": "v2", "k2": "v2"}
print(d.items())
d2 = {v: k for k, v in d.items()}
print({k.upper(): v for k, v in d.items()})
