class Data():
    def __init__(self):
        self.paths = []
    def add_paths(self, list):
        print('Add data!')
        print(list)
        print(type(list))
        print(self.paths)
    def rm_data(self, path):
        self.paths.remove(path)
    def show_data(self):
        for path in self.paths:
            print(path)