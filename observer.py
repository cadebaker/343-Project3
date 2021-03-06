from abc import ABCMeta, abstractmethod


"""******************************************************
*Class that was provided by Professor Woodring's notes 
*to implement the observer functionality into Zork
******************************************************"""
#observer class with an update method
class Observer(object):
        __metaclass__ = ABCMeta

        @abstractmethod
        def updateCl(self):
                pass

"""******************************************************
*Class that was provided by Professor Woodring's notes 
*to implement the observable functionality into Zork
******************************************************"""                                
class Observable(object):

        def __init__(self):    
                self.observers = []

        def add_observer(self, observer):
                if not observer in self.observers:
                        self.observers.append(observer)

        def remove_observe(self, observer):
                if observer in self.observers:
                        self.observers.remove(observer)

        def remove_all_observers(self):
                self.observers = []

        def update(self):
                for observer in self.observers:
                        observer.updateCl()
