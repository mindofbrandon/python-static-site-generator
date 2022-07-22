import pyyaml
import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = r'^(?:-|\+){3}\s*$'
    __regex = re.compile(__delimiter, re.MULTILINE)
    
    @classmethod # is this the decorator?
    def load(cls, string): # make it with appropriate decorator?
        _, fm, content = cls.__regex.split(string, 2) # add a depth of 2
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        if self.data == "type":
            return self.data["type"]
        else:
            return None
    
    @type.setter
    def type(self):
        self.data["type"] = type

    def __getitem__(self):
        return self.data[self.values()]
    
    def __iter__(self):
        self.data
    
    def __len__(self):
        return len(self.data)