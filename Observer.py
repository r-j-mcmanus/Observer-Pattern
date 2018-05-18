
class Observer:
    def __init__(self, subject = None):
        if subject == None:
            return 
        subject.attach(self)

    def update(self, state):
        print "observer update", state

class Subject(object):
    def __init__(self):
        self.observers = set()
        self.__state = None

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.add(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.__state)

    def getState(self): 
        return self.__state
    def setState(self, state): 
        self.__state = state
        self.notify()
    def delState(self): 
        del self.__state

    state = property(getState, setState, delState, "I'm the 'state' property.")



subject = Subject()
subject.state = "State 1"
observer = Observer(subject)
subject.state = "State 2"
subject.detach(observer)
print "observers", subject.observers
