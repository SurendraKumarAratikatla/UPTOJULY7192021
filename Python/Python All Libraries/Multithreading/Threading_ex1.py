import time

start = time.perf_counter()
def dosomething():
    print("Sleeping 1 second....")
    time.sleep(1)
    print('Done sleeping')

dosomething()
dosomething()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds')