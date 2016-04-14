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

    @animation.simple_wait
    def test_default(self):
        time.sleep(5)
        self.assertEqual(True, True)
        pass

