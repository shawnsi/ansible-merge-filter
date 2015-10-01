#!/usr/bin/env python

import sys
import unittest

sys.path.append('./filter_plugins')

from merge import merge

class TestMerge(unittest.TestCase):

    def test_identity(self):
        identity = {}

        other = {}
        merged = merge(identity, other)
        self.assertDictEqual(merged, other)

        other = {'foo': 1}
        merged = merge(identity, other)
        self.assertDictEqual(merged, other)

        other = {'foo': {'bar': 1}}
        merged = merge(identity, other)
        self.assertDictEqual(merged, other)

    def test_sum(self):
        a, b = {'foo': 1}, {'foo': 1}
        merged = merge(a, b)
        self.assertDictEqual(merged, {'foo': 2})

    def test_sum_recursion(self):
        a, b = {'foo': {'bar': 1}}, {'foo': {'bar': 1}}
        merged = merge(a, b)
        self.assertDictEqual(merged, {'foo': {'bar': 2}})

    def test_sum_lists(self):
        a, b = {'foo': [1]}, {'foo': [1]}
        merged = merge(a, b)
        self.assertDictEqual(merged, {'foo': [1, 1]})

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

