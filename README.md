Thread Timeout Demo
=======

### (or: Why does the SafeExecution#timeout function not work when used as a decorator?)

I was trying to write a function decorator to wrap a long task in a Process that would be killed if a timeout expires.

I came up with this a working but not elegant version that explicitly calls the `timeout` function and assigns back the decorated function. There are better ways to do this, but I'm trying to learn. This is, in fact, my first attempt at threading and/or multiprocessing in Python, so I'm just trying to replicate what I remember from Java and C. 

The working version is exemplified by the "Working demo" commit. The "Non working demo" commit just uses the "@" decorator syntax to accomplish the same result. The decorator returns successfully, but when I call the decorated function what actually happens (Python 3.3 on Windows 7) is:

    Traceback (most recent call last):
      File "C:\Users\mm\git\timeout\example.py", line 14, in <module>
        primes(30000)
      File "C:\Users\mm\git\timeout\safeexec.py", line 25, in __call__
        ret = self.thread.start()
      File "C:\Python33\lib\multiprocessing\process.py", line 111, in start
        self._popen = Popen(self)
      File "C:\Python33\lib\multiprocessing\forking.py", line 241, in __init__
        dump(process_obj, to_child, HIGHEST_PROTOCOL)
      File "C:\Python33\lib\multiprocessing\forking.py", line 160, in dump
        ForkingPickler(file, protocol).dump(obj)
    _pickle.PicklingError: Can't pickle <class 'function'>: attribute lookup builtin
    s.function failed
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "C:\Python33\lib\multiprocessing\forking.py", line 344, in main
        self = load(from_parent)
    EOFError

It seems that losing the original reference to the function makes pickling it impossible. (Or forbidden?)

The working demo bypasses this by importing the function from an external module, as suggested by Mr. Fooz on the original [Stack Overflow thread](http://stackoverflow.com/questions/14990478/why-does-this-function-not-work-when-used-as-a-decorator). My original workaround was to just use a different name for the new function, but that would also require to modify the code using the function to refer to the decorated version.

Anybody has any idea of what is happening under the hood? Is the original function being turned into something different when I assign the decorated version to the identifier referencing it?
