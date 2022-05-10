import unittest


class BookTest(unittest.TestCase):
    def test_name(self):
        self.assertEqual(("Щегол"), "Щегол")

    def test_author(self):
        self.assertEqual(("Донна Тартт"), "Донна Тартт")

    def test_year(self):
        self.assertEqual(("2020"), "2020")

if __name__ == '__main__':
    unittest.main()