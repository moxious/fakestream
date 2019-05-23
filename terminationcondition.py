# Termination conditions are wrapper classes that let us know when to stop.
import time

class TerminationCondition:
    def __init__(self): pass
    def ran(self, payload): pass
    def finished(self): return False

class TimedRun(TerminationCondition):
    def __init__(self, ms):
        TerminationCondition.__init__(self)
        self.start_time = int(round(time.time() * 1000))
        self.end_time = self.start_time + ms
    
    def ran(self, payload): pass

    def finished(self):
        return int(round(time.time() * 1000)) >= self.end_time

class CountRun(TerminationCondition):
    def __init__(self, n):
        TerminationCondition.__init__(self)
        self.limit = n
        self.times = 0
    
    def ran(self, payload):
        self.times = self.times + 1
    
    def finished(self):
        return self.times >= self.limit