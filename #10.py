# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time

# no idea if this is correct.
# should I use Threads?


def scheduler(job, n, data):
    n = n/1000
    time.sleep(n)
    job(data)


def job_fun(data):
    print(f'{data}')


scheduler(job_fun, 3, 1)
# scheduler(job_fun, 3, 2)
# scheduler(job_fun, 3, 3)
# scheduler(job_fun, 3, 4)
# scheduler(job_fun, 3, 5)
# scheduler(job_fun, 3, 6)
# scheduler(job_fun, 3, 7)
