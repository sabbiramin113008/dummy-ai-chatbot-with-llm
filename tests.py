# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 29 Sep 2023
email: sabbir.amin@goava.com, sabbiramin.cse11ruet@gmail.com

"""
import unittest

import utils


class TestBasicIntentFinder(unittest.TestCase):
    def test_intent_with_sample_queries(self):
        queries = ['what are the product?',
                   'Do you have product A?',
                   'how much stock do you have?',
                   'let me know the price'
                   ]
        for q in queries:
            print('intent:', utils.get_intent(q))

    def test_intent_with_spacy(self):
        queries = ['what are the product?',
                   'Do you have product A?',
                   'how much stock do you have?',
                   'let me know the price'
                   ]
        for q in queries:
            print('intent:', utils.get_intent_by_spacy(q))


if __name__ == '__main__':
    unittest.main()
