# coding:utf-8
import time
from multiprocessing import pool


def compute_sum():
    count = 0
    i = 0
    while i<10000000:
        count += i**2
        i += 1

def main():
    t1 = time.time()
    p = pool.Pool(3)
    for i in range(10):
        # compute_sum()
        p.apply_async(compute_sum)
    p.close()
    p.join()
    t2 = time.time()
    print(f'程序运行用时：{t2-t1}')



if __name__ == '__main__':
    main()