
cache = {}

def triple_step(n):
    if n in cache:
        return cache[n]
    else:
        if n < 0 :
            return 0
        elif n == 0:
            return 1
        else:
            cache[n] = triple_step(n -1) + triple_step(n-2) + triple_step(n-3)
            return cache[n]

print triple_step(33)
print triple_step(30)
