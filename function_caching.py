from functools import lru_cache
import time
# print(dir(time))
# print(dir(functools

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5


print(fx(20))
print(fx(5))
print(fx(10))
    
print(fx(20))
print(fx(5))
print(fx(10))
