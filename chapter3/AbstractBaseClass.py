import abc

# FIXME - it cannot be that hard to declare interfaces and allow for duck typing... Example below is nice
# implementation of interface in Py
"""
import abc
class Repository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_employee(self, company_name: str, id: int) -> Employee
        pass
"""
# TODO - search for interface definition in python
# TODO - stopped on pg. 81 / Demystifying the magic

class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractmethod
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented
