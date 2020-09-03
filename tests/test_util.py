import unittest
import os
import sys
from functions.util import amino_dict, str_checker, mass_dict

class aminodictTest(unittest.TestCase):

    def setUp(self):
        self.fake_amino_dict = amino_dict(os.path.join(os.getcwd(),
                                               "docs/base.def"))

    def test_Instance(self):
        self.assertIsInstance(self.fake_amino_dict, dict)

    def test_ala_codons(self):
        self.assertEqual(self.fake_amino_dict['Ala'],
                         ['GCT', 'GCC', 'GCA', 'GCG'])

    def test_ala_codons_length(self):
        self.ala = []
        for codon in self.fake_amino_dict['Ala']:
            self.ala.append(len(codon) == 3)
        self.assertTrue(any(self.ala))

    def test_ala1(self):
        self.assertIn('GCT', self.fake_amino_dict['Ala'])

    def test_ala2(self):
        self.assertIn('GCC', self.fake_amino_dict['Ala'])

    def test_ala3(self):
        self.assertIn('GCA', self.fake_amino_dict['Ala'])

    def test_ala4(self):
        self.assertIn('GCG', self.fake_amino_dict['Ala'])

    def test_empty(self):
        self.assertRaises(TypeError, os.path.abspath(""))

class massdictTest(unittest.TestCase):

    def setUp(self):
        self.fake_mass_dict = mass_dict(os.path.join(os.getcwd(),
                                         "docs/baseMass.def"))

    def test_Instance(self):
        self.assertIsInstance(self.fake_mass_dict, dict)

    def test_ala_mass(self):
        self.assertEqual(self.fake_mass_dict['Ala'], 71.03)

    def test_empty(self):
        self.assertRaises(TypeError, os.path.abspath(""))

class str_checkerTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(None, str_checker(""))

    def test_float(self):
        self.assertEqual(True, str_checker("125.0"))

    def test_integer(self):
        self.assertEqual(True, str_checker("125"))

    def test_not_number(self):
        self.assertEqual(False, str_checker("125a"))

    def test_not_float_dot(self):
        self.assertEqual(False, str_checker("125."))

    def test_not_dot_float(self):
        self.assertEqual(False, str_checker(".125"))

    def test_dot_float_dot(self):
        self.assertEqual(None, str_checker("1.25."))

if __name__ == '__main__':
    unittest.main()
