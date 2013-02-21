from multiprocessing import Process
from threading import Timer
from functools import partial

class SafeExecution(object):

    def __init__(self, task, timeout):
        self.setFunction(task)
        self.setTimeout(timeout)

    def setFunction(self, task):
        self.task = task
        self.thread = None

    def setTimeout(self, timeout):
        self.timeout = timeout

    def _break(self):
        self.thread.terminate()

    def __call__(self, *kw):
        timer = Timer(self.timeout, self._break)
        timer.start()
        self.thread = Process(target=self.task, args=kw)
        ret = self.thread.start()
        self.thread.join()
        timer.cancel()
        return ret

def settimeout(timeout):
    return partial(SafeExecution, timeout=timeout)
