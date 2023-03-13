import unittest

def suffix_adder_for_duck_names(prefix):
    valid_inputs = ["J", "K", "L", "M", "N", "O", "P", "Q"]

    if prefix == "O" or prefix == "Q":
        suffix = "uack"
        return prefix + suffix
    elif prefix in valid_inputs:
        suffix = "ack"
        return prefix + suffix
    else: 
        return 'Not a valid input.'


class Test_suffix_adder(unittest.TestCase):
    def test_jack(self):
        print('Testing Jack')
        self.assertEqual(suffix_adder_for_duck_names('J'), 'Jack')

    def test_kack(self):
        print('Testing Kack')
        self.assertEqual(suffix_adder_for_duck_names('K'), 'Kack')

    def test_lack(self):
        print('Testing Lack')
        self.assertEqual(suffix_adder_for_duck_names('L'), 'Lack')

    def test_mack(self):
        print('Testing Mack')
        self.assertEqual(suffix_adder_for_duck_names('M'), 'Mack')

    def test_nack(self):
        print('Testing Nack')
        self.assertEqual(suffix_adder_for_duck_names('N'), 'Nack')

    def test_ouack(self):
        print('Testing Ouack')
        self.assertEqual(suffix_adder_for_duck_names('O'), 'Ouack')

    def test_pack(self):
        print('Testing Pack')
        self.assertEqual(suffix_adder_for_duck_names('P'), 'Pack')

    def test_quack(self):
        print('Testing Quack')
        self.assertEqual(suffix_adder_for_duck_names('Q'), 'Quack') 


test = Test_suffix_adder()
test_jack = test.test_jack()
test_kack = test.test_kack()
test_lack = test.test_lack()
test_mack = test.test_mack()
test_nack = test.test_nack()
test_oack = test.test_ouack()
test_pack = test.test_pack()
test_qack = test.test_quack()

