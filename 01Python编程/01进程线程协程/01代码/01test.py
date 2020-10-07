# encoding:utf-8
import time

def computeNum():
    t1 = time.time()
    count = 0
    i = 0
    while i<50000000:
        count += i
        i += 1
    t2 = time.time()
    dt = t2 - t1
    return dt

def computeNum2():
    t1 = time.time()
    count = 0
    i = 50000000
    while i<100000000:
        count += i
        i += 1
    t2 = time.time()
    dt = t2 - t1
    return dt

def main():
  dt1 = computeNum()
  dt2 = computeNum2()
  dt = dt1 + dt2
  print(dt)


if __name__ == '__main__':
    main()