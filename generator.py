def gen_py():
    for i in range(10):
        yield i


gen = gen_py()

for j in gen:
    print(j)