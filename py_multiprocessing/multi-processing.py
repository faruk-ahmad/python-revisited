"""
A moduel for multiprocessing using the multiprocessing module
"""

import multiprocessing
import time


def do_something(seconds):
    """
    A dummy function to test multiprocessing using the multiprocessing module
    """

    print(f"Starting task - {seconds}")
    time.sleep(seconds)
    print(f"Finished task - {seconds}")


start_time = time.perf_counter()

# # we create a process by metioning the do_something method as target
# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# # now we need to start the processes
# p1.start()
# p2.start()

# # To wait to finish all of our initiated process we need to join the processes
# p1.join()
# p2.join()


# lets do it now in another way
secs = [5, 4, 3, 2, 1]

processes = []

for sec in secs:
    p = multiprocessing.Process(target=do_something, args=[sec])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

end_time = time.perf_counter()

print(f"Time taken: {end_time - start_time}")