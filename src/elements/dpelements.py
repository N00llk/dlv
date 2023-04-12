import abc

from .efm_patterns import *
from .dfm_patterns import *


class DPElement(metaclass=abc.ABCMeta):
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def to_html(self):
        pass
