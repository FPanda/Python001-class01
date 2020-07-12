import os
from concurrent.futures import ProcessPoolExecutor

class MultiProcessWorker:
    def __init__(self,num):
        print("初始化多进程管理类")
        self.executor = ProcessPoolExecutor(num)
 
    def pingIp(self, ip_list):
        res = self.executor.map(self.ping_handler, ip_list)
        return list(res)

    def ping_handler(self, args):
        print("启动worker子进程：%s" % os.getpid())
        print("结束worker子进程：%s" % os.getpid())


