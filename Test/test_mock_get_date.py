import unittest
from unittest import mock

import Scripts.get_date

class TestMockGetDate(unittest.TestCase):
    
    @mock.patch("Scripts.get_date.get_date")
    def test_by_mock(self,get_date_mock):
        get_date_mock.return_value = "20200309"
        date = Scripts.get_date.get_date()
        self.assertEqual("20200309",date)

        
    @mock.patch("Scripts.get_date.get_date")
    def test_by_mock2(self,get_date_mock):
        get_date_mock.return_value = "20200310"
        date = Scripts.get_date.get_date()
        self.assertNotEqual("20200309",date)
