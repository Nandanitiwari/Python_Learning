# import functools
from functools import lru_cache

import time 
# @functools.lru_cache(maxsize=None)
@lru_cache(maxsize=None)

def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
#here it will not take time bcs it already executed for 20,2 and 6
#here it did'nt compute again, it fetch it from catch , bcs here we use lru_cache
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

#here it will again take time for 61,bcs its new 
print(fx(61))
print("done for 61")
