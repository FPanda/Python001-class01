from multiprocessing import Queue
from multiprocessing.pool import Pool
from time import sleep
import os

class MultiProcessWorker:
    def __init__(self,num):
        print("初始化多进程管理类")
        self.num = num
        self.work_queue = Queue()
        self.processPool = Pool(self.num)
 
    def pingIp(self, ip_list):
        for i in ip_list:
            print("启动ip地址处理进程：%s" % i)
            self.processPool.apply_async(self.work_handler, (i, self.work_queue,))

    def close(self):
        self.processPool.close()
        self.processPool.join()

    def work_handler(self, args):
        print("启动worker子进程：%s" % os.getpid())
        ip = args[0]
        q = args[1]
        print("处理ip地址：%s" % ip)
        sleep(5)
        print("结束worker子进程：%s" % os.getpid())


