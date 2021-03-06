import os
from concurrent.futures import ThreadPoolExecutor
import utils

class MultiThreadWorker:
    def __init__(self,num):
        print("初始化多线程管理类")
        self.executor = ThreadPoolExecutor(num)
 
    def pingIp(self, ip_list):
        res = self.executor.map(self.ping_handler, ip_list, timeout=10)
        return list(res)

    def ping_handler(self, args):
        print("ip地址是：%s" % args)
        if utils.ping_one(args) == True:
            return args
        else:
            return ''
 
