import time

import fib

t0 = time.time()
fib.fib(40)
print(time.time() - t0)
