"""
A module for multiprocessing using the concurrent module
"""
import concurrent.futures
import time


def do_something(seconds):
    """
    A dummy function to test multiprocessing using the concurrent module
    """

    print(f"Starting task - {seconds}")
    time.sleep(seconds)
    return f"Finished task - {seconds}"


start_time = time.perf_counter()

# 1. let do the concurrent task here
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)

#     print(f1.result())
#     print(f2.result())

# 2. lets do it in different way

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     results = [executor.submit(do_something, 1) for _ in range(10)]

#     for f in results:
#         print(f.result())


# 3. We can also use as_completed feature so that results are returnes as soon as they completed

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     results = [executor.submit(do_something, 1) for _ in range(10)]
    
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())


# 4. another way by assigning different time sleeping for each process

# secs = [5, 4, 3, 2, 1]

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     results = [executor.submit(do_something, sec) for sec in secs]

#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

# 5. We can also use executor.map to do it in another way

secs = [5, 4, 3, 2, 1]

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(do_something, secs)

    # but now the executor directly return the result from the function
    # not need to call the result function on f
    for f in results:
        print(f)

end_time = time.perf_counter()

print(f"Total time taken: {end_time - start_time}")