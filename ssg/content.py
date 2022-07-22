import pyyaml
import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)
    
    def load(cls, string): # make it with appropriate decorator?
        _, fm, content = cls.__regex.split(string, 2) # add a depth of 2
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata, content)