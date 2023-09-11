import functools

@functools.lru_cache(maxsize=None)
def expensive_function(n):
    print(f"Computing result for {n}")
    return n * 2

for i in range(5):
    result = expensive_function(i)
    print(f"Result for {i}: {result}")

cached_result = expensive_function(2)

print(f"Cached result for 2: {cached_result}")
