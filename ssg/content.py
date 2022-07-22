import pyyaml
import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)
    
    def load(self, cls, string): # make it with appropriate decorator?
        self.__regex.split(string) # add a depth of 2?
        load(fm, Loader)
        return cls(metadata, content)