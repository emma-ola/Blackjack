import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_user_win_main(self):
        user_final_deck = sum([10, 1])
        computer_final_deck = sum([2, 5, 7])
        result = main.user_win(user_final_deck, computer_final_deck)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
