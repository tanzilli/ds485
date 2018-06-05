from timeit import default_timer as timer
import time

start = timer()

time.sleep(0.5)

end = timer()
print(end - start)