
class ResultHandler:
    def __init__(self, output_filename):
        self.output = output_filename

    def resultHandler(self, result):
        if self.output=='':
            print("测试结果：")
            print(result)
