from multiProcessWorker import MultiProcessWorker
from multiThreadWorker import MultiThreadWorker
from resultHandler import ResultHandler

class WorkerFactory:
    def __init__(self, type, workers, output_filename):
        self.resultHd = ResultHandler(output_filename)
        if type=='proc':
            self.factory = MultiProcessWorker(workers)
        elif type=='thread':
            self.factory = MultiThreadWorker(workers)

    def pingIp(self, ip_list):
        self.result = self.factory.pingIp(ip_list)

    def save(self):
        self.resultHd.resultHandler(self.result)
