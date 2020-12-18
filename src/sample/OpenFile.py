import os


class OpenFile(object):

    def read(self, path):
        result = ""
        with open(path, "r+") as f:
            for line in f:
                result += line + "\n"

        return result

    def delete(self, path):
        if os.path.exists(path):
            os.remove(path)
        else:
            raise Exception("File doesn't exist")

    def write(self, path, text):
        with open(path, "w+") as f:
            f.write(text)


