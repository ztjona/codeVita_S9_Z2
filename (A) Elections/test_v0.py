# -*- coding: utf-8 -*-
'''
Python 3.9
[MSC v.1916 64 bit (AMD64)]
22 / 10 / 2020
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
'I find that I don't understand things unless I try to program them.'
-Donald E. Knuth
'''

import unittest
from unittest.mock import patch, call
import elections

''' Pruebas y más pruebas
################################################### '''


class Auxiliar:

    cases = 2

    def __init__(self, case):
        ''' Constructor
        ############################################### '''

        if case == 0:
            self.prints = ['14', '--AB--AB---A--']
            self.resps = ['A', ]
        elif case == 1:
            self.prints = ['38', 'B--BA---AA----BB--AB---AA--BB---BB--A']
            self.resps = ['B', ]

    def printFn(self, query):
        ''' Mock of print function
        ############################################### '''
        print('printed:', query)

    def inputGen(self):
        ''' Mock of input
        ############################################### '''

        yield from self.prints


class Pruebas(unittest.TestCase):
    ''' Los métodos de prueba deben empezar como test_*
    '''

    # al mockear se debe poner la ruta completa.
    @patch('elections.print', create=True)
    @patch('elections.input', create=True)
    def test_P1(self, input_mock, print_mock):
        ''' 
        
        ############################################### '''
        for case in range(Auxiliar.cases):
            print('=============== CASE: ', case)
            decors = Auxiliar(case)
            printFn = decors.printFn
            inputGen = decors.inputGen
            print_mock.side_effect = printFn
            input_mock.inputGen = inputGen()
            input_mock.side_effect = lambda: next(input_mock.inputGen)

            elections.main()
            calls = [call(x) for x in decors.resps]
            print_mock.assert_has_calls(calls)
        return

    '''
    # Skips this test only
    self.skipTest('Just examples, use as template!.')
    self.assertEqual(a, b)  # a == b
    self.assertNotEqual(a, b)  # a != b
    self.assertTrue(x)  # bool(x) is True
    self.assertFalse(x)  # bool(x) is False
    self.assertIs(a, b)  # a is b
    self.assertIsNot(a, b)  # a is not b
    self.assertIsNone(x)  # x is None
    self.assertIsNotNone(x)  # x is not None
    self.assertIn(a, b)  # a in b
    self.assertNotIn(a, b)  # a not in b
    self.assertIsInstance(a, b)  # isinstance(a, b)
    self.assertNotIsInstance(a, b)  # not isinstance(a, b)
    self.assertAlmostEqual(a, b)  # round(a-b, 7) == 0
    self.assertNotAlmostEqual(a, b)  # round(a-b, 7) != 0
    self.assertGreater(a, b)  # a > b
    self.assertGreaterEqual(a, b)  # a >= b
    self.assertLess(a, b)  # a < b
    self.assertLessEqual(a, b)  # a <= b
    self.assertRegex(s, r)  # r.search(s)
    self.assertNotRegex(s, r)  # not r.search(s)
    # sorted(a) == sorted(b) and works with unhashable objs
    self.assertItemsEqual(a, b)
    # all the key/value pairs in a exist in b
    self.assertDictContainsSubset(a, b)
    # a and b have the same elements in the same number, regardless of their order
    self.assertCountEqual(a, b)
    # Compare different types of objects
    self.assertMultiLineEqual(a, b)  # Compare strings
    self.assertSequenceEqual(a, b)  # Compare sequences
    self.assertListEqual(a, b)  # Compare lists
    self.assertTupleEqual(a, b)  # Compare tuples
    self.assertSetEqual(a, b)  # Compare sets
    self.assertDictEqual(a, b)  # Compare dicts
    # To Test code that MUST Raise Exceptions:
    '''
