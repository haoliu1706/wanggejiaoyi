# coding: utf-8

import os
import sys
import time
import unittest
from unittest import mock

sys.path.append('.')

TEST_CLIENTS = os.environ.get('EZ_TEST_CLIENTS', 'ht')

IS_WIN_PLATFORM = sys.platform != 'darwin'

@unittest.skipUnless('ht' in TEST_CLIENTS and IS_WIN_PLATFORM, 'skip ht test')
class TestHTClientTrader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import autologin as easytrader
        if 'ht' not in TEST_CLIENTS:
            return

        # input your test account and password
        cls._ACCOUNT = os.environ.get('EZ_TEST_HT_ACCOUNT') or 'your account'
        cls._PASSWORD = os.environ.get(
            'EZ_TEST_HT_password') or 'your password'
        cls._COMM_PASSWORD = os.environ.get(
            'EZ_TEST_HT_comm_password') or 'your comm password'

        cls._user = easytrader.use('ht_client')
        cls._user.prepare(
            user=cls._ACCOUNT,
            password=cls._PASSWORD,
            comm_password=cls._COMM_PASSWORD)

    def test_balance(self):
        time.sleep(3)
        result = self._user.balance

    def test_today_entrusts(self):
        result = self._user.today_entrusts

    def test_today_trades(self):
        result = self._user.today_trades

    def test_cancel_entrusts(self):
        result = self._user.cancel_entrusts

    def test_cancel_entrust(self):
        result = self._user.cancel_entrust('123456789')

    def test_invalid_buy(self):
        import autologin
        with self.assertRaises(autologin.exceptions.TradeError):
            result = self._user.buy('511990', 1, 1e10)

    def test_invalid_sell(self):
        import autologin
        with self.assertRaises(autologin.exceptions.TradeError):
            result = self._user.sell('162411', 200, 1e10)

    def test_auto_ipo(self):
        self._user.auto_ipo()


if __name__ == '__main__':
    unittest.main()