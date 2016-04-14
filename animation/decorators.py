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


# classes
# -------
class WaitAnimator(object):
    _animations = {
        'bar': (
            '[=      ]', '[ =     ]', '[  =    ]', '[   =   ]',
            '[    =  ]', '[     = ]', '[      =]', '[      =]',
            '[     = ]', '[    =  ]', '[   =   ]', '[  =    ]',
            '[ =     ]', '[=      ]'
        ),
        'dots': (
            '.  \n   \n   ', ' . \n   \n   ', '  .\n   \n   ',
            '   \n  .\n   ', '   \n   \n  .', '   \n   \n . ',
            '   \n   \n.  ', '   \n.  \n   '
        ),
        'text': (
            '.        ', '..       ', '...      ',
            '....     ', '.....    ', '......   ',
            '.......  ', '........ ', '.........'
        )
    }

    def __init__(self, animation='text', text='waiting'):
        self._animation = self._animations[animation]
        self.text = text
        return

    def _animate(self):
        global _waits
        _waits.append(self)
        time.sleep(0.2)
        self._count = 0
        newlines = len(filter(lambda x: x == '\n', self._animation[0]))
        reverser = ''.join(map(lambda x: '\b' if x != '\n' else '\033[A', self._animation[0]))
        sys.stdout.write(''.join(['\n' + self.text] + ['\n']*(newlines)))
        while True:
            if self._count < 0:
                break
            if self._count != 0:
                sys.stdout.write(reverser)
            sys.stdout.write(self._animation[self._count % len(self._animation)])
            sys.stdout.flush()
            time.sleep(0.2)
            self._count += 1
        return

    def start(self):
        self.thread = threading.Thread(target=self._animate)
        self.thread.start()
        return

    def stop(self):
        time.sleep(1)
        self._count = -9999
        return
