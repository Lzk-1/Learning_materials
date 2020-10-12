# encoding:utf-8
import threading
import time


class MyThread(threading.Thread):

    def __init__(self,name,age):
        super().__init__()
        self.name = name
        self.age = age

    def run(self):
        print(f"Hi {self.name}, good day today, we love {self.age} you")
        time.sleep(5)




if __name__ == '__main__':
    t1 = MyThread('lzk','25')
    t2 = MyThread('lbq','25')
    t1.start()
    t2.start()
    print(threading.enumerate())