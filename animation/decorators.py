# -*- coding: utf-8 -*-
#
# Decorators for terminal-based wait animations
#
# @author <bprinty@gmail.com>
# ------------------------------------------------


# imports
# -------
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

for sig in ['SIGINT', 'SIGINT', 'SIGUSR1', 'SIGUSR2', 'SIGTERM']:
    if hasattr(signal, sig):
        signal.signal(getattr(signal, sig), end_wait_threads)


# animation objects
# -----------------
class Wait(object):
    """
    Class for managing wait animations.

    Args:
        animation (str, tuple): String reference to animation or tuple
            with custom animation.
        text (str): Optional text to print before animation.
        speed (float): Number of seconds each cycle of animation.

    Examples:
        >>> animation = Wait()
        >>> animation.start()
        >>> long_running_function()
        >>> animation.stop()
    """

    def __init__(self, animation='elipses', text='waiting', speed=0.2):
        if isinstance(animation, (list, tuple)):
            self._data = animation
        else:
            self._data = getattr(animations, animation)
        assert len(self._data) > 0, 'Incorrect animation specified!'
        self.animation = animation
        self.text = text
        self.speed = speed
        self.reverser = ''.join(map(lambda x: '\b' if x != '\n' else '\033[A', self._data[0]))
        return

    def _animate(self):
        global _waits
        _waits.append(self)
        self._count = 0
        
        sys.stdout.write(self.text)
        while True:
            if self._count < 0:
                break
            if self._count != 0:
                sys.stdout.write(self.reverser)
            sys.stdout.write(self._data[self._count % len(self._data)])
            sys.stdout.flush()
            time.sleep(self.speed)
            self._count += 1
        return

    def start(self):
        """
        Start animation thread.
        """
        self.thread = threading.Thread(target=self._animate)
        self.thread.start()
        return

    def stop(self):
        """
        Stop animation thread.
        """
        time.sleep(self.speed)
        self._count = -9999
        sys.stdout.write(self.reverser + '\r\033[K\033[A')
        sys.stdout.flush()
        return


# decorators
# ----------
def wait(animation='elipses', text='', speed=0.2):
    """
    Decorator for adding wait animation to long running
    functions.

    Args:
        animation (str, tuple): String reference to animation or tuple
            with custom animation.
        speed (float): Number of seconds each cycle of animation.

    Examples:
        >>> @animation.wait('bar')
        >>> def long_running_function():
        >>>     ... 5 seconds later ...
        >>>     return
    """
    def decorator(func):
        func.animation = animation
        func.speed = speed
        func.text = text

        @wraps(func)
        def wrapper(*args, **kwargs):
            animation = func.animation
            text = func.text
            if not isinstance(animation, (list, tuple)) and \
                    not hasattr(animations, animation):
                text = animation if text == '' else text
                animation = 'elipses'
            wait = Wait(animation=animation, text=text, speed=func.speed)
            wait.start()
            try:
                ret = func(*args, **kwargs)
            finally:
                wait.stop()
            sys.stdout.write('\n')
            return ret
        return wrapper
    return decorator


def simple_wait(func):
    """
    Decorator for adding simple text wait animation to
    long running functions.

    Examples:
        >>> @animation.simple_wait
        >>> def long_running_function():
        >>>     ... 5 seconds later ...
        >>>     return
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        wait = Wait()
        wait.start()
        try:
            ret = func(*args, **kwargs)
        finally:
            wait.stop()
        sys.stdout.write('\n')
        return ret
    return wrapper
