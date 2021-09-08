import unittest
from unittest import IsolatedAsyncioTestCase
from Sneil import get_matrix, sneil, StructureException, ConnectionException, StatusException

CONNECTION = "Connection or request error: {}."
STATUS = "Error response {} while requesting {}."

SOURCE_URL = ['https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt',
              'http://1.164.13.103:8888/',
              'http://213.143.14.113:23/',
              'http://165.22.107.109/'] #505

INPUT = [[1],
         [1, 2,
          3, 4],
         [10, 20, 30, 40,
          50, 60, 70, 80,
          90, 100, 110, 120,
          130, 140, 150, 160],
         [1, 2, 3, 4, 5,
          6, 7, 8, 9, 10,
          11, 12, 13, 14, 15,
          16, 17, 18, 19, 20,
          21, 22, 23, 24, 25],
         [1, 2,
          3, 4, 5]
         ]

ANSWER = [[1],
          [1, 3,
           4, 2],
          [10, 50, 90, 130,
           140, 150, 160, 120,
           80, 40, 30, 20,
           60, 100, 110, 70],
          [1, 6, 11, 16, 21,
           22, 23, 24, 25, 20,
           15, 10, 5, 4, 3,
           2, 7, 12, 17, 18,
           19, 14, 9, 8, 13]]


class TestSneil(unittest.TestCase):

    # def setUp(self):
    #   self.calculator = get_matrix()

    def test_one(self):
        self.assertEqual(sneil(INPUT[0]), ANSWER[0])

    def test_two(self):
        self.assertEqual(sneil(INPUT[1]), ANSWER[1])

    def test_four(self):
        self.assertEqual(sneil(INPUT[2]), ANSWER[2])

    def test_five(self):
        self.assertEqual(sneil(INPUT[3]), ANSWER[3])

    def test_quadratic(self):
        with self.assertRaises(StructureException):
            sneil(INPUT[4])


class Test(IsolatedAsyncioTestCase):
    async def test_response(self):
        res = await get_matrix(SOURCE_URL[0])
        self.assertEqual(res, ANSWER[2])

    async def test_response2(self):
        with self.assertRaises(ConnectionException):
            await get_matrix(SOURCE_URL[1])

    async def test_response3(self):
        with self.assertRaises(ConnectionException):
            await get_matrix(SOURCE_URL[2])

    async def test_response4(self):
        with self.assertRaises(StatusException):
            await get_matrix(SOURCE_URL[3])


if __name__ == "__main__":
    unittest.main()
