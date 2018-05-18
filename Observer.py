class Observer:
    def __init__(self, publisher = None):
        if publisher == None:
            return 
        publisher.attach(self)

    def update(self, event):
        print "observer update called, should be overwriten in implimentation"
        print "event:", event.name, event.value

class Event:
    name = "hello"
    value = "world"
    #ect

class Publisher(object):
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
        self.notify(event)
    def delEvent(self): 
        del self.__event

    state = property(getEvent, setEvent, delEvent, "I'm the 'event' property.")



publisher = Publisher()
print "adding publisher"
observer = Observer(publisher)
print "publisher observers:", publisher.observers
publisher.state = Event()
print "removing publisher"
publisher.detach(observer)
print "publisher observers:", publisher.observers