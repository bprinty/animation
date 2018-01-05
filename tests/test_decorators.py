#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# testing for animation
# 
# @author <bprinty@gmail.com>
# ------------------------------------------------


# imports
# -------
import unittest
import animation
import time


# tests
# -----
class TestAnimation(unittest.TestCase):
    _wait = 2

    @animation.simple_wait
    def test_default(self):
        time.sleep(self._wait)
        self.assertEqual(True, True)
        pass

    @animation.wait('bar')
    def test_bar(self):
        time.sleep(self._wait)
        self.assertEqual(True, True)
        pass

    @animation.wait('dots')
    def test_dots(self):
        time.sleep(self._wait)
        self.assertEqual(True, True)
        pass

    @animation.wait('elipses')
    def test_elipses(self):
        time.sleep(self._wait)
        self.assertEqual(True, True)
        pass

    @animation.wait('spinner')
    def test_spinner(self):
        time.sleep(self._wait)
        self.assertEqual(True, True)
        pass

    @animation.wait('pulse')
    def test_pulse(self):
        time.sleep(self._wait)
        self.assertEqual(True, True)
        pass

    @animation.wait('custom wait')
    def test_text_resolution(self):
        time.sleep(self._wait)
        self.assertEqual(True, True)
        pass

    @animation.wait('bar', speed=0.05)
    def test_speed(self):
        time.sleep(self._wait)
        self.assertEqual(True, True)
        pass

    @animation.wait(('-', '/', '|', '\\'))
    def test_custom_animation(self):
        time.sleep(self._wait)
        self.assertEqual(True, True)
        return
