class RainData:
    def __init__(self, file_path):
        self.name = self.load(file_path)
        self.data = {}
        self.load()

    def load(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        self.name = lines[0]

if __name__ =='__main__':
    hayden