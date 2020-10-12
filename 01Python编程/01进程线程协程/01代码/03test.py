# encoding:utf-8
import os
import time
from multiprocessing import Process


def computeNum():
    print("子进程1id:" + str(os.getpid()))
    count = 0
    i = 0
    while i<50000000:
        count += i**2
        i += 1

def computeNum2():
    print("子进程2id:" + str(os.getpid()))
    count = 0
    i = 50000000
    while i<100000000:
        count += i**2
        i += 1

def main():
    # dt1 = time.time()
    # computeNum()
    # computeNum2()
    # dt2 = time.time()
    # dt = dt2 - dt1
    # print(f'正常用时：{dt}')
    #
    # time.sleep(5)

    print("主进程id:"+str(os.getpid()))
    t1 = time.time()
    p1 = Process(target=computeNum)
    p2 = Process(target=computeNum2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    t2 = time.time()
    print(f'进程用时：{t2-t1}')



if __name__ == '__main__':
    main()