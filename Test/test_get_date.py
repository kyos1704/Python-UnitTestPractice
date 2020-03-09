import sys
import os
from Scripts.get_date import get_date

import unittest


class TestDate(unittest.TestCase):
    def test_date(self):
        date = get_date()
        import datetime
        self.assertEqual(datetime.datetime.now(),date)




if __name__ == "__main__":
    unitttest.main()