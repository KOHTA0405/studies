import unittest

from power import power, times


class TestMyPower(unittest.TestCase):
    def test_power(self):
        base = 2
        exp = 3
        # assert power(base, exp) == 8, "This should be 8"
        self.assertEqual(power(base, exp), 8)
        # 引数に文字列を与えたときに、TypeErrorを起きる かどうか確認するテスト
        with self.assertRaises(TypeError):
            power(2, 3)

    def test_times(self):
        num1 = 2
        num2 = 3
        # assert times(num1, num2) == 6, "This should be 6"
        self.assertEqual(times(num1, num2), 6)

if __name__ == "__main__":
    # test_power()
    # test_times()
    unittest.main()

# ターミナルから実行するときは、モジュールを-mで指定して実行することもある
# python -m unittest test_power.py