def generator(n):
    for i in range(n):
        yield i*i
a=generator(100)
#print(a,type(a))
print(next(a))
print(next(a))
print(next(a))

#ONE MORE WAY TO CREATE GENERATOR
b=(i*i for i in range(100)) #b is a generator , NOT a tuple comprehension
print(next(b))
print(next(b))
print(next(b))