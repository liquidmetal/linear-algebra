#!/usr/bin/python

class Matrix(object):
    def __init__(self, m, n):
        self._base = []
        self._m = m
        self._n = n
        for i in range(m):
            self._base.append([0] * n)

    def set(self, i, j, value):
        if i >= self._m:
            raise IndexError("Row out of bounds: %d" % i)

        if j >= self._n:
            raise IndexError("Column out of bounds: %d" % j)

        self._base[i][j] = value
        return

    def transpose(self):
        oldbase= self._base
        self._base = []
        for i in range(self._n):
            self._base.append([])
            for j in range(self._m):
                self._base[i].append(oldbase[j][i])

    def submatrix(self, rows, cols):
        m = Matrix(len(rows), len(cols))

        row = 0
        col = 0
        for i in rows:
            col = 0
            for j in cols:
                m.set(row, col, self._base[i][j])
                col += 1

            row += 1

        return m

    def det(self):
        if self._m != self._n:
            raise IndexError("You can calculate the determinant only for square matrices")

        if self._m == 1:
            return self._base[0][0]
        else:
            power = 1
            det = 0
            for i in range(self._m):
                prod = self._base[0][i] * power
                power = -1 * power

                r = range(self._m)
                c = range(self._n)
                r.remove(0)
                c.remove(i)

                sub = self.submatrix(r, c)
                det += prod*sub.det()

            return det



    @classmethod
    def eye(cls, m):
        newMatrix = cls(m, m)
        for i in range(m):
            newMatrix.set(i, i, 1)
        return newMatrix

    def __str__(self):
        ret = "\n"
        for i in range(len(self._base)):
            ret += "  "
            for j in range(len(self._base[i])):
                ret += "%.4f " % self._base[i][j]

            ret += "\n"

        return ret

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        # Ensure the dimensions match
        if self._m != other._m or self._n != other._n:
            return False

        for i in range(self._m):
            for j in range(self._n):
                if self._base[i][j] != other._base[i][j]:
                    return False

        return True

    def __add__(self, other):
        if self._m != other._m or self._n != other._n:
            raise IndexError("Dimension mismatch between matrices")

        m = Matrix(self._m, self._n)
        for i in range(self._m):
            for j in range(self._n):
                m.set(i, j, self._base[i][j] + other._base[i][j])

        return m

    def __sub__(self, other):
        if self._m != other._m or self._n != other._n:
            raise IndexError("Dimension mismatch between matrices")

        m = Matrix(self._m, self._n)
        for i in range(self._m):
            for j in range(self._n):
                m.set(i, j, self._base[i][j] - other._base[i][j])

        return m

    def __neg__(self):
        m = Matrix(self._m, self._n)
        for i in range(self._m):
            for j in range(self._n):
                m.set(i, j, -self._base[i][j])

        return m

    def __pos__(self):
        m = Matrix(self._m, self._n)
        for i in range(self._m):
            for j in range(self._n):
                m.set(i, j, self._base[i][j])

        return m

