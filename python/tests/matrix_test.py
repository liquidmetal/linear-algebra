#!/usr/bin/python

from matrix import Matrix
import unittest

class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.m = Matrix(3, 3)
        self.e = Matrix.eye(3)
        pass

    def tearDown(self):
        pass

    def test_create(self):
        self.assertNotEqual(self.m, None)

    def test_transpose(self):
        self.m.set(1, 0, 10)
        self.m.transpose()
        
        against = Matrix(3, 3)
        against.set(0, 1, 10)

        self.assertEqual(self.m, against)

        against = Matrix.eye(3)
        self.e.transpose()
        self.assertEqual(self.e, against)

    def test_add(self):
        self.assertEqual(self.m + self.e, self.e)


    def test_subtract(self):
        self.assertEqual(self.e - self.m, self.e)

    def test_negate(self):
        self.assertEqual(-self.m, self.m)

        m = Matrix(3, 3)
        m.set(0, 0, -1)
        m.set(1, 1, -1)
        m.set(2, 2, -1)

        self.assertEqual(-self.e, m)

    def test_pos(self):
        self.assertEqual(+self.m, self.m)
        self.assertEqual(+self.e, self.e)

    def test_submatrix(self):
        e2 = Matrix.eye(2)
        self.assertEqual(e2, self.e.submatrix(range(2), range(2)))

    def test_determinant(self):
        self.assertEqual(self.e.det(), 1)
        self.assertEqual(self.m.det(), 0)

        m = Matrix(3, 3)
        m.set(0, 0, 1)
        m.set(0, 1, 2)
        m.set(0, 2, 3)
        m.set(1, 0, 4)
        m.set(1, 1, 5)
        m.set(1, 2, 6)
        m.set(2, 0, 7)
        m.set(2, 1, 8)
        m.set(2, 2, 9)
        self.assertEqual(m.det(), 0)
