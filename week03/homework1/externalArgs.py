import argparse 

class MyParser:
    def __init__(self):
        parser = argparse.ArgumentParser() 

        parser.add_argument( 
        '-n', 
        dest='workers',
        type=int,
        default=1,
        help='Process or Thread Numbers' 
        ) 

        parser.add_argument( 
        '-f', 
        dest='work_type',
        action='store',
        help='Work Type: ping or tcp'
        )

        parser.add_argument( 
        '-ip', 
        dest='ip_range',
        action='store',
        help='Scan ip range'
        )

        parser.add_argument( 
        '-w', 
        dest='output_filename',
        action='store',
        help='Result file name.'
        )

        parser.add_argument( 
        '-m', 
        dest='worker_type',
        default='proc',
        action='store',
        help='Specify to use Mutiple Process or Mutiple Thread'
        )

        self.parser = parser

    def decodeArgs(self):
        result = self.parser.parse_args()

        ip_list = result.ip_range.split('-')

        if len(ip_list) > 1:
            ip_start = ip_list[0]
            ip_end = ip_list[1]
        else:
            ip_start = ip_list[0]
            ip_end = ip_list[0]

        argsDict = dict(workers=result.workers, work_type=result.work_type, ip_start=ip_start, ip_end=ip_end, output_filename=result.output_filename, worker_type=result.worker_type)
        
        return argsDict

