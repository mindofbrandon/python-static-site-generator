from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = self.source.Path()
        self.dest = self.dest.Path()

    def create_dir(self, path):
        directory = self.dest + '/' + relative_to(self.source)
        mkdir(directory, parents=True, exist_ok=True)

    def build(self):
        mkdir(self.dest, parents=True, exist_ok=True)
