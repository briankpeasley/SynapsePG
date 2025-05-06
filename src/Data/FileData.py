
class FileData():
    @staticmethod
    def get_value(params):
        with open(params, "r") as f:
            return f.read()