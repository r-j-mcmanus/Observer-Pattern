
class Observer:
    def __init__(self, subject = None):
        if subject == None:
            return 
        subject.attach(self)

    def update(self, event):
        print "observer update called, should be overwriten in implimentation"

class Event:
    name = None
    value = None
    #ect

class Subject(object):
    def __init__(self):
        self.observers = set()
        self.__event = None

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.add(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(self.__event)

    def getEvent(self): 
        return self.__event
    def setEvent(self, event): 
        self.__event = event
        self.notify()
    def delEvent(self): 
        del self.__event

    state = property(getEvent, setEvent, delEvent, "I'm the 'event' property.")



subject = Subject()
subject.state = "State 1"
observer = Observer(subject)
subject.state = "State 2"
subject.detach(observer)
print "observers", subject.observers
