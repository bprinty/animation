# -*- coding: utf-8 -*-
#
# TODO: add description
# 
# @author <bprinty@gmail.com>
# ------------------------------------------------


# imports
# -------
import os
import sys
import threading
import time
import signal
from functools import wraps
from . import animations


# signal management
# -----------------
_waits = []
def end_wait_threads(signal, frame):
    global _waits
    for wait in _waits:
        wait.stop()
    sys.stdout.write('\n')
    return

signal.signal(signal.SIGINT, end_wait_threads)
signal.signal(signal.SIGINT, end_wait_threads)
signal.signal(signal.SIGUSR1, end_wait_threads)
signal.signal(signal.SIGUSR2, end_wait_threads)
signal.signal(signal.SIGTERM, end_wait_threads)


# animation objects
# -----------------
class Wait(object):

    def __init__(self, animation='elipses', text='waiting', speed=0.2):
        assert hasattr(animations, animation), 'Animation not supported!'
        self._data = getattr(animations, animation)
        self.animation = animation
        self.text = text
        self.speed = speed
        return

    def _animate(self):
        global _waits
        _waits.append(self)
        self._count = 0
        newlines = len(filter(lambda x: x == '\n', self._data[0]))
        reverser = ''.join(map(lambda x: '\b' if x != '\n' else '\033[A', self._data[0]))
        sys.stdout.write(''.join(['\n' + self.text] + ['\n']*(newlines - 1)))
        while True:
            if self._count < 0:
                break
            if self._count != 0:
                sys.stdout.write(reverser)
            sys.stdout.write(self._data[self._count % len(self._data)])
            sys.stdout.flush()
            time.sleep(self.speed)
            self._count += 1
        return

    def start(self):
        self.thread = threading.Thread(target=self._animate)
        self.thread.start()
        return

    def stop(self):
        time.sleep(self.speed)
        self._count = -9999
        return


# decorators
# ----------
def wait(animation, speed=0.2):
    """
    Decorator for ...

    :param timing: When to update state (pre/post).
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            text = ''
            if not hasattr(animations, animation):
                text = animation
                animation = 'elipses'
            wait = Wait(animation=animation, text=text, speed=speed)
            wait.start()
            ret = func(*args, **kwargs)
            wait.stop()
            return ret
        return wrapper
    return decorator


def simple_wait(func):
    """
    Decorator for ...
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        wait = Wait(animation=animation, text=text)
        wait.start()
        ret = func(*args, **kwargs)
        wait.stop()
        return ret
    return wrapper

