from externalArgs import MyParser
import ipHandler 
from workerFactory import WorkerFactory

if __name__ == '__main__':
    parser = MyParser()
    args = parser.decodeArgs()
    print(args)

    worker = WorkerFactory(args['worker_type'], args['workers'] ,args['output_filename'])
    
    if args['work_type'] == 'ping':
        worker.pingIp(ipHandler.convertIpRangeToIpList(args['ip_start'], args['ip_end']))

    worker.save()
