from multiProcessWorker import MultiProcessWorker

class WorkerFactory:
    def __init__(self, type, workers):
        if type=='proc':
            self.factory = MultiProcessWorker(workers)

    def pingIp(self, ip_list):
        self.factory.pingIp(ip_list)

    def close(self):
        self.factory.close()
