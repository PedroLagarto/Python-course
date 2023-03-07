import unittest

def sufix_adder(prefix):
    if prefix == 'J':
        return 'Jack'
    elif prefix == 'K':
        return 'Kack'
    elif prefix == 'L':
        return 'Lack'
    elif prefix == 'M':
        return 'Mack'
    elif prefix == 'N':
        return 'Nack'
    elif prefix == 'O':
        return 'Ouack'
    elif prefix == 'P':
        return 'Pack'
    elif prefix == 'Q':
        return 'Quack'
    else:
        return 'Not a valid input.'

class Test_suffix_adder(unittest.TestCase):
    def test_jack(self):
        print('Testing Jack')
        self.assertEqual(sufix_adder('J'), 'Jack')

    def test_kack(self):
        print('Testing Kack')
        self.assertEqual(sufix_adder('K'), 'Kack')

    def test_lack(self):
        print('Testing Lack')
        self.assertEqual(sufix_adder('L'), 'Lack')

    def test_mack(self):
        print('Testing Mack')
        self.assertEqual(sufix_adder('M'), 'Mack')

    def test_nack(self):
        print('Testing Nack')
        self.assertEqual(sufix_adder('N'), 'Nack')

    def test_ouack(self):
        print('Testing Ouack')
        self.assertEqual(sufix_adder('O'), 'Ouack')

    def test_pack(self):
        print('Testing Pack')
        self.assertEqual(sufix_adder('P'), 'Pack')

    def test_quack(self):
        print('Testing Quack')
        self.assertEqual(sufix_adder('Q'), 'Quack') 


test = Test_suffix_adder()
test_jack = test.test_jack()
test_kack = test.test_kack()
test_lack = test.test_lack()
test_mack = test.test_mack()
test_nack = test.test_nack()
test_oack = test.test_ouack()
test_pack = test.test_pack()
test_qack = test.test_quack()

